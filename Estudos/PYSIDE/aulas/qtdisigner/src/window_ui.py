# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 576)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 651, 521))
        self.gridLayoutpricipal = QGridLayout(self.gridLayoutWidget)
        self.gridLayoutpricipal.setObjectName(u"gridLayoutpricipal")
        self.gridLayoutpricipal.setContentsMargins(0, 0, 0, 0)
        self.labelresult = QLabel(self.gridLayoutWidget)
        self.labelresult.setObjectName(u"labelresult")
        font = QFont()
        font.setPointSize(24)
        self.labelresult.setFont(font)
        self.labelresult.setCursor(QCursor(Qt.ArrowCursor))
        self.labelresult.setTextFormat(Qt.PlainText)
        self.labelresult.setAlignment(Qt.AlignCenter)

        self.gridLayoutpricipal.addWidget(self.labelresult, 0, 0, 1, 1)

        self.gridLayout_secundaria = QGridLayout()
        self.gridLayout_secundaria.setObjectName(u"gridLayout_secundaria")
        self.label_name = QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font)

        self.gridLayout_secundaria.addWidget(self.label_name, 0, 0, 1, 1)

        self.line_name = QLineEdit(self.gridLayoutWidget)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setFont(font)

        self.gridLayout_secundaria.addWidget(self.line_name, 0, 1, 1, 1)

        self.pushButton_send = QPushButton(self.gridLayoutWidget)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setFont(font)

        self.gridLayout_secundaria.addWidget(self.pushButton_send, 0, 2, 1, 1)


        self.gridLayoutpricipal.addLayout(self.gridLayout_secundaria, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 692, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelresult.setText(QCoreApplication.translate("MainWindow", u"Nao ha nada aqui", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Seu nome", None))
        self.line_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome...", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

