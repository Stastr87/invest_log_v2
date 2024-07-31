# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instrument_card.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)
import instrument_card_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(611, 493)
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
        self.Save = QPushButton(self.backFrame)
        self.Save.setObjectName(u"Save")
        self.Save.setGeometry(QRect(278, 432, 171, 30))
        self.Save.setMinimumSize(QSize(171, 30))
        self.Save.setMaximumSize(QSize(171, 30))
        self.Save.setStyleSheet(u"QPushButton {\n"
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
        self.Save.setIcon(icon)
        self.Save.setIconSize(QSize(20, 20))
        self.description = QTextEdit(self.backFrame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(11, 109, 551, 150))
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
        self.bond_nkd = QLineEdit(self.backFrame)
        self.bond_nkd.setObjectName(u"bond_nkd")
        self.bond_nkd.setGeometry(QRect(289, 62, 90, 34))
        self.bond_nkd.setMinimumSize(QSize(71, 34))
        self.bond_nkd.setMaximumSize(QSize(90, 16777215))
        self.bond_nkd.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 5px;")
        self.Instrument_price = QLineEdit(self.backFrame)
        self.Instrument_price.setObjectName(u"Instrument_price")
        self.Instrument_price.setGeometry(QRect(17, 62, 130, 34))
        self.Instrument_price.setMinimumSize(QSize(121, 34))
        self.Instrument_price.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Instrument_price.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.instrument_quantity = QLineEdit(self.backFrame)
        self.instrument_quantity.setObjectName(u"instrument_quantity")
        self.instrument_quantity.setGeometry(QRect(153, 62, 130, 34))
        self.instrument_quantity.setMinimumSize(QSize(91, 34))
        self.instrument_quantity.setContextMenuPolicy(Qt.CustomContextMenu)
        self.instrument_quantity.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.total_price = QLineEdit(self.backFrame)
        self.total_price.setObjectName(u"total_price")
        self.total_price.setGeometry(QRect(385, 62, 171, 34))
        self.total_price.setMinimumSize(QSize(171, 34))
        self.total_price.setContextMenuPolicy(Qt.CustomContextMenu)
        self.total_price.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Instrument_card", None))
        self.Save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.Cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.bond_nkd.setText(QCoreApplication.translate("Dialog", u"\u041d\u041a\u0414", None))
        self.bond_nkd.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u041a\u0414", None))
        self.Instrument_price.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.Instrument_price.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.instrument_quantity.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.instrument_quantity.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0431\u0443\u043c\u0430\u0433 \u0432 \u043f\u043e\u0440\u0442\u0444\u0435\u043b\u0435", None))
        self.total_price.setText(QCoreApplication.translate("Dialog", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.total_price.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
    # retranslateUi

