# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_tongji.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win_tongji(object):
    def setupUi(self, win_tongji):
        win_tongji.setObjectName("win_tongji")
        win_tongji.resize(696, 526)
        self.zonglan_table = QtWidgets.QTableWidget(win_tongji)
        self.zonglan_table.setGeometry(QtCore.QRect(30, 60, 301, 431))
        self.zonglan_table.setRowCount(0)
        self.zonglan_table.setColumnCount(3)
        self.zonglan_table.setObjectName("zonglan_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.zonglan_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.zonglan_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.zonglan_table.setHorizontalHeaderItem(2, item)
        self.zonglan_table.horizontalHeader().setDefaultSectionSize(75)
        self.zonglan_table.horizontalHeader().setSortIndicatorShown(False)
        self.zonglan_table.horizontalHeader().setStretchLastSection(True)
        self.paihangbang_table = QtWidgets.QTableWidget(win_tongji)
        self.paihangbang_table.setGeometry(QtCore.QRect(360, 60, 301, 431))
        self.paihangbang_table.setRowCount(0)
        self.paihangbang_table.setColumnCount(3)
        self.paihangbang_table.setObjectName("paihangbang_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.paihangbang_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.paihangbang_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.paihangbang_table.setHorizontalHeaderItem(2, item)
        self.paihangbang_table.horizontalHeader().setDefaultSectionSize(75)
        self.paihangbang_table.horizontalHeader().setSortIndicatorShown(False)
        self.paihangbang_table.horizontalHeader().setStretchLastSection(True)
        self.hint_zonglan_table = QtWidgets.QLabel(win_tongji)
        self.hint_zonglan_table.setGeometry(QtCore.QRect(110, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_zonglan_table.setFont(font)
        self.hint_zonglan_table.setObjectName("hint_zonglan_table")
        self.hint_paihangbang_table = QtWidgets.QLabel(win_tongji)
        self.hint_paihangbang_table.setGeometry(QtCore.QRect(430, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_paihangbang_table.setFont(font)
        self.hint_paihangbang_table.setObjectName("hint_paihangbang_table")

        self.retranslateUi(win_tongji)
        QtCore.QMetaObject.connectSlotsByName(win_tongji)

    def retranslateUi(self, win_tongji):
        _translate = QtCore.QCoreApplication.translate
        win_tongji.setWindowTitle(_translate("win_tongji", "统计"))
        item = self.zonglan_table.horizontalHeaderItem(0)
        item.setText(_translate("win_tongji", "时间（年-月）"))
        item = self.zonglan_table.horizontalHeaderItem(1)
        item.setText(_translate("win_tongji", "销售量（本）"))
        item = self.zonglan_table.horizontalHeaderItem(2)
        item.setText(_translate("win_tongji", "销售额（元）"))
        item = self.paihangbang_table.horizontalHeaderItem(0)
        item.setText(_translate("win_tongji", "书目ID"))
        item = self.paihangbang_table.horizontalHeaderItem(1)
        item.setText(_translate("win_tongji", "销售量（本）"))
        item = self.paihangbang_table.horizontalHeaderItem(2)
        item.setText(_translate("win_tongji", "销售额（元）"))
        self.hint_zonglan_table.setText(_translate("win_tongji", "销售情况总览"))
        self.hint_paihangbang_table.setText(_translate("win_tongji", "具体时间排行榜"))