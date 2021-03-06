# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_xiaoshou.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win_xiaoshou(object):
    def setupUi(self, win_xiaoshou):
        win_xiaoshou.setObjectName("win_xiaoshou")
        win_xiaoshou.resize(697, 524)
        self.book_table = QtWidgets.QTableWidget(win_xiaoshou)
        self.book_table.setGeometry(QtCore.QRect(30, 60, 301, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_table.sizePolicy().hasHeightForWidth())
        self.book_table.setSizePolicy(sizePolicy)
        self.book_table.setAutoScrollMargin(16)
        self.book_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.book_table.setObjectName("book_table")
        self.book_table.setColumnCount(3)
        self.book_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.book_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.book_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.book_table.setHorizontalHeaderItem(2, item)
        self.book_table.horizontalHeader().setCascadingSectionResizes(False)
        self.book_table.horizontalHeader().setDefaultSectionSize(80)
        self.book_table.horizontalHeader().setMinimumSectionSize(25)
        self.book_table.horizontalHeader().setSortIndicatorShown(False)
        self.book_table.horizontalHeader().setStretchLastSection(True)
        self.book_table.verticalHeader().setHighlightSections(True)
        self.book_table.verticalHeader().setStretchLastSection(False)
        self.hint_book_table = QtWidgets.QLabel(win_xiaoshou)
        self.hint_book_table.setGeometry(QtCore.QRect(130, 0, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_book_table.setFont(font)
        self.hint_book_table.setObjectName("hint_book_table")
        self.book_table_btn = QtWidgets.QPushButton(win_xiaoshou)
        self.book_table_btn.setGeometry(QtCore.QRect(30, 480, 301, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.book_table_btn.setFont(font)
        self.book_table_btn.setAutoDefault(False)
        self.book_table_btn.setObjectName("book_table_btn")
        self.xiaoshou_table = QtWidgets.QTableWidget(win_xiaoshou)
        self.xiaoshou_table.setGeometry(QtCore.QRect(350, 60, 321, 411))
        self.xiaoshou_table.setRowCount(0)
        self.xiaoshou_table.setColumnCount(3)
        self.xiaoshou_table.setObjectName("xiaoshou_table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.xiaoshou_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.xiaoshou_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.xiaoshou_table.setHorizontalHeaderItem(2, item)
        self.xiaoshou_table.horizontalHeader().setDefaultSectionSize(75)
        self.xiaoshou_table.horizontalHeader().setSortIndicatorShown(False)
        self.xiaoshou_table.horizontalHeader().setStretchLastSection(True)
        self.xiaoshou_table_xiaoshou_btn = QtWidgets.QPushButton(win_xiaoshou)
        self.xiaoshou_table_xiaoshou_btn.setGeometry(QtCore.QRect(350, 480, 321, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.xiaoshou_table_xiaoshou_btn.setFont(font)
        self.xiaoshou_table_xiaoshou_btn.setAutoDefault(False)
        self.xiaoshou_table_xiaoshou_btn.setObjectName("xiaoshou_table_xiaoshou_btn")
        self.hint_xiaoshou_table = QtWidgets.QLabel(win_xiaoshou)
        self.hint_xiaoshou_table.setGeometry(QtCore.QRect(480, 0, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.hint_xiaoshou_table.setFont(font)
        self.hint_xiaoshou_table.setObjectName("hint_xiaoshou_table")

        self.retranslateUi(win_xiaoshou)
        QtCore.QMetaObject.connectSlotsByName(win_xiaoshou)

    def retranslateUi(self, win_xiaoshou):
        _translate = QtCore.QCoreApplication.translate
        win_xiaoshou.setWindowTitle(_translate("win_xiaoshou", "销售"))
        item = self.book_table.horizontalHeaderItem(0)
        item.setText(_translate("win_xiaoshou", "ID"))
        item = self.book_table.horizontalHeaderItem(1)
        item.setText(_translate("win_xiaoshou", "书名"))
        item = self.book_table.horizontalHeaderItem(2)
        item.setText(_translate("win_xiaoshou", "库存"))
        self.hint_book_table.setText(_translate("win_xiaoshou", "藏书列表"))
        self.book_table_btn.setText(_translate("win_xiaoshou", "添加到销售单"))
        item = self.xiaoshou_table.horizontalHeaderItem(0)
        item.setText(_translate("win_xiaoshou", "ID"))
        item = self.xiaoshou_table.horizontalHeaderItem(1)
        item.setText(_translate("win_xiaoshou", "书名"))
        item = self.xiaoshou_table.horizontalHeaderItem(2)
        item.setText(_translate("win_xiaoshou", "数量"))
        self.xiaoshou_table_xiaoshou_btn.setText(_translate("win_xiaoshou", "确认销售"))
        self.hint_xiaoshou_table.setText(_translate("win_xiaoshou", "销售单"))
