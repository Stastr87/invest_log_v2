# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'etf_instrument_card.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import ui.instrument_card_v2_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1003, 840)
        self.backFrame = QFrame(Dialog)
        self.backFrame.setObjectName(u"backFrame")
        self.backFrame.setGeometry(QRect(10, 10, 981, 821))
        self.backFrame.setStyleSheet(u"border: solid 1px;\n"
"border-radius: 7px;\n"
"background-color: rgb(235,235,235);")
        self.backFrame.setFrameShape(QFrame.StyledPanel)
        self.backFrame.setFrameShadow(QFrame.Raised)
        self.Instrument_price = QLineEdit(self.backFrame)
        self.Instrument_price.setObjectName(u"Instrument_price")
        self.Instrument_price.setGeometry(QRect(18, 86, 130, 34))
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
        self.instrument_quantity.setGeometry(QRect(154, 86, 171, 34))
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
        self.total_price.setGeometry(QRect(330, 86, 231, 34))
        self.total_price.setMinimumSize(QSize(171, 34))
        self.total_price.setContextMenuPolicy(Qt.CustomContextMenu)
        self.total_price.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.total_label = QLabel(self.backFrame)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setGeometry(QRect(333, 68, 112, 16))
        self.total_label.setStyleSheet(u"color: rgb(89, 89, 89);")
        self.qty_label = QLabel(self.backFrame)
        self.qty_label.setObjectName(u"qty_label")
        self.qty_label.setGeometry(QRect(158, 68, 65, 16))
        self.qty_label.setStyleSheet(u"color: rgb(89, 89, 89);")
        self.price_label = QLabel(self.backFrame)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setGeometry(QRect(20, 69, 63, 16))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.price_label.setFont(font)
        self.price_label.setStyleSheet(u"color: rgb(89, 89, 89);")
        self.weight_value_lable = QLabel(self.backFrame)
        self.weight_value_lable.setObjectName(u"weight_value_lable")
        self.weight_value_lable.setGeometry(QRect(570, 68, 120, 16))
        self.weight_value_lable.setFont(font)
        self.weight_value_lable.setStyleSheet(u"color: rgb(89, 89, 89);")
        self.weight_value = QLineEdit(self.backFrame)
        self.weight_value.setObjectName(u"weight_value")
        self.weight_value.setGeometry(QRect(567, 86, 131, 34))
        self.weight_value.setMinimumSize(QSize(121, 34))
        self.weight_value.setContextMenuPolicy(Qt.CustomContextMenu)
        self.weight_value.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"font-size:12pt;\n"
"padding-left: 5px;\n"
"background-color:rgb(245, 245, 245);")
        self.etf_instrument_card_label = QLabel(self.backFrame)
        self.etf_instrument_card_label.setObjectName(u"etf_instrument_card_label")
        self.etf_instrument_card_label.setGeometry(QRect(1, 11, 981, 22))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.etf_instrument_card_label.setFont(font1)
        self.etf_instrument_card_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-weight:bolt;\n"
