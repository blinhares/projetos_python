# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workerui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_mywidget(object):
    def setupUi(self, mywidget):
        if not mywidget.objectName():
            mywidget.setObjectName(u"mywidget")
        mywidget.resize(400, 300)
        self.gridLayoutWidget = QWidget(mywidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 371, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.button1 = QPushButton(self.gridLayoutWidget)
        self.button1.setObjectName(u"button1")
        font1 = QFont()
        font1.setPointSize(20)
        self.button1.setFont(font1)

        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)

        self.button_2 = QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setFont(font1)

        self.gridLayout.addWidget(self.button_2, 1, 1, 1, 1)


        self.retranslateUi(mywidget)

        QMetaObject.connectSlotsByName(mywidget)
    # setupUi

    def retranslateUi(self, mywidget):
        mywidget.setWindowTitle(QCoreApplication.translate("mywidget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("mywidget", u"L2", None))
        self.label.setText(QCoreApplication.translate("mywidget", u"L1", None))
        self.button1.setText(QCoreApplication.translate("mywidget", u"b1", None))
        self.button_2.setText(QCoreApplication.translate("mywidget", u"b2", None))
    # retranslateUi

