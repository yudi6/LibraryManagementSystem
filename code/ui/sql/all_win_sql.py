from ui.all_win import WinMain, WinJinhuo, WinTuihuo, WinTongji, WinXiaoshou
from ui.utils import tuple_to_str_list
import time

class WinMainSQL(WinMain):
    def __init__(self, library):
        WinMain.__init__(self, library)


class WinJinhuoSQL(WinJinhuo):
    def __init__(self, library):
        self.library = library
        WinJinhuo.__init__(self, library)


    def get_book_name_sql(self, name: str) -> tuple:
        return tuple_to_str_list(self.library.get_inf_by_name(name))

    def get_jinhuo_table_sql(self, table):
        for line in table:
            self.library.call_supply(line)

    def get_book_table_sql(self) -> tuple:
        return  tuple_to_str_list(self.library.get_store())


class WinTuihuoSQL(WinTuihuo):
    def __init__(self, library):
        self.library = library
        WinTuihuo.__init__(self, library)

    def add_tuihuo_books_to_book_table_sql(self, lst) -> tuple:
        pass

    def get_book_table_sql(self) -> tuple:
        return tuple_to_str_list(self.library.show_saleid())


    def get_tuihuo_table_after_select_xiaoshou_table_sql(self, lst) -> tuple:
        sale_id = lst[0][0]
        return tuple_to_str_list(self.library.show_inf_by_sale_id(sale_id))

    def deal_with_tuihuo_items_sql(self, lst):
        pass

class WinTongjiSQL(WinTongji):
    def __init__(self, library):
        self.library = library
        WinTongji.__init__(self, library)

    def get_tongji_table_sql(self) -> tuple:
        pass

    def get_paihangbang_by_ym(self, ym: str) -> tuple:
        pass


class WinXiaoshouSQL(WinXiaoshou):
    def __init__(self, library):
        self.library = library
        WinXiaoshou.__init__(self, library)


    def remove_items_from_book_table_sql(self, lst) -> tuple:
        time_now = str(int(time.time()))
        for line in lst:
            tuple_in = (time_now,line[0],line[2],time_now)
            self.library.call_sale_book(tuple_in)
        return tuple_to_str_list(self.library.get_store())


    def get_book_table_sql(self) -> tuple:
        return  tuple_to_str_list(self.library.get_store())