"font-size:14pt;")
        self.etf_instrument_card_label.setFrameShadow(QFrame.Sunken)
        self.etf_instrument_card_label.setTextFormat(Qt.PlainText)
        self.etf_instrument_card_label.setScaledContents(True)
        self.etf_instrument_card_label.setAlignment(Qt.AlignCenter)
        self.etf_instrument_card_label.setIndent(2)
        self.figi_label = QLabel(self.backFrame)
        self.figi_label.setObjectName(u"figi_label")
        self.figi_label.setGeometry(QRect(7, 39, 971, 20))
        self.figi_label.setMouseTracking(False)
        self.figi_label.setStyleSheet(u"color: rgb(89, 89, 89);")
        self.figi_label.setAlignment(Qt.AlignCenter)
        self.period_label = QLabel(self.backFrame)
        self.period_label.setObjectName(u"period_label")
        self.period_label.setGeometry(QRect(12, 718, 59, 18))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setKerning(False)
        self.period_label.setFont(font2)
        self.period_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:12pt;")
        self.period_label.setFrameShadow(QFrame.Sunken)
        self.period_label.setTextFormat(Qt.PlainText)
        self.period_label.setScaledContents(True)
        self.period_label.setAlignment(Qt.AlignCenter)
        self.period_label.setIndent(2)
        self.Cancel = QPushButton(self.backFrame)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setGeometry(QRect(290, 785, 171, 30))
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
        icon = QIcon()
        icon.addFile(u":/icons/icons/undo_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Cancel.setIcon(icon)
        self.Cancel.setIconSize(QSize(20, 20))
        self.line_chart = QPushButton(self.backFrame)
        self.line_chart.setObjectName(u"line_chart")
        self.line_chart.setGeometry(QRect(120, 748, 111, 30))
        self.line_chart.setMinimumSize(QSize(81, 30))
        self.line_chart.setMaximumSize(QSize(171, 30))
        self.line_chart.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u"icons/show_chart_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.line_chart.setIcon(icon1)
        self.line_chart.setIconSize(QSize(20, 20))
        self.Save = QPushButton(self.backFrame)
        self.Save.setObjectName(u"Save")
        self.Save.setGeometry(QRect(490, 785, 171, 30))
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/save_as_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Save.setIcon(icon2)
        self.Save.setIconSize(QSize(20, 20))
        self.candle_chart = QPushButton(self.backFrame)
        self.candle_chart.setObjectName(u"candle_chart")
        self.candle_chart.setGeometry(QRect(240, 748, 111, 30))
        self.candle_chart.setMinimumSize(QSize(81, 30))
        self.candle_chart.setMaximumSize(QSize(171, 30))
        self.candle_chart.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u"icons/candlestick_chart_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.candle_chart.setIcon(icon3)
        self.candle_chart.setIconSize(QSize(20, 20))
        self.end_date = QDateEdit(self.backFrame)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setEnabled(True)
        self.end_date.setGeometry(QRect(208, 710, 119, 33))
        self.end_date.setMinimumSize(QSize(0, 33))
        self.end_date.setStyleSheet(u"border: 5px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;")
        self.end_date.setCalendarPopup(True)
        self.end_date.setTimeSpec(Qt.LocalTime)
        self.chart_type_label = QLabel(self.backFrame)
        self.chart_type_label.setObjectName(u"chart_type_label")
        self.chart_type_label.setGeometry(QRect(13, 754, 94, 18))
        self.chart_type_label.setFont(font2)
        self.chart_type_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-size:12pt;")
        self.chart_type_label.setFrameShadow(QFrame.Sunken)
        self.chart_type_label.setTextFormat(Qt.PlainText)
        self.chart_type_label.setScaledContents(True)
        self.chart_type_label.setAlignment(Qt.AlignCenter)
        self.chart_type_label.setIndent(2)
        self.start_date = QDateEdit(self.backFrame)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setEnabled(True)
        self.start_date.setGeometry(QRect(78, 710, 110, 33))
        self.start_date.setMinimumSize(QSize(0, 33))
        self.start_date.setContextMenuPolicy(Qt.NoContextMenu)
        self.start_date.setStyleSheet(u"border: 5px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(230, 230, 230);\n"
"font-size:12pt;\n"
"")
        self.start_date.setCurrentSection(QDateTimeEdit.DaySection)
        self.start_date.setCalendarPopup(True)
        self.space_label = QLabel(self.backFrame)
        self.space_label.setObjectName(u"space_label")
        self.space_label.setGeometry(QRect(194, 710, 16, 26))
        self.space_label.setMouseTracking(False)
        self.space_label.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font-weight:bolt;\n"
"font-size:14pt;")
        self.space_label.setAlignment(Qt.AlignCenter)
        self.description = QTextEdit(self.backFrame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(10, 130, 961, 150))
        self.description.setMinimumSize(QSize(421, 150))
        self.description.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"font-size:12pt;\n"
"padding-left: 10px;")
        self.chart_widget = QWebEngineView(self.backFrame)
        self.chart_widget.setObjectName(u"chart_widget")
        self.chart_widget.setGeometry(QRect(10, 290, 961, 411))
        self.chart_widget.setStyleSheet(u"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color:rgb(230, 230, 230);\n"
"color: rgb(89, 89, 89);\n"
"background-color:rgb(245, 245, 245);\n"
"padding-left: 10px;")
        self.chart_widget.setUrl(QUrl(u"about:blank"))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Instrument_price.setText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.Instrument_price.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.instrument_quantity.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.instrument_quantity.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0431\u0443\u043c\u0430\u0433 \u0432 \u043f\u043e\u0440\u0442\u0444\u0435\u043b\u0435", None))
        self.total_price.setText(QCoreApplication.translate("Dialog", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.total_price.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.total_label.setText(QCoreApplication.translate("Dialog", u"\u0418\u0442\u043e\u0433\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.qty_label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.price_label.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.weight_value_lable.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0441 \u0432 \u043f\u043e\u0440\u0442\u0444\u0435\u043b\u0435", None))
        self.weight_value.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.weight_value.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0426\u0435\u043d\u0430", None))
        self.etf_instrument_card_label.setText(QCoreApplication.translate("Dialog", u"etf_instrument_card", None))
        self.figi_label.setText(QCoreApplication.translate("Dialog", u"figi", None))
        self.period_label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0438\u043e\u0434:", None))
        self.Cancel.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.line_chart.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u043d\u0438\u044f", None))
        self.Save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.candle_chart.setText(QCoreApplication.translate("Dialog", u"OHLC", None))
        self.chart_type_label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.space_label.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
    # retranslateUi

