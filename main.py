import shutil
import subprocess
import sys
import winreg
import re
import os
import uuid
import traceback
import sympy
from sympy import Symbol, solve


from ui_main import Ui_MainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow

plugins_path = os.path.join(os.path.dirname(__file__), "plugins")
os.environ['QT_PLUGIN_PATH'] = plugins_path

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # initial var
        self.original_dir = None
        self.page_tlv185x = None
        self.InteractiveHtmlBomStatus = None
        self.InteractiveHtmlBomCore = None
        self.InteractiveHtmlBomLoader = None
        self.allowInstall_InteractiveHtml = None
        self.InteractiveHtmlBomIDPatch = None
        self.page_selectProduct = None
        self.page_interactiveHtml = None
        self.identityId = None
        self.product_pixMap = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_page()
        self.setWindowTitle("Production Select...")
        self.setup_var()
        self.setup_slot()
        self.setup_git()

    def setup_var(self):
        self.identityId = uuid.UUID(int=uuid.getnode()).hex[-12:]
        self.ui.lineEdit_PendingIdentityID.setText(self.identityId)
        self.ui.lineEdit_PendingIdentityID.setEnabled(False)
        self.ui.pushButton_InstallPatch.setEnabled(False)
        self.ui.pushButton_CheckEnvironment.setEnabled(False)
        self.InteractiveHtmlBomIDPatch = False
        self.allowInstall_InteractiveHtml = False
        self.InteractiveHtmlBomLoader = False
        self.InteractiveHtmlBomCore = False
        self.ui.product_emoji.setPixmap(QPixmap(self.redirect_res("./src/PendingActivation.png")))
        self.ui.label_Emoji.setPixmap(QPixmap(self.redirect_res("./src/welcom.png")))
        self.ui.doubleSpinBox_CalculatorHy_r1.setValue(205000.00)
        self.ui.doubleSpinBox_CalculatorHy_r2.setValue(100000.00)
        self.ui.doubleSpinBox_CalculatorHy_r3.setValue(820000.00)
        self.ui.doubleSpinBox_CalculatorHy_Vref.setValue(3.30)
        self.ui.lineEdit_CalculatorHy_L2H.setEnabled(False)
        self.ui.lineEdit_CalculatorHy_H2L.setEnabled(False)
        self.ui.lineEdit_CalculatorHy_TH.setEnabled(False)
        self.ui.lineEdit_CalculatorVar_TH.setEnabled(False)
        # set default checkbox
        self.ui.doubleSpinBox_CalculatorVar_Vref.setValue(3.3)
        self.ui.doubleSpinBox_CalculatorVar_r2.setValue(100000)
        self.ui.lineEdit_CalculatorVar_H2L.setText(str(1.25))
        self.ui.lineEdit_CalculatorVar_L2H.setText(str(1))
        self.ui.checkBox_CalculatorVar_r2.setChecked(True)
        self.ui.doubleSpinBox_CalculatorVar_r2.setEnabled(True)
        self.ui.checkBox_CalculatorVar_r1.setChecked(False)
        self.ui.doubleSpinBox_CalculatorVar_r1.setEnabled(False)
        self.ui.checkBox_CalculatorVar_r3.setChecked(False)
        self.ui.doubleSpinBox_CalculatorVar_r3.setEnabled(False)

    def setup_page(self):
        self.page_selectProduct = 0
        self.page_interactiveHtml = 1
        self.page_tlv185x = 2

    def setup_slot(self):
        self.ui.pushButton_SelectProduct.clicked.connect(self.submit_product)
        self.ui.pushButton_CheckEnvironment.clicked.connect(self.submit_CheckEnvironment_Interactive)
        self.ui.pushButton_InstallPatch.clicked.connect(self.submit_install_patch)
        self.ui.pushButton_CalculatorVar_RUN.clicked.connect(self.submit_calculator_var)
        self.ui.pushButton_CalculatorHy_RUN.clicked.connect(self.submit_calculator_hy)
        self.ui.checkBox_CalculatorVar_r1.checkStateChanged.connect(self.fixCheckBox_CalculatorVar_r1)
        self.ui.checkBox_CalculatorVar_r2.checkStateChanged.connect(self.fixCheckBox_CalculatorVar_r2)
        self.ui.checkBox_CalculatorVar_r3.checkStateChanged.connect(self.fixCheckBox_CalculatorVar_r3)

    def setup_git(self):
        self.original_dir = os.path.dirname(__file__)
        # get git path
        self.git_path = os.path.join(self.original_dir, "Main", "gitExe", "bin", "git.exe")
        # ack git path
        if not os.path.exists(self.git_path):
            raise FileNotFoundError(f"git.exe not found at {self.git_path}")
        self.cmd = f'"{self.git_path}" rev-parse --short HEAD'

    def submit_product(self):
        if self.ui.lineEdit_PendingIdentityID.text() != "" and self.ui.lineEdit_ActiveID.text() != "":
            if self.ui.comboBox_SelectProduct.currentIndex() == 0:
                self.setWindowTitle("Production: Interactive Html Bom Installer")
                self.ui.stackedWidget.setCurrentIndex(self.page_interactiveHtml)
                self.ui.pushButton_CheckEnvironment.setEnabled(True)
            elif self.ui.comboBox_SelectProduct.currentIndex() == 1:
                self.setWindowTitle("Production: TLV185X Caculator")
                self.ui.stackedWidget.setCurrentIndex(self.page_tlv185x)
                # self.ui.pushButton_CheckEnvironment.setEnabled(True)
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
            self.error_product_interactiveHtml()

