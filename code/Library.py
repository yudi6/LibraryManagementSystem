from PyMySQL import PyMySQL
from Create import *
from Operation import *
class Library(PyMySQL):
    def __init__(self, host, user, pwd):
        PyMySQL.__init__(self, host, user, pwd)
        self._init_database()
        self._init_table()
        self.insert_new_book()
        # self.purchase_book()
        self._quit()

    def _init_database(self):
        self.cursor.execute(CREATE_DATABASE)
        self.cursor.execute(USE_DATABASE)

    def _init_table(self):
        self.cursor.execute(CREAT_TABLE_BOOK)
        self.cursor.execute(CREAT_TABLE_SUPPLIER)
        self.cursor.execute(CREAT_TABLE_SUPPLIER_PRICE)
        self.cursor.execute(CREAT_TABLE_SUPPLY_LIST)
        self.cursor.execute(CREAT_TABLE_STOREHOUSE)
        self.cursor.execute(CREAT_TABLE_SALE)
        self.cursor.execute(CREAT_TABLE_REFUND)

    def insert_new_book(self):
        args = ['12','关于建设双一流高校','罗俊','中山大学出版社','18']
        self.change(INSERT_NEW_BOOK, args)
        pass

    def purchase_book(self):
        #   库存表修改
        # args = ['2','罗俊2','19']
        # self.change(, args)
        pass

    def return_book(self):
        #   销售表查询
        query = "select"
        args = []
        self.change(query, args)
        #   库存表修改
        query = "update"
        args = []
        self.change(query, args)
        #   退货表修改
        query = "insert"
        args = []
        self.change(query, args)

    def sell_book(self):
        #   库存表查询
        query = "select"
        args = []
        self.search(query, args)
        #   库存表修改
        query = "insert"
        args = []
        self.change(query, args)
        #   销售表修改
        query = "select"
        args = []

    def statistics(self):
        #   销售表查询

        #   输出结果
        pass