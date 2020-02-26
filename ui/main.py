# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from ui import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 709)
        MainWindow.setMaximumSize(QSize(3000, 2300))
        icon = QIcon()
        icon.addFile(u":/images/images/main.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/images/images/checked.png", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/images/images/checked.png", QSize(), QIcon.Selected, QIcon.Off)
        icon.addFile(u":/images/images/checked.png", QSize(), QIcon.Selected, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_20 = QGridLayout(self.centralwidget)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(210, 350))
        palette = QPalette()
        brush = QBrush(QColor(170, 170, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        brush1 = QBrush(QColor(160, 160, 160, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        self.frame1.setPalette(palette)
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.frame1.setFont(font)
        self.frame1.setMouseTracking(True)
        self.frame1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame1.setAutoFillBackground(True)
        self.frame1.setFrameShape(QFrame.Box)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.frame1.setLineWidth(1)
        self.frame1.setMidLineWidth(1)
        self.gridLayout_44 = QGridLayout(self.frame1)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.frame = QFrame(self.frame1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_plate_1 = QLabel(self.frame)
        self.label_plate_1.setObjectName(u"label_plate_1")
        self.label_plate_1.setMinimumSize(QSize(0, 14))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_plate_1.setFont(font1)
        self.label_plate_1.setFrameShadow(QFrame.Sunken)
        self.label_plate_1.setAlignment(Qt.AlignCenter)
        self.label_plate_1.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_plate_1, 0, 0, 1, 2)

        self.label_plate_2 = QLabel(self.frame)
        self.label_plate_2.setObjectName(u"label_plate_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_plate_2.setFont(font2)

        self.gridLayout_2.addWidget(self.label_plate_2, 1, 0, 1, 1)

        self.w1 = QLineEdit(self.frame)
        self.w1.setObjectName(u"w1")
        self.w1.setFont(font2)

        self.gridLayout_2.addWidget(self.w1, 1, 1, 1, 1)

        self.label_plate_3 = QLabel(self.frame)
        self.label_plate_3.setObjectName(u"label_plate_3")
        self.label_plate_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_plate_3, 2, 0, 1, 1)

        self.w2 = QLineEdit(self.frame)
        self.w2.setObjectName(u"w2")
        self.w2.setFont(font2)

        self.gridLayout_2.addWidget(self.w2, 2, 1, 1, 1)

        self.label_plate_4 = QLabel(self.frame)
        self.label_plate_4.setObjectName(u"label_plate_4")
        self.label_plate_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_plate_4, 3, 0, 1, 1)

        self.h1 = QLineEdit(self.frame)
        self.h1.setObjectName(u"h1")
        self.h1.setFont(font2)

        self.gridLayout_2.addWidget(self.h1, 3, 1, 1, 1)

        self.label_plate_5 = QLabel(self.frame)
        self.label_plate_5.setObjectName(u"label_plate_5")
        self.label_plate_5.setFont(font2)

        self.gridLayout_2.addWidget(self.label_plate_5, 4, 0, 1, 1)

        self.h2 = QLineEdit(self.frame)
        self.h2.setObjectName(u"h2")
        self.h2.setFont(font2)

        self.gridLayout_2.addWidget(self.h2, 4, 1, 1, 1)

        self.label_plate_6 = QLabel(self.frame)
        self.label_plate_6.setObjectName(u"label_plate_6")
        self.label_plate_6.setFont(font2)

        self.gridLayout_2.addWidget(self.label_plate_6, 5, 0, 1, 1)

        self.t1 = QLineEdit(self.frame)
        self.t1.setObjectName(u"t1")
        self.t1.setFont(font2)

        self.gridLayout_2.addWidget(self.t1, 5, 1, 1, 1)

        self.label_plate_7 = QLabel(self.frame)
        self.label_plate_7.setObjectName(u"label_plate_7")
        self.label_plate_7.setFont(font2)

        self.gridLayout_2.addWidget(self.label_plate_7, 6, 0, 1, 1)

        self.t2 = QLineEdit(self.frame)
        self.t2.setObjectName(u"t2")
        self.t2.setFont(font2)

        self.gridLayout_2.addWidget(self.t2, 6, 1, 1, 1)


        self.gridLayout_44.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.frame1)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_14)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_plate_8 = QLabel(self.frame_14)
        self.label_plate_8.setObjectName(u"label_plate_8")
        self.label_plate_8.setFont(font1)
        self.label_plate_8.setFrameShadow(QFrame.Sunken)
        self.label_plate_8.setAlignment(Qt.AlignCenter)
        self.label_plate_8.setWordWrap(False)

        self.gridLayout_43.addWidget(self.label_plate_8, 0, 0, 1, 2)

        self.label_plate_9 = QLabel(self.frame_14)
        self.label_plate_9.setObjectName(u"label_plate_9")
        self.label_plate_9.setFont(font2)

        self.gridLayout_43.addWidget(self.label_plate_9, 1, 0, 1, 1)

        self.w3 = QLineEdit(self.frame_14)
        self.w3.setObjectName(u"w3")
        self.w3.setFont(font2)

        self.gridLayout_43.addWidget(self.w3, 1, 1, 1, 1)

        self.label_plate_10 = QLabel(self.frame_14)
        self.label_plate_10.setObjectName(u"label_plate_10")
        self.label_plate_10.setFont(font2)

        self.gridLayout_43.addWidget(self.label_plate_10, 2, 0, 1, 1)

        self.h3 = QLineEdit(self.frame_14)
        self.h3.setObjectName(u"h3")
        self.h3.setFont(font2)

        self.gridLayout_43.addWidget(self.h3, 2, 1, 1, 1)

        self.label_plate_11 = QLabel(self.frame_14)
        self.label_plate_11.setObjectName(u"label_plate_11")
        self.label_plate_11.setFont(font2)

        self.gridLayout_43.addWidget(self.label_plate_11, 3, 0, 1, 1)

        self.t3 = QLineEdit(self.frame_14)
        self.t3.setObjectName(u"t3")
        self.t3.setFont(font2)

        self.gridLayout_43.addWidget(self.t3, 3, 1, 1, 1)


        self.gridLayout_44.addWidget(self.frame_14, 1, 0, 1, 1)

        self.label_plate_12 = QLabel(self.frame1)
        self.label_plate_12.setObjectName(u"label_plate_12")
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_plate_12.setFont(font3)
        self.label_plate_12.setFrameShadow(QFrame.Sunken)
        self.label_plate_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_plate_12.setWordWrap(False)

        self.gridLayout_44.addWidget(self.label_plate_12, 2, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame1, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setMidLineWidth(1)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setFrameShadow(QFrame.Sunken)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(False)

        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 2)

        self.label_63 = QLabel(self.frame_5)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font2)

        self.gridLayout_5.addWidget(self.label_63, 1, 0, 1, 1)

        self.o1 = QLineEdit(self.frame_5)
        self.o1.setObjectName(u"o1")
        self.o1.setFont(font2)

        self.gridLayout_5.addWidget(self.o1, 1, 1, 1, 1)

        self.label_64 = QLabel(self.frame_5)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font2)

        self.gridLayout_5.addWidget(self.label_64, 2, 0, 1, 1)

        self.o2 = QLineEdit(self.frame_5)
        self.o2.setObjectName(u"o2")
        self.o2.setFont(font2)

        self.gridLayout_5.addWidget(self.o2, 2, 1, 1, 1)

        self.label_65 = QLabel(self.frame_5)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font2)

        self.gridLayout_5.addWidget(self.label_65, 3, 0, 1, 1)

        self.o3 = QLineEdit(self.frame_5)
        self.o3.setObjectName(u"o3")
        self.o3.setFont(font2)

        self.gridLayout_5.addWidget(self.o3, 3, 1, 1, 1)

        self.label_74 = QLabel(self.frame_5)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font2)

        self.gridLayout_5.addWidget(self.label_74, 4, 0, 1, 1)

        self.ej = QLineEdit(self.frame_5)
        self.ej.setObjectName(u"ej")
        self.ej.setFont(font2)

        self.gridLayout_5.addWidget(self.ej, 4, 1, 1, 1)


        self.gridLayout_20.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_33 = QFrame(self.centralwidget)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_33)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.frame_19 = QFrame(self.frame_33)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Panel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_19)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.order_number = QLineEdit(self.frame_19)
        self.order_number.setObjectName(u"order_number")
        font4 = QFont()
        font4.setPointSize(12)
        self.order_number.setFont(font4)
        self.order_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.order_number, 0, 1, 1, 1)

        self.label_79 = QLabel(self.frame_19)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font2)

        self.gridLayout_10.addWidget(self.label_79, 0, 0, 1, 1)


        self.gridLayout_45.addWidget(self.frame_19, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_33, 2, 1, 1, 1)

        self.frame_31 = QFrame(self.centralwidget)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_31)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.frame_6 = QFrame(self.frame_31)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Panel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.selectPath = QLineEdit(self.frame_6)
        self.selectPath.setObjectName(u"selectPath")
        font5 = QFont()
        font5.setPointSize(10)
        self.selectPath.setFont(font5)
        self.selectPath.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.selectPath, 0, 1, 1, 1)

        self.selectPathButton = QToolButton(self.frame_6)
        self.selectPathButton.setObjectName(u"selectPathButton")

        self.gridLayout_6.addWidget(self.selectPathButton, 0, 3, 1, 1)

        self.selectPathSaveButton = QPushButton(self.frame_6)
        self.selectPathSaveButton.setObjectName(u"selectPathSaveButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/save forder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectPathSaveButton.setIcon(icon1)

        self.gridLayout_6.addWidget(self.selectPathSaveButton, 0, 4, 1, 1)

        self.label_78 = QLabel(self.frame_6)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font2)

        self.gridLayout_6.addWidget(self.label_78, 0, 0, 1, 1)

        self.file_type = QComboBox(self.frame_6)
        self.file_type.addItem("")
        self.file_type.addItem("")
        self.file_type.addItem("")
        self.file_type.addItem("")
        self.file_type.addItem("")
        self.file_type.setObjectName(u"file_type")
        self.file_type.setMinimumSize(QSize(50, 0))

        self.gridLayout_6.addWidget(self.file_type, 0, 2, 1, 1)


        self.gridLayout_42.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_31)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setMidLineWidth(2)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.clearDimentionsButton = QPushButton(self.frame_4)
        self.clearDimentionsButton.setObjectName(u"clearDimentionsButton")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearDimentionsButton.setIcon(icon2)

        self.gridLayout_4.addWidget(self.clearDimentionsButton, 0, 0, 1, 1)

        self.saveDimentionsButton = QPushButton(self.frame_4)
        self.saveDimentionsButton.setObjectName(u"saveDimentionsButton")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveDimentionsButton.setIcon(icon3)

        self.gridLayout_4.addWidget(self.saveDimentionsButton, 0, 1, 1, 1)

        self.exportButton = QPushButton(self.frame_4)
        self.exportButton.setObjectName(u"exportButton")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportButton.setIcon(icon4)

        self.gridLayout_4.addWidget(self.exportButton, 0, 2, 1, 1)


        self.gridLayout_42.addWidget(self.frame_4, 1, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_31, 2, 2, 1, 2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(350, 530))
        self.frame_2.setMaximumSize(QSize(10000000, 16777215))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setMidLineWidth(1)
        self.gridLayout_23 = QGridLayout(self.frame_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label, 0, 0, 1, 2)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Box)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_8)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font6)
        self.label_22.setFrameShadow(QFrame.Sunken)
        self.label_22.setWordWrap(False)

        self.gridLayout_32.addWidget(self.label_22, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_27 = QLabel(self.frame_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font5)

        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)

        self.t_gpx = QLineEdit(self.frame_8)
        self.t_gpx.setObjectName(u"t_gpx")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_gpx.sizePolicy().hasHeightForWidth())
        self.t_gpx.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.t_gpx, 0, 1, 1, 1)

        self.label_33 = QLabel(self.frame_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font5)

        self.gridLayout_3.addWidget(self.label_33, 0, 2, 1, 1)

        self.t_gpy = QLineEdit(self.frame_8)
        self.t_gpy.setObjectName(u"t_gpy")
        sizePolicy.setHeightForWidth(self.t_gpy.sizePolicy().hasHeightForWidth())
        self.t_gpy.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.t_gpy, 0, 3, 1, 1)

        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font5)

        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)

        self.t_gpd = QLineEdit(self.frame_8)
        self.t_gpd.setObjectName(u"t_gpd")
        sizePolicy.setHeightForWidth(self.t_gpd.sizePolicy().hasHeightForWidth())
        self.t_gpd.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.t_gpd, 1, 1, 1, 1)

        self.label_34 = QLabel(self.frame_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)

        self.gridLayout_3.addWidget(self.label_34, 1, 2, 1, 1)

        self.t_gph = QLineEdit(self.frame_8)
        self.t_gph.setObjectName(u"t_gph")
        sizePolicy.setHeightForWidth(self.t_gph.sizePolicy().hasHeightForWidth())
        self.t_gph.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.t_gph, 1, 3, 1, 1)

        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)

        self.gridLayout_3.addWidget(self.label_23, 2, 0, 1, 1)

        self.t_gpl = QLineEdit(self.frame_8)
        self.t_gpl.setObjectName(u"t_gpl")
        sizePolicy.setHeightForWidth(self.t_gpl.sizePolicy().hasHeightForWidth())
        self.t_gpl.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.t_gpl, 2, 1, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_9)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setFrameShadow(QFrame.Sunken)
        self.label_24.setWordWrap(False)

        self.gridLayout_31.addWidget(self.label_24, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_36 = QLabel(self.frame_9)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font5)

        self.gridLayout_8.addWidget(self.label_36, 0, 0, 1, 1)

        self.t_rpx = QLineEdit(self.frame_9)
        self.t_rpx.setObjectName(u"t_rpx")
        sizePolicy.setHeightForWidth(self.t_rpx.sizePolicy().hasHeightForWidth())
        self.t_rpx.setSizePolicy(sizePolicy)
        self.t_rpx.setFont(font5)

        self.gridLayout_8.addWidget(self.t_rpx, 0, 1, 1, 1)

        self.label_38 = QLabel(self.frame_9)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)

        self.gridLayout_8.addWidget(self.label_38, 0, 2, 1, 1)

        self.t_rpy = QLineEdit(self.frame_9)
        self.t_rpy.setObjectName(u"t_rpy")
        sizePolicy.setHeightForWidth(self.t_rpy.sizePolicy().hasHeightForWidth())
        self.t_rpy.setSizePolicy(sizePolicy)
        self.t_rpy.setFont(font5)

        self.gridLayout_8.addWidget(self.t_rpy, 0, 3, 1, 1)

        self.label_37 = QLabel(self.frame_9)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)

        self.gridLayout_8.addWidget(self.label_37, 1, 0, 1, 1)

        self.t_rpd = QLineEdit(self.frame_9)
        self.t_rpd.setObjectName(u"t_rpd")
        sizePolicy.setHeightForWidth(self.t_rpd.sizePolicy().hasHeightForWidth())
        self.t_rpd.setSizePolicy(sizePolicy)
        self.t_rpd.setFont(font5)

        self.gridLayout_8.addWidget(self.t_rpd, 1, 1, 1, 1)

        self.label_46 = QLabel(self.frame_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font5)

        self.gridLayout_8.addWidget(self.label_46, 1, 2, 1, 1)

        self.t_rpl = QLineEdit(self.frame_9)
        self.t_rpl.setObjectName(u"t_rpl")
        sizePolicy.setHeightForWidth(self.t_rpl.sizePolicy().hasHeightForWidth())
        self.t_rpl.setSizePolicy(sizePolicy)
        self.t_rpl.setFont(font5)

        self.gridLayout_8.addWidget(self.t_rpl, 1, 3, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_8, 1, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_9)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.gridLayout_31.addWidget(self.frame_34, 2, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_9, 1, 1, 1, 1)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Box)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_29 = QLabel(self.frame_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 15))
        self.label_29.setFont(font6)
        self.label_29.setFrameShadow(QFrame.Sunken)
        self.label_29.setWordWrap(False)

        self.gridLayout_19.addWidget(self.label_29, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_40 = QLabel(self.frame_10)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font5)

        self.gridLayout_9.addWidget(self.label_40, 0, 0, 1, 1)

        self.t_ppx = QLineEdit(self.frame_10)
        self.t_ppx.setObjectName(u"t_ppx")
        sizePolicy.setHeightForWidth(self.t_ppx.sizePolicy().hasHeightForWidth())
        self.t_ppx.setSizePolicy(sizePolicy)
        self.t_ppx.setFont(font5)

        self.gridLayout_9.addWidget(self.t_ppx, 0, 1, 1, 1)

        self.label_41 = QLabel(self.frame_10)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font5)

        self.gridLayout_9.addWidget(self.label_41, 0, 2, 1, 1)

        self.t_ppy = QLineEdit(self.frame_10)
        self.t_ppy.setObjectName(u"t_ppy")
        sizePolicy.setHeightForWidth(self.t_ppy.sizePolicy().hasHeightForWidth())
        self.t_ppy.setSizePolicy(sizePolicy)
        self.t_ppy.setFont(font5)

        self.gridLayout_9.addWidget(self.t_ppy, 0, 3, 1, 1)

        self.label_39 = QLabel(self.frame_10)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font5)

        self.gridLayout_9.addWidget(self.label_39, 1, 0, 1, 1)

        self.t_ppd = QLineEdit(self.frame_10)
        self.t_ppd.setObjectName(u"t_ppd")
        sizePolicy.setHeightForWidth(self.t_ppd.sizePolicy().hasHeightForWidth())
        self.t_ppd.setSizePolicy(sizePolicy)
        self.t_ppd.setFont(font5)

        self.gridLayout_9.addWidget(self.t_ppd, 1, 1, 1, 1)

        self.label_42 = QLabel(self.frame_10)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font5)

        self.gridLayout_9.addWidget(self.label_42, 1, 2, 1, 1)

        self.t_pph = QLineEdit(self.frame_10)
        self.t_pph.setObjectName(u"t_pph")
        sizePolicy.setHeightForWidth(self.t_pph.sizePolicy().hasHeightForWidth())
        self.t_pph.setSizePolicy(sizePolicy)
        self.t_pph.setFont(font5)

        self.gridLayout_9.addWidget(self.t_pph, 1, 3, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.frame_35 = QFrame(self.frame_10)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.gridLayout_19.addWidget(self.frame_35, 2, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_10, 2, 0, 1, 1)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_16)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_121 = QLabel(self.frame_16)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMaximumSize(QSize(16777215, 15))
        self.label_121.setFont(font6)
        self.label_121.setFrameShadow(QFrame.Sunken)
        self.label_121.setWordWrap(False)

        self.gridLayout_21.addWidget(self.label_121, 0, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_122 = QLabel(self.frame_16)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font5)

        self.gridLayout_15.addWidget(self.label_122, 0, 0, 1, 1)

        self.t_pbx = QLineEdit(self.frame_16)
        self.t_pbx.setObjectName(u"t_pbx")
        sizePolicy.setHeightForWidth(self.t_pbx.sizePolicy().hasHeightForWidth())
        self.t_pbx.setSizePolicy(sizePolicy)
        self.t_pbx.setFont(font5)

        self.gridLayout_15.addWidget(self.t_pbx, 0, 1, 1, 1)

        self.label_123 = QLabel(self.frame_16)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font5)

        self.gridLayout_15.addWidget(self.label_123, 0, 2, 1, 1)

        self.t_pby = QLineEdit(self.frame_16)
        self.t_pby.setObjectName(u"t_pby")
        sizePolicy.setHeightForWidth(self.t_pby.sizePolicy().hasHeightForWidth())
        self.t_pby.setSizePolicy(sizePolicy)
        self.t_pby.setFont(font5)

        self.gridLayout_15.addWidget(self.t_pby, 0, 3, 1, 1)

        self.label_124 = QLabel(self.frame_16)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font5)

        self.gridLayout_15.addWidget(self.label_124, 1, 0, 1, 1)

        self.t_pbw = QLineEdit(self.frame_16)
        self.t_pbw.setObjectName(u"t_pbw")
        sizePolicy.setHeightForWidth(self.t_pbw.sizePolicy().hasHeightForWidth())
        self.t_pbw.setSizePolicy(sizePolicy)
        self.t_pbw.setFont(font5)

        self.gridLayout_15.addWidget(self.t_pbw, 1, 1, 1, 1)

        self.label_125 = QLabel(self.frame_16)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font5)

        self.gridLayout_15.addWidget(self.label_125, 1, 2, 1, 1)

        self.t_pbl = QLineEdit(self.frame_16)
        self.t_pbl.setObjectName(u"t_pbl")
        sizePolicy.setHeightForWidth(self.t_pbl.sizePolicy().hasHeightForWidth())
        self.t_pbl.setSizePolicy(sizePolicy)
        self.t_pbl.setFont(font5)

        self.gridLayout_15.addWidget(self.t_pbl, 1, 3, 1, 1)

        self.label_126 = QLabel(self.frame_16)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font5)

        self.gridLayout_15.addWidget(self.label_126, 2, 0, 1, 1)

        self.t_pbh = QLineEdit(self.frame_16)
        self.t_pbh.setObjectName(u"t_pbh")
        sizePolicy.setHeightForWidth(self.t_pbh.sizePolicy().hasHeightForWidth())
        self.t_pbh.setSizePolicy(sizePolicy)
        self.t_pbh.setFont(font5)

        self.gridLayout_15.addWidget(self.t_pbh, 2, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_15, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_16, 2, 1, 1, 1)

        self.frame_25 = QFrame(self.frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Box)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_25)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_144 = QLabel(self.frame_25)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setFont(font6)
        self.label_144.setFrameShadow(QFrame.Sunken)
        self.label_144.setWordWrap(False)

        self.gridLayout_27.addWidget(self.label_144, 0, 0, 1, 1)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_145 = QLabel(self.frame_25)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font5)

        self.gridLayout_28.addWidget(self.label_145, 0, 0, 1, 1)

        self.t_sllrx = QLineEdit(self.frame_25)
        self.t_sllrx.setObjectName(u"t_sllrx")
        sizePolicy.setHeightForWidth(self.t_sllrx.sizePolicy().hasHeightForWidth())
        self.t_sllrx.setSizePolicy(sizePolicy)
        self.t_sllrx.setFont(font5)

        self.gridLayout_28.addWidget(self.t_sllrx, 0, 1, 1, 1)

        self.label_146 = QLabel(self.frame_25)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font5)

        self.gridLayout_28.addWidget(self.label_146, 0, 2, 1, 1)

        self.t_sllry = QLineEdit(self.frame_25)
        self.t_sllry.setObjectName(u"t_sllry")
        sizePolicy.setHeightForWidth(self.t_sllry.sizePolicy().hasHeightForWidth())
        self.t_sllry.setSizePolicy(sizePolicy)
        self.t_sllry.setFont(font5)

        self.gridLayout_28.addWidget(self.t_sllry, 0, 3, 1, 1)

        self.label_147 = QLabel(self.frame_25)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font5)

        self.gridLayout_28.addWidget(self.label_147, 1, 0, 1, 1)

        self.t_sllrw = QLineEdit(self.frame_25)
        self.t_sllrw.setObjectName(u"t_sllrw")
        sizePolicy.setHeightForWidth(self.t_sllrw.sizePolicy().hasHeightForWidth())
        self.t_sllrw.setSizePolicy(sizePolicy)
        self.t_sllrw.setFont(font5)

        self.gridLayout_28.addWidget(self.t_sllrw, 1, 1, 1, 1)

        self.label_148 = QLabel(self.frame_25)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font5)

        self.gridLayout_28.addWidget(self.label_148, 1, 2, 1, 1)

        self.t_sllrl = QLineEdit(self.frame_25)
        self.t_sllrl.setObjectName(u"t_sllrl")
        sizePolicy.setHeightForWidth(self.t_sllrl.sizePolicy().hasHeightForWidth())
        self.t_sllrl.setSizePolicy(sizePolicy)
        self.t_sllrl.setFont(font5)

        self.gridLayout_28.addWidget(self.t_sllrl, 1, 3, 1, 1)

        self.label_149 = QLabel(self.frame_25)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font5)

        self.gridLayout_28.addWidget(self.label_149, 2, 0, 1, 1)

        self.t_sllrh = QLineEdit(self.frame_25)
        self.t_sllrh.setObjectName(u"t_sllrh")
        sizePolicy.setHeightForWidth(self.t_sllrh.sizePolicy().hasHeightForWidth())
        self.t_sllrh.setSizePolicy(sizePolicy)
        self.t_sllrh.setFont(font5)

        self.gridLayout_28.addWidget(self.t_sllrh, 2, 1, 1, 1)


        self.gridLayout_27.addLayout(self.gridLayout_28, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_25, 3, 0, 1, 1)

        self.frame_26 = QFrame(self.frame_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Box)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_26)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_151 = QLabel(self.frame_26)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font6)
        self.label_151.setFrameShadow(QFrame.Sunken)
        self.label_151.setWordWrap(False)

        self.gridLayout_29.addWidget(self.label_151, 0, 0, 1, 1)

        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_152 = QLabel(self.frame_26)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font5)

        self.gridLayout_34.addWidget(self.label_152, 0, 0, 1, 1)

        self.t_sludx = QLineEdit(self.frame_26)
        self.t_sludx.setObjectName(u"t_sludx")
        sizePolicy.setHeightForWidth(self.t_sludx.sizePolicy().hasHeightForWidth())
        self.t_sludx.setSizePolicy(sizePolicy)
        self.t_sludx.setFont(font5)

        self.gridLayout_34.addWidget(self.t_sludx, 0, 1, 1, 1)

        self.label_153 = QLabel(self.frame_26)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setFont(font5)

        self.gridLayout_34.addWidget(self.label_153, 0, 2, 1, 1)

        self.t_sludy = QLineEdit(self.frame_26)
        self.t_sludy.setObjectName(u"t_sludy")
        sizePolicy.setHeightForWidth(self.t_sludy.sizePolicy().hasHeightForWidth())
        self.t_sludy.setSizePolicy(sizePolicy)
        self.t_sludy.setFont(font5)

        self.gridLayout_34.addWidget(self.t_sludy, 0, 3, 1, 1)

        self.label_154 = QLabel(self.frame_26)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setFont(font5)

        self.gridLayout_34.addWidget(self.label_154, 1, 0, 1, 1)

        self.t_sludw = QLineEdit(self.frame_26)
        self.t_sludw.setObjectName(u"t_sludw")
        sizePolicy.setHeightForWidth(self.t_sludw.sizePolicy().hasHeightForWidth())
        self.t_sludw.setSizePolicy(sizePolicy)
        self.t_sludw.setFont(font5)

        self.gridLayout_34.addWidget(self.t_sludw, 1, 1, 1, 1)

        self.label_155 = QLabel(self.frame_26)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font5)

        self.gridLayout_34.addWidget(self.label_155, 1, 2, 1, 1)

        self.t_sludl = QLineEdit(self.frame_26)
        self.t_sludl.setObjectName(u"t_sludl")
        sizePolicy.setHeightForWidth(self.t_sludl.sizePolicy().hasHeightForWidth())
        self.t_sludl.setSizePolicy(sizePolicy)
        self.t_sludl.setFont(font5)

        self.gridLayout_34.addWidget(self.t_sludl, 1, 3, 1, 1)

        self.label_156 = QLabel(self.frame_26)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font5)

        self.gridLayout_34.addWidget(self.label_156, 2, 0, 1, 1)

        self.t_sludh = QLineEdit(self.frame_26)
        self.t_sludh.setObjectName(u"t_sludh")
        sizePolicy.setHeightForWidth(self.t_sludh.sizePolicy().hasHeightForWidth())
        self.t_sludh.setSizePolicy(sizePolicy)
        self.t_sludh.setFont(font5)

        self.gridLayout_34.addWidget(self.t_sludh, 2, 1, 1, 1)


        self.gridLayout_29.addLayout(self.gridLayout_34, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_26, 3, 1, 1, 1)

        self.label_plate_13 = QLabel(self.frame_2)
        self.label_plate_13.setObjectName(u"label_plate_13")
        self.label_plate_13.setFont(font3)
        self.label_plate_13.setFrameShadow(QFrame.Sunken)
        self.label_plate_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_plate_13.setWordWrap(False)

        self.gridLayout_23.addWidget(self.label_plate_13, 4, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_2, 0, 1, 2, 1)

        self.frame_13 = QFrame(self.centralwidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(410, 530))
        self.frame_13.setMaximumSize(QSize(5000000, 16777215))
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_13.setMidLineWidth(1)
        self.gridLayout_24 = QGridLayout(self.frame_13)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.frame_3 = QFrame(self.frame_13)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_3)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font6)
        self.label_30.setFrameShadow(QFrame.Sunken)
        self.label_30.setWordWrap(False)

        self.gridLayout.addWidget(self.label_30, 0, 0, 1, 3)

        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font5)

        self.gridLayout.addWidget(self.label_31, 1, 0, 1, 2)

        self.f_gpx = QLineEdit(self.frame_3)
        self.f_gpx.setObjectName(u"f_gpx")
        self.f_gpx.setFont(font5)

        self.gridLayout.addWidget(self.f_gpx, 1, 2, 1, 1)

        self.label_43 = QLabel(self.frame_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font5)

        self.gridLayout.addWidget(self.label_43, 1, 3, 1, 1)

        self.f_gpy = QLineEdit(self.frame_3)
        self.f_gpy.setObjectName(u"f_gpy")
        self.f_gpy.setFont(font5)

        self.gridLayout.addWidget(self.f_gpy, 1, 4, 1, 1)

        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font5)

        self.gridLayout.addWidget(self.label_32, 2, 0, 1, 2)

        self.f_gpd = QLineEdit(self.frame_3)
        self.f_gpd.setObjectName(u"f_gpd")
        self.f_gpd.setFont(font5)

        self.gridLayout.addWidget(self.f_gpd, 2, 2, 1, 1)

        self.f_gph = QLineEdit(self.frame_3)
        self.f_gph.setObjectName(u"f_gph")
        self.f_gph.setFont(font5)

        self.gridLayout.addWidget(self.f_gph, 2, 4, 1, 1)

        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font5)

        self.gridLayout.addWidget(self.label_45, 3, 0, 1, 1)

        self.f_gpl = QLineEdit(self.frame_3)
        self.f_gpl.setObjectName(u"f_gpl")
        self.f_gpl.setFont(font5)

        self.gridLayout.addWidget(self.f_gpl, 3, 2, 1, 1)

        self.label_44 = QLabel(self.frame_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font5)

        self.gridLayout.addWidget(self.label_44, 2, 3, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_3, 1, 0, 2, 2)

        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_55 = QLabel(self.frame_11)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font6)
        self.label_55.setFrameShadow(QFrame.Sunken)
        self.label_55.setWordWrap(False)

        self.gridLayout_11.addWidget(self.label_55, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_54 = QLabel(self.frame_11)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font5)

        self.horizontalLayout_6.addWidget(self.label_54)

        self.f_prx = QLineEdit(self.frame_11)
        self.f_prx.setObjectName(u"f_prx")
        self.f_prx.setFont(font5)

        self.horizontalLayout_6.addWidget(self.f_prx)

        self.label_52 = QLabel(self.frame_11)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font5)

        self.horizontalLayout_6.addWidget(self.label_52)

        self.f_pry = QLineEdit(self.frame_11)
        self.f_pry.setObjectName(u"f_pry")
        self.f_pry.setFont(font5)

        self.horizontalLayout_6.addWidget(self.f_pry)


        self.gridLayout_11.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_53 = QLabel(self.frame_11)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_53)

        self.f_prd = QLineEdit(self.frame_11)
        self.f_prd.setObjectName(u"f_prd")
        self.f_prd.setFont(font5)

        self.horizontalLayout_7.addWidget(self.f_prd)

        self.label_75 = QLabel(self.frame_11)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_75)

        self.f_prd2 = QLineEdit(self.frame_11)
        self.f_prd2.setObjectName(u"f_prd2")
        self.f_prd2.setFont(font5)

        self.horizontalLayout_7.addWidget(self.f_prd2)


        self.gridLayout_11.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_71 = QLabel(self.frame_11)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_71)

        self.f_prh = QLineEdit(self.frame_11)
        self.f_prh.setObjectName(u"f_prh")
        self.f_prh.setFont(font5)

        self.horizontalLayout_8.addWidget(self.f_prh)

        self.label_72 = QLabel(self.frame_11)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_72)

        self.f_prh2 = QLineEdit(self.frame_11)
        self.f_prh2.setObjectName(u"f_prh2")
        self.f_prh2.setFont(font5)

        self.horizontalLayout_8.addWidget(self.f_prh2)


        self.gridLayout_11.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_11, 1, 2, 2, 2)

        self.label_76 = QLabel(self.frame_13)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font6)
        self.label_76.setFrameShadow(QFrame.Sunken)
        self.label_76.setWordWrap(False)

        self.gridLayout_24.addWidget(self.label_76, 2, 1, 1, 1)

        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_70 = QLabel(self.frame_12)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font6)
        self.label_70.setFrameShadow(QFrame.Sunken)
        self.label_70.setWordWrap(False)

        self.gridLayout_7.addWidget(self.label_70, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_68 = QLabel(self.frame_12)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_68)

        self.f_ppx = QLineEdit(self.frame_12)
        self.f_ppx.setObjectName(u"f_ppx")
        self.f_ppx.setFont(font5)

        self.horizontalLayout_9.addWidget(self.f_ppx)

        self.label_67 = QLabel(self.frame_12)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_67)

        self.f_ppy = QLineEdit(self.frame_12)
        self.f_ppy.setObjectName(u"f_ppy")
        self.f_ppy.setFont(font5)

        self.horizontalLayout_9.addWidget(self.f_ppy)


        self.gridLayout_7.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_66 = QLabel(self.frame_12)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_66)

        self.f_ppd = QLineEdit(self.frame_12)
        self.f_ppd.setObjectName(u"f_ppd")
        self.f_ppd.setFont(font5)

        self.horizontalLayout_10.addWidget(self.f_ppd)

        self.label_69 = QLabel(self.frame_12)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_69)

        self.f_pph = QLineEdit(self.frame_12)
        self.f_pph.setObjectName(u"f_pph")
        self.f_pph.setFont(font5)

        self.horizontalLayout_10.addWidget(self.f_pph)


        self.gridLayout_7.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.frame_32 = QFrame(self.frame_12)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_32, 3, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_12, 3, 0, 2, 2)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_17)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_127 = QLabel(self.frame_17)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font6)
        self.label_127.setFrameShadow(QFrame.Sunken)
        self.label_127.setWordWrap(False)

        self.gridLayout_22.addWidget(self.label_127, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_128 = QLabel(self.frame_17)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font5)

        self.gridLayout_16.addWidget(self.label_128, 0, 0, 1, 1)

        self.f_pbx = QLineEdit(self.frame_17)
        self.f_pbx.setObjectName(u"f_pbx")
        self.f_pbx.setFont(font5)

        self.gridLayout_16.addWidget(self.f_pbx, 0, 1, 1, 1)

        self.label_129 = QLabel(self.frame_17)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font5)

        self.gridLayout_16.addWidget(self.label_129, 0, 2, 1, 1)

        self.f_pby = QLineEdit(self.frame_17)
        self.f_pby.setObjectName(u"f_pby")
        self.f_pby.setFont(font5)

        self.gridLayout_16.addWidget(self.f_pby, 0, 3, 1, 1)

        self.label_130 = QLabel(self.frame_17)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setFont(font5)

        self.gridLayout_16.addWidget(self.label_130, 1, 0, 1, 1)

        self.f_pbw = QLineEdit(self.frame_17)
        self.f_pbw.setObjectName(u"f_pbw")
        self.f_pbw.setFont(font5)

        self.gridLayout_16.addWidget(self.f_pbw, 1, 1, 1, 1)

        self.label_131 = QLabel(self.frame_17)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setFont(font5)

        self.gridLayout_16.addWidget(self.label_131, 1, 2, 1, 1)

        self.f_pbl = QLineEdit(self.frame_17)
        self.f_pbl.setObjectName(u"f_pbl")
        self.f_pbl.setFont(font5)

        self.gridLayout_16.addWidget(self.f_pbl, 1, 3, 1, 1)

        self.label_132 = QLabel(self.frame_17)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font5)

        self.gridLayout_16.addWidget(self.label_132, 2, 0, 1, 1)

        self.f_pbh = QLineEdit(self.frame_17)
        self.f_pbh.setObjectName(u"f_pbh")
        self.f_pbh.setFont(font5)

        self.gridLayout_16.addWidget(self.f_pbh, 2, 1, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_16, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_17, 3, 2, 2, 2)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_15)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_89 = QLabel(self.frame_15)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font6)
        self.label_89.setFrameShadow(QFrame.Sunken)
        self.label_89.setWordWrap(False)

        self.gridLayout_14.addWidget(self.label_89, 0, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_90 = QLabel(self.frame_15)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font5)

        self.gridLayout_13.addWidget(self.label_90, 0, 0, 1, 1)

        self.f_aglry = QLineEdit(self.frame_15)
        self.f_aglry.setObjectName(u"f_aglry")
        self.f_aglry.setFont(font5)

        self.gridLayout_13.addWidget(self.f_aglry, 0, 3, 1, 1)

        self.label_92 = QLabel(self.frame_15)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font5)

        self.gridLayout_13.addWidget(self.label_92, 1, 0, 1, 1)

        self.label_93 = QLabel(self.frame_15)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font5)

        self.gridLayout_13.addWidget(self.label_93, 1, 2, 1, 1)

        self.f_aglrh = QLineEdit(self.frame_15)
        self.f_aglrh.setObjectName(u"f_aglrh")
        self.f_aglrh.setFont(font5)

        self.gridLayout_13.addWidget(self.f_aglrh, 1, 3, 1, 1)

        self.label_94 = QLabel(self.frame_15)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font5)

        self.gridLayout_13.addWidget(self.label_94, 2, 0, 1, 1)

        self.f_aglra = QLineEdit(self.frame_15)
        self.f_aglra.setObjectName(u"f_aglra")
        self.f_aglra.setFont(font5)

        self.gridLayout_13.addWidget(self.f_aglra, 2, 1, 1, 1)

        self.f_aglrx = QLineEdit(self.frame_15)
        self.f_aglrx.setObjectName(u"f_aglrx")
        self.f_aglrx.setFont(font5)

        self.gridLayout_13.addWidget(self.f_aglrx, 0, 1, 1, 1)

        self.label_91 = QLabel(self.frame_15)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font5)

        self.gridLayout_13.addWidget(self.label_91, 0, 2, 1, 1)

        self.f_aglrd = QLineEdit(self.frame_15)
        self.f_aglrd.setObjectName(u"f_aglrd")
        self.f_aglrd.setFont(font5)

        self.gridLayout_13.addWidget(self.f_aglrd, 1, 1, 1, 1)

        self.label_150 = QLabel(self.frame_15)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font5)

        self.gridLayout_13.addWidget(self.label_150, 2, 2, 1, 1)

        self.f_aglrl = QLineEdit(self.frame_15)
        self.f_aglrl.setObjectName(u"f_aglrl")
        self.f_aglrl.setFont(font5)

        self.gridLayout_13.addWidget(self.f_aglrl, 2, 3, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_13, 1, 0, 2, 2)


        self.gridLayout_24.addWidget(self.frame_15, 5, 0, 2, 2)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Box)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_18)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_95 = QLabel(self.frame_18)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font6)
        self.label_95.setFrameShadow(QFrame.Sunken)
        self.label_95.setWordWrap(False)

        self.gridLayout_17.addWidget(self.label_95, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_96 = QLabel(self.frame_18)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font5)

        self.gridLayout_18.addWidget(self.label_96, 0, 0, 1, 1)

        self.f_agudy = QLineEdit(self.frame_18)
        self.f_agudy.setObjectName(u"f_agudy")
        self.f_agudy.setFont(font5)

        self.gridLayout_18.addWidget(self.f_agudy, 0, 3, 1, 1)

        self.label_97 = QLabel(self.frame_18)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font5)

        self.gridLayout_18.addWidget(self.label_97, 1, 0, 1, 1)

        self.label_98 = QLabel(self.frame_18)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font5)

        self.gridLayout_18.addWidget(self.label_98, 1, 2, 1, 1)

        self.f_agudh = QLineEdit(self.frame_18)
        self.f_agudh.setObjectName(u"f_agudh")
        self.f_agudh.setFont(font5)

        self.gridLayout_18.addWidget(self.f_agudh, 1, 3, 1, 1)

        self.label_99 = QLabel(self.frame_18)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font5)

        self.gridLayout_18.addWidget(self.label_99, 2, 0, 1, 1)

        self.f_aguda = QLineEdit(self.frame_18)
        self.f_aguda.setObjectName(u"f_aguda")
        self.f_aguda.setFont(font5)

        self.gridLayout_18.addWidget(self.f_aguda, 2, 1, 1, 1)

        self.f_agudx = QLineEdit(self.frame_18)
        self.f_agudx.setObjectName(u"f_agudx")
        self.f_agudx.setFont(font5)

        self.gridLayout_18.addWidget(self.f_agudx, 0, 1, 1, 1)

        self.label_100 = QLabel(self.frame_18)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font5)

        self.gridLayout_18.addWidget(self.label_100, 0, 2, 1, 1)

        self.f_agudd = QLineEdit(self.frame_18)
        self.f_agudd.setObjectName(u"f_agudd")
        self.f_agudd.setFont(font5)

        self.gridLayout_18.addWidget(self.f_agudd, 1, 1, 1, 1)

        self.label_157 = QLabel(self.frame_18)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setFont(font5)

        self.gridLayout_18.addWidget(self.label_157, 2, 2, 1, 1)

        self.f_agudl = QLineEdit(self.frame_18)
        self.f_agudl.setObjectName(u"f_agudl")
        self.f_agudl.setFont(font5)

        self.gridLayout_18.addWidget(self.f_agudl, 2, 3, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_18, 1, 0, 2, 2)


        self.gridLayout_24.addWidget(self.frame_18, 5, 2, 2, 2)

        self.label_73 = QLabel(self.frame_13)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font6)
        self.label_73.setFrameShadow(QFrame.Sunken)
        self.label_73.setWordWrap(False)

        self.gridLayout_24.addWidget(self.label_73, 6, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_13)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_47 = QLabel(self.frame_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font6)
        self.label_47.setFrameShadow(QFrame.Sunken)
        self.label_47.setWordWrap(False)

        self.gridLayout_12.addWidget(self.label_47, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_50 = QLabel(self.frame_7)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_50)

        self.f_spd = QLineEdit(self.frame_7)
        self.f_spd.setObjectName(u"f_spd")
        self.f_spd.setFont(font5)

        self.horizontalLayout_2.addWidget(self.f_spd)

        self.label_58 = QLabel(self.frame_7)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_58)

        self.f_spd2 = QLineEdit(self.frame_7)
        self.f_spd2.setObjectName(u"f_spd2")
        self.f_spd2.setFont(font5)

        self.horizontalLayout_2.addWidget(self.f_spd2)

        self.label_57 = QLabel(self.frame_7)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_57)

        self.f_spd3 = QLineEdit(self.frame_7)
        self.f_spd3.setObjectName(u"f_spd3")
        self.f_spd3.setFont(font5)

        self.horizontalLayout_2.addWidget(self.f_spd3)


        self.gridLayout_12.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_59 = QLabel(self.frame_7)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font5)

        self.horizontalLayout.addWidget(self.label_59)

        self.f_sph = QLineEdit(self.frame_7)
        self.f_sph.setObjectName(u"f_sph")
        self.f_sph.setFont(font5)

        self.horizontalLayout.addWidget(self.f_sph)

        self.label_61 = QLabel(self.frame_7)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font5)

        self.horizontalLayout.addWidget(self.label_61)

        self.f_sph2 = QLineEdit(self.frame_7)
        self.f_sph2.setObjectName(u"f_sph2")
        self.f_sph2.setFont(font5)

        self.horizontalLayout.addWidget(self.f_sph2)

        self.label_60 = QLabel(self.frame_7)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font5)

        self.horizontalLayout.addWidget(self.label_60)

        self.f_sph3 = QLineEdit(self.frame_7)
        self.f_sph3.setObjectName(u"f_sph3")
        self.f_sph3.setFont(font5)

        self.horizontalLayout.addWidget(self.f_sph3)


        self.gridLayout_12.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_48 = QLabel(self.frame_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_48)

        self.f_spx = QLineEdit(self.frame_7)
        self.f_spx.setObjectName(u"f_spx")
        self.f_spx.setFont(font5)

        self.horizontalLayout_3.addWidget(self.f_spx)

        self.label_49 = QLabel(self.frame_7)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_49)

        self.f_spy = QLineEdit(self.frame_7)
        self.f_spy.setObjectName(u"f_spy")
        self.f_spy.setFont(font5)

        self.horizontalLayout_3.addWidget(self.f_spy)


        self.gridLayout_12.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_7, 7, 0, 1, 3)

        self.label_plate_14 = QLabel(self.frame_13)
        self.label_plate_14.setObjectName(u"label_plate_14")
        self.label_plate_14.setFont(font3)
        self.label_plate_14.setFrameShadow(QFrame.Sunken)
        self.label_plate_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_plate_14.setWordWrap(False)

        self.gridLayout_24.addWidget(self.label_plate_14, 7, 3, 1, 1)

        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))
        self.label_2.setFont(font6)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.label_2, 0, 0, 1, 4)


        self.gridLayout_20.addWidget(self.frame_13, 0, 2, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.w1, self.w2)
        QWidget.setTabOrder(self.w2, self.h1)
        QWidget.setTabOrder(self.h1, self.h2)
        QWidget.setTabOrder(self.h2, self.t1)
        QWidget.setTabOrder(self.t1, self.t2)
        QWidget.setTabOrder(self.t2, self.w3)
        QWidget.setTabOrder(self.w3, self.h3)
        QWidget.setTabOrder(self.h3, self.t3)
        QWidget.setTabOrder(self.t3, self.t_gpx)
        QWidget.setTabOrder(self.t_gpx, self.t_gpy)
        QWidget.setTabOrder(self.t_gpy, self.t_gpd)
        QWidget.setTabOrder(self.t_gpd, self.t_gph)
        QWidget.setTabOrder(self.t_gph, self.t_gpl)
        QWidget.setTabOrder(self.t_gpl, self.t_rpx)
        QWidget.setTabOrder(self.t_rpx, self.t_rpy)
        QWidget.setTabOrder(self.t_rpy, self.t_rpd)
        QWidget.setTabOrder(self.t_rpd, self.t_rpl)
        QWidget.setTabOrder(self.t_rpl, self.t_ppx)
        QWidget.setTabOrder(self.t_ppx, self.t_ppy)
        QWidget.setTabOrder(self.t_ppy, self.t_ppd)
        QWidget.setTabOrder(self.t_ppd, self.t_pph)
        QWidget.setTabOrder(self.t_pph, self.t_pbx)
        QWidget.setTabOrder(self.t_pbx, self.t_pby)
        QWidget.setTabOrder(self.t_pby, self.t_pbw)
        QWidget.setTabOrder(self.t_pbw, self.t_pbl)
        QWidget.setTabOrder(self.t_pbl, self.t_pbh)
        QWidget.setTabOrder(self.t_pbh, self.t_sllrx)
        QWidget.setTabOrder(self.t_sllrx, self.t_sllry)
        QWidget.setTabOrder(self.t_sllry, self.t_sllrw)
        QWidget.setTabOrder(self.t_sllrw, self.t_sllrl)
        QWidget.setTabOrder(self.t_sllrl, self.t_sllrh)
        QWidget.setTabOrder(self.t_sllrh, self.t_sludx)
        QWidget.setTabOrder(self.t_sludx, self.t_sludy)
        QWidget.setTabOrder(self.t_sludy, self.t_sludw)
        QWidget.setTabOrder(self.t_sludw, self.t_sludl)
        QWidget.setTabOrder(self.t_sludl, self.t_sludh)
        QWidget.setTabOrder(self.t_sludh, self.f_gpx)
        QWidget.setTabOrder(self.f_gpx, self.f_gpy)
        QWidget.setTabOrder(self.f_gpy, self.f_gpd)
        QWidget.setTabOrder(self.f_gpd, self.f_gph)
        QWidget.setTabOrder(self.f_gph, self.f_gpl)
        QWidget.setTabOrder(self.f_gpl, self.f_prx)
        QWidget.setTabOrder(self.f_prx, self.f_pry)
        QWidget.setTabOrder(self.f_pry, self.f_prd)
        QWidget.setTabOrder(self.f_prd, self.f_prd2)
        QWidget.setTabOrder(self.f_prd2, self.f_prh)
        QWidget.setTabOrder(self.f_prh, self.f_prh2)
        QWidget.setTabOrder(self.f_prh2, self.f_ppx)
        QWidget.setTabOrder(self.f_ppx, self.f_ppy)
        QWidget.setTabOrder(self.f_ppy, self.f_ppd)
        QWidget.setTabOrder(self.f_ppd, self.f_pph)
        QWidget.setTabOrder(self.f_pph, self.f_pbx)
        QWidget.setTabOrder(self.f_pbx, self.f_pby)
        QWidget.setTabOrder(self.f_pby, self.f_pbw)
        QWidget.setTabOrder(self.f_pbw, self.f_pbl)
        QWidget.setTabOrder(self.f_pbl, self.f_pbh)
        QWidget.setTabOrder(self.f_pbh, self.f_aglrx)
        QWidget.setTabOrder(self.f_aglrx, self.f_aglry)
        QWidget.setTabOrder(self.f_aglry, self.f_aglrd)
        QWidget.setTabOrder(self.f_aglrd, self.f_aglrh)
        QWidget.setTabOrder(self.f_aglrh, self.f_aglra)
        QWidget.setTabOrder(self.f_aglra, self.f_aglrl)
        QWidget.setTabOrder(self.f_aglrl, self.f_agudx)
        QWidget.setTabOrder(self.f_agudx, self.f_agudy)
        QWidget.setTabOrder(self.f_agudy, self.f_agudd)
        QWidget.setTabOrder(self.f_agudd, self.f_agudh)
        QWidget.setTabOrder(self.f_agudh, self.f_aguda)
        QWidget.setTabOrder(self.f_aguda, self.f_agudl)
        QWidget.setTabOrder(self.f_agudl, self.f_spx)
        QWidget.setTabOrder(self.f_spx, self.f_spy)
        QWidget.setTabOrder(self.f_spy, self.f_spd)
        QWidget.setTabOrder(self.f_spd, self.f_spd2)
        QWidget.setTabOrder(self.f_spd2, self.f_spd3)
        QWidget.setTabOrder(self.f_spd3, self.f_sph)
        QWidget.setTabOrder(self.f_sph, self.f_sph2)
        QWidget.setTabOrder(self.f_sph2, self.f_sph3)
        QWidget.setTabOrder(self.f_sph3, self.o1)
        QWidget.setTabOrder(self.o1, self.o2)
        QWidget.setTabOrder(self.o2, self.o3)
        QWidget.setTabOrder(self.o3, self.ej)
        QWidget.setTabOrder(self.ej, self.order_number)
        QWidget.setTabOrder(self.order_number, self.selectPath)
        QWidget.setTabOrder(self.selectPath, self.selectPathButton)
        QWidget.setTabOrder(self.selectPathButton, self.selectPathSaveButton)
        QWidget.setTabOrder(self.selectPathSaveButton, self.clearDimentionsButton)
        QWidget.setTabOrder(self.clearDimentionsButton, self.saveDimentionsButton)
        QWidget.setTabOrder(self.saveDimentionsButton, self.exportButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u91d1\u578b\u4f5c\u6210", None))
        self.label_plate_1.setText(QCoreApplication.translate("MainWindow", u"\u203b\u203b\u3000\u30e1\u30a4\u30f3\u30d7\u30ec\u30fc\u30c8\u3000\u203b\u203b", None))
        self.label_plate_2.setText(QCoreApplication.translate("MainWindow", u"\u5e45\u30fbPL\u9762\u5074", None))
        self.w1.setText("")
        self.w1.setPlaceholderText("")
        self.label_plate_3.setText(QCoreApplication.translate("MainWindow", u"\u5e45\u30fb\u6a5f\u4f53\u5074", None))
        self.w2.setText("")
        self.w2.setPlaceholderText("")
        self.label_plate_4.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u3055\u30fbPL\u9762\u5074", None))
        self.h1.setText("")
        self.h1.setPlaceholderText("")
        self.label_plate_5.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u3055\u30fb\u6a5f\u4f53\u5074", None))
        self.h2.setText("")
        self.h2.setPlaceholderText("")
        self.label_plate_6.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52d5\u578b\u677f\u539a", None))
        self.t1.setText("")
        self.t1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f8b\uff1a 30,60,35", None))
        self.label_plate_7.setText(QCoreApplication.translate("MainWindow", u"\u56fa\u5b9a\u578b\u677f\u539a", None))
        self.t2.setText("")
        self.t2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f8b\uff1a 30,25", None))
        self.label_plate_8.setText(QCoreApplication.translate("MainWindow", u"\u203b\u203b\u3000EJ\u30d7\u30ec\u30fc\u30c8\u3000\u203b\u203b", None))
        self.label_plate_9.setText(QCoreApplication.translate("MainWindow", u"\u5e45\u3000\u3000\u3000\u3000\u3000\u3000", None))
        self.w3.setText("")
        self.w3.setPlaceholderText("")
        self.label_plate_10.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u3055", None))
        self.h3.setText("")
        self.h3.setPlaceholderText("")
        self.label_plate_11.setText(QCoreApplication.translate("MainWindow", u"\u677f\u539a", None))
        self.t3.setText("")
        self.t3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4f8b\uff1a10,15", None))
        self.label_plate_12.setText(QCoreApplication.translate("MainWindow", u"* \u677f\u539a\u306fPL\u9762\u3088\u308a\u306e\u5bf8\u6cd5\u3067\u3059\u3002", None))
#if QT_CONFIG(accessibility)
        self.frame_5.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u203b\u203b\u3000\u91d1\u578b\u958b\u304d\u3000\u203b\u203b", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u88fd\u54c1\u5074\u3000\u3000\u3000", None))
        self.o1.setText("")
        self.o1.setPlaceholderText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u30e9\u30f3\u30ca\u30fc\u5074", None))
        self.o2.setText("")
        self.o2.setPlaceholderText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u30ce\u30ba\u30eb\u5074", None))
        self.o3.setText("")
        self.o3.setPlaceholderText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"EJ\u91cf", None))
        self.ej.setText("")
        self.ej.setPlaceholderText("")
        self.order_number.setText("")
        self.order_number.setPlaceholderText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u53d7\u6ce8", None))
        self.selectPath.setText("")
        self.selectPath.setPlaceholderText("")
        self.selectPathButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.selectPathSaveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5148", None))
        self.file_type.setItemText(0, QCoreApplication.translate("MainWindow", u"step", None))
        self.file_type.setItemText(1, QCoreApplication.translate("MainWindow", u"stp", None))
        self.file_type.setItemText(2, QCoreApplication.translate("MainWindow", u"iges", None))
        self.file_type.setItemText(3, QCoreApplication.translate("MainWindow", u"igs", None))
        self.file_type.setItemText(4, QCoreApplication.translate("MainWindow", u"FCStd", None))

        self.clearDimentionsButton.setText(QCoreApplication.translate("MainWindow", u"\u524a\u9664", None))
        self.saveDimentionsButton.setText(QCoreApplication.translate("MainWindow", u"\u5bf8\u6cd5\u4fdd\u5b58", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u6210", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u203b\u203b\u3000\u79fb\u52d5\u578b\u306e\u90e8\u54c1\u3000\u203b\u203b\u3000", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"GP", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"RP", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.t_rpx.setText("")
        self.t_rpx.setPlaceholderText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.t_rpy.setText("")
        self.t_rpy.setPlaceholderText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.t_rpd.setText("")
        self.t_rpd.setPlaceholderText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.t_rpl.setText("")
        self.t_rpl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7701\u7565\u53ef", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u30c6\u30fc\u30d1\u30d4\u30f3", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.t_ppx.setText("")
        self.t_ppx.setPlaceholderText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.t_ppy.setText("")
        self.t_ppy.setPlaceholderText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.t_ppd.setText("")
        self.t_ppd.setPlaceholderText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.t_pph.setText("")
        self.t_pph.setPlaceholderText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"\u30c6\u30fc\u30d1\u30d6\u30ed\u30c3\u30af\uff08\u4e0a\u4e0b\uff09", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.t_pbx.setText("")
        self.t_pbx.setPlaceholderText("")
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.t_pby.setText("")
        self.t_pby.setPlaceholderText("")
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.t_pbw.setText("")
        self.t_pbw.setPlaceholderText("")
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.t_pbl.setText("")
        self.t_pbl.setPlaceholderText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.t_pbh.setText("")
        self.t_pbh.setPlaceholderText("")
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"\u30b9\u30e9\u30a4\u30c9\u30b3\u30a2\u30fb\u5de6\u53f3", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.t_sllrx.setText("")
        self.t_sllrx.setPlaceholderText("")
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.t_sllry.setText("")
        self.t_sllry.setPlaceholderText("")
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.t_sllrw.setText("")
        self.t_sllrw.setPlaceholderText("")
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.t_sllrl.setText("")
        self.t_sllrl.setPlaceholderText("")
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.t_sllrh.setText("")
        self.t_sllrh.setPlaceholderText("")
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"\u30b9\u30e9\u30a4\u30c9\u30b3\u30a2\u30fb\u4e0a\u4e0b", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.t_sludx.setText("")
        self.t_sludx.setPlaceholderText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.t_sludy.setText("")
        self.t_sludy.setPlaceholderText("")
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.t_sludw.setText("")
        self.t_sludw.setPlaceholderText("")
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.t_sludl.setText("")
        self.t_sludl.setPlaceholderText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.t_sludh.setText("")
        self.t_sludh.setPlaceholderText("")
        self.label_plate_13.setText(QCoreApplication.translate("MainWindow", u"\u203bH\u306fPL\u9762\u3088\u308a\u306e\u9ad8\u3055\u3067\u3059\u3002", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"GP", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.f_gpx.setText("")
        self.f_gpx.setPlaceholderText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.f_gpy.setText("")
        self.f_gpy.setPlaceholderText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.f_gpd.setText("")
        self.f_gpd.setPlaceholderText("")
        self.f_gph.setText("")
        self.f_gph.setPlaceholderText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.f_gpl.setText("")
        self.f_gpl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7701\u7565\u53ef", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u30d7\u30e9\u30dc\u30eb\u30c8", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.f_prx.setText("")
        self.f_prx.setPlaceholderText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Y ", None))
        self.f_pry.setText("")
        self.f_pry.setPlaceholderText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.f_prd.setText("")
        self.f_prd.setPlaceholderText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.f_prd2.setText("")
        self.f_prd2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30dc\u30eb\u30c8", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.f_prh.setText("")
        self.f_prh.setPlaceholderText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"H2", None))
        self.f_prh2.setText("")
        self.f_prh2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30dc\u30eb\u30c8", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u3000", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u30c6\u30fc\u30d1\u30d4\u30f3", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.f_ppx.setText("")
        self.f_ppx.setPlaceholderText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.f_ppy.setText("")
        self.f_ppy.setPlaceholderText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.f_ppd.setText("")
        self.f_ppd.setPlaceholderText("")
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.f_pph.setText("")
        self.f_pph.setPlaceholderText("")
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"\u30c6\u30fc\u30d1\u30d6\u30ed\u30c3\u30af\uff08\u4e0a\u4e0b\uff09", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.f_pbx.setText("")
        self.f_pbx.setPlaceholderText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.f_pby.setText("")
        self.f_pby.setPlaceholderText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.f_pbw.setText("")
        self.f_pbw.setPlaceholderText("")
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.f_pbl.setText("")
        self.f_pbl.setPlaceholderText("")
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.f_pbh.setText("")
        self.f_pbh.setPlaceholderText("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30f3\u30ae\u30e5\u30e9\u30d4\u30f3\u30fb\u5de6\u53f3", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.f_aglry.setText("")
        self.f_aglry.setPlaceholderText("")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.f_aglrh.setText("")
        self.f_aglrh.setPlaceholderText("")
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u03b1", None))
        self.f_aglra.setText("")
        self.f_aglra.setPlaceholderText("")
        self.f_aglrx.setText("")
        self.f_aglrx.setPlaceholderText("")
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.f_aglrd.setText("")
        self.f_aglrd.setPlaceholderText("")
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.f_aglrl.setText("")
        self.f_aglrl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7701\u7565\u53ef", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"\u30a2\u30f3\u30ae\u30e5\u30e9\u30d4\u30f3\u30fb\u4e0a\u4e0b", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.f_agudy.setText("")
        self.f_agudy.setPlaceholderText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.f_agudh.setText("")
        self.f_agudh.setPlaceholderText("")
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"\u03b1", None))
        self.f_aguda.setText("")
        self.f_aguda.setPlaceholderText("")
        self.f_agudx.setText("")
        self.f_agudx.setPlaceholderText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.f_agudd.setText("")
        self.f_agudd.setPlaceholderText("")
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.f_agudl.setText("")
        self.f_agudl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7701\u7565\u53ef", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u3000\u3000", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"SP", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.f_spd.setText("")
        self.f_spd.setPlaceholderText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.f_spd2.setText("")
        self.f_spd2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30ab\u30e9\u30fc", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.f_spd3.setText("")
        self.f_spd3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30dc\u30eb\u30c8", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.f_sph.setText("")
        self.f_sph.setPlaceholderText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"H2", None))
        self.f_sph2.setText("")
        self.f_sph2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30ab\u30e9\u30fc", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"H3", None))
        self.f_sph3.setText("")
        self.f_sph3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30dc\u30eb\u30c8", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.f_spx.setText("")
        self.f_spx.setPlaceholderText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.f_spy.setText("")
        self.f_spy.setPlaceholderText("")
        self.label_plate_14.setText(QCoreApplication.translate("MainWindow", u"\u203bH\u306fPL\u9762\u3088\u308a\u306e\u9ad8\u3055\u3067\u3059\u3002", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u203b\u203b\u3000\u56fa\u5b9a\u578b\u306e\u90e8\u54c1\u3000\u203b\u203b\u3000", None))
    # retranslateUi

