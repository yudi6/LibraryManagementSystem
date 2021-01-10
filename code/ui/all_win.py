import sys
from ui.win_ui.win_main import Ui_MainWindow
from ui.win_ui.win_jinhuo import Ui_win_jinhuo
from ui.win_ui.win_tuihuo import Ui_win_tuihuo
from ui.win_ui.win_tongji import Ui_win_tongji
from ui.win_ui.win_xiaoshou import Ui_win_xiaoshou
from ui.utils import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QAbstractItemView
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class WinMain(QMainWindow):
    def __init__(self, library):
        self.library = library
        QMainWindow.__init__(self)
        self.win_main = Ui_MainWindow()
        self.win_main.setupUi(self)

        # 插入背景图片
        palette = QPalette()
        palette.setBrush(QPalette.Background,
                         QBrush(QPixmap('./ui/img/main_win_header.jpg')))
        self.setPalette(palette)
        self.setFixedSize(791, 711)


class WinJinhuo(QDialog):
    def __init__(self, library):
        self.library = library
        QDialog.__init__(self)
        self.win_jinhuo = Ui_win_jinhuo()
        self.win_jinhuo.setupUi(self)
        self.win_jinhuo.book_name_btn.clicked.connect(self.book_name_btn_event)
        self.win_jinhuo.jin_huo_btn.clicked.connect(self.jin_huo_btn_event)
        self.init_jin_huo_table()
        self.init_book_table()
        self.hahaha = []
        self.book_table = None
        self.jinhuo_table = None
        self.jionhuo_table_2 = None

    def init_jin_huo_table(self):
        self.win_jinhuo.jin_huo_table.setSelectionBehavior(1)
        make_middle(self.win_jinhuo.jin_huo_table)
        self.win_jinhuo.jin_huo_table.horizontalHeader().resizeSection(0, 70)
        self.win_jinhuo.jin_huo_table.horizontalHeader().resizeSection(1, 70)
        self.win_jinhuo.jin_huo_table.horizontalHeader().resizeSection(2, 80)
        self.win_jinhuo.jin_huo_table.horizontalHeader().resizeSection(3, 70)

    def init_book_table(self):
        self.win_jinhuo.book_table.setSelectionBehavior(1)
        make_middle(self.win_jinhuo.book_table, [1])
        self.win_jinhuo.book_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.win_jinhuo.book_table.horizontalHeader().resizeSection(0, 70)
        self.win_jinhuo.book_table.horizontalHeader().resizeSection(1, 160)
        self.win_jinhuo.book_table.horizontalHeader().resizeSection(2, 20)
        refresh_all_in_table(self.win_jinhuo.book_table, self.get_book_table_sql())

    def book_name_btn_event(self):
        data = self.get_book_name_sql(self.win_jinhuo.input_win_name.toPlainText())
        if data is None or data == '':
            return
        refresh_all_in_table(self.win_jinhuo.jin_huo_table, data)
        make_items_free(self.win_jinhuo.jin_huo_table, 2)

    def jin_huo_btn_event(self):
        selected_items = get_selected_items_in_table(self.win_jinhuo.jin_huo_table, 4)
        for _i in range(len(selected_items)):
            self.hahaha.append(selected_items[_i])
        if selected_items == [] or selected_items is None:
            return
        tmp3 = list(selected_items)
        new_list = [i[:1]+i[2:] for i in tmp3]
        self.get_jinhuo_table_sql(new_list)
        tmp2 = self.get_book_table_sql()
        refresh_all_in_table(self.win_jinhuo.book_table, tmp2)
        self.book_table = tmp2
        make_middle(self.win_jinhuo.book_table, [1])
        refresh_all_in_table(self.win_jinhuo.jin_huo_table_2, tuple(self.hahaha))

    def get_book_name_sql(self, name: str) -> tuple:
        pass

    def get_jinhuo_table_sql(self, table) -> tuple:
        pass

    def get_book_table_sql(self) -> tuple:
        pass


