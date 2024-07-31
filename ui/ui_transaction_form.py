# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaction_form.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
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
        self.label.setGeometry(QRect(18, 10, 541, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-weight:bolt;\n"
"font-size:14pt;")
        self.label.setFrameShape(QFrame.Box)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(2)
        self.dateTimeEdit = QDateTimeEdit(self.backFrame)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(12, 64, 134, 34))
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
        self.Transactio_type = QComboBox(self.backFrame)
        self.Transactio_type.addItem("")
        self.Transactio_type.addItem("")
        self.Transactio_type.setObjectName(u"Transactio_type")
        self.Transactio_type.setGeometry(QRect(152, 64, 71, 34))
        self.Transactio_type.setMinimumSize(QSize(71, 34))
        self.Transactio_type.setStyleSheet(u"padding-left: 10px;\n"
"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;")
        self.Transactio_type.setFrame(True)
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
        self.Brocker = QComboBox(self.backFrame)
        self.Brocker.addItem("")
        self.Brocker.addItem("")
        self.Brocker.setObjectName(u"Brocker")
        self.Brocker.setGeometry(QRect(229, 64, 131, 34))
        self.Brocker.setMinimumSize(QSize(131, 34))
        self.Brocker.setMaximumSize(QSize(241, 34))
        self.Brocker.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 10px;")
        self.description = QTextEdit(self.backFrame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(11, 189, 551, 231))
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
        self.ticker_edit.setGeometry(QRect(12, 106, 197, 34))
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
        self.volume_edit.setGeometry(QRect(198, 149, 90, 34))
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
        self.price_edit.setGeometry(QRect(89, 149, 100, 34))
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
        self.fee_edit.setGeometry(QRect(294, 149, 90, 34))
        self.fee_edit.setMinimumSize(QSize(0, 34))
        self.fee_edit.setMaximumSize(QSize(90, 16777215))
        self.fee_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 5px;")
        self.Brocker_account = QComboBox(self.backFrame)
        self.Brocker_account.setObjectName(u"Brocker_account")
        self.Brocker_account.setGeometry(QRect(366, 64, 201, 34))
        self.Brocker_account.setMinimumSize(QSize(161, 34))
        self.Brocker_account.setMaximumSize(QSize(241, 34))
        self.Brocker_account.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 10px;")
        self.Brocker_account.setInsertPolicy(QComboBox.InsertAtBottom)
        self.Currency = QLineEdit(self.backFrame)
        self.Currency.setObjectName(u"Currency")
        self.Currency.setGeometry(QRect(13, 149, 70, 34))
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
        self.instrument_name.setGeometry(QRect(215, 106, 351, 34))
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
        self.nkd_edit.setGeometry(QRect(390, 149, 90, 34))
        self.nkd_edit.setMinimumSize(QSize(0, 34))
        self.nkd_edit.setMaximumSize(QSize(90, 16777215))
        self.nkd_edit.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 5px;")

        self.retranslateUi(Dialog)

        self.Brocker.setCurrentIndex(-1)
        self.Brocker_account.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Transaction_form", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd.MM.yyyy HH:mm", None))
        self.Transactio_type.setItemText(0, QCoreApplication.translate("Dialog", u"Buy", None))
        self.Transactio_type.setItemText(1, QCoreApplication.translate("Dialog", u"Sell", None))

        self.Save_all.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.Brocker.setItemText(0, QCoreApplication.translate("Dialog", u"\u0422\u0438\u043d\u044c\u043a\u043e\u0432", None))
        self.Brocker.setItemText(1, QCoreApplication.translate("Dialog", u"\u0411\u041a\u0421", None))

        self.Brocker.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0411\u0440\u043e\u043a\u0435\u0440", None))
        self.description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.Cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.ticker_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043a\u0435\u0440", None))
        self.volume_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u044a\u0435\u043c", None))
        self.price_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.fee_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f", None))
        self.Brocker_account.setCurrentText("")
        self.Brocker_account.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u0447\u0435\u0442", None))
        self.Currency.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0430\u043b\u044e\u0442\u0430", None))
        self.instrument_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430", None))
        self.nkd_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u041a\u0414", None))
    # retranslateUi

