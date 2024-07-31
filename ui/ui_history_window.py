# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
import ui.history_window_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1443, 675)
        self.general_widget = QWidget(Form)
        self.general_widget.setObjectName(u"general_widget")
        self.general_widget.setGeometry(QRect(6, 6, 1431, 661))
        self.general_widget.setStyleSheet(u"border: solid 1px;\n"
"border-radius: 7px;\n"
"background-color: rgb(235,235,235);")
        self.Edit_transaction = QPushButton(self.general_widget)
        self.Edit_transaction.setObjectName(u"Edit_transaction")
        self.Edit_transaction.setGeometry(QRect(261, 9, 230, 35))
        self.Edit_transaction.setMinimumSize(QSize(171, 35))
        self.Edit_transaction.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
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
        icon.addFile(u":/icons/icons/edit_square_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Edit_transaction.setIcon(icon)
        self.Edit_transaction.setIconSize(QSize(24, 24))
        self.add_transaction_from_table = QPushButton(self.general_widget)
        self.add_transaction_from_table.setObjectName(u"add_transaction_from_table")
        self.add_transaction_from_table.setGeometry(QRect(497, 9, 230, 35))
        self.add_transaction_from_table.setMinimumSize(QSize(171, 35))
        self.add_transaction_from_table.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
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
        icon1.addFile(u":/icons/icons/post_add_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_transaction_from_table.setIcon(icon1)
        self.add_transaction_from_table.setIconSize(QSize(24, 24))
        self.ticker_edit = QLineEdit(self.general_widget)
        self.ticker_edit.setObjectName(u"ticker_edit")
        self.ticker_edit.setGeometry(QRect(868, 56, 197, 34))
        self.ticker_edit.setMinimumSize(QSize(197, 34))
        self.ticker_edit.setMaximumSize(QSize(197, 34))
        self.ticker_edit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ticker_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
"font-size:12pt;")
        self.instrument_name = QLineEdit(self.general_widget)
        self.instrument_name.setObjectName(u"instrument_name")
        self.instrument_name.setGeometry(QRect(1071, 55, 351, 35))
        self.instrument_name.setMinimumSize(QSize(311, 34))
        self.instrument_name.setContextMenuPolicy(Qt.CustomContextMenu)
        self.instrument_name.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
"font-size:12pt;")
        self.results_table = QTableWidget(self.general_widget)
        self.results_table.setObjectName(u"results_table")
        self.results_table.setGeometry(QRect(12, 168, 1411, 481))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.results_table.sizePolicy().hasHeightForWidth())
        self.results_table.setSizePolicy(sizePolicy)
        self.results_table.setTabletTracking(True)
        self.results_table.setStyleSheet(u"QFrame{border: solid 2px;\n"
"border-radius: 7px;\n"
"border-color:rgb(0, 0, 0);\n"
"background-color:rgb(249, 249, 249);\n"
"}\n"
"\n"
"\n"
"")
        self.results_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.results_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.results_table.setAlternatingRowColors(True)
        self.results_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.results_table.setSortingEnabled(True)
        self.Delete_selection = QPushButton(self.general_widget)
        self.Delete_selection.setObjectName(u"Delete_selection")
        self.Delete_selection.setGeometry(QRect(733, 9, 230, 35))
        self.Delete_selection.setMinimumSize(QSize(171, 35))
        self.Delete_selection.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
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
        icon2.addFile(u":/icons/icons/delete_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Delete_selection.setIcon(icon2)
        self.Delete_selection.setIconSize(QSize(24, 24))
        self.Add_transaction = QPushButton(self.general_widget)
        self.Add_transaction.setObjectName(u"Add_transaction")
        self.Add_transaction.setGeometry(QRect(25, 9, 230, 35))
        self.Add_transaction.setMinimumSize(QSize(171, 35))
        self.Add_transaction.setMaximumSize(QSize(230, 35))
        self.Add_transaction.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
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
        icon3.addFile(u":/icons/icons/add_box_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Add_transaction.setIcon(icon3)
        self.Add_transaction.setIconSize(QSize(24, 24))
        self.db_query = QPushButton(self.general_widget)
        self.db_query.setObjectName(u"db_query")
        self.db_query.setGeometry(QRect(26, 109, 230, 35))
        self.db_query.setMinimumSize(QSize(230, 35))
        self.db_query.setMaximumSize(QSize(230, 35))
        self.db_query.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
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
        icon4.addFile(u":/icons/icons/database_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.db_query.setIcon(icon4)
        self.db_query.setIconSize(QSize(24, 24))
        self.Brocker_account = QComboBox(self.general_widget)
        self.Brocker_account.setObjectName(u"Brocker_account")
        self.Brocker_account.setGeometry(QRect(661, 56, 201, 34))
        self.Brocker_account.setMinimumSize(QSize(161, 34))
        self.Brocker_account.setMaximumSize(QSize(241, 34))
        self.Brocker_account.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"background-color:rgb(249, 249, 249);\n"
"color: rgb(89, 89, 89);\n"
"border-color:rgb(230, 230, 230);\n"
"font-size:12pt;")
        self.Brocker_account.setInsertPolicy(QComboBox.InsertAtBottom)
        self.brocker_query = QPushButton(self.general_widget)
        self.brocker_query.setObjectName(u"brocker_query")
        self.brocker_query.setGeometry(QRect(263, 109, 230, 35))
        self.brocker_query.setMinimumSize(QSize(230, 35))
        self.brocker_query.setMaximumSize(QSize(230, 35))
        self.brocker_query.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
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
        icon5.addFile(u"icons/quick_reference_all_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.brocker_query.setIcon(icon5)
        self.brocker_query.setIconSize(QSize(24, 24))
        self.period_control = QFrame(self.general_widget)
        self.period_control.setObjectName(u"period_control")
        self.period_control.setGeometry(QRect(25, 49, 491, 46))
        self.period_control.setMinimumSize(QSize(393, 46))
        self.end_date = QDateEdit(self.period_control)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setEnabled(True)
        self.end_date.setGeometry(QRect(380, 6, 110, 35))
        self.end_date.setMinimumSize(QSize(110, 28))
        self.end_date.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
"font-size:12pt;")
        self.end_date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(4, 0, 2)))
        self.end_date.setCalendarPopup(True)
        self.end_date.setTimeSpec(Qt.LocalTime)
        self.spacer = QLabel(self.period_control)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setGeometry(QRect(364, 9, 16, 22))
        self.spacer.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:12pt;")
        self.start_date = QDateEdit(self.period_control)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setEnabled(True)
        self.start_date.setGeometry(QRect(248, 6, 110, 35))
        self.start_date.setMinimumSize(QSize(110, 28))
        self.start_date.setContextMenuPolicy(Qt.NoContextMenu)
        self.start_date.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
