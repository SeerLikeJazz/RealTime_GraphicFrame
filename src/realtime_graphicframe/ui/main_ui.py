# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 795)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 500))
        self.frame_menu.setStyleSheet(u"text-align: left;")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_menu)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.listWidget = QListWidget(self.groupBox_3)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_10.addWidget(self.listWidget)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_search = QPushButton(self.groupBox_3)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(11)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setCheckable(False)

        self.horizontalLayout_8.addWidget(self.pushButton_search)

        self.pushButton_connect = QPushButton(self.groupBox_3)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy)
        self.pushButton_connect.setMinimumSize(QSize(0, 0))
        self.pushButton_connect.setMaximumSize(QSize(16777215, 40))
        self.pushButton_connect.setFont(font)
        self.pushButton_connect.setInputMethodHints(Qt.ImhSensitiveData)
        self.pushButton_connect.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.pushButton_connect, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.pushButton_start = QPushButton(self.groupBox_3)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(120, 40))
        self.pushButton_start.setMaximumSize(QSize(120, 40))
        self.pushButton_start.setFont(font)
        self.pushButton_start.setInputMethodHints(Qt.ImhNone)
        self.pushButton_start.setCheckable(True)

        self.verticalLayout_10.addWidget(self.pushButton_start)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_9.addWidget(self.lineEdit)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(120, 25))
        self.pushButton_3.setMaximumSize(QSize(120, 25))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_9.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 25))
        self.pushButton_2.setMaximumSize(QSize(120, 25))

        self.verticalLayout_8.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Scale = QGroupBox(self.tab_2)
        self.Scale.setObjectName(u"Scale")
        self.verticalLayout_11 = QVBoxLayout(self.Scale)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.Scale)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.comboBox_timescale = QComboBox(self.Scale)
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.addItem("")
        self.comboBox_timescale.setObjectName(u"comboBox_timescale")
        self.comboBox_timescale.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_6.addWidget(self.comboBox_timescale)

        self.label_9 = QLabel(self.Scale)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.Scale)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.comboBox_vertscale = QComboBox(self.Scale)
        self.comboBox_vertscale.addItem("")
        self.comboBox_vertscale.addItem("")
        self.comboBox_vertscale.addItem("")
        self.comboBox_vertscale.addItem("")
        self.comboBox_vertscale.addItem("")
        self.comboBox_vertscale.setObjectName(u"comboBox_vertscale")
        self.comboBox_vertscale.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_7.addWidget(self.comboBox_vertscale)

        self.label_11 = QLabel(self.Scale)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.label_11)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)


        self.verticalLayout_3.addWidget(self.Scale)

        self.groupBox_filter = QGroupBox(self.tab_2)
        self.groupBox_filter.setObjectName(u"groupBox_filter")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_filter)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox_filter)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_highpass = QComboBox(self.groupBox_filter)
        self.comboBox_highpass.addItem("")
        self.comboBox_highpass.addItem("")
        self.comboBox_highpass.addItem("")
        self.comboBox_highpass.addItem("")
        self.comboBox_highpass.addItem("")
        self.comboBox_highpass.setObjectName(u"comboBox_highpass")

        self.horizontalLayout_2.addWidget(self.comboBox_highpass)

        self.label = QLabel(self.groupBox_filter)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.groupBox_filter)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox_lowpass = QComboBox(self.groupBox_filter)
        self.comboBox_lowpass.addItem("")
        self.comboBox_lowpass.addItem("")
        self.comboBox_lowpass.addItem("")
        self.comboBox_lowpass.addItem("")
        self.comboBox_lowpass.setObjectName(u"comboBox_lowpass")

        self.horizontalLayout_3.addWidget(self.comboBox_lowpass)

        self.label_2 = QLabel(self.groupBox_filter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_filter)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.comboBox_notch = QComboBox(self.groupBox_filter)
        self.comboBox_notch.addItem("")
        self.comboBox_notch.addItem("")
        self.comboBox_notch.addItem("")
        self.comboBox_notch.setObjectName(u"comboBox_notch")

        self.horizontalLayout_5.addWidget(self.comboBox_notch)

        self.label_7 = QLabel(self.groupBox_filter)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.label_7)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_filter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy1)
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_main)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setLineWidth(0)
        self.page_signal = QWidget()
        self.page_signal.setObjectName(u"page_signal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_signal.sizePolicy().hasHeightForWidth())
        self.page_signal.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.page_signal)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.GroupBox_signal = QGroupBox(self.page_signal)
        self.GroupBox_signal.setObjectName(u"GroupBox_signal")
        sizePolicy2.setHeightForWidth(self.GroupBox_signal.sizePolicy().hasHeightForWidth())
        self.GroupBox_signal.setSizePolicy(sizePolicy2)
        self.GroupBox_signal.setFocusPolicy(Qt.ClickFocus)
        self.GroupBox_signal.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.GroupBox_signal.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.horizontalLayout_4 = QHBoxLayout(self.GroupBox_signal)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_plot = QGridLayout()
        self.gridLayout_plot.setObjectName(u"gridLayout_plot")
        self.gridLayout_plot.setHorizontalSpacing(0)
        self.gridLayout_plot.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addLayout(self.gridLayout_plot)

        self.horizontalLayout_4.setStretch(0, 9)

        self.verticalLayout_4.addWidget(self.GroupBox_signal)

        self.verticalLayout_4.setStretch(0, 9)
        self.stackedWidget.addWidget(self.page_signal)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_main)

        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.comboBox_timescale.setCurrentIndex(4)
        self.comboBox_vertscale.setCurrentIndex(4)
        self.comboBox_highpass.setCurrentIndex(0)
        self.comboBox_lowpass.setCurrentIndex(0)
        self.comboBox_notch.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MEMS Mirror Scanning", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Data Recording", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"LabStreamingLayer", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start streaming", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Device", None))
        self.Scale.setTitle(QCoreApplication.translate("MainWindow", u"Scale", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.comboBox_timescale.setItemText(0, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_timescale.setItemText(1, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox_timescale.setItemText(2, QCoreApplication.translate("MainWindow", u"100", None))
        self.comboBox_timescale.setItemText(3, QCoreApplication.translate("MainWindow", u"200", None))
        self.comboBox_timescale.setItemText(4, QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBox_timescale.setItemText(5, QCoreApplication.translate("MainWindow", u"1000", None))
        self.comboBox_timescale.setItemText(6, QCoreApplication.translate("MainWindow", u"4000", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Vert", None))
        self.comboBox_vertscale.setItemText(0, QCoreApplication.translate("MainWindow", u"10mV", None))
        self.comboBox_vertscale.setItemText(1, QCoreApplication.translate("MainWindow", u"25mV", None))
        self.comboBox_vertscale.setItemText(2, QCoreApplication.translate("MainWindow", u"50mV", None))
        self.comboBox_vertscale.setItemText(3, QCoreApplication.translate("MainWindow", u"100mV", None))
        self.comboBox_vertscale.setItemText(4, QCoreApplication.translate("MainWindow", u"200mV", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"/Div", None))
        self.groupBox_filter.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"High Pass", None))
        self.comboBox_highpass.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_highpass.setItemText(1, QCoreApplication.translate("MainWindow", u"0.1", None))
        self.comboBox_highpass.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_highpass.setItemText(3, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_highpass.setItemText(4, QCoreApplication.translate("MainWindow", u"20", None))

        self.comboBox_highpass.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Low Pass", None))
        self.comboBox_lowpass.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_lowpass.setItemText(1, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_lowpass.setItemText(2, QCoreApplication.translate("MainWindow", u"40", None))
        self.comboBox_lowpass.setItemText(3, QCoreApplication.translate("MainWindow", u"70", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Notch", None))
        self.comboBox_notch.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_notch.setItemText(1, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox_notch.setItemText(2, QCoreApplication.translate("MainWindow", u"60", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Display", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Channels", None))
        self.GroupBox_signal.setTitle(QCoreApplication.translate("MainWindow", u"EEG Signal(100\u00b5V/Div-2s/page)", None))
    # retranslateUi

