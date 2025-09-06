import shutil
import subprocess
import sys
import winreg
import re
import os
import uuid
from sys import exception

from ui_main import Ui_MainWindow

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

def query_reg(hive, flag):
    """
    get windows all installed software
    """
    # winreg.ConnectRegistry(None, hive): 连接注册表; hive：windows下的HKEY_常量
    reg_instance = winreg.ConnectRegistry(None, hive)
    # winreg.OpenKey(reg, regedit_path, 0, reg_type):操作注册表（读取，写入等）
    # reg: 连接的注册表; regedit_path:注册表的路径; reg_type:需要对注册表的操作类型
    aKey = winreg.OpenKey(reg_instance, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)
    # winreg.QueryInfoKey(key):获取注册表的相关信息; 返回一个元组：(此注册表的子key数量， 0， 自从1600.1.1上次修改时间（纳秒）)key:打开的注册表
    count_subkey = winreg.QueryInfoKey(aKey)[0]
    software_list = []
    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]
            if "Cadence" in software['name']:
                try:
                    software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
                except EnvironmentError:
                    software['version'] = 'undefined'

                try:
                    software['InstallLocation'] = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
                except EnvironmentError:
                    software['InstallLocation'] = 'undefined'

                try:
                    software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
                except EnvironmentError:
                    software['publisher'] = 'undefined'

                software_list.append(software)
        except EnvironmentError:
            continue
    return software_list

