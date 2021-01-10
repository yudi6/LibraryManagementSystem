from ui.sql.all_win_sql import *
from PyQt5.QtWidgets import QApplication
from ui.utils import *
import sys


class UI(object):
    def __init__(self, library):
        self.app = QApplication(sys.argv)
        self.win_main = WinMainSQL(library)
        self.win_jinhuo = WinJinhuoSQL(library)
        self.win_tuihuo = WinTuihuoSQL(library)
        self.win_tongji = WinTongjiSQL(library)
        self.win_xiaoshou = WinXiaoshouSQL(library)

        btn1 = self.win_main.win_main.btn_jinhuo
        btn1.clicked.connect(self.win_jinhuo.show)
        btn1.clicked.connect(self.btn1_event)

        btn2 = self.win_main.win_main.btn_tuihuo
        btn2.clicked.connect(self.win_tuihuo.show)
        btn2.clicked.connect(self.btn2_event)

        btn3 = self.win_main.win_main.btn_tongji
        btn3.clicked.connect(self.win_tongji.show)
        btn3.clicked.connect(self.btn3_event)

        btn4 = self.win_main.win_main.btn_xiaoshou
        btn4.clicked.connect(self.win_xiaoshou.show)
        btn4.clicked.connect(self.btn4_event)

        self.win_main.show()
        self.exit()

    def btn2_event(self):
        refresh_all_in_table(self.win_tuihuo.win_tuihuo.xiaoshou_table, self.win_tuihuo.get_book_table_sql())

    def btn3_event(self):
        refresh_all_in_table(self.win_tongji.win_tongji.zonglan_table, self.win_tongji.get_tongji_table_sql())

    def btn1_event(self):
        refresh_all_in_table(self.win_jinhuo.win_jinhuo.book_table, self.win_jinhuo.get_book_table_sql())

    def btn4_event(self):
        refresh_all_in_table(self.win_xiaoshou.win_xiaoshou.book_table, self.win_xiaoshou.get_book_table_sql())

    def exit(self):
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    ui = UI()
    ui.exit()