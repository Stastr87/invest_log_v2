# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_view.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QFrame,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
import table_view_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1435, 741)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.results_table = QTableWidget(self.centralwidget)
        self.results_table.setObjectName(u"results_table")
        self.results_table.setGeometry(QRect(9, 120, 1411, 541))
        self.results_table.setStyleSheet(u"QTableView{\n"
"background-color: rgb(220,220,220);\n"
"border: 2px solid;\n"
"border-radius: 7px;\n"
"border-color: rgb(205, 205, 205);}\n"
"QTableView::section{\n"
"background-color:rgb(235, 235, 235);\n"
"border:none;\n"
"height:50px;\n"
"font-size:14pt;}\n"
"QTableView::item{\n"
"border-style:none;\n"
"}\n"
"QTableView::item:selected{\n"
"border-style:none;\n"
"background-color:rgb(220, 220, 220);}")
        self.db_query = QPushButton(self.centralwidget)
        self.db_query.setObjectName(u"db_query")
        self.db_query.setGeometry(QRect(411, 66, 171, 35))
        self.db_query.setMinimumSize(QSize(171, 35))
        self.db_query.setMaximumSize(QSize(171, 35))
        self.db_query.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(235,235, 235);\n"
"border: 1px solid;\n"
"border-color: rgb(220, 220,220);}\n"
"QPushButton:pressed{\n"
"background-color:rgb(215, 215,215);\n"
"border: 2px solid;\n"
"border-bottom-color:  rgb(190,190,190);\n"
"border-top-color: rgb(170,170,170);\n"
"border-left-color: rgb(170,170,170);\n"
"border-right-color:  rgb(190,190,190);}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/database_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.db_query.setIcon(icon)
        self.db_query.setIconSize(QSize(24, 24))
        self.period_control = QFrame(self.centralwidget)
        self.period_control.setObjectName(u"period_control")
        self.period_control.setGeometry(QRect(12, 61, 393, 46))
        self.period_control.setMinimumSize(QSize(393, 46))
        self.period_control.setMaximumSize(QSize(393, 46))
        self.end_date = QDateEdit(self.period_control)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setEnabled(True)
        self.end_date.setGeometry(QRect(274, 9, 110, 28))
        self.end_date.setMinimumSize(QSize(110, 28))
        self.end_date.setMaximumSize(QSize(91, 28))
        self.end_date.setStyleSheet(u"border: 5px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;")
        self.end_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(4, 0, 2)))
        self.end_date.setCalendarPopup(True)
        self.end_date.setTimeSpec(Qt.LocalTime)
        self.spacer = QLabel(self.period_control)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setGeometry(QRect(262, 9, 16, 22))
        self.spacer.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:12pt;")
        self.search_label = QLabel(self.period_control)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(9, 9, 131, 22))
        self.search_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:12pt;")
        self.start_date = QDateEdit(self.period_control)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setEnabled(True)
        self.start_date.setGeometry(QRect(146, 9, 110, 28))
        self.start_date.setMinimumSize(QSize(110, 28))
        self.start_date.setMaximumSize(QSize(0, 28))
        self.start_date.setContextMenuPolicy(Qt.NoContextMenu)
        self.start_date.setStyleSheet(u"border: 5px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;\n"
"")
        self.start_date.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(16, 0, 0)))
        self.start_date.setCurrentSection(QDateTimeEdit.DaySection)
        self.start_date.setCalendarPopup(True)
        self.Add_transaction = QPushButton(self.centralwidget)
        self.Add_transaction.setObjectName(u"Add_transaction")
        self.Add_transaction.setGeometry(QRect(22, 21, 230, 35))
        self.Add_transaction.setMinimumSize(QSize(171, 35))
        self.Add_transaction.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(235,235, 235);\n"
