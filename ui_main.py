# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 651)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.PendingActivation = QWidget()
        self.PendingActivation.setObjectName(u"PendingActivation")
        self.gridLayout_5 = QGridLayout(self.PendingActivation)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(200, 60, 200, 60)
        self.verticalLayout_ProductSelect = QVBoxLayout()
        self.verticalLayout_ProductSelect.setObjectName(u"verticalLayout_ProductSelect")
        self.product_emoji = QLabel(self.PendingActivation)
        self.product_emoji.setObjectName(u"product_emoji")
        self.product_emoji.setPixmap(QPixmap(u"src/PendingActivation.png"))
        self.product_emoji.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_ProductSelect.addWidget(self.product_emoji)

        self.label_info = QLabel(self.PendingActivation)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_ProductSelect.addWidget(self.label_info)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_ActiveID = QLineEdit(self.PendingActivation)
        self.lineEdit_ActiveID.setObjectName(u"lineEdit_ActiveID")
        self.lineEdit_ActiveID.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_ActiveID, 1, 1, 1, 1)

        self.lineEdit_PendingIdentityID = QLineEdit(self.PendingActivation)
        self.lineEdit_PendingIdentityID.setObjectName(u"lineEdit_PendingIdentityID")
        self.lineEdit_PendingIdentityID.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_PendingIdentityID, 0, 1, 1, 1)

        self.label_SelectProduct = QLabel(self.PendingActivation)
        self.label_SelectProduct.setObjectName(u"label_SelectProduct")
        self.label_SelectProduct.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_SelectProduct, 2, 0, 1, 1)

        self.label_PendingIdentityID = QLabel(self.PendingActivation)
        self.label_PendingIdentityID.setObjectName(u"label_PendingIdentityID")
        self.label_PendingIdentityID.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_PendingIdentityID, 0, 0, 1, 1)

        self.label_Author = QLabel(self.PendingActivation)
        self.label_Author.setObjectName(u"label_Author")
        self.label_Author.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_Author, 4, 0, 1, 2)

        self.pushButton_SelectProduct = QPushButton(self.PendingActivation)
        self.pushButton_SelectProduct.setObjectName(u"pushButton_SelectProduct")
        self.pushButton_SelectProduct.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.pushButton_SelectProduct, 3, 0, 1, 2)

        self.label_LastUpdate = QLabel(self.PendingActivation)
        self.label_LastUpdate.setObjectName(u"label_LastUpdate")
        self.label_LastUpdate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_LastUpdate, 5, 0, 1, 2)

        self.comboBox_SelectProduct = QComboBox(self.PendingActivation)
        self.comboBox_SelectProduct.addItem("")
        self.comboBox_SelectProduct.setObjectName(u"comboBox_SelectProduct")
        self.comboBox_SelectProduct.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.comboBox_SelectProduct, 2, 1, 1, 1)

        self.label_ActiveID = QLabel(self.PendingActivation)
        self.label_ActiveID.setObjectName(u"label_ActiveID")
        self.label_ActiveID.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.label_ActiveID, 1, 0, 1, 1)


        self.verticalLayout_ProductSelect.addLayout(self.gridLayout_4)


        self.gridLayout_5.addLayout(self.verticalLayout_ProductSelect, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PendingActivation)
        self.InteractiveHtmlSetup = QWidget()
        self.InteractiveHtmlSetup.setObjectName(u"InteractiveHtmlSetup")
        self.gridLayout_3 = QGridLayout(self.InteractiveHtmlSetup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(160, 20, 160, 60)
        self.verticalLayout_setup = QVBoxLayout()
        self.verticalLayout_setup.setObjectName(u"verticalLayout_setup")
        self.label_Emoji = QLabel(self.InteractiveHtmlSetup)
        self.label_Emoji.setObjectName(u"label_Emoji")
        self.label_Emoji.setPixmap(QPixmap(u"src/welcom.png"))
        self.label_Emoji.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Emoji.setWordWrap(True)

        self.verticalLayout_setup.addWidget(self.label_Emoji)

        self.label_status = QLabel(self.InteractiveHtmlSetup)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_setup.addWidget(self.label_status)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_InteractiveHtmlBomID = QLineEdit(self.InteractiveHtmlSetup)
        self.lineEdit_InteractiveHtmlBomID.setObjectName(u"lineEdit_InteractiveHtmlBomID")
        self.lineEdit_InteractiveHtmlBomID.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.lineEdit_InteractiveHtmlBomID, 1, 1, 1, 1)

        self.lineEdit_CadenceDirectory = QLineEdit(self.InteractiveHtmlSetup)
        self.lineEdit_CadenceDirectory.setObjectName(u"lineEdit_CadenceDirectory")
        self.lineEdit_CadenceDirectory.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.lineEdit_CadenceDirectory, 0, 1, 1, 1)

        self.label_PatchID = QLabel(self.InteractiveHtmlSetup)
        self.label_PatchID.setObjectName(u"label_PatchID")
        self.label_PatchID.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_PatchID, 3, 0, 1, 1)

        self.label_CadenceDirectory = QLabel(self.InteractiveHtmlSetup)
        self.label_CadenceDirectory.setObjectName(u"label_CadenceDirectory")
        self.label_CadenceDirectory.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_CadenceDirectory, 0, 0, 1, 1)

        self.label_InteractiveHtmlBomID = QLabel(self.InteractiveHtmlSetup)
        self.label_InteractiveHtmlBomID.setObjectName(u"label_InteractiveHtmlBomID")
        self.label_InteractiveHtmlBomID.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_InteractiveHtmlBomID, 1, 0, 1, 1)

        self.lineEdit_exportJsonID = QLineEdit(self.InteractiveHtmlSetup)
        self.lineEdit_exportJsonID.setObjectName(u"lineEdit_exportJsonID")
        self.lineEdit_exportJsonID.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.lineEdit_exportJsonID, 2, 1, 1, 1)

        self.label_exportJsonID = QLabel(self.InteractiveHtmlSetup)
        self.label_exportJsonID.setObjectName(u"label_exportJsonID")
        self.label_exportJsonID.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_exportJsonID, 2, 0, 1, 1)

        self.lineEdit_PatchID = QLineEdit(self.InteractiveHtmlSetup)
        self.lineEdit_PatchID.setObjectName(u"lineEdit_PatchID")
        self.lineEdit_PatchID.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.lineEdit_PatchID, 3, 1, 1, 1)


        self.verticalLayout_setup.addLayout(self.gridLayout_2)

        self.pushButton_CheckEnvironment = QPushButton(self.InteractiveHtmlSetup)
        self.pushButton_CheckEnvironment.setObjectName(u"pushButton_CheckEnvironment")
        self.pushButton_CheckEnvironment.setMinimumSize(QSize(80, 40))
        font = QFont()
        font.setBold(False)
        font.setUnderline(False)
        self.pushButton_CheckEnvironment.setFont(font)
        self.pushButton_CheckEnvironment.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_CheckEnvironment.setMouseTracking(True)
        self.pushButton_CheckEnvironment.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_CheckEnvironment.setCheckable(False)

        self.verticalLayout_setup.addWidget(self.pushButton_CheckEnvironment)

        self.pushButton_InstallPatch = QPushButton(self.InteractiveHtmlSetup)
        self.pushButton_InstallPatch.setObjectName(u"pushButton_InstallPatch")
        self.pushButton_InstallPatch.setMinimumSize(QSize(80, 40))
        self.pushButton_InstallPatch.setCheckable(False)
        self.pushButton_InstallPatch.setChecked(False)

        self.verticalLayout_setup.addWidget(self.pushButton_InstallPatch)

        self.CadenceInteractiveHtmlAbout = QLabel(self.InteractiveHtmlSetup)
        self.CadenceInteractiveHtmlAbout.setObjectName(u"CadenceInteractiveHtmlAbout")
        self.CadenceInteractiveHtmlAbout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_setup.addWidget(self.CadenceInteractiveHtmlAbout)


        self.verticalLayout.addLayout(self.verticalLayout_setup)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.InteractiveHtmlSetup)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.product_emoji.setText("")
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Before entering the user interface, \n"
"you need to enter the activation ID and \n"
"select the product", None))
        self.label_SelectProduct.setText(QCoreApplication.translate("MainWindow", u"Select Product", None))
        self.label_PendingIdentityID.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.label_Author.setText(QCoreApplication.translate("MainWindow", u"Designed by github.com@Sodeug", None))
        self.pushButton_SelectProduct.setText(QCoreApplication.translate("MainWindow", u"Select Product", None))
        self.label_LastUpdate.setText(QCoreApplication.translate("MainWindow", u"Last Update Date: 2025/09/06", None))
        self.comboBox_SelectProduct.setItemText(0, QCoreApplication.translate("MainWindow", u"InteractiveHtml", None))

        self.label_ActiveID.setText(QCoreApplication.translate("MainWindow", u"Active ID", None))
        self.label_Emoji.setText("")
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status: Ready...", None))
        self.label_PatchID.setText(QCoreApplication.translate("MainWindow", u"Patch ID", None))
        self.label_CadenceDirectory.setText(QCoreApplication.translate("MainWindow", u"Cadence Directory", None))
        self.label_InteractiveHtmlBomID.setText(QCoreApplication.translate("MainWindow", u"InteractiveHtmlBom ID", None))
        self.label_exportJsonID.setText(QCoreApplication.translate("MainWindow", u"exportJson ID", None))
        self.pushButton_CheckEnvironment.setText(QCoreApplication.translate("MainWindow", u"Check Environment", None))
#if QT_CONFIG(shortcut)
        self.pushButton_CheckEnvironment.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_InstallPatch.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.CadenceInteractiveHtmlAbout.setText(QCoreApplication.translate("MainWindow", u"UI\n"
"github.com@SoDebug\n"
"Credits\n"
"github.com@openscopeproject\\InteractiveHtmlBom\n"
"github.com@juulsA\\exportJson", None))
    # retranslateUi

