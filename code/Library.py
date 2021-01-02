from PyMySQL import PyMySQL

class Library(PyMySQL):
    def __init__(self, host, user, pwd):
        PyMySQL.__init__(self, host, user, pwd)
        self._init_database()
        self._init_table()
        self.purchase_book()
        self._quit()

    def _init_database(self):
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS BookSale DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
        self.cursor.execute('use booksale;')

    def _init_table(self):
        sql = """CREATE TABLE IF NOT EXISTS `book` (
        	  `id` int(11) NOT NULL AUTO_INCREMENT,
        	  `name` varchar(255) NOT NULL,
        	  `store` int(11) NOT NULL,
        	  PRIMARY KEY (`id`)
        	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
        # #   表的创建
        # query = "create table "
        self.cursor.execute(sql)

    def purchase_book(self):
        #   库存表修改
        query = "insert into book values(%s, %s, %s)"
        args = ['2','罗俊2','19']
        self.change(query, args)
        # #   进货表修改
        # query = "insert"
        # args = []
        # self.change(query, args)

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