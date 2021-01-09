from ui.all_win import WinMain, WinJinhuo, WinTuihuo, WinTongji, WinXiaoshou


class WinMainSQL(WinMain):
    def __init__(self, library):
        WinMain.__init__(self)


class WinJinhuoSQL(WinJinhuo):
    def __init__(self, library):
        WinJinhuo.__init__(self)
        self.library = library

    def get_book_name_sql(self, name: str) -> tuple:

        pass

    def get_jinhuo_table_sql(self, table) -> tuple:
        pass

    def get_book_table_sql(self) -> tuple:
        pass


class WinTuihuoSQL(WinTuihuo):
    def __init__(self, library):
        WinTuihuo.__init__(self)
        self.library = library

    def add_tuihuo_books_to_book_table_sql(self, lst) -> tuple:
        pass


class WinTongjiSQL(WinTongji):
    def __init__(self, library):
        WinTongji.__init__(self)
        self.library = library

    def get_tongji_table_sql(self) -> tuple:
        pass

    def get_paihangbang_by_ym(self, ym: str) -> tuple:
        pass


class WinXiaoshouSQL(WinXiaoshou):
    def __init__(self, library):
        WinXiaoshou.__init__(self)
        self.library = library

    def remove_items_from_book_table_sql(self, lst) -> tuple:
        pass
