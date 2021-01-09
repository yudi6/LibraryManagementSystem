from PyMySQL import PyMySQL
from Create import *
from Operation import *

class Library(PyMySQL):
    def __init__(self, host, user, pwd):
        PyMySQL.__init__(self, host, user, pwd)
        self._init_database()
        self._init_table()
        self._init_trigger()
        self._init_procedure()

    def _init_database(self):
        self.cursor.execute(CREATE_DATABASE)
        self.cursor.execute(USE_DATABASE)

    def _init_table(self):
        self.cursor.execute(CREAT_TABLE_BOOK)
        self.cursor.execute(CREAT_TABLE_SUPPLIER)
        self.cursor.execute(CREAT_TABLE_SUPPLIER_PRICE)
        self.cursor.execute(CREAT_TABLE_STOREHOUSE)
        self.cursor.execute(CREAT_TABLE_SALE)
        self.cursor.execute(CREAT_TABLE_REFUND)

    def _init_trigger(self):
        self.cursor.execute(DROP_TRIGGER_TR_AFTER_IN_REFUND)
        self.cursor.execute(CREATE_TRIGGER_TR_AFTER_IN_REFUND)
        self.cursor.execute(DROP_TRIGGER_TR_AFTER_IN_SALE)
        self.cursor.execute(CREATE_TRIGGER_TR_AFTER_IN_SALE)

    def _init_procedure(self):
        self.cursor.execute(DROP_PROCEDURE_SUPPLY)
        self.cursor.execute(CREATE_PROCEDURE_SUPPLY)
        self.cursor.execute(DROP_PROCEDURE_REFUNDBOOK)
        self.cursor.execute(CREATE_PROCEDURE_REFUNDBOOK)
        self.cursor.execute(DROP_PROCEDURE_GET_SUPPLIER)
        self.cursor.execute(CREATE_PROCEDURE_GET_SUPPLIER)
        self.cursor.execute(DROP_PROCEDURE_SALEBOOK)
        self.cursor.execute(CREATE_PROCEDURE_SALEBOOK)
        self.cursor.execute(DROP_PROCEDURE_SELECT_BOOK)
        self.cursor.execute(CREATE_PROCEDURE_SELECT_BOOK)

    def insert_new_book(self):
        args = ['12','关于建设双一流高校','罗俊','中山大学出版社','18']
        self.change(INSERT_NEW_BOOK, args)
        pass

    def purchase_book(self):
        pass

    def return_book(self):
        query = "select"
        args = []
        self.change(query, args)
        query = "update"
        args = []
        self.change(query, args)
        query = "insert"
        args = []
        self.change(query, args)

    def sell_book(self):
        query = "select"
        args = []
        self.search(query, args)
        query = "insert"
        args = []
        self.change(query, args)
        query = "select"
        args = []

    def statistics(self):
        pass