# >>>>>>>>>>>>> COMMENT ID CHECK <<<<<<<<<<<<<<<<

    def interactiveHtml_check_InteractiveHtmlBomId(self):
        os.chdir(self.redirect_res("./Main/InteractiveHtmlBom"))
        git_id = self.git_commitID_get()
        os.chdir(self.original_dir)
        if "not a git repository" not in git_id :
            self.ui.lineEdit_InteractiveHtmlBomID.setText(git_id)
            self.ui.lineEdit_InteractiveHtmlBomID.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.lineEdit_InteractiveHtmlBomID.setText("Warnings: NOT a git repository")
            self.error_product_interactiveHtml()

    def interactiveHtml_check_exportJsonIDId(self):
        os.chdir(self.redirect_res("./Main/exportJson"))
        git_id = self.git_commitID_get()
        os.chdir(self.original_dir)
        if "not a git repository" not in git_id :
            self.ui.lineEdit_exportJsonID.setText(git_id)
            self.ui.lineEdit_exportJsonID.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.lineEdit_exportJsonID.setText("Warnings: NOT a git repository")
            self.error_product_interactiveHtml()

    def interactiveHtml_check_patchId(self):
        os.chdir(self.original_dir)
        git_id = self.git_commitID_get()
        if "not a git repository" not in git_id :
            self.ui.lineEdit_PatchID.setText(git_id)
            self.ui.lineEdit_PatchID.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.lineEdit_PatchID.setText("Warnings: NOT a git repository")
            self.error_product_interactiveHtml()

