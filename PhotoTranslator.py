from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import pytesseract
from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator
import os
import configparser
import sqlite3
from datetime import datetime
from PyQt5.QtWinExtras import QtWin

translator = Translator(service_urls=['translate.google.com'])
dir = os.getcwd() + r"\tess\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = dir
cfg = {
            "lang1": None,
            "lang2": None,
            "login": None,
            "password": None,
            "is_registr": None,
        }
conn = sqlite3.connect('baze.db')
cursor = conn.cursor()
his = False


class Ui_PhotoTranslator(object): # класс интерфейса
    def setupUi(self, PhotoTranslator):
        PhotoTranslator.setObjectName("PhotoTranslator")
        PhotoTranslator.resize(880, 579)
        PhotoTranslator.setMinimumSize(QtCore.QSize(880, 579))
        PhotoTranslator.setMaximumSize(QtCore.QSize(880, 579))
        PhotoTranslator.setStyleSheet("background-color: rgb(57, 57, 57);")
        PhotoTranslator.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(PhotoTranslator)
        self.centralwidget.setObjectName("centralwidget")
        self.frm_second = QtWidgets.QFrame(self.centralwidget)
        self.frm_second.setGeometry(QtCore.QRect(10, 10, 861, 61))
        self.frm_second.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                      "border-radius: 10px")
        self.frm_second.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_second.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_second.setObjectName("frm_second")
        self.lbl_name = QtWidgets.QLabel(self.frm_second)
        self.lbl_name.setGeometry(QtCore.QRect(82, 0, 701, 61))
        self.lbl_name.setStyleSheet("QWidget {\n"
                                    "    color: white;\n"
                                    "    font-family: Arial;\n"
                                    "    font-size: 14pt;\n"
                                    "    font-weight: 600;\n"
                                    "    border-radius: 10px\n"
                                    "}\n"
                                    "")
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frm_second)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(790, 10, 61, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_profile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_profile.sizePolicy().hasHeightForWidth())
        self.pb_profile.setSizePolicy(sizePolicy)
        self.pb_profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_profile.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_profile.setStyleSheet("QWidget {\n"
                                      "    color: white;\n"
                                      "    font-family: Arial;\n"
                                      "    font-size: 10pt;\n"
                                      "    font-weight: 600;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "")
        self.pb_profile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/account_circle_FILL0_wght400_GRAD0_opsz24_negate.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_profile.setIcon(icon)
        self.pb_profile.setObjectName("pb_profile")
        self.horizontalLayout.addWidget(self.pb_profile)
        self.pb_quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_quit.sizePolicy().hasHeightForWidth())
        self.pb_quit.setSizePolicy(sizePolicy)
        self.pb_quit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_quit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_quit.setStyleSheet("QWidget {\n"
                                   "    color: white;\n"
                                   "    font-family: Arial;\n"
                                   "    font-size: 10pt;\n"
                                   "    font-weight: 600;\n"
                                   "    border-radius: 10px\n"
                                   "}\n"
                                   "")
        self.pb_quit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_quit.setIcon(icon1)
        self.pb_quit.setObjectName("pb_quit")
        self.horizontalLayout.addWidget(self.pb_quit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frm_second)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_back_mm = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_back_mm.sizePolicy().hasHeightForWidth())
        self.pb_back_mm.setSizePolicy(sizePolicy)
        self.pb_back_mm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_back_mm.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_back_mm.setStyleSheet("QWidget {\n"
                                      "    color: white;\n"
                                      "    font-family: Arial;\n"
                                      "    font-size: 10pt;\n"
                                      "    font-weight: 600;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "")
        self.pb_back_mm.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/arrow_back_FILL0_wght400_GRAD0_opsz24_negate.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_back_mm.setIcon(icon2)
        self.pb_back_mm.setObjectName("pb_back_mm")
        self.horizontalLayout_2.addWidget(self.pb_back_mm)
        self.pb_history = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_history.sizePolicy().hasHeightForWidth())
        self.pb_history.setSizePolicy(sizePolicy)
        self.pb_history.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_history.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_history.setStyleSheet("QWidget {\n"
                                      "    color: white;\n"
                                      "    font-family: Arial;\n"
                                      "    font-size: 10pt;\n"
                                      "    font-weight: 600;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "")
        self.pb_history.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/history_FILL0_wght400_GRAD0_opsz24_negate.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_history.setIcon(icon3)
        self.pb_history.setObjectName("pb_history")
        self.horizontalLayout_2.addWidget(self.pb_history)
        self.frm_main_info = QtWidgets.QFrame(self.centralwidget)
        self.frm_main_info.setGeometry(QtCore.QRect(10, 80, 861, 491))
        self.frm_main_info.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 10px")
        self.frm_main_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_main_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_main_info.setObjectName("frm_main_info")
        self.pb_set_image = QtWidgets.QPushButton(self.frm_main_info)
        self.pb_set_image.setGeometry(QtCore.QRect(320, 180, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_set_image.sizePolicy().hasHeightForWidth())
        self.pb_set_image.setSizePolicy(sizePolicy)
        self.pb_set_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_set_image.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_set_image.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    background-color:  rgb(26, 110, 163);\n"
"    font-size: 13pt;\n"
"    font-weight: 600;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 110, 190);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(26, 110, 200);\n"
"}\n"
"\n"
"")
        self.pb_set_image.setObjectName("pb_set_image")
        self.cb_lang1 = QtWidgets.QComboBox(self.frm_main_info)
        self.cb_lang1.setGeometry(QtCore.QRect(20, 10, 171, 31))
        self.cb_lang1.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    background-color:  rgb(26, 110, 163);\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 110, 190);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(26, 110, 200);\n"