class WinTuihuo(QDialog):
    def __init__(self, library):
        self.library = library
        QDialog.__init__(self)
        self.win_tuihuo = Ui_win_tuihuo()
        self.win_tuihuo.setupUi(self)
        self.init_xiaoshou_table()
        self.init_tuihuo_table()
        self.win_tuihuo.xiaoshou_table.clicked.connect(self.xiaoshou_table_event)
        self.win_tuihuo.tuihuo_table_tuihuo_btn.clicked.connect(self.tuihuo_table_tuihuo_btn_event)

    def init_xiaoshou_table(self):
        self.win_tuihuo.xiaoshou_table.setSelectionBehavior(1)
        make_middle(self.win_tuihuo.xiaoshou_table, [1])
        self.win_tuihuo.xiaoshou_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        refresh_all_in_table(self.win_tuihuo.xiaoshou_table, self.get_book_table_sql())

    def init_tuihuo_table(self):
        self.win_tuihuo.tuihuo_table.setSelectionBehavior(1)
        make_middle(self.win_tuihuo.tuihuo_table, [1])
        self.win_tuihuo.tuihuo_table.horizontalHeader().resizeSection(0, 120)
        self.win_tuihuo.tuihuo_table.horizontalHeader().resizeSection(1, 120)
        self.win_tuihuo.tuihuo_table.horizontalHeader().resizeSection(2, 120)

    def xiaoshou_table_event(self):
        selected_item = get_selected_items_in_table(self.win_tuihuo.xiaoshou_table, 1)
        tmp = self.get_tuihuo_table_after_select_xiaoshou_table_sql(selected_item)
        refresh_all_in_table(self.win_tuihuo.tuihuo_table, tmp)
        make_middle(self.win_tuihuo.tuihuo_table)
        # self.deal_with_tuihuo_items_sql(selected_item)

    def tuihuo_table_tuihuo_btn_event(self):
        items_lst = get_selected_items_in_table(self.win_tuihuo.xiaoshou_table, 1)
        if items_lst == [] or items_lst is None:
            return
        self.deal_with_tuihuo_items_sql(items_lst)
        refresh_all_in_table(self.win_tuihuo.xiaoshou_table, self.get_book_table_sql())

    def deal_with_tuihuo_items_sql(self, lst):
        pass

    def get_tuihuo_table_after_select_xiaoshou_table_sql(self, lst) -> tuple:
        pass

    def get_book_table_sql(self) -> tuple:
        pass

class WinTongji(QDialog):
    def __init__(self, library):
        self.library = library
        QDialog.__init__(self)
        self.win_tongji = Ui_win_tongji()
        self.win_tongji.setupUi(self)
        self.init_zonglan_table()
        self.init_paihangbang_table()
        self.win_tongji.zonglan_table.clicked.connect(self.show_paihangbang)

    def init_zonglan_table(self):
        self.win_tongji.zonglan_table.setSelectionBehavior(1)
        make_middle(self.win_tongji.zonglan_table)
        self.win_tongji.zonglan_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.win_tongji.zonglan_table.horizontalHeader().resizeSection(0, 100)
        self.win_tongji.zonglan_table.horizontalHeader().resizeSection(1, 100)
        self.win_tongji.zonglan_table.horizontalHeader().resizeSection(2, 50)
        refresh_all_in_table(self.win_tongji.zonglan_table, self.get_tongji_table_sql())

    def init_paihangbang_table(self):
        self.win_tongji.paihangbang_table.setSelectionBehavior(1)
        make_middle(self.win_tongji.paihangbang_table)
        self.win_tongji.paihangbang_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.win_tongji.paihangbang_table.horizontalHeader().resizeSection(0, 100)
        self.win_tongji.paihangbang_table.horizontalHeader().resizeSection(1, 100)
        self.win_tongji.paihangbang_table.horizontalHeader().resizeSection(2, 50)

    def show_paihangbang(self):
        selected_item = get_selected_items_in_table(self.win_tongji.zonglan_table, 3)
        tmp = self.get_paihangbang_by_ym(selected_item[0][0])
        refresh_all_in_table(self.win_tongji.paihangbang_table, tmp)
        make_middle(self.win_tongji.paihangbang_table)

    def get_tongji_table_sql(self) -> tuple:
        pass

    def get_paihangbang_by_ym(self, ym: str) -> tuple:
        pass


