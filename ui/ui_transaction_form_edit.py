# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaction_form_edit.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateTimeEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import ui.transaction_form_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 495)
        self.backFrame = QFrame(Dialog)
        self.backFrame.setObjectName(u"backFrame")
        self.backFrame.setGeometry(QRect(10, 10, 581, 471))
        self.backFrame.setStyleSheet(u"border: solid 1px;\n"
"border-radius: 7px;\n"
"background-color: rgb(235,235,235);")
        self.backFrame.setFrameShape(QFrame.StyledPanel)
        self.backFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.backFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(28, 10, 521, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-weight:bolt;\n"
"font-size:14pt;")
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(2)
        self.dateTimeEdit = QDateTimeEdit(self.backFrame)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(14, 61, 134, 34))
        self.dateTimeEdit.setMinimumSize(QSize(121, 34))
        self.dateTimeEdit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left:5px;")
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateTimeEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(8, 0, 0)))
        self.dateTimeEdit.setDate(QDate(2023, 1, 1))
        self.dateTimeEdit.setTime(QTime(8, 0, 0))
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.Save_all = QPushButton(self.backFrame)
        self.Save_all.setObjectName(u"Save_all")
        self.Save_all.setGeometry(QRect(278, 432, 171, 30))
        self.Save_all.setMinimumSize(QSize(171, 30))
        self.Save_all.setMaximumSize(QSize(171, 30))
        self.Save_all.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(220, 220, 220);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(225,225, 225);\n"
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
        icon.addFile(u":/icons/icons/save_as_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Save_all.setIcon(icon)
        self.Save_all.setIconSize(QSize(20, 20))
        self.description = QTextEdit(self.backFrame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(11, 219, 551, 201))
        self.description.setMinimumSize(QSize(421, 150))
        self.description.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 10px;")
        self.Cancel = QPushButton(self.backFrame)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setGeometry(QRect(101, 432, 171, 30))
        self.Cancel.setMinimumSize(QSize(171, 30))
        self.Cancel.setMaximumSize(QSize(171, 30))
        self.Cancel.setStyleSheet(u"QPushButton {\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 30 px;\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(220, 220, 220);\n"
"font-size:12pt;}\n"
"QPushButton:hover {\n"
"background-color:rgb(225,225, 225);\n"
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
        icon1.addFile(u":/icons/icons/undo_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Cancel.setIcon(icon1)
        self.Cancel.setIconSize(QSize(20, 20))
        self.ticker_edit = QLineEdit(self.backFrame)
        self.ticker_edit.setObjectName(u"ticker_edit")
        self.ticker_edit.setGeometry(QRect(12, 114, 197, 34))
        self.ticker_edit.setMinimumSize(QSize(197, 34))
        self.ticker_edit.setMaximumSize(QSize(197, 34))
        self.ticker_edit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ticker_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.volume_edit = QLineEdit(self.backFrame)
        self.volume_edit.setObjectName(u"volume_edit")
        self.volume_edit.setGeometry(QRect(198, 180, 90, 34))
        self.volume_edit.setMinimumSize(QSize(0, 34))
        self.volume_edit.setMaximumSize(QSize(90, 16777215))
        self.volume_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 5px;")
        self.price_edit = QLineEdit(self.backFrame)
        self.price_edit.setObjectName(u"price_edit")
        self.price_edit.setGeometry(QRect(89, 180, 100, 34))
        self.price_edit.setMinimumSize(QSize(100, 34))
        self.price_edit.setMaximumSize(QSize(100, 34))
        self.price_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left:5px;")
        self.fee_edit = QLineEdit(self.backFrame)
        self.fee_edit.setObjectName(u"fee_edit")
        self.fee_edit.setGeometry(QRect(294, 180, 90, 34))
        self.fee_edit.setMinimumSize(QSize(0, 34))
        self.fee_edit.setMaximumSize(QSize(90, 16777215))
        self.fee_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 5px;")
        self.Currency = QLineEdit(self.backFrame)
        self.Currency.setObjectName(u"Currency")
        self.Currency.setGeometry(QRect(13, 180, 70, 34))
        self.Currency.setMinimumSize(QSize(0, 34))
        self.Currency.setMaximumSize(QSize(70, 16777215))
        self.Currency.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left:5px;")
        self.instrument_name = QLineEdit(self.backFrame)
        self.instrument_name.setObjectName(u"instrument_name")
        self.instrument_name.setGeometry(QRect(215, 114, 351, 34))
        self.instrument_name.setMinimumSize(QSize(311, 34))
        self.instrument_name.setContextMenuPolicy(Qt.CustomContextMenu)
        self.instrument_name.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.nkd_edit = QLineEdit(self.backFrame)
        self.nkd_edit.setObjectName(u"nkd_edit")
        self.nkd_edit.setGeometry(QRect(390, 180, 90, 34))
        self.nkd_edit.setMinimumSize(QSize(0, 34))
        self.nkd_edit.setMaximumSize(QSize(90, 16777215))
        self.nkd_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 5px;")
        self.transaction_type = QLineEdit(self.backFrame)
        self.transaction_type.setObjectName(u"transaction_type")
        self.transaction_type.setGeometry(QRect(154, 61, 51, 34))
        self.transaction_type.setMinimumSize(QSize(0, 34))
        self.transaction_type.setMaximumSize(QSize(51, 34))
        self.transaction_type.setContextMenuPolicy(Qt.CustomContextMenu)
        self.transaction_type.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.brocker_name = QLineEdit(self.backFrame)
        self.brocker_name.setObjectName(u"brocker_name")
        self.brocker_name.setGeometry(QRect(211, 61, 130, 34))
        self.brocker_name.setMinimumSize(QSize(0, 34))
        self.brocker_name.setMaximumSize(QSize(131, 34))
        self.brocker_name.setContextMenuPolicy(Qt.CustomContextMenu)
        self.brocker_name.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.account_name = QLineEdit(self.backFrame)
        self.account_name.setObjectName(u"account_name")
        self.account_name.setGeometry(QRect(348, 61, 215, 34))
        self.account_name.setMinimumSize(QSize(215, 34))
        self.account_name.setMaximumSize(QSize(215, 34))
        self.account_name.setContextMenuPolicy(Qt.CustomContextMenu)
        self.account_name.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.Date_label = QLabel(self.backFrame)
        self.Date_label.setObjectName(u"Date_label")
        self.Date_label.setGeometry(QRect(18, 44, 28, 16))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.Date_label.setFont(font1)
        self.Date_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Date_label.setFrameShadow(QFrame.Sunken)
        self.Date_label.setTextFormat(Qt.PlainText)
        self.Date_label.setScaledContents(True)
        self.Date_label.setAlignment(Qt.AlignCenter)
        self.Date_label.setIndent(2)
        self.Type_label = QLabel(self.backFrame)
        self.Type_label.setObjectName(u"Type_label")
        self.Type_label.setGeometry(QRect(160, 43, 20, 16))
        self.Type_label.setFont(font1)
        self.Type_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Type_label.setFrameShadow(QFrame.Sunken)
        self.Type_label.setTextFormat(Qt.PlainText)
        self.Type_label.setScaledContents(True)
        self.Type_label.setAlignment(Qt.AlignCenter)
        self.Type_label.setIndent(2)
        self.Brocker_label = QLabel(self.backFrame)
        self.Brocker_label.setObjectName(u"Brocker_label")
        self.Brocker_label.setGeometry(QRect(220, 43, 43, 16))
        self.Brocker_label.setFont(font1)
        self.Brocker_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Brocker_label.setFrameShadow(QFrame.Sunken)
        self.Brocker_label.setTextFormat(Qt.PlainText)
        self.Brocker_label.setScaledContents(True)
        self.Brocker_label.setAlignment(Qt.AlignCenter)
        self.Brocker_label.setIndent(2)
        self.Account_label = QLabel(self.backFrame)
        self.Account_label.setObjectName(u"Account_label")
        self.Account_label.setGeometry(QRect(353, 43, 28, 16))
        self.Account_label.setFont(font1)
        self.Account_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Account_label.setFrameShadow(QFrame.Sunken)
        self.Account_label.setTextFormat(Qt.PlainText)
        self.Account_label.setScaledContents(True)
        self.Account_label.setAlignment(Qt.AlignCenter)
        self.Account_label.setIndent(2)
        self.Ticker_label = QLabel(self.backFrame)
        self.Ticker_label.setObjectName(u"Ticker_label")
        self.Ticker_label.setGeometry(QRect(18, 96, 33, 16))
        self.Ticker_label.setFont(font1)
        self.Ticker_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Ticker_label.setFrameShadow(QFrame.Sunken)
        self.Ticker_label.setTextFormat(Qt.PlainText)
        self.Ticker_label.setScaledContents(True)
        self.Ticker_label.setAlignment(Qt.AlignCenter)
        self.Ticker_label.setIndent(2)
        self.Instrument_name_label = QLabel(self.backFrame)
        self.Instrument_name_label.setObjectName(u"Instrument_name_label")
        self.Instrument_name_label.setGeometry(QRect(220, 98, 141, 16))
        self.Instrument_name_label.setFont(font1)
        self.Instrument_name_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Instrument_name_label.setFrameShadow(QFrame.Sunken)
        self.Instrument_name_label.setTextFormat(Qt.PlainText)
        self.Instrument_name_label.setScaledContents(True)
        self.Instrument_name_label.setAlignment(Qt.AlignCenter)
        self.Instrument_name_label.setIndent(2)
        self.Currency_label = QLabel(self.backFrame)
        self.Currency_label.setObjectName(u"Currency_label")
        self.Currency_label.setGeometry(QRect(18, 162, 45, 16))
        self.Currency_label.setFont(font1)
        self.Currency_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Currency_label.setFrameShadow(QFrame.Sunken)
        self.Currency_label.setTextFormat(Qt.PlainText)
        self.Currency_label.setScaledContents(True)
        self.Currency_label.setAlignment(Qt.AlignCenter)
        self.Currency_label.setIndent(2)
        self.Price_label = QLabel(self.backFrame)
        self.Price_label.setObjectName(u"Price_label")
        self.Price_label.setGeometry(QRect(90, 160, 41, 20))
        self.Price_label.setFont(font1)
        self.Price_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Price_label.setFrameShadow(QFrame.Sunken)
        self.Price_label.setTextFormat(Qt.PlainText)
        self.Price_label.setScaledContents(True)
        self.Price_label.setAlignment(Qt.AlignCenter)
        self.Price_label.setIndent(2)
        self.Value_label = QLabel(self.backFrame)
        self.Value_label.setObjectName(u"Value_label")
        self.Value_label.setGeometry(QRect(202, 160, 71, 20))
        self.Value_label.setFont(font1)
        self.Value_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Value_label.setFrameShadow(QFrame.Sunken)
        self.Value_label.setTextFormat(Qt.PlainText)
        self.Value_label.setScaledContents(True)
        self.Value_label.setAlignment(Qt.AlignCenter)
        self.Value_label.setIndent(2)
        self.Fee_label = QLabel(self.backFrame)
        self.Fee_label.setObjectName(u"Fee_label")
        self.Fee_label.setGeometry(QRect(293, 160, 71, 20))
        self.Fee_label.setFont(font1)
        self.Fee_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.Fee_label.setFrameShadow(QFrame.Sunken)
        self.Fee_label.setTextFormat(Qt.PlainText)
        self.Fee_label.setScaledContents(True)
        self.Fee_label.setAlignment(Qt.AlignCenter)
        self.Fee_label.setIndent(2)
        self.NKD_label = QLabel(self.backFrame)
        self.NKD_label.setObjectName(u"NKD_label")
        self.NKD_label.setGeometry(QRect(395, 160, 31, 20))
        self.NKD_label.setFont(font1)
        self.NKD_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:10pt;")
        self.NKD_label.setFrameShadow(QFrame.Sunken)
        self.NKD_label.setTextFormat(Qt.PlainText)
        self.NKD_label.setScaledContents(True)
        self.NKD_label.setAlignment(Qt.AlignCenter)
        self.NKD_label.setIndent(2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Transaction_form_edit", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd.MM.yyyy HH:mm", None))
        self.Save_all.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.Cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.ticker_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043a\u0435\u0440", None))
        self.volume_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u044a\u0435\u043c", None))
        self.price_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.fee_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f", None))
        self.Currency.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u043b\u044e\u0442\u0430", None))
        self.instrument_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.nkd_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u041a\u0414", None))
        self.transaction_type.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.brocker_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0411\u0440\u043e\u043a\u0435\u0440", None))
        self.account_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u0447\u0435\u0442", None))
        self.Date_label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430", None))
        self.Type_label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.Brocker_label.setText(QCoreApplication.translate("Dialog", u"\u0411\u0440\u043e\u043a\u0435\u0440", None))
        self.Account_label.setText(QCoreApplication.translate("Dialog", u"\u0421\u0447\u0435\u0442", None))
        self.Ticker_label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043a\u0435\u0440", None))
        self.Instrument_name_label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.Currency_label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u043b\u044e\u0442\u0430", None))
        self.Price_label.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.Value_label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.Fee_label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f", None))
        self.NKD_label.setText(QCoreApplication.translate("Dialog", u"\u041d\u041a\u0414", None))
    # retranslateUi

