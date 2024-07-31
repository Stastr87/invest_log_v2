# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(274, 300)
        self.test_button = QPushButton(Form)
        self.test_button.setObjectName(u"test_button")
        self.test_button.setGeometry(QRect(11, 13, 253, 24))
        self.test_button.setMinimumSize(QSize(253, 24))
        self.load_position_data = QPushButton(Form)
        self.load_position_data.setObjectName(u"load_position_data")
        self.load_position_data.setGeometry(QRect(11, 43, 253, 24))
        self.load_position_data.setMinimumSize(QSize(253, 24))
        self.update_accounts = QPushButton(Form)
        self.update_accounts.setObjectName(u"update_accounts")
        self.update_accounts.setGeometry(QRect(11, 73, 253, 24))
        self.update_accounts.setMinimumSize(QSize(253, 24))
        self.update_instruments = QPushButton(Form)
        self.update_instruments.setObjectName(u"update_instruments")
        self.update_instruments.setGeometry(QRect(11, 103, 253, 24))
        self.update_instruments.setMinimumSize(QSize(253, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.test_button.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u0437\u0438\u0446\u0438\u0439 \u043f\u043e \u0441\u0447\u0435\u0442\u0430\u043c", None))
        self.load_position_data.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u0438", None))
        self.update_accounts.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0441\u0447\u0435\u0442\u043e\u0432", None))
        self.update_instruments.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
    # retranslateUi