"font-size:12pt;\n"
"")
        self.start_date.setDateTime(QDateTime(QDate(2022, 12, 29), QTime(20, 0, 0)))
        self.start_date.setCurrentSection(QDateTimeEdit.DaySection)
        self.start_date.setCalendarPopup(True)
        self.operations_period = QRadioButton(self.period_control)
        self.operations_period.setObjectName(u"operations_period")
        self.operations_period.setGeometry(QRect(70, 11, 181, 20))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.operations_period.sizePolicy().hasHeightForWidth())
        self.operations_period.setSizePolicy(sizePolicy1)
        self.operations_period.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:12pt;")
        self.operations_period.setChecked(True)
        self.all_operations = QRadioButton(self.period_control)
        self.all_operations.setObjectName(u"all_operations")
        self.all_operations.setGeometry(QRect(10, 10, 51, 20))
        self.all_operations.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:12pt;")
        self.Brocker = QComboBox(self.general_widget)
        self.Brocker.addItem("")
        self.Brocker.addItem("")
        self.Brocker.setObjectName(u"Brocker")
        self.Brocker.setGeometry(QRect(524, 56, 131, 34))
        self.Brocker.setMinimumSize(QSize(131, 34))
        self.Brocker.setMaximumSize(QSize(241, 34))
        self.Brocker.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(249, 249, 249);\n"
"font-size:12pt;")

        self.retranslateUi(Form)

        self.Brocker_account.setCurrentIndex(-1)
        self.Brocker.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Edit_transaction.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.add_transaction_from_table.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ticker_edit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0422\u0438\u043a\u0435\u0440", None))
        self.instrument_name.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.Delete_selection.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Add_transaction.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.db_query.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0440\u043e\u0441\u0438\u0442\u044c \u0430\u0440\u0445\u0438\u0432", None))
        self.Brocker_account.setCurrentText("")
        self.Brocker_account.setPlaceholderText(QCoreApplication.translate("Form", u"\u0421\u0447\u0435\u0442", None))
        self.brocker_query.setText(QCoreApplication.translate("Form", u"\u0410\u0440\u0445\u0438\u0432 \u0431\u0440\u043e\u043a\u0435\u0440\u0430", None))
        self.spacer.setText(QCoreApplication.translate("Form", u"-", None))
        self.operations_period.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434 ", None))
        self.all_operations.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435", None))
        self.Brocker.setItemText(0, QCoreApplication.translate("Form", u"\u0422\u0438\u043d\u044c\u043a\u043e\u0432", None))
        self.Brocker.setItemText(1, QCoreApplication.translate("Form", u"\u0411\u041a\u0421", None))

        self.Brocker.setPlaceholderText(QCoreApplication.translate("Form", u"\u0411\u0440\u043e\u043a\u0435\u0440", None))
    # retranslateUi