"border: 1px solid;\n"
"border-color: rgb(220, 220,220);}\n"
"QPushButton:pressed{\n"
"background-color:rgb(215, 215,215);\n"
"border: 2px solid;\n"
"border-bottom-color:  rgb(190,190,190);\n"
"border-top-color: rgb(170,170,170);\n"
"border-left-color: rgb(170,170,170);\n"
"border-right-color:  rgb(190,190,190);}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add_box_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Add_transaction.setIcon(icon1)
        self.Add_transaction.setIconSize(QSize(24, 24))
        self.Edit_transaction = QPushButton(self.centralwidget)
        self.Edit_transaction.setObjectName(u"Edit_transaction")
        self.Edit_transaction.setGeometry(QRect(258, 21, 230, 35))
        self.Edit_transaction.setMinimumSize(QSize(171, 35))
        self.Edit_transaction.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(235,235, 235);\n"
"border: 1px solid;\n"
"border-color: rgb(220, 220,220);}\n"
"QPushButton:pressed{\n"
"background-color:rgb(215, 215,215);\n"
"border: 2px solid;\n"
"border-bottom-color:  rgb(190,190,190);\n"
"border-top-color: rgb(170,170,170);\n"
"border-left-color: rgb(170,170,170);\n"
"border-right-color:  rgb(190,190,190);}\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/edit_square_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Edit_transaction.setIcon(icon2)
        self.Edit_transaction.setIconSize(QSize(24, 24))
        self.Delete_selection = QPushButton(self.centralwidget)
        self.Delete_selection.setObjectName(u"Delete_selection")
        self.Delete_selection.setGeometry(QRect(730, 21, 230, 35))
        self.Delete_selection.setMinimumSize(QSize(171, 35))
        self.Delete_selection.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(235,235, 235);\n"
"border: 1px solid;\n"
"border-color: rgb(220, 220,220);}\n"
"QPushButton:pressed{\n"
"background-color:rgb(215, 215,215);\n"
"border: 2px solid;\n"
"border-bottom-color:  rgb(190,190,190);\n"
"border-top-color: rgb(170,170,170);\n"
"border-left-color: rgb(170,170,170);\n"
"border-right-color:  rgb(190,190,190);}\n"
"\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/delete_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Delete_selection.setIcon(icon3)
        self.Delete_selection.setIconSize(QSize(24, 24))
        self.brocker_query = QPushButton(self.centralwidget)
        self.brocker_query.setObjectName(u"brocker_query")
        self.brocker_query.setGeometry(QRect(588, 66, 171, 35))
        self.brocker_query.setMinimumSize(QSize(171, 35))
        self.brocker_query.setMaximumSize(QSize(171, 35))
        self.brocker_query.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(235,235, 235);\n"
"border: 1px solid;\n"
"border-color: rgb(220, 220,220);}\n"
"QPushButton:pressed{\n"
"background-color:rgb(215, 215,215);\n"
"border: 2px solid;\n"
"border-bottom-color:  rgb(190,190,190);\n"
"border-top-color: rgb(170,170,170);\n"
"border-left-color: rgb(170,170,170);\n"
"border-right-color:  rgb(190,190,190);}\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icons/quick_reference_all_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.brocker_query.setIcon(icon4)
        self.brocker_query.setIconSize(QSize(24, 24))
        self.add_transaction_from_table = QPushButton(self.centralwidget)
        self.add_transaction_from_table.setObjectName(u"add_transaction_from_table")
        self.add_transaction_from_table.setGeometry(QRect(494, 21, 230, 35))
        self.add_transaction_from_table.setMinimumSize(QSize(171, 35))
        self.add_transaction_from_table.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(235,235, 235);\n"
"border: 1px solid;\n"
"border-color: rgb(220, 220,220);}\n"
"QPushButton:pressed{\n"
"background-color:rgb(215, 215,215);\n"
"border: 2px solid;\n"
"border-bottom-color:  rgb(190,190,190);\n"
"border-top-color: rgb(170,170,170);\n"
"border-left-color: rgb(170,170,170);\n"
"border-right-color:  rgb(190,190,190);}\n"
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/post_add_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_transaction_from_table.setIcon(icon5)
        self.add_transaction_from_table.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"InvestLog", None))
        self.db_query.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441\u0438\u0442\u044c \u0430\u0440\u0445\u0438\u0432", None))
        self.spacer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.search_label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0438 \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434 ", None))
        self.Add_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.Edit_transaction.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.Delete_selection.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.brocker_query.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432 \u0431\u0440\u043e\u043a\u0435\u0440\u0430", None))
        self.add_transaction_from_table.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

