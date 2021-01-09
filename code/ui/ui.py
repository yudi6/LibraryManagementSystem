from ui.sql.all_win_sql import *
from PyQt5.QtWidgets import QApplication
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

        btn2 = self.win_main.win_main.btn_tuihuo
        btn2.clicked.connect(self.win_tuihuo.show)

        btn3 = self.win_main.win_main.btn_tongji
        btn3.clicked.connect(self.win_tongji.show)

        btn4 = self.win_main.win_main.btn_xiaoshou
        btn4.clicked.connect(self.win_xiaoshou.show)

        self.win_main.show()
        self.exit()

    def exit(self):
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    ui = UI()
    ui.exit()