from sql.all_win_sql import *
from PyQt5.QtWidgets import QApplication
import sys


class UI(object):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.win_main = WinMain()
        self.win_jinhuo = WinJinhuo()
        self.win_tuihuo = WinTuihuo()
        self.win_tongji = WinTongji()
        self.win_xiaoshou = WinXiaoshou()

        btn1 = self.win_main.win_main.btn_jinhuo
        btn1.clicked.connect(self.win_jinhuo.show)

        btn2 = self.win_main.win_main.btn_tuihuo
        btn2.clicked.connect(self.win_tuihuo.show)

        btn3 = self.win_main.win_main.btn_tongji
        btn3.clicked.connect(self.win_tongji.show)

        btn4 = self.win_main.win_main.btn_xiaoshou
        btn4.clicked.connect(self.win_xiaoshou.show)

        self.win_main.show()

    def exit(self):
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    ui = UI()
    ui.exit()