"}\n"
"QComboBox::drop-down {\n"
"   border: none;\n"
"}\n"
"\n"
"")
        self.cb_lang1.setObjectName("cb_lang1")
        self.cb_lang2 = QtWidgets.QComboBox(self.frm_main_info)
        self.cb_lang2.setGeometry(QtCore.QRect(670, 10, 171, 31))
        self.cb_lang2.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    background-color:  rgb(26, 110, 163);\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 110, 190);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(26, 110, 200);\n"
"}\n"
"QComboBox::drop-down {\n"
"   border: none;\n"
"}\n"
"\n"
"")
        self.cb_lang2.setObjectName("cb_lang2")
        self.image = QtWidgets.QLabel(self.frm_main_info)
        self.image.setGeometry(QtCore.QRect(0, 60, 861, 431))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("1.png"))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.pb_back = QtWidgets.QPushButton(self.frm_main_info)
        self.pb_back.setGeometry(QtCore.QRect(340, 10, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_back.sizePolicy().hasHeightForWidth())
        self.pb_back.setSizePolicy(sizePolicy)
        self.pb_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_back.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_back.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    background-color:  rgb(26, 110, 163);\n"
"    font-size: 10pt;\n"
"    font-weight: 600;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(26, 110, 190);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(26, 110, 200);\n"
"}\n"
"\n"
"")
        self.pb_back.setObjectName("pb_back")
        self.lbl_drop = QtWidgets.QLabel(self.frm_main_info)
        self.lbl_drop.setGeometry(QtCore.QRect(60, 240, 741, 171))
        self.lbl_drop.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    font-size: 14pt;\n"
