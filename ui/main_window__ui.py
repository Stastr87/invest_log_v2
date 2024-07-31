# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(858, 1114)
        self.open_table_view = QAction(MainWindow)
        self.open_table_view.setObjectName(u"open_table_view")
        self.open_test_panel = QAction(MainWindow)
        self.open_test_panel.setObjectName(u"open_test_panel")
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.general_widget = QWidget(self.centralwidget)
        self.general_widget.setObjectName(u"general_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.general_widget.sizePolicy().hasHeightForWidth())
        self.general_widget.setSizePolicy(sizePolicy)
        self.general_widget.setMinimumSize(QSize(840, 0))
        self.general_widget.setContextMenuPolicy(Qt.NoContextMenu)
        self.general_widget.setStyleSheet(u"border: solid 1px;\n"
"border-radius: 7px;\n"
"background-color: rgb(235,235,235);")
        self.frame_3 = QFrame(self.general_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(230, 13, 211, 91))
        self.frame_3.setMinimumSize(QSize(181, 91))
        self.frame_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_3.setStyleSheet(u"QFrame{border: 1px solid;\n"
"border-radius: 15px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);\n"
"}\n"
"QFrame:hover {border: 1px solid;\n"
"border-color: rgb(220, 220,220);}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3_label = QLabel(self.frame_3)
        self.frame_3_label.setObjectName(u"frame_3_label")
        self.frame_3_label.setGeometry(QRect(4, 0, 201, 21))
        self.frame_3_label.setMinimumSize(QSize(151, 21))
        self.frame_3_label.setStyleSheet(u"QLabel{border-style: solid;\n"
"border-width: 0px;\n"
"border-color: black;\n"
"font-weight:bolt;\n"
"font-size:12pt;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_3_label.setFrameShape(QFrame.Panel)
        self.frame_3_label.setFrameShadow(QFrame.Plain)
        self.frame_3_label.setLineWidth(-1)
        self.frame_3_label.setMidLineWidth(-1)
        self.frame_3_label.setTextFormat(Qt.PlainText)
        self.frame_3_label.setAlignment(Qt.AlignCenter)
        self.frame_3_label.setWordWrap(True)
        self.frame_3_label.setMargin(-1)
        self.frame_1 = QFrame(self.general_widget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setGeometry(QRect(12, 13, 211, 91))
        self.frame_1.setMinimumSize(QSize(181, 91))
        self.frame_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_1.setStyleSheet(u"QFrame{border: 1px solid;\n"
"border-radius: 15px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);\n"
"}\n"
"QFrame:hover {border: 1px solid;\n"
"border-color: rgb(220, 220,220);}")
        self.frame_1.setFrameShape(QFrame.Panel)
        self.frame_1.setFrameShadow(QFrame.Plain)
        self.frame_1_label = QLabel(self.frame_1)
        self.frame_1_label.setObjectName(u"frame_1_label")
        self.frame_1_label.setGeometry(QRect(10, 0, 191, 21))
        self.frame_1_label.setMinimumSize(QSize(151, 21))
        self.frame_1_label.setStyleSheet(u"QLabel {border-style: solid;\n"
"                border-width: 0px;\n"
"               border-color: black;\n"
"               font-weight:bolt;\n"
"               font-size:12pt;\n"
"background-color: rgba(0, 0, 0, 0);}\n"
"\n"
"\n"
"")
        self.frame_1_label.setFrameShape(QFrame.Panel)
        self.frame_1_label.setFrameShadow(QFrame.Plain)
        self.frame_1_label.setLineWidth(-1)
        self.frame_1_label.setMidLineWidth(-1)
        self.frame_1_label.setAlignment(Qt.AlignCenter)
        self.total_maney_value_label = QLabel(self.frame_1)
        self.total_maney_value_label.setObjectName(u"total_maney_value_label")
        self.total_maney_value_label.setGeometry(QRect(10, 40, 191, 21))
        self.total_maney_value_label.setMinimumSize(QSize(151, 21))
        self.total_maney_value_label.setStyleSheet(u"QLabel {border-style: solid;\n"
"                border-width: 0px;\n"
"               border-color: black;\n"
"               font-weight:bolt;\n"
"               font-size:14pt;\n"
"background-color: rgba(0, 0, 0, 0);}\n"
"\n"
"\n"
"")
        self.total_maney_value_label.setFrameShape(QFrame.Panel)
        self.total_maney_value_label.setFrameShadow(QFrame.Plain)
        self.total_maney_value_label.setLineWidth(-1)
        self.total_maney_value_label.setMidLineWidth(-1)
        self.total_maney_value_label.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.general_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(12, 112, 211, 91))
        self.frame_2.setMinimumSize(QSize(181, 91))
        self.frame_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_2.setStyleSheet(u"QFrame{border: 1px solid;\n"
"border-radius: 15px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);\n"
"}\n"
"QFrame:hover {border: 1px solid;\n"
"border-color: rgb(220, 220,220);}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.general_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(230, 112, 211, 91))
        self.frame_4.setMinimumSize(QSize(181, 91))
        self.frame_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_4.setStyleSheet(u"QFrame{border: 1px solid;\n"
"border-radius: 15px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);\n"
"}\n"
"QFrame:hover {border: 1px solid;\n"
"border-color: rgb(220, 220,220);}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.general_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(449, 13, 381, 190))
        self.frame_5.setMinimumSize(QSize(181, 91))
        self.frame_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_5.setStyleSheet(u"QFrame{border: 1px solid;\n"
"border-radius: 15px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);\n"
"}\n"
"QFrame:hover {border: 1px solid;\n"
"border-color: rgb(220, 220,220);}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.widget2 = QWidget(self.general_widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(3, 212, 831, 841))
        self.verticalLayout_4 = QVBoxLayout(self.widget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.positions_table = QTableWidget(self.widget2)
        self.positions_table.setObjectName(u"positions_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.positions_table.sizePolicy().hasHeightForWidth())
        self.positions_table.setSizePolicy(sizePolicy1)
        self.positions_table.setTabletTracking(True)
        self.positions_table.setStyleSheet(u"QFrame{border: 1px solid;}")
        self.positions_table.setFrameShape(QFrame.StyledPanel)
        self.positions_table.setFrameShadow(QFrame.Sunken)
        self.positions_table.setMidLineWidth(1)
        self.positions_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.positions_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.positions_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.positions_table.setAlternatingRowColors(True)
        self.positions_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.positions_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.positions_table.setShowGrid(False)
        self.positions_table.setSortingEnabled(False)

        self.horizontalLayout.addWidget(self.positions_table)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.accounts_table = QTableWidget(self.widget2)
        self.accounts_table.setObjectName(u"accounts_table")
        sizePolicy1.setHeightForWidth(self.accounts_table.sizePolicy().hasHeightForWidth())
        self.accounts_table.setSizePolicy(sizePolicy1)
        self.accounts_table.setContextMenuPolicy(Qt.NoContextMenu)
        self.accounts_table.setStyleSheet(u"QFrame{border: 1px solid;}")
        self.accounts_table.setFrameShape(QFrame.WinPanel)
        self.accounts_table.setFrameShadow(QFrame.Raised)
        self.accounts_table.setMidLineWidth(1)
        self.accounts_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.accounts_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.accounts_table.setAlternatingRowColors(True)
        self.accounts_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.accounts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.accounts_table.setShowGrid(False)

        self.horizontalLayout.addWidget(self.accounts_table)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.widget2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(100, 40))
        self.groupBox.setStyleSheet(u"border: solid 1px;\n"
"border-radius: 7px;\n"
"background-color: rgb(235,235,235);")
        self.last_update_lable = QLabel(self.groupBox)
        self.last_update_lable.setObjectName(u"last_update_lable")
        self.last_update_lable.setGeometry(QRect(134, 0, 561, 41))
        self.last_update_lable.setMinimumSize(QSize(151, 21))
        self.last_update_lable.setStyleSheet(u"QLabel {border-style: solid;\n"
"                border-width: 0px;\n"
"               border-color: black;\n"
"               font-weight:bolt;\n"
"               font-size:12pt;\n"
"	color: rgb(125, 125, 125);\n"
"background-color: rgba(0, 0, 0, 0);}\n"
"\n"
"\n"
"")
        self.last_update_lable.setFrameShape(QFrame.Panel)
        self.last_update_lable.setFrameShadow(QFrame.Plain)
        self.last_update_lable.setLineWidth(1)
        self.last_update_lable.setMidLineWidth(1)
        self.last_update_lable.setTextFormat(Qt.PlainText)
        self.last_update_lable.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.general_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 858, 22))
        self.main_menu = QMenu(self.menubar)
        self.main_menu.setObjectName(u"main_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.main_menu.menuAction())
        self.main_menu.addAction(self.open_table_view)
        self.main_menu.addAction(self.open_test_panel)
        self.main_menu.addSeparator()
        self.main_menu.addAction(self.exit_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_table_view.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b", None))
        self.open_test_panel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u0430\u044f \u043f\u0430\u043d\u0435\u043b\u044c", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438...", None))
        self.frame_3_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432", None))
        self.frame_1_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0432\u0441\u0435\u0445 \u0430\u043a\u0442\u0438\u0432\u043e\u0432", None))
        self.total_maney_value_label.setText(QCoreApplication.translate("MainWindow", u"000000000000000000", None))
        self.last_update_lable.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.main_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
    # retranslateUi