# >>>>>>>>>>>>> COMMENT ID CHECK <<<<<<<<<<<<<<<<

    def copy_file(self, src_file, dst_file):
        try:
            shutil.copyfile(src_file, dst_file)
            print(f"file copied: {src_file} -> {src_file}")
        except Exception as error:
            self.error = str(error)
            self.error_product_interactiveHtml()

    def interactiveHtml_generatePath(self):
        try:
            self.copy_file(self.redirect_res("./Main/exportJson/exportJson.il"),
                           self.redirect_res("./Main/exportJson/exportJson.il.bak"))
            self.copy_file(self.redirect_res("./Main/autoFill.patch"), self.redirect_res("./Main/exportJson/autoFill.patch"))
        except Exception as error:
            self.InteractiveHtmlBomIDPatch = False
            self.error = str(error)
            self.error_product_interactiveHtml()
        try:
            os.chdir(self.redirect_res("./Main/exportJson"))
            path_cmd = f'"{self.git_path}" apply autoFill.patch'
            stdout = subprocess.getoutput(path_cmd)
            os.chdir(self.original_dir)
            self.InteractiveHtmlBomIDPatch = True
        except Exception as error:
            self.InteractiveHtmlBomIDPatch = False
            self.error = str(error)
            self.error_product_interactiveHtml()

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
            self.allowInstall_InteractiveHtml = True
            self.ui.pushButton_InstallPatch.setEnabled(True)
            self.InteractiveHtmlBomStatus = QPixmap(self.redirect_res("./src/blobdoctor.png"))
            self.ui.label_Emoji.setPixmap(self.InteractiveHtmlBomStatus)
            self.ui.label_status.setText("Check Environment Pass!")
            self.ui.pushButton_CheckEnvironment.setEnabled(False)
        else:
            self.error = "Check Environment Failed!"
            self.ui.label_status.setText("Not Found Cadence Production")
            self.allowInstall_InteractiveHtml = False
            self.ui.pushButton_InstallPatch.setEnabled(False)
            self.error_product_interactiveHtml()
        self.interactiveHtml_check_InteractiveHtmlBomId()
        self.interactiveHtml_check_exportJsonIDId()
        self.interactiveHtml_check_patchId()

    def install_loader(self, target_path: str):
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
            except:
                self.InteractiveHtmlBomLoader = False
        else:
            print("New Install")
        with open(start_file_path, "a") as f:
            f.write('\nloadi("exportJson.il" )\nloadi("jsonDecode.il" )\n')
            self.InteractiveHtmlBomLoader = True

    def install_core(self, main_path: str, home_path: str):
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
                        self.error = f"Source file {src_file} does not exist, skipping copy."
            else:
                self.error = f"Source directory {src_main} does not exist, skipping copy."
            core = os.path.join(main_path, "Main", "InteractiveHtmlBom")
            if os.path.exists(core):
                core_target = os.path.join(home_path, "InteractiveHtmlBom")
                shutil.copytree(core, core_target, dirs_exist_ok=True)
                runtime = os.path.join(main_path, "Main", "runtime")
                runtime_target = os.path.join(home_path, "InteractiveHtmlBom", "runtime")
                shutil.copytree(runtime, runtime_target, dirs_exist_ok=True)
            else:
                self.error = f"Source directory {src_main} does not exist, skipping copy."
            self.InteractiveHtmlBomCore = True
        except:
            self.InteractiveHtmlBomCore = False
            self.error_product_interactiveHtml()

    def submit_install_patch(self):
        if self.allowInstall_InteractiveHtml:
            try:
                self.interactiveHtml_generatePath()
            except Exception as error:
                self.error = f"Failed to generate Interactive Html Bom installation path. details: {error}"
                self.error_product_interactiveHtml()
            if self.InteractiveHtmlBomIDPatch:
                try:
                    self.install_loader(self.ui.lineEdit_CadenceDirectory.text())
                except Exception as error:
                    self.error = f"Failed to install Interactive Html Bom Loader. details: {traceback.format_exc()}"
                    self.error_product_interactiveHtml()
                if self.InteractiveHtmlBomLoader:
                    try:
                        work_dir = os.path.dirname(__file__)
                        self.install_core(work_dir, self.ui.lineEdit_CadenceDirectory.text())
                    except Exception as error:
                        self.error = f"Failed to install Interactive Html Bom Core. details: {traceback.format_exc()}"
                        self.error_product_interactiveHtml()
                    if self.InteractiveHtmlBomCore:
                        self.InteractiveHtmlBomStatus = QPixmap(self.redirect_res("./src/done.png"))
                        self.ui.label_Emoji.setPixmap(self.InteractiveHtmlBomStatus)
                        self.ui.label_status.setText("InteractiveHtml Install Done!")
                        self.ui.pushButton_InstallPatch.setEnabled(False)
        else:
            self.error = f"self.allowInstall_InteractiveHtml:{self.allowInstall_InteractiveHtml}"
            self.error_product_interactiveHtml()

    def error_product_interactiveHtml(self):
        self.ui.label_status.setText(self.error)
        self.product_pixMap = QPixmap(self.redirect_res("./src/error.png"))
        self.ui.label_Emoji.setPixmap(self.product_pixMap)

    def redirect_res(self, src_path: str):
        # if hasattr(sys, '_MEIPASS'):
        #     return os.path.join(getattr(sys, '_MEIPASS'), src_path)
        dst_path = os.path.join(os.path.dirname(__file__), src_path)
        return dst_path

    def resistors_parallel(self, r1: int, r2: int):
        total_value = 1 / (1 / r1 + 1 / r2)
        return total_value

    def submit_calculator_var(self):
        L2H = float(self.ui.lineEdit_CalculatorVar_L2H.text())
        H2L = float(self.ui.lineEdit_CalculatorVar_H2L.text())
        self.ui.lineEdit_CalculatorVar_TH.setText(str(format(H2L-L2H, ".3f")))
        if self.ui.checkBox_CalculatorVar_r1.isChecked():
            x = self.ui.doubleSpinBox_CalculatorVar_r1.value()
            y = Symbol('R2')
            z = Symbol('R3')
            v = float(self.ui.doubleSpinBox_CalculatorVar_Vref.value())
            fun1 = v * y * (x + z) / (x * z + y * (x + z)) - H2L
            fun2 = v * y * z / (y * z + x * (y + z)) - L2H
            z = solve([fun1, fun2], [y, z])
            # Render the calculation results to the UI
            self.ui.doubleSpinBox_CalculatorVar_r2.setValue(float(format(z[0][0], ".3f")))
            self.ui.doubleSpinBox_CalculatorVar_r3.setValue(float(format(z[0][1], ".3f")))
        elif self.ui.checkBox_CalculatorVar_r2.isChecked():
            x = Symbol('R1')
            y = self.ui.doubleSpinBox_CalculatorVar_r2.value()
            z = Symbol('R3')
            v = float(self.ui.doubleSpinBox_CalculatorVar_Vref.value())
            fun1 = v * y * (x + z) / (x * z + y * (x + z)) - H2L
            fun2 = v * y * z / (y * z + x * (y + z)) - L2H
            z = solve([fun1, fun2], [x, z])
            # Render the calculation results to the UI
            self.ui.doubleSpinBox_CalculatorVar_r1.setValue(float(format(z[0][0], ".3f")))
            self.ui.doubleSpinBox_CalculatorVar_r3.setValue(float(format(z[0][1], ".3f")))
        elif self.ui.checkBox_CalculatorVar_r3.isChecked():
            x = Symbol('R1')
            y = Symbol('R2')
            z = self.ui.doubleSpinBox_CalculatorVar_r3.value()
            v = float(self.ui.doubleSpinBox_CalculatorVar_Vref.value())
            fun1 = v * y * (x + z) / (x * z + y * (x + z)) - H2L
            fun2 = v * y * z / (y * z + x * (y + z)) - L2H
            z = solve([fun1, fun2], [x, y])
            # Render the calculation results to the UI
            self.ui.doubleSpinBox_CalculatorVar_r1.setValue(float(format(z[0][0], ".3f")))
            self.ui.doubleSpinBox_CalculatorVar_r2.setValue(float(format(z[1][1], ".3f")))

    def fixCheckBox_CalculatorVar_r1(self):
        if self.ui.checkBox_CalculatorVar_r1.isChecked():
            self.ui.doubleSpinBox_CalculatorVar_r1.setEnabled(True)
            self.ui.checkBox_CalculatorVar_r2.setChecked(False)
            self.ui.doubleSpinBox_CalculatorVar_r2.setEnabled(False)
            self.ui.checkBox_CalculatorVar_r3.setChecked(False)
            self.ui.doubleSpinBox_CalculatorVar_r3.setEnabled(False)

    def fixCheckBox_CalculatorVar_r2(self):
        if self.ui.checkBox_CalculatorVar_r2.isChecked():
            self.ui.doubleSpinBox_CalculatorVar_r2.setEnabled(True)
            self.ui.checkBox_CalculatorVar_r1.setChecked(False)
            self.ui.doubleSpinBox_CalculatorVar_r1.setEnabled(False)
            self.ui.checkBox_CalculatorVar_r3.setChecked(False)
            self.ui.doubleSpinBox_CalculatorVar_r3.setEnabled(False)

    def fixCheckBox_CalculatorVar_r3(self):
        if self.ui.checkBox_CalculatorVar_r3.isChecked():
            self.ui.doubleSpinBox_CalculatorVar_r3.setEnabled(True)
            self.ui.checkBox_CalculatorVar_r1.setChecked(False)
            self.ui.doubleSpinBox_CalculatorVar_r1.setEnabled(False)
            self.ui.checkBox_CalculatorVar_r2.setChecked(False)
            self.ui.doubleSpinBox_CalculatorVar_r2.setEnabled(False)

    def submit_calculator_hy(self):
        x = self.ui.doubleSpinBox_CalculatorHy_r1.value()
        y = self.ui.doubleSpinBox_CalculatorHy_r2.value()
        z = self.ui.doubleSpinBox_CalculatorHy_r3.value()
        v = self.ui.doubleSpinBox_CalculatorHy_Vref.value()
        L2H = Symbol('L2H')
        H2L = Symbol('H2L')
        fun1 = v * y / (self.resistors_parallel(x,z)+y) - H2L
        fun2 = v * (self.resistors_parallel(y,z))/(x+self.resistors_parallel(y,z)) - L2H
        z = solve([fun1, fun2], [L2H, H2L])
        # Render the calculation results to the UI
        self.ui.lineEdit_CalculatorHy_H2L.setText(str(format(z[H2L], ".3f")))
        self.ui.lineEdit_CalculatorHy_L2H.setText(str(format(z[L2H], ".3f")))
        self.ui.lineEdit_CalculatorHy_TH.setText(str(format(z[H2L]-z[L2H], ".3f")))





if __name__ == "__main__":
    # check_environment()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())