"    font-weight: 600;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"")
        self.lbl_drop.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_drop.setObjectName("lbl_drop")
        self.image.raise_()
        self.pb_set_image.raise_()
        self.cb_lang1.raise_()
        self.cb_lang2.raise_()
        self.pb_back.raise_()
        self.lbl_drop.raise_()
        self.image.hide()
        self.pb_back.hide()
        self.cb_lang1.addItems(["Русский", "Английский", "Французский", "Немецкий", "Польский", "Турецкий"])
        self.cb_lang2.addItems(["Русский", "Английский", "Французский", "Немецкий", "Польский", "Турецкий"])
        self.pb_set_image.clicked.connect(self.open_image)
        self.lbl_drop.setAcceptDrops(True)
        self.lbl_drop.dragEnterEvent = self.drag
        self.lbl_drop.dropEvent = self.drop_image
        self.pb_back.clicked.connect(self.back)
        self.pb_quit.clicked.connect(self.quit)
        self.image.mousePressEvent = self.copy_text
        self.notification = QtWidgets.QMessageBox(self.centralwidget)
        self.notification.setIcon(QtWidgets.QMessageBox.Information)
        self.notification.setText("Текст скопирован")
        self.notification.setWindowTitle("Уведомление")
        PhotoTranslator.setCentralWidget(self.centralwidget)
        self.frm_reg = QtWidgets.QFrame(self.centralwidget)
        self.frm_reg.setGeometry(QtCore.QRect(10, 80, 861, 491))
        self.frm_reg.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                   "border-radius: 10px")
        self.frm_reg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_reg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_reg.setObjectName("frm_reg")
        self.pb_login = QtWidgets.QPushButton(self.frm_reg)
        self.pb_login.setGeometry(QtCore.QRect(250, 10, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_login.sizePolicy().hasHeightForWidth())
        self.pb_login.setSizePolicy(sizePolicy)
        self.pb_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_login.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_login.setStyleSheet("QWidget {\n"
                                    "    color: white;\n"
                                    "    font-family: Arial;\n"
                                    "    background-color:  rgb(26, 110, 163);\n"
                                    "    font-size: 10pt;\n"
                                    "    font-weight: 600;\n"
                                    "    border-radius: 10px\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(26, 110, 190);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color:  rgb(26, 110, 200);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.pb_login.setObjectName("pb_login")
        self.le_login = QtWidgets.QLineEdit(self.frm_reg)
        self.le_login.setGeometry(QtCore.QRect(230, 180, 411, 31))
        self.le_login.setStyleSheet("QWidget {\n"
                                    "    color: white;\n"
                                    "    font-family: Arial;\n"
                                    "    background-color:  rgb(26, 110, 163);\n"
                                    "    font-size: 10pt;\n"
                                    "    font-weight: 600;\n"
                                    "    border-radius: 10px\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(26, 110, 190);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color:  rgb(26, 110, 200);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.le_login.setAlignment(QtCore.Qt.AlignCenter)
        self.le_login.setObjectName("le_login")
        self.pb_registr = QtWidgets.QPushButton(self.frm_reg)
        self.pb_registr.setGeometry(QtCore.QRect(440, 10, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_registr.sizePolicy().hasHeightForWidth())
        self.pb_registr.setSizePolicy(sizePolicy)
        self.pb_registr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_registr.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_registr.setStyleSheet("QWidget {\n"
                                      "    color: rgb(26, 110, 163);\n"
                                      "    font-family: Arial;\n"
                                      "    background-color:  rgb(255, 255, 255);\n"
                                      "    font-size: 10pt;\n"
                                      "    font-weight: 600;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(245, 245, 245);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  rgb(235, 235, 235);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.pb_registr.setObjectName("pb_registr")
        self.lbl_login = QtWidgets.QLabel(self.frm_reg)
        self.lbl_login.setGeometry(QtCore.QRect(0, 150, 861, 21))
        self.lbl_login.setStyleSheet("QWidget {\n"
                                     "    color: white;\n"
                                     "    font-family: Arial;\n"
                                     "    font-size: 14pt;\n"
                                     "    font-weight: 600;\n"
                                     "    border-radius: 10px\n"
                                     "}\n"
                                     "")
        self.lbl_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_login.setObjectName("lbl_login")
        self.le_password = QtWidgets.QLineEdit(self.frm_reg)
        self.le_password.setGeometry(QtCore.QRect(230, 260, 411, 31))
        self.le_password.setStyleSheet("QWidget {\n"
                                       "    color: white;\n"
                                       "    font-family: Arial;\n"
                                       "    background-color:  rgb(26, 110, 163);\n"
                                       "    font-size: 10pt;\n"
                                       "    font-weight: 600;\n"
                                       "    border-radius: 10px\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(26, 110, 190);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color:  rgb(26, 110, 200);\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.le_password.setAlignment(QtCore.Qt.AlignCenter)
        self.le_password.setObjectName("le_password")
        self.lbl_password = QtWidgets.QLabel(self.frm_reg)
        self.lbl_password.setGeometry(QtCore.QRect(0, 230, 861, 21))
        self.lbl_password.setStyleSheet("QWidget {\n"
                                        "    color: white;\n"
                                        "    font-family: Arial;\n"
                                        "    font-size: 14pt;\n"
                                        "    font-weight: 600;\n"
                                        "    border-radius: 10px\n"
                                        "}\n"
                                        "")
        self.lbl_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_password.setObjectName("lbl_password")
        self.pb_entry = QtWidgets.QPushButton(self.frm_reg)
        self.pb_entry.setGeometry(QtCore.QRect(350, 430, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_entry.sizePolicy().hasHeightForWidth())
        self.pb_entry.setSizePolicy(sizePolicy)
        self.pb_entry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_entry.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_entry.setStyleSheet("QWidget {\n"
                                    "    color: white;\n"
                                    "    font-family: Arial;\n"
                                    "    background-color:  rgb(26, 110, 163);\n"
                                    "    font-size: 10pt;\n"
                                    "    font-weight: 600;\n"
                                    "    border-radius: 10px\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(26, 110, 190);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color:  rgb(26, 110, 200);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.pb_entry.setObjectName("pb_entry")
        self.frm_history = QtWidgets.QFrame(self.centralwidget)
        self.frm_history.setGeometry(QtCore.QRect(10, 80, 861, 491))
        self.frm_history.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                       "border-radius: 10px")
        self.frm_history.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_history.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_history.setObjectName("frm_history")
        self.pb_login_for_history = QtWidgets.QPushButton(self.frm_history)
        self.pb_login_for_history.setGeometry(QtCore.QRect(340, 240, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_login_for_history.sizePolicy().hasHeightForWidth())
        self.pb_login_for_history.setSizePolicy(sizePolicy)
        self.pb_login_for_history.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_login_for_history.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_login_for_history.setStyleSheet("QWidget {\n"
                                                "    color: white;\n"
                                                "    font-family: Arial;\n"
                                                "    background-color:  rgb(26, 110, 163);\n"
                                                "    font-size: 10pt;\n"
                                                "    font-weight: 600;\n"
                                                "    border-radius: 10px\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(26, 110, 190);\n"
                                                "}\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color:  rgb(26, 110, 200);\n"
                                                "}\n"
                                                "\n"
                                                "")
        self.pb_login_for_history.setObjectName("pb_login_for_history")
        self.lbl_log_for_history = QtWidgets.QLabel(self.frm_history)
        self.lbl_log_for_history.setGeometry(QtCore.QRect(0, 200, 861, 21))
        self.lbl_log_for_history.setStyleSheet("QWidget {\n"
                                               "    color: white;\n"
                                               "    font-family: Arial;\n"
                                               "    font-size: 14pt;\n"
                                               "    font-weight: 600;\n"
                                               "    border-radius: 10px\n"
                                               "}\n"
                                               "")
        self.lbl_log_for_history.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_log_for_history.setObjectName("lbl_log_for_history")
        self.frm_profile = QtWidgets.QFrame(self.centralwidget)
        self.frm_profile.setGeometry(QtCore.QRect(10, 80, 861, 491))
        self.frm_profile.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                       "border-radius: 10px")
        self.frm_profile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_profile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_profile.setObjectName("frm_profile")
        self.lbl_your_login = QtWidgets.QLabel(self.frm_profile)
        self.lbl_your_login.setGeometry(QtCore.QRect(0, 10, 861, 61))
        self.lbl_your_login.setStyleSheet("QWidget {\n"
                                          "    color: white;\n"
                                          "    font-family: Arial;\n"
                                          "    font-size: 12pt;\n"
                                          "    font-weight: 600;\n"
                                          "    border-radius: 10px\n"
                                          "}\n"
                                          "")
        self.lbl_your_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_your_login.setObjectName("lbl_your_login")
        self.pb_acount_leave = QtWidgets.QPushButton(self.frm_profile)
        self.pb_acount_leave.setGeometry(QtCore.QRect(340, 80, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_acount_leave.sizePolicy().hasHeightForWidth())
        self.pb_acount_leave.setSizePolicy(sizePolicy)
        self.pb_acount_leave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pb_acount_leave.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pb_acount_leave.setStyleSheet("QWidget {\n"
                                           "    color: white;\n"
                                           "    font-family: Arial;\n"
                                           "    background-color:  rgb(26, 110, 163);\n"
                                           "    font-size: 10pt;\n"
                                           "    font-weight: 600;\n"
                                           "    border-radius: 10px\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(26, 110, 190);\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color:  rgb(26, 110, 200);\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.pb_acount_leave.setObjectName("pb_acount_leave")
        self.frm_profile.hide()
        self.frm_reg.hide()
        self.retranslateUi(PhotoTranslator)
        self.text = None
        self.log_in = True
        self.pb_back_mm.hide()
        self.pb_profile.clicked.connect(self.profile)
        self.pb_back_mm.clicked.connect(self.back_mm)
        self.pb_login.clicked.connect(self.login)
        self.pb_registr.clicked.connect(self.registr)
        self.pb_history.clicked.connect(self.history)
        self.frm_history.hide()
        self.lbl_log_for_history.hide()
        self.pb_login_for_history.hide()
        self.pb_login_for_history.clicked.connect(self.profile)
        self.pb_entry.clicked.connect(self.entry)
        self.pb_acount_leave.clicked.connect(self.exit_profile)
        QtCore.QMetaObject.connectSlotsByName(PhotoTranslator)

        def mousePressEvent(event):
            if event.button() == Qt.LeftButton:
                if self.frm_second.underMouse(): # если frm_second под курсором в момент нажатия, обновляем координату, флаг draggable = true
                    self.draggable = True
                    self.offset = event.pos()

        def mouseMoveEvent(event):
            if self.draggable:
                PhotoTranslator.move(event.globalPos() - self.offset) # флаг draggable = true, передвигаем интерфейс на нужную координату

        def mouseReleaseEvent(event):
            if event.button() == Qt.LeftButton: # если лкм отпущена, флаг draggable = false
                self.draggable = False

        self.frm_second.mousePressEvent = mousePressEvent
        self.frm_second.mouseMoveEvent = mouseMoveEvent
        self.frm_second.mouseReleaseEvent = mouseReleaseEvent
        self.lang_index = {
            'rus': 0,
            'eng': 1,
            'fra': 2,
            'deu': 3,
            'pol': 4,
            'tur': 5
        }
        self.lang_index_inv = {
            0: 'rus',
            1: 'eng',
            2: 'fra',
            3: 'deu',
            4: 'pol',
            5: 'tur'
        }
        self.lang_ab = {
            "rus": "ru",
            "eng": "en",
            "fra": "fr",
            "deu": "de",
            "pol": "pl",
            "tur": "tr"
        }
        self.read_cfg()

    def exit_profile(self): # функция выхода из профиля
        cfg['login'] = None
        cfg['password'] = None
        cfg['is_registr'] = 'False'
        self.write_cfg('login', '')
        self.write_cfg('password', '')
        self.write_cfg('is_registr', 'False')
        self.le_password.clear()
        self.le_login.clear()
        self.back_mm()

    def entry(self): # функция входа/регистрации
        if not self.log_in:
            cursor.execute("SELECT * FROM users WHERE login = ?", (self.le_login.text(),))
            if cursor.fetchall():
                self.error("Аккаунт с таком логином уже зарегистрирован")
            else:
                if len(self.le_login.text().strip()) < 4:
                    self.error("Длина логина должна быть больше 4 символов")
                elif len(self.le_password.text().strip()) < 8:
                    self.error("Длина пароля должна быть больше 8 символов")
                else:
                    cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", (self.le_login.text(), self.le_password.text()))
                    conn.commit()
                    cfg['login'] = self.le_login.text()
                    cfg['password'] = self.le_password.text()
                    cfg['is_registr'] = 'True'
                    self.write_cfg('login', self.le_login.text())
                    self.write_cfg('password', self.le_password.text())
                    self.write_cfg('is_registr', 'True')
                    self.profile()

        else:
            cursor.execute("SELECT * FROM users WHERE login = ?", (self.le_login.text(),))
            data = cursor.fetchone()
            if data is not None:
                if self.le_password.text() == data[2]:
                    cfg['login'] = self.le_login.text()
                    cfg['password'] = self.le_password.text()
                    cfg['is_registr'] = 'True'
                    self.write_cfg('login', self.le_login.text())
                    self.write_cfg('password', self.le_password.text())
                    self.write_cfg('is_registr', 'True')
                    self.profile()
                else:
                    self.error("Неверный пароль")
            else:
                self.error(f"Аккаунт с логином '{self.le_login.text()}' не найден")

    def login(self): # функция смены оформления кнопки входа
        self.pb_login.setStyleSheet("QWidget {\n"
                                    "    color: white;\n"
                                    "    font-family: Arial;\n"
                                    "    background-color:  rgb(26, 110, 163);\n"
                                    "    font-size: 10pt;\n"
                                    "    font-weight: 600;\n"
                                    "    border-radius: 10px\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(26, 110, 190);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color:  rgb(26, 110, 200);\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.pb_registr.setStyleSheet("QWidget {\n"
                                      "    color: rgb(26, 110, 163);\n"
                                      "    font-family: Arial;\n"
                                      "    background-color:  rgb(255, 255, 255);\n"
                                      "    font-size: 10pt;\n"
                                      "    font-weight: 600;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(245, 245, 245);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  rgb(235, 235, 235);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.pb_entry.setText("Войти")
        self.log_in = True

    def registr(self): # функция смены оформления кнопки регистрации
        self.pb_login.setStyleSheet("QWidget {\n"
                                      "    color: rgb(26, 110, 163);\n"
                                      "    font-family: Arial;\n"
                                      "    background-color:  rgb(255, 255, 255);\n"
                                      "    font-size: 10pt;\n"
                                      "    font-weight: 600;\n"
                                      "    border-radius: 10px\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(245, 245, 245);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  rgb(235, 235, 235);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.pb_registr.setStyleSheet("QWidget {\n"
                                    "    color: white;\n"
                                    "    font-family: Arial;\n"
                                    "    background-color:  rgb(26, 110, 163);\n"
                                    "    font-size: 10pt;\n"
                                    "    font-weight: 600;\n"
                                    "    border-radius: 10px\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(26, 110, 190);\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color:  rgb(26, 110, 200);\n"
                                    "}\n"
                                    "\n"
                                    "")

        self.pb_entry.setText("Зарегистрироваться")
        self.log_in = False

    def profile(self): # функция показа профиля
        self.frm_history.hide()
        self.frm_main_info.hide()
        self.pb_back_mm.show()
        if cfg['is_registr'] == 'True':
            self.frm_profile.show()
            self.lbl_your_login.setText(f"Ваш логин - {cfg['login']}")
        else:
            self.frm_reg.show()

    def back_mm(self): # функция возвращения в меню
        self.frm_reg.hide()
        self.frm_history.hide()
        self.frm_main_info.show()
        self.pb_back_mm.hide()
        self.frm_profile.hide()

    def back(self): # функция возвращения в меню из виджета перевода
        self.lbl_drop.show()
        self.pb_back.hide()
        self.pb_set_image.show()
        self.image.hide()
        self.cb_lang1.show()
        self.cb_lang2.show()
        self.frm_history.hide()

    def history(self): # функция показа истории
        global his
        self.frm_history.show()
        self.frm_reg.hide()
        self.frm_profile.hide()
        self.pb_back_mm.show()
        print(cfg["is_registr"])
        if cfg["is_registr"] == 'False':
            self.lbl_log_for_history.show()
            self.pb_login_for_history.show()
            if his:
                self.scroll_area.hide()
                self.lbl_log_for_history.show()
                self.pb_login_for_history.show()
        else:
            his = True
            self.lbl_log_for_history.hide()
            self.pb_login_for_history.hide()
            cursor.execute("SELECT id FROM users WHERE login = ?", (cfg["login"],))
            user_id = cursor.fetchone()[0]
            cursor.execute("SELECT id, text, photo, date FROM history WHERE user_id = ?", (user_id,))
            self.scroll_area = QtWidgets.QScrollArea(self.frm_history)
            self.scroll_area.setGeometry(QtCore.QRect(10, 0, 841, 491))
            self.scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.scroll_area.setStyleSheet('''
                QScrollBar:vertical {
                    width: 8px;
                    background: transparent;
                    margin: 0 0 0 0;
                }
                QScrollBar::handle:vertical {
                    background: rgba(0, 0, 0, 0.25);
                    border-radius: 4px;
                    min-height: 20px;
                }
                QScrollBar::sub-page:vertical,
                QScrollBar::add-page:vertical {
                    background: none;
                }
                QScrollBar:horizontal {
                    height: 8px;
                    background: transparent;
                    margin: 0 0 0 0;
                }
                QScrollBar::handle:horizontal {
                    background: rgba(0, 0, 0, 0.25);
                    border-radius: 4px;
                    min-width: 20px;
                }
                QScrollBar::sub-page:horizontal,
                QScrollBar::add-page:horizontal {
                    background: none;
                }
            ''')

            self.scroll_area.verticalScrollBar().setStyleSheet('''
                QScrollBar::add-line:vertical,
                QScrollBar::sub-line:vertical {
                    height: 0px;
                    background: transparent;
                }
                QScrollBar::add-page:vertical,
                QScrollBar::sub-page:vertical {
                    background: none;
                }
            ''')

            self.scroll_area.horizontalScrollBar().setStyleSheet('''
                QScrollBar::add-line:horizontal,
                QScrollBar::sub-line:horizontal {
                    width: 0px;
                    background: transparent;
                }
                QScrollBar::add-page:horizontal,
                QScrollBar::sub-page:horizontal {
                    background: none;
                }
            ''')
            content_widget = QtWidgets.QWidget()
            content_widget.setStyleSheet("background: transparent;")
            content_layout = QtWidgets.QVBoxLayout(content_widget)

            def delete_widget(id_im): # функция удаления изображения из бд
                cursor.execute("DELETE FROM history WHERE id = ?", (id_im,))
                conn.commit()
                self.history()

            def copy_text(text): # функция копирования текста в буфер обмена
                clipboard = QtWidgets.QApplication.clipboard()
                clipboard.setText(text)
                self.notification.show()

            def open_image(photo, date): # функция открытия изображения в отдельном диалоге
                dialog = QtWidgets.QDialog()
                dialog.setWindowTitle(date)
                dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.WindowMaximized)
                image_label = QtWidgets.QLabel(dialog)
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(photo)
                image_label.setPixmap(pixmap)
                image_label.setAlignment(QtCore.Qt.AlignCenter)
                image_label.setScaledContents(True)
                layout = QtWidgets.QVBoxLayout(dialog)
                layout.addWidget(image_label)
                dialog.exec_()

            for i in cursor.fetchall(): # цикл отображения всех элементов истории из бд
                id_im, text, photo, date = i

                frame = QtWidgets.QFrame()
                frame.setStyleSheet("background-color: rgb(65, 65, 65);\n"
                                    "border-radius: 10px")
                frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame.setFrameShadow(QtWidgets.QFrame.Raised)
                frame.setObjectName(f"frame_{id_im}")
                frame.setFixedSize(811, 241)
                frame_layout = QtWidgets.QHBoxLayout(frame)
                frame_layout.setContentsMargins(10, 10, 10, 10)

                image_label = QtWidgets.QLabel()
                image = QtGui.QPixmap()
                image.loadFromData(photo)
                image = image.scaledToWidth(309)
                image_label.setPixmap(image)
                frame_layout.addWidget(image_label)

                date_label = QtWidgets.QLabel(date)
                date_label.setStyleSheet("color: white;\n"
                                         "font-family: Arial;\n"
                                         "font-size: 10pt;\n"
                                         "font-weight: 600;\n"
                                         "border-radius: 10px;")
                date_label.setAlignment(QtCore.Qt.AlignCenter)
                date_label.setFixedSize(40, 24)

                text_layout = QtWidgets.QVBoxLayout()
                text_edit = QtWidgets.QTextEdit()
                text_edit.setPlainText(text)
                text_edit.setStyleSheet("color: white;\n"
                             "font-family: Arial;\n"
                             "font-size: 10pt;\n"
                             "font-weight: 600;\n"
                             "border-radius: 10px;")

                text_edit.verticalScrollBar().setStyleSheet('''
                                QScrollBar::add-line:vertical,
                                QScrollBar::sub-line:vertical {
                                    height: 0px;
                                    background: transparent;
                                }
                                QScrollBar::add-page:vertical,
                                QScrollBar::sub-page:vertical {
                                    background: none;
                                }
                            ''')

                text_edit.horizontalScrollBar().setStyleSheet('''
                                QScrollBar::add-line:horizontal,
                                QScrollBar::sub-line:horizontal {
                                    width: 0px;
                                    background: transparent;
                                }
                                QScrollBar::add-page:horizontal,
                                QScrollBar::sub-page:horizontal {
                                    background: none;
                                }
                            ''')
                text_edit.setReadOnly(True)
                text_layout.addWidget(text_edit)

                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("ui/content_copy_FILL0_wght400_GRAD0_opsz24_negate.png"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("ui/fullscreen_FILL0_wght400_GRAD0_opsz24_negate.png"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("ui/delete_FILL0_wght400_GRAD0_opsz24_negate.png"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                button_layout = QtWidgets.QVBoxLayout()
                delete_button = QtWidgets.QPushButton("")
                button_layout.addWidget(delete_button)
                delete_button.setIcon(icon6)
                copy_button = QtWidgets.QPushButton("")
                button_layout.addWidget(copy_button)
                copy_button.setIcon(icon4)
                open_button = QtWidgets.QPushButton("")
                button_layout.addWidget(open_button)
                open_button.setIcon(icon5)
                delete_button.clicked.connect(lambda _, id_im=id_im: delete_widget(id_im))
                copy_button.clicked.connect(lambda _, text=text: copy_text(text))
                open_button.clicked.connect(lambda _, photo=photo: open_image(photo, date))
                delete_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                copy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                open_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

                frame_layout.addLayout(text_layout)
                frame_layout.addLayout(button_layout)
                content_layout.addWidget(frame)

            self.scroll_area.setWidget(content_widget)
            self.scroll_area.show()
            self.frm_history.adjustSize()

    def open_image(self): # функция открытия изображения с помощью диалога
        file_name = QFileDialog.getOpenFileName(caption="Выберите фото", filter="*.png *.jpg *.jpeg")
        if file_name:
            self.display_image(file_name[0])

    def read_cfg(self): # функция чтения конфига
        config = configparser.ConfigParser()
        config.read("config.txt")
        cfg["lang1"] = config["Config"]["lang1"]
        cfg["lang2"] = config["Config"]["lang2"]
        cfg["login"] = config["Config"]["login"]
        cfg["password"] = config["Config"]["password"]
        cfg["is_registr"] = config["Config"]["is_registr"]

        self.cb_lang1.setCurrentIndex(self.lang_index[cfg["lang1"]])

        self.cb_lang2.setCurrentIndex(self.lang_index[cfg["lang2"]])

    def write_cfg(self, name, value): # функция записи в конфиг
        config = configparser.ConfigParser()
        config.read("config.txt")
        config.set("Config", name, value)
        with open("config.txt", 'w') as f:
            config.write(f)

    def display_image(self, file_name): # функция распознования, перевода и отображения изображения
        self.write_cfg("lang1", self.lang_index_inv[self.cb_lang1.currentIndex()])
        self.write_cfg("lang2", self.lang_index_inv[self.cb_lang2.currentIndex()])
        if file_name:
            translator = Translator(service_urls=['translate.google.com'])
            image = Image.open(file_name).convert('RGB')
            text_data = pytesseract.image_to_string(image.convert('L'), lang=self.lang_index_inv[self.cb_lang1.currentIndex()])
            if text_data == "":
                self.error("Текст на изображении не распознан")
                return 0
            print(text_data)
            count_str = text_data.count('\n')
            cleantext = text_data.replace('\n', ' ')
            print(cleantext)
            try:
                translate_text = translator.translate(cleantext, src=self.lang_ab[self.lang_index_inv[self.cb_lang1.currentIndex()]], dest=self.lang_ab[self.lang_index_inv[self.cb_lang2.currentIndex()]]).text
            except Exception as ex:
                print(ex)
            print(translate_text)
            self.text = translate_text
            words = translate_text.split()
            print(words)
            trans_text = []
            trans_text_lines = []
            i = 0

            for _ in range(count_str):
                if i < len(words) % count_str:
                    trans_text.append(words[i * len(words) // count_str:(i + 1) * len(words) // count_str + 1])
                else:
                    trans_text.append(words[i * len(words) // count_str:(i + 1) * len(words) // count_str])
                i += 1

            print(trans_text)

            for i in trans_text:
                trans_text_lines.append(' '.join(i))

            print(trans_text_lines)

            dark_image = image.copy()
            w, h = dark_image.size
            pixels = dark_image.load()

            for i in range(w):
                for j in range(h):
                    r, g, b = pixels[i, j]
                    dr = int(r * (1 - 0.87))
                    dg = int(g * (1 - 0.87))
                    db = int(b * (1 - 0.87))
                    pixels[i, j] = (dr, dg, db)

            font_s = 14
            draw = ImageDraw.Draw(dark_image)
            for i, eng_line in enumerate(text_data.split("\n")):
                if i < len(trans_text_lines):
                    rus_line = trans_text_lines[i]
                else:
                    break

                font_w = (font_s * len(rus_line)) * 0.7
                print(w, font_w)
                while font_w > w + 100:
                    font_s -= 1
                    print(font_s)
                    font_w = font_s * len(rus_line) * 0.7
                font = ImageFont.truetype("arial.ttf", font_s)
                draw.text((10, 5 + int(h / count_str) * i), rus_line, font=font, fill=(255, 255, 255))
                font_s = 14

            dark_image.save("trans_image.png")
            pmap = QPixmap("trans_image.png")
            scpxmap = pmap.scaled(self.image.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.image.setPixmap(scpxmap)
            self.image.show()
            if cfg["is_registr"] == 'True':
                cursor.execute("SELECT id FROM users WHERE login = ?", (cfg["login"],))
                user_id = cursor.fetchone()[0]
                with open("trans_image.png", "rb") as f:
                    image = f.read()
                cursor.execute(f"INSERT INTO history (user_id, text, photo, date) VALUES (?, ?, ?, ?)", (user_id, self.text, image, str(datetime.now().strftime("%d.%m.%Y %H:%M"))))
                conn.commit()

            self.pb_back.show()
            self.pb_set_image.hide()
            self.lbl_drop.hide()
            self.cb_lang1.hide()
            self.cb_lang2.hide()

    def drag(self, ev): # функция, проверяющая содержит ли переданный объект данные MIME в формате URL
        if ev.mimeData().hasUrls:
            ev.acceptProposedAction()

    def drop_image(self, ev): # функция, проверяющая, нужного ли формата дропнутое изображения
        files = ev.mimeData().urls()
        file_name = str(files).split("'")[1][8:]
        if file_name[-4:] == ".png" or file_name[-4:] == ".jpg" or file_name[-5:] == ".jpeg":
            self.display_image(file_name)
        else:
            self.error("Выбран файл неверного формата. Поддерживаемые форматы: PNG, JPG, JPEG")

    def quit(self): # функция выхода из программы
        reply = QMessageBox.question(self.centralwidget, "Подтверждение выхода", "Вы точно хотите выйти?", QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.write_cfg("lang1", self.lang_index_inv[self.cb_lang1.currentIndex()])
            self.write_cfg("lang2", self.lang_index_inv[self.cb_lang2.currentIndex()])
            cursor.close()
            conn.close()
            QtWidgets.qApp.quit()

    def error(self, message): # функция отображения MessageBox с ошибкой
        error = QMessageBox()
        error.setIcon(QMessageBox.Warning)
        error.setText(message)
        error.setWindowTitle("Ошибка")
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

    def copy_text(self, event): # функция копирования текста в буфер обмена
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.text)
        self.notification.show()

    def retranslateUi(self, PhotoTranslator): # функция, устанавливающая текст на обьекты
        _translate = QtCore.QCoreApplication.translate
        PhotoTranslator.setWindowTitle(_translate("PhotoTranslator", "MainWindow"))
        self.lbl_name.setText(_translate("PhotoTranslator", "Переводчик по фото"))
        self.pb_set_image.setText(_translate("PhotoTranslator", "Выбрать фото"))
        self.pb_back.setText(_translate("PhotoTranslator", "Вернуться обратно"))
        self.lbl_drop.setText(_translate("PhotoTranslator", "Или переместите в эту область"))
        self.pb_login.setText(_translate("PhotoTranslator", "Вход"))
        self.pb_registr.setText(_translate("PhotoTranslator", "Регистрация"))
        self.lbl_login.setText(_translate("PhotoTranslator", "Логин"))
        self.lbl_password.setText(_translate("PhotoTranslator", "Пароль"))
        self.pb_entry.setText(_translate("PhotoTranslator", "Войти"))
        self.pb_login_for_history.setText(_translate("PhotoTranslator", "Войти в аккаунт"))
        self.lbl_log_for_history.setText(_translate("PhotoTranslator", "Для пользования историей вам необходимо войти в аккаунт"))
        self.lbl_your_login.setText(_translate("PhotoTranslator", f"Ваш логин - {cfg['login']}"))
        self.pb_acount_leave.setText(_translate("PhotoTranslator", "Выйти из аккаунта"))


if __name__ == "__main__":
    import sys
    QtWin.setCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
    app = QtWidgets.QApplication(sys.argv)
    PhotoTranslator = QtWidgets.QMainWindow()
    ui = Ui_PhotoTranslator()

    PhotoTranslator.setWindowTitle("Переводчик по фото")
    ui.setupUi(PhotoTranslator)
    PhotoTranslator.show()
    sys.exit(app.exec_())