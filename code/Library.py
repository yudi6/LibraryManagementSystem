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

    def get_inf_by_name(self, name):
        args = [name,]
        return self.search(SHOW_INF_BY_BOOK_NAME, args)

    def call_supply(self, line):
        self.cursor.callproc('supply', line)
        self.conn.commit()

    def get_store(self):
        args = []
        return self.search(SHOW_STORE,[])

    def call_sale_book(self, line):
        self.cursor.callproc('SaleBook', line)
        self.conn.commit()

    def call_RefundBook(self, saleID):
        self.cursor.callproc('RefundBook',[saleID,])
        self.conn.commit()

    def show_saleid(self):
        return self.search(SHOW_ALL_SALEID,[])

    def show_inf_by_sale_id(self, sale_id):
        return self.search(SHOW_SALE_BY_SALEID,args=[sale_id,])

    def show_month(self):
        return self.search(SHOW_MOUTH_DATA,[])

    def show_fuck(self,ym):
        return self.search(SHOW_FUCK_DATA,[ym,])
