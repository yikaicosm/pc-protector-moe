# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame_mine.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FrameMine(object):
    def setupUi(self, FrameMine):
        FrameMine.setObjectName("FrameMine")
        FrameMine.resize(800, 513)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrameMine.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(FrameMine)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lt_exist_ship = QtWidgets.QListWidget(self.centralwidget)
        self.lt_exist_ship.setGeometry(QtCore.QRect(10, 30, 261, 451))
        self.lt_exist_ship.setObjectName("lt_exist_ship")
        self.lt_not_exist_ship = QtWidgets.QListWidget(self.centralwidget)
        self.lt_not_exist_ship.setGeometry(QtCore.QRect(290, 30, 261, 451))
        self.lt_not_exist_ship.setObjectName("lt_not_exist_ship")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(560, 20, 221, 141))
        self.groupBox.setObjectName("groupBox")
        self.cb_type = QtWidgets.QComboBox(self.groupBox)
        self.cb_type.setGeometry(QtCore.QRect(60, 70, 151, 22))
        self.cb_type.setObjectName("cb_type")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 54, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 41, 21))
        self.label_5.setObjectName("label_5")
        self.ed_name = QtWidgets.QLineEdit(self.groupBox)
        self.ed_name.setGeometry(QtCore.QRect(60, 100, 151, 20))
        self.ed_name.setObjectName("ed_name")
        self.cb_count_2 = QtWidgets.QCheckBox(self.groupBox)
        self.cb_count_2.setGeometry(QtCore.QRect(90, 40, 61, 19))
        self.cb_count_2.setChecked(True)
        self.cb_count_2.setObjectName("cb_count_2")
        self.cb_count_3 = QtWidgets.QCheckBox(self.groupBox)
        self.cb_count_3.setGeometry(QtCore.QRect(30, 40, 61, 19))
        self.cb_count_3.setChecked(True)
        self.cb_count_3.setObjectName("cb_count_3")
        self.cb_count_4 = QtWidgets.QCheckBox(self.groupBox)
        self.cb_count_4.setGeometry(QtCore.QRect(90, 20, 61, 19))
        self.cb_count_4.setChecked(True)
        self.cb_count_4.setObjectName("cb_count_4")
        self.cb_count_5 = QtWidgets.QCheckBox(self.groupBox)
        self.cb_count_5.setGeometry(QtCore.QRect(150, 20, 61, 19))
        self.cb_count_5.setChecked(True)
        self.cb_count_5.setObjectName("cb_count_5")
        self.cb_count_6 = QtWidgets.QCheckBox(self.groupBox)
        self.cb_count_6.setGeometry(QtCore.QRect(30, 20, 61, 19))
        self.cb_count_6.setChecked(True)
        self.cb_count_6.setObjectName("cb_count_6")
        self.cb_count_1 = QtWidgets.QCheckBox(self.groupBox)
        self.cb_count_1.setGeometry(QtCore.QRect(150, 40, 61, 19))
        self.cb_count_1.setChecked(True)
        self.cb_count_1.setObjectName("cb_count_1")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 160, 231, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tw_detail = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_detail.setGeometry(QtCore.QRect(10, 20, 211, 291))
        self.tw_detail.setObjectName("tw_detail")
        self.tw_detail.setColumnCount(0)
        self.tw_detail.setRowCount(0)
        self.bt_detail = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_detail.setGeometry(QtCore.QRect(10, 310, 211, 23))
        self.bt_detail.setObjectName("bt_detail")
        self.tv_exist = QtWidgets.QLabel(self.centralwidget)
        self.tv_exist.setGeometry(QtCore.QRect(10, 490, 61, 16))
        self.tv_exist.setObjectName("tv_exist")
        self.tv_not_exist = QtWidgets.QLabel(self.centralwidget)
        self.tv_not_exist.setGeometry(QtCore.QRect(290, 490, 61, 16))
        self.tv_not_exist.setObjectName("tv_not_exist")
        FrameMine.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrameMine)
        QtCore.QMetaObject.connectSlotsByName(FrameMine)

    def retranslateUi(self, FrameMine):
        _translate = QtCore.QCoreApplication.translate
        FrameMine.setWindowTitle(_translate("FrameMine", "护萌宝-图鉴"))
        self.label.setText(_translate("FrameMine", "已解锁:"))
        self.label_2.setText(_translate("FrameMine", "未解锁:"))
        self.groupBox.setTitle(_translate("FrameMine", "搜索"))
        self.cb_type.setItemText(0, _translate("FrameMine", "全部"))
        self.cb_type.setItemText(1, _translate("FrameMine", "航母"))
        self.cb_type.setItemText(2, _translate("FrameMine", "轻母"))
        self.cb_type.setItemText(3, _translate("FrameMine", "装母"))
        self.cb_type.setItemText(4, _translate("FrameMine", "战列"))
        self.cb_type.setItemText(5, _translate("FrameMine", "航战"))
        self.cb_type.setItemText(6, _translate("FrameMine", "战巡"))
        self.cb_type.setItemText(7, _translate("FrameMine", "重巡"))
        self.cb_type.setItemText(8, _translate("FrameMine", "航巡"))
        self.cb_type.setItemText(9, _translate("FrameMine", "雷巡"))
        self.cb_type.setItemText(10, _translate("FrameMine", "轻巡"))
        self.cb_type.setItemText(11, _translate("FrameMine", "重炮"))
        self.cb_type.setItemText(12, _translate("FrameMine", "驱逐"))
        self.cb_type.setItemText(13, _translate("FrameMine", "潜母"))
        self.cb_type.setItemText(14, _translate("FrameMine", "潜艇"))
        self.cb_type.setItemText(15, _translate("FrameMine", "炮潜"))
        self.cb_type.setItemText(16, _translate("FrameMine", "补给"))
        self.cb_type.setItemText(17, _translate("FrameMine", "导驱"))
        self.cb_type.setItemText(18, _translate("FrameMine", "防驱"))
        self.cb_type.setItemText(19, _translate("FrameMine", "其他"))
        self.label_4.setText(_translate("FrameMine", "类型:"))
        self.label_5.setText(_translate("FrameMine", "名称:"))
        self.cb_count_2.setText(_translate("FrameMine", "两星"))
        self.cb_count_3.setText(_translate("FrameMine", "三星"))
        self.cb_count_4.setText(_translate("FrameMine", "四星"))
        self.cb_count_5.setText(_translate("FrameMine", "五星"))
        self.cb_count_6.setText(_translate("FrameMine", "六星"))
        self.cb_count_1.setText(_translate("FrameMine", "一星"))
        self.groupBox_2.setTitle(_translate("FrameMine", "信息"))
        self.bt_detail.setText(_translate("FrameMine", "查看详细/掉落信息"))
        self.tv_exist.setText(_translate("FrameMine", "共:"))
        self.tv_not_exist.setText(_translate("FrameMine", "共:"))