class WinXiaoshou(QDialog):
    def __init__(self, library):
        self.library = library
        QDialog.__init__(self)
        self.win_xiaoshou = Ui_win_xiaoshou()
        self.win_xiaoshou.setupUi(self)
        self.init_book_table()
        self.init_xiaoshou_table()
        self.win_xiaoshou.book_table_btn.clicked.connect(self.book_table_btn_event)
        self.win_xiaoshou.xiaoshou_table_xiaoshou_btn.clicked.connect(self.xiaoshou_table_xiaoshou_btn_event)

    def init_book_table(self):
        self.win_xiaoshou.book_table.setSelectionBehavior(1)
        make_middle(self.win_xiaoshou.book_table, [1])
        self.win_xiaoshou.book_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.win_xiaoshou.book_table.horizontalHeader().resizeSection(0, 70)
        self.win_xiaoshou.book_table.horizontalHeader().resizeSection(1, 130)
        self.win_xiaoshou.book_table.horizontalHeader().resizeSection(2, 40)
        refresh_all_in_table(self.win_xiaoshou.book_table, self.get_book_table_sql())

    def init_xiaoshou_table(self):
        self.win_xiaoshou.xiaoshou_table.setSelectionBehavior(1)
        make_middle(self.win_xiaoshou.xiaoshou_table, [1])
        self.win_xiaoshou.xiaoshou_table.horizontalHeader().resizeSection(0, 70)
        self.win_xiaoshou.xiaoshou_table.horizontalHeader().resizeSection(1, 170)
        self.win_xiaoshou.xiaoshou_table.horizontalHeader().resizeSection(2, 20)

    def book_table_btn_event(self):
        selected_items = get_selected_items_in_table(self.win_xiaoshou.book_table, 3)
        item_num = len(selected_items)
        if item_num == 0:
            return
        all_lst = []

        for _i in range(item_num):
            item_lst = []
            for _j in range(2):
                item_lst.append(selected_items[_i][_j])
            item_lst.append('')
            all_lst.append(tuple(item_lst))

        add_item_to_table(self.win_xiaoshou.xiaoshou_table, tuple(all_lst))
        make_middle(self.win_xiaoshou.xiaoshou_table, [1])

    def xiaoshou_table_addrow_btn_event(self):
        add_item_to_table(self.win_xiaoshou.xiaoshou_table, (('', '', '', ),))

    def xiaoshou_table_removerow_btn_event(self):
        remove_items_from_table(self.win_xiaoshou.xiaoshou_table)

    def xiaoshou_table_xiaoshou_btn_event(self):
        items_lst = get_all_items_in_table(self.win_xiaoshou.xiaoshou_table)
        if items_lst is None or items_lst == []:
            return
        tmp = self.remove_items_from_book_table_sql(items_lst)
        refresh_all_in_table(self.win_xiaoshou.book_table, tmp)
        # make_middle(self.win_tuihuo.book_table, [1])

    def remove_items_from_book_table_sql(self, lst) -> tuple:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = WinMain()
    win_jinhuo = WinJinhuo()
    win_tuihuo = WinTuihuo()
    win_tongji = WinTongji()
    win_xiaoshou = WinXiaoshou()

    btn1 = win_main.win_main.btn_jinhuo
    btn1.clicked.connect(win_jinhuo.show)

    btn2 = win_main.win_main.btn_tuihuo
    btn2.clicked.connect(win_tuihuo.show)

    btn3 = win_main.win_main.btn_tongji
    btn3.clicked.connect(win_tongji.show)

    btn4 = win_main.win_main.btn_xiaoshou
    btn4.clicked.connect(win_xiaoshou.show)

    win_main.show()
    sys.exit(app.exec_())
