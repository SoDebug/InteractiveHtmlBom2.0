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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 651)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_info.setWordWrap(True)

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
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_status.setWordWrap(True)

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
        self.PN_16702A = QWidget()
        self.PN_16702A.setObjectName(u"PN_16702A")
        self.gridLayout_6 = QGridLayout(self.PN_16702A)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.PN_16702A)
        self.tabWidget.setObjectName(u"tabWidget")
        self.TLV185x_Calculator = QWidget()
        self.TLV185x_Calculator.setObjectName(u"TLV185x_Calculator")
        self.gridLayout_7 = QGridLayout(self.TLV185x_Calculator)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.CalculatorHy = QGroupBox(self.TLV185x_Calculator)
        self.CalculatorHy.setObjectName(u"CalculatorHy")
        self.gridLayout_9 = QGridLayout(self.CalculatorHy)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.doubleSpinBox_CalculatorHy_Vref = QDoubleSpinBox(self.CalculatorHy)
        self.doubleSpinBox_CalculatorHy_Vref.setObjectName(u"doubleSpinBox_CalculatorHy_Vref")
        self.doubleSpinBox_CalculatorHy_Vref.setDecimals(5)

        self.gridLayout_10.addWidget(self.doubleSpinBox_CalculatorHy_Vref, 0, 1, 1, 1)

        self.label_CalculatorHy_TH = QLabel(self.CalculatorHy)
        self.label_CalculatorHy_TH.setObjectName(u"label_CalculatorHy_TH")

        self.gridLayout_10.addWidget(self.label_CalculatorHy_TH, 6, 0, 1, 1)

        self.label_CalculatorHy_Vref = QLabel(self.CalculatorHy)
        self.label_CalculatorHy_Vref.setObjectName(u"label_CalculatorHy_Vref")

        self.gridLayout_10.addWidget(self.label_CalculatorHy_Vref, 0, 0, 1, 1)

        self.doubleSpinBox_CalculatorHy_r3 = QDoubleSpinBox(self.CalculatorHy)
        self.doubleSpinBox_CalculatorHy_r3.setObjectName(u"doubleSpinBox_CalculatorHy_r3")
        self.doubleSpinBox_CalculatorHy_r3.setMaximum(9999999.990000000223517)

        self.gridLayout_10.addWidget(self.doubleSpinBox_CalculatorHy_r3, 3, 1, 1, 1)

        self.label_CalculatorHy_H2L = QLabel(self.CalculatorHy)
        self.label_CalculatorHy_H2L.setObjectName(u"label_CalculatorHy_H2L")

        self.gridLayout_10.addWidget(self.label_CalculatorHy_H2L, 4, 0, 1, 1)

        self.lineEdit_CalculatorHy_L2H = QLineEdit(self.CalculatorHy)
        self.lineEdit_CalculatorHy_L2H.setObjectName(u"lineEdit_CalculatorHy_L2H")

        self.gridLayout_10.addWidget(self.lineEdit_CalculatorHy_L2H, 5, 1, 1, 1)

        self.label_CalculatorHy_L2H = QLabel(self.CalculatorHy)
        self.label_CalculatorHy_L2H.setObjectName(u"label_CalculatorHy_L2H")

        self.gridLayout_10.addWidget(self.label_CalculatorHy_L2H, 5, 0, 1, 1)

        self.lineEdit_CalculatorHy_H2L = QLineEdit(self.CalculatorHy)
        self.lineEdit_CalculatorHy_H2L.setObjectName(u"lineEdit_CalculatorHy_H2L")

        self.gridLayout_10.addWidget(self.lineEdit_CalculatorHy_H2L, 4, 1, 1, 1)

        self.lineEdit_CalculatorHy_TH = QLineEdit(self.CalculatorHy)
        self.lineEdit_CalculatorHy_TH.setObjectName(u"lineEdit_CalculatorHy_TH")

        self.gridLayout_10.addWidget(self.lineEdit_CalculatorHy_TH, 6, 1, 1, 1)

        self.doubleSpinBox_CalculatorHy_r2 = QDoubleSpinBox(self.CalculatorHy)
        self.doubleSpinBox_CalculatorHy_r2.setObjectName(u"doubleSpinBox_CalculatorHy_r2")
        self.doubleSpinBox_CalculatorHy_r2.setMaximum(9999999.990000000223517)

        self.gridLayout_10.addWidget(self.doubleSpinBox_CalculatorHy_r2, 2, 1, 1, 1)

        self.label_CalculatorHy_r3 = QLabel(self.CalculatorHy)
        self.label_CalculatorHy_r3.setObjectName(u"label_CalculatorHy_r3")

        self.gridLayout_10.addWidget(self.label_CalculatorHy_r3, 3, 0, 1, 1)

        self.label_CalculatorHy_r2 = QLabel(self.CalculatorHy)
        self.label_CalculatorHy_r2.setObjectName(u"label_CalculatorHy_r2")

        self.gridLayout_10.addWidget(self.label_CalculatorHy_r2, 2, 0, 1, 1)

        self.label_CalculatorHy_r1 = QLabel(self.CalculatorHy)
        self.label_CalculatorHy_r1.setObjectName(u"label_CalculatorHy_r1")

        self.gridLayout_10.addWidget(self.label_CalculatorHy_r1, 1, 0, 1, 1)

        self.doubleSpinBox_CalculatorHy_r1 = QDoubleSpinBox(self.CalculatorHy)
        self.doubleSpinBox_CalculatorHy_r1.setObjectName(u"doubleSpinBox_CalculatorHy_r1")
        self.doubleSpinBox_CalculatorHy_r1.setMaximum(9999999.990000000223517)

        self.gridLayout_10.addWidget(self.doubleSpinBox_CalculatorHy_r1, 1, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.pushButton_CalculatorHy_RUN = QPushButton(self.CalculatorHy)
        self.pushButton_CalculatorHy_RUN.setObjectName(u"pushButton_CalculatorHy_RUN")

        self.gridLayout_9.addWidget(self.pushButton_CalculatorHy_RUN, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.CalculatorHy, 0, 0, 1, 1)

        self.CalculatorVar = QGroupBox(self.TLV185x_Calculator)
        self.CalculatorVar.setObjectName(u"CalculatorVar")
        self.gridLayout_11 = QGridLayout(self.CalculatorVar)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.doubleSpinBox_CalculatorVar_r3 = QDoubleSpinBox(self.CalculatorVar)
        self.doubleSpinBox_CalculatorVar_r3.setObjectName(u"doubleSpinBox_CalculatorVar_r3")
        self.doubleSpinBox_CalculatorVar_r3.setMaximum(9999999.990000000223517)

        self.gridLayout_8.addWidget(self.doubleSpinBox_CalculatorVar_r3, 3, 1, 1, 1)

        self.label_CalculatorVar_H2L = QLabel(self.CalculatorVar)
        self.label_CalculatorVar_H2L.setObjectName(u"label_CalculatorVar_H2L")

        self.gridLayout_8.addWidget(self.label_CalculatorVar_H2L, 4, 0, 1, 1)

        self.label_CalculatorVar_TH = QLabel(self.CalculatorVar)
        self.label_CalculatorVar_TH.setObjectName(u"label_CalculatorVar_TH")

        self.gridLayout_8.addWidget(self.label_CalculatorVar_TH, 6, 0, 1, 1)

        self.doubleSpinBox_CalculatorVar_r1 = QDoubleSpinBox(self.CalculatorVar)
        self.doubleSpinBox_CalculatorVar_r1.setObjectName(u"doubleSpinBox_CalculatorVar_r1")
        self.doubleSpinBox_CalculatorVar_r1.setMaximum(9999999.990000000223517)

        self.gridLayout_8.addWidget(self.doubleSpinBox_CalculatorVar_r1, 1, 1, 1, 1)

        self.label_CalculatorVar_r3 = QLabel(self.CalculatorVar)
        self.label_CalculatorVar_r3.setObjectName(u"label_CalculatorVar_r3")

        self.gridLayout_8.addWidget(self.label_CalculatorVar_r3, 3, 0, 1, 1)

        self.doubleSpinBox_CalculatorVar_r2 = QDoubleSpinBox(self.CalculatorVar)
        self.doubleSpinBox_CalculatorVar_r2.setObjectName(u"doubleSpinBox_CalculatorVar_r2")
        self.doubleSpinBox_CalculatorVar_r2.setMaximum(9999999.990000000223517)

        self.gridLayout_8.addWidget(self.doubleSpinBox_CalculatorVar_r2, 2, 1, 1, 1)

        self.label_CalculatorVar_r2 = QLabel(self.CalculatorVar)
        self.label_CalculatorVar_r2.setObjectName(u"label_CalculatorVar_r2")

        self.gridLayout_8.addWidget(self.label_CalculatorVar_r2, 2, 0, 1, 1)

        self.label_CalculatorVar_r1 = QLabel(self.CalculatorVar)
        self.label_CalculatorVar_r1.setObjectName(u"label_CalculatorVar_r1")

        self.gridLayout_8.addWidget(self.label_CalculatorVar_r1, 1, 0, 1, 1)

        self.label_CalculatorVar_L2H = QLabel(self.CalculatorVar)
        self.label_CalculatorVar_L2H.setObjectName(u"label_CalculatorVar_L2H")

        self.gridLayout_8.addWidget(self.label_CalculatorVar_L2H, 5, 0, 1, 1)

        self.label_CalculatorVar_Vref = QLabel(self.CalculatorVar)
        self.label_CalculatorVar_Vref.setObjectName(u"label_CalculatorVar_Vref")

        self.gridLayout_8.addWidget(self.label_CalculatorVar_Vref, 0, 0, 1, 1)

        self.checkBox_CalculatorVar_r1 = QCheckBox(self.CalculatorVar)
        self.checkBox_CalculatorVar_r1.setObjectName(u"checkBox_CalculatorVar_r1")

        self.gridLayout_8.addWidget(self.checkBox_CalculatorVar_r1, 1, 2, 1, 1)

        self.checkBox_CalculatorVar_r2 = QCheckBox(self.CalculatorVar)
        self.checkBox_CalculatorVar_r2.setObjectName(u"checkBox_CalculatorVar_r2")

        self.gridLayout_8.addWidget(self.checkBox_CalculatorVar_r2, 2, 2, 1, 1)

        self.checkBox_CalculatorVar_r3 = QCheckBox(self.CalculatorVar)
        self.checkBox_CalculatorVar_r3.setObjectName(u"checkBox_CalculatorVar_r3")

        self.gridLayout_8.addWidget(self.checkBox_CalculatorVar_r3, 3, 2, 1, 1)

        self.doubleSpinBox_CalculatorVar_Vref = QDoubleSpinBox(self.CalculatorVar)
        self.doubleSpinBox_CalculatorVar_Vref.setObjectName(u"doubleSpinBox_CalculatorVar_Vref")
        self.doubleSpinBox_CalculatorVar_Vref.setDecimals(5)

        self.gridLayout_8.addWidget(self.doubleSpinBox_CalculatorVar_Vref, 0, 1, 1, 2)

        self.lineEdit_CalculatorVar_TH = QLineEdit(self.CalculatorVar)
        self.lineEdit_CalculatorVar_TH.setObjectName(u"lineEdit_CalculatorVar_TH")

        self.gridLayout_8.addWidget(self.lineEdit_CalculatorVar_TH, 6, 1, 1, 2)

        self.lineEdit_CalculatorVar_H2L = QLineEdit(self.CalculatorVar)
        self.lineEdit_CalculatorVar_H2L.setObjectName(u"lineEdit_CalculatorVar_H2L")

        self.gridLayout_8.addWidget(self.lineEdit_CalculatorVar_H2L, 4, 1, 1, 2)

        self.lineEdit_CalculatorVar_L2H = QLineEdit(self.CalculatorVar)
        self.lineEdit_CalculatorVar_L2H.setObjectName(u"lineEdit_CalculatorVar_L2H")

        self.gridLayout_8.addWidget(self.lineEdit_CalculatorVar_L2H, 5, 1, 1, 2)


        self.gridLayout_11.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.pushButton_CalculatorVar_RUN = QPushButton(self.CalculatorVar)
        self.pushButton_CalculatorVar_RUN.setObjectName(u"pushButton_CalculatorVar_RUN")

        self.gridLayout_11.addWidget(self.pushButton_CalculatorVar_RUN, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.CalculatorVar, 0, 1, 1, 1)

        self.tabWidget.addTab(self.TLV185x_Calculator, "")
        self.PythonExec = QWidget()
        self.PythonExec.setObjectName(u"PythonExec")
        self.tabWidget.addTab(self.PythonExec, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PN_16702A)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 813, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


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
        self.comboBox_SelectProduct.setItemText(0, QCoreApplication.translate("MainWindow", u"InteractiveHtml(Cadence)", None))
        self.comboBox_SelectProduct.setItemText(1, QCoreApplication.translate("MainWindow", u"Inverting Hysteresis Comparator", None))

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
        self.CalculatorHy.setTitle(QCoreApplication.translate("MainWindow", u"Calculator Hy From Variables(R1\u3001R2\u3001R3)", None))
        self.label_CalculatorHy_TH.setText(QCoreApplication.translate("MainWindow", u"Total Hysteresis(V)", None))
        self.label_CalculatorHy_Vref.setText(QCoreApplication.translate("MainWindow", u"Vref(V)", None))
        self.label_CalculatorHy_H2L.setText(QCoreApplication.translate("MainWindow", u"High-to-Low Trip Voltage(V)", None))
        self.label_CalculatorHy_L2H.setText(QCoreApplication.translate("MainWindow", u"Low-to-High Trip Voltage(V)", None))
        self.label_CalculatorHy_r3.setText(QCoreApplication.translate("MainWindow", u"R3(ohm)", None))
        self.label_CalculatorHy_r2.setText(QCoreApplication.translate("MainWindow", u"R2(ohm)", None))
        self.label_CalculatorHy_r1.setText(QCoreApplication.translate("MainWindow", u"R1(ohm)", None))
        self.pushButton_CalculatorHy_RUN.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.CalculatorVar.setTitle(QCoreApplication.translate("MainWindow", u"Calculator Variables(R1\u3001R2\u3001R3) from Hy", None))
        self.label_CalculatorVar_H2L.setText(QCoreApplication.translate("MainWindow", u"High-to-Low Trip Voltage(V)", None))
        self.label_CalculatorVar_TH.setText(QCoreApplication.translate("MainWindow", u"Total Hysteresis(V)", None))
        self.label_CalculatorVar_r3.setText(QCoreApplication.translate("MainWindow", u"R3(ohm)", None))
        self.label_CalculatorVar_r2.setText(QCoreApplication.translate("MainWindow", u"R2(ohm)", None))
        self.label_CalculatorVar_r1.setText(QCoreApplication.translate("MainWindow", u"R1(ohm)", None))
        self.label_CalculatorVar_L2H.setText(QCoreApplication.translate("MainWindow", u"Low-to-High Trip Voltage(V)", None))
        self.label_CalculatorVar_Vref.setText(QCoreApplication.translate("MainWindow", u"Vref(V)", None))
        self.checkBox_CalculatorVar_r1.setText(QCoreApplication.translate("MainWindow", u"Uss Fixed Value", None))
        self.checkBox_CalculatorVar_r2.setText(QCoreApplication.translate("MainWindow", u"Uss Fixed Value", None))
        self.checkBox_CalculatorVar_r3.setText(QCoreApplication.translate("MainWindow", u"Uss Fixed Value", None))
        self.pushButton_CalculatorVar_RUN.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TLV185x_Calculator), QCoreApplication.translate("MainWindow", u"TLV185x Calculator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PythonExec), QCoreApplication.translate("MainWindow", u"Python Exec", None))
    # retranslateUi