def deal_path_reg():
    software_list = query_reg(winreg.HKEY_LOCAL_MACHINE,
                                               winreg.KEY_WOW64_32KEY) + query_reg(
        winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + query_reg(winreg.HKEY_CURRENT_USER, 0)
    locked_product = {}
    for software in software_list:
        if 'SPB' in software['InstallLocation']:
            locked_product['name'] = software['name']
            locked_product['InstallLocation'] = software['InstallLocation']
            locked_product['version'] = software['version']
            locked_product['publisher'] = software['publisher']
            # 使用正则表达式提取父目录：匹配直到最后一个分隔符(/或\)之前的所有内容
            # regex: ^(.*)[/\\][^/\\]*$  ? 组1为父目录
            match = re.match(r'^(.*)[/\\][^/\\]*$', locked_product["InstallLocation"])
            if match:
                parent_dir = match.group(1)
            else:
                # 如果路径没有分隔符（如单纯文件名），父目录视为当前目录('.')
                parent_dir = None
            target_path = os.path.join(parent_dir, "SPB_DATA", "pcbenv")
        else:
            target_path = None
        return target_path

def query_env():
    if "HOME" in os.environ:
        target_path = os.path.join(os.environ['HOME'], "pcbenv")
    else:
        target_path = None
    return target_path

def install_loader(target_path: str):
    start_file_path = os.path.join(target_path, "allegro.ilinit")
    if os.path.exists(start_file_path):
        try:
            swap_file = start_file_path + "swap"
            with open(start_file_path, "r") as infile, open(swap_file, "w") as outfile:
                for line in infile:
                    if ("exportJson" not in line) and ("jsonDecode" not in line):
                        outfile.write(line)
            shutil.copy2(swap_file, start_file_path)
            try:
                os.remove(swap_file)
            except FileNotFoundError:
                print("Swap file not found, skipping deletion.")
        except :
            return False
    else:
        print("New Install")
    with open(start_file_path, "a") as f:
        f.write('\nloadi("exportJson.il" )\nloadi("jsonDecode.il" )\n')
        return True

def install_core(main_path:str, home_path:str):
    try:
        src_main = os.path.join(main_path, "Main", "exportJson")
        if os.path.exists(src_main):
            core_list = ["exportJson.il", "jsonDecode.il"]
            for module in core_list:
                src_file = os.path.join(src_main, module)
                dst_dir = os.path.join(home_path, module)
                if os.path.exists(src_file):
                    shutil.copy2(src_file, dst_dir)
                else:
                    print(f"Source file {src_file} does not exist, skipping copy.")
                    return False
        else:
            print(f"Source directory {src_main} does not exist, skipping copy.")
            return False
        core = os.path.join(main_path, "Main", "InteractiveHtmlBom")
        if os.path.exists(core):
            core_target = os.path.join(home_path, "InteractiveHtmlBom")
            shutil.copytree(core, core_target, dirs_exist_ok=True)
        else:
            print(f"Source directory {src_main} does not exist, skipping copy.")
            return False
        return True
    except:
        return False

def check_environment():
    target_path = query_env()
    target_path = None
    if target_path is None:
        target_path = deal_path_reg()
    loader_status = install_loader(target_path)
    work_dir = os.getcwd()
    core_status = install_core(work_dir, target_path)


    print(target_path)

class MainWindow(QMainWindow):
    signal_check_bom = Signal(str)
    signal_check_bom_terminate = Signal()

    signal_preprocess_mkdir = Signal(str)
    signal_preprocess_nan = Signal(list)
    signal_preprocess_classify = Signal()
    signal_preprocess_terminate = Signal()

    signal_setup_post = Signal(str, str, list)
    signal_share_debug = Signal(bool)
    signal_share_config = Signal(dict)
    signal_post_remove_unofficial = Signal()
    signal_post_BOMMergeDuplicate = Signal(str)
    signal_post_merge_similar = Signal(str)
    signal_post_make_sort = Signal(str, str)

    signal_bom_patch_runtime = Signal()
    signal_bom_patch_collector = Signal(str, str, str, list)

    def __init__(self):
        super(MainWindow, self).__init__()
        # initial var
        self.page_selectProduct = None
        self.page_interactiveHtml = None
        self.identityId = None
        self.product_pixMap = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_page()
        self.setWindowTitle("Production Select...")
        self.get_activeId()
        self.setup_slot()
        self.setup_git()

    def setup_page(self):
        self.page_selectProduct = 0
        self.page_interactiveHtml = 1

    def get_activeId(self):
        self.identityId = uuid.UUID(int=uuid.getnode()).hex[-12:]
        self.ui.lineEdit_PendingIdentityID.setText(self.identityId)
        self.ui.lineEdit_PendingIdentityID.setEnabled(False)

    def setup_slot(self):
        self.ui.pushButton_SelectProduct.clicked.connect(self.submit_product)
        self.ui.pushButton_CheckEnvironment.clicked.connect(self.submit_CheckEnvironment_Interactive)

    def setup_git(self):
        self.original_dir = os.getcwd()
        # get git path
        self.git_path = os.path.join(self.original_dir, "Main", "gitExe", "bin", "git.exe")
        # ack git path
        if not os.path.exists(self.git_path):
            raise FileNotFoundError(f"git.exe not found at {self.git_path}")

        self.cmd = f'"{self.git_path}" rev-parse --short HEAD'

    def submit_product(self):
        if self.ui.lineEdit_PendingIdentityID.text() != "" and self.ui.lineEdit_ActiveID.text() != "":
            if self.ui.comboBox_SelectProduct.currentIndex() == 0:
                self.ui.stackedWidget.setCurrentIndex(self.page_interactiveHtml)
            else:
                self.product_pixMap = QPixmap(self.redirect_res("./src/Thinking.png"))
                self.ui.product_emoji.setPixmap(self.product_pixMap)
                self.ui.label_info.setText("Unsupported Production")
        else:
            self.product_pixMap = QPixmap(self.redirect_res("./src/Thinking.png"))
            self.ui.product_emoji.setPixmap(self.product_pixMap)
            self.ui.label_info.setText("Unofficial Production, or Production had been modified!")

    def query_reg(self, hive, flag):
        """
        get windows all installed software
        """
        # winreg.ConnectRegistry(None, hive): 连接注册表; hive：windows下的HKEY_常量
        reg_instance = winreg.ConnectRegistry(None, hive)
        # winreg.OpenKey(reg, regedit_path, 0, reg_type):操作注册表（读取，写入等）
        # reg: 连接的注册表; regedit_path:注册表的路径; reg_type:需要对注册表的操作类型
        aKey = winreg.OpenKey(reg_instance, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                              0, winreg.KEY_READ | flag)
        # winreg.QueryInfoKey(key):获取注册表的相关信息; 返回一个元组：(此注册表的子key数量， 0， 自从1600.1.1上次修改时间（纳秒）)key:打开的注册表
        count_subkey = winreg.QueryInfoKey(aKey)[0]
        software_list = []
        for i in range(count_subkey):
            software = {}
            try:
                asubkey_name = winreg.EnumKey(aKey, i)
                asubkey = winreg.OpenKey(aKey, asubkey_name)
                software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]
                if "Cadence" in software['name']:
                    try:
                        software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
                    except EnvironmentError:
                        software['version'] = 'undefined'

                    try:
                        software['InstallLocation'] = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
                    except EnvironmentError:
                        software['InstallLocation'] = 'undefined'

                    try:
                        software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
                    except EnvironmentError:
                        software['publisher'] = 'undefined'

                    software_list.append(software)
            except EnvironmentError:
                continue
        return software_list

    def git_commitID_get(self):
        try:
            stdout = subprocess.getoutput(self.cmd)
            return stdout.strip()
        except Exception as error:
            self.error = str(error)
            self.error()

    def interactiveHtml_check_InteractiveHtmlBomId(self):
        os.chdir(self.redirect_res("./Main/InteractiveHtmlBom"))
        print(os.getcwd())
        git_id = self.git_commitID_get()
        print(git_id)
        os.chdir(self.original_dir)
        if "not a git repository" not in git_id :
            self.ui.lineEdit_InteractiveHtmlBomID.setText(git_id)
            self.ui.lineEdit_InteractiveHtmlBomID.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.lineEdit_InteractiveHtmlBomID.setText("Warnings: NOT a git repository")
            self.error()

    def interactiveHtml_check_exportJsonIDId(self):
        os.chdir(self.redirect_res("./Main/exportJson"))
        print(os.getcwd())
        git_id = self.git_commitID_get()
        print(git_id)
        os.chdir(self.original_dir)
        if "not a git repository" not in git_id :
            self.ui.lineEdit_exportJsonID.setText(git_id)
            self.ui.lineEdit_exportJsonID.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.lineEdit_exportJsonID.setText("Warnings: NOT a git repository")
            self.error()

    def interactiveHtml_check_patchId(self):
        os.chdir(self.original_dir)
        print(os.getcwd())
        git_id = self.git_commitID_get()
        print(git_id)
        if "not a git repository" not in git_id :
            self.ui.lineEdit_PatchID.setText(git_id)
            self.ui.lineEdit_PatchID.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.lineEdit_PatchID.setText("Warnings: NOT a git repository")
            self.error()

    def submit_CheckEnvironment_Interactive(self):
        if "HOME" in os.environ:
            target_path = os.path.join(os.environ['HOME'], "pcbenv")
        else:
            software_list = self.query_reg(winreg.HKEY_LOCAL_MACHINE,
                                      winreg.KEY_WOW64_32KEY) + self.query_reg(
                winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + self.query_reg(winreg.HKEY_CURRENT_USER, 0)
            locked_product = {}
            for software in software_list:
                if 'SPB' in software['InstallLocation']:
                    locked_product['name'] = software['name']
                    locked_product['InstallLocation'] = software['InstallLocation']
                    locked_product['version'] = software['version']
                    locked_product['publisher'] = software['publisher']
                    # 使用正则表达式提取父目录：匹配直到最后一个分隔符(/或\)之前的所有内容
                    # regex: ^(.*)[/\\][^/\\]*$  ? 组1为父目录
                    match = re.match(r'^(.*)[/\\][^/\\]*$', locked_product["InstallLocation"])
                    if match:
                        parent_dir = match.group(1)
                    else:
                        # 如果路径没有分隔符（如单纯文件名），父目录视为当前目录('.')
                        parent_dir = None
                    target_path = os.path.join(parent_dir, "SPB_DATA", "pcbenv")
                    break
                else:
                    target_path = None
        if target_path is not None:
            self.ui.lineEdit_CadenceDirectory.setText(target_path)
            self.ui.lineEdit_CadenceDirectory.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.label_info.setText("Not Found Cadence Production")
            self.error()
        self.interactiveHtml_check_InteractiveHtmlBomId()
        self.interactiveHtml_check_exportJsonIDId()
        self.interactiveHtml_check_patchId()

    def error_product_interactiveHtml(self):
        self.ui.lineEdit_CadenceDirectory.setText(self.error)
        self.product_pixMap = QPixmap(self.redirect_res("./src/error.png"))

        self.ui.label_Emoji.setPixmap(self.product_pixMap)
        self.ui.label_info.setText(self.error)

    def redirect_res(self, src_path: str):
        """
        PyInstaller打包资源之后索引路径需要重定向

        :param src_path: 未封包前的索引路径
        """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(getattr(sys, '_MEIPASS'), src_path)
        return src_path

if __name__ == "__main__":
    # check_environment()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())