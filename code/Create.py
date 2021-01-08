CREATE_DATABASE = """CREATE DATABASE IF NOT EXISTS bookManagement DEFAULT CHARSET utf8 COLLATE utf8_general_ci;"""
USE_DATABASE = """use bookManagement;"""

CREAT_TABLE_BOOK =  """CREATE TABLE IF NOT EXISTS `book` (
    BookID varchar(8),      
    BookName varchar(40),
    Author varchar(40),
    Publisher varchar(40),
    sellPrice int,
    primary key (BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_SUPPLIER =  """CREATE TABLE IF NOT EXISTS `supplier` (
    supplierID varchar(8),
    supplierName VARCHAR(20),
    primary key (supplierID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_SUPPLIER_PRICE =  """CREATE TABLE IF NOT EXISTS `supplierPrice` (
    supplierID varchar(8),
    BookID varchar(8),
    Price NUMERIC(5,2),
    primary key (supplierID,BookID),
    FOREIGN key (supplierID) REFERENCES supplier(supplierID),
    FOREIGN key (BookID) REFERENCES book(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_SUPPLY_LIST =  """CREATE TABLE IF NOT EXISTS `supplyList` (
    supplierID varchar(8),
    BookID varchar(8),
    Price numeric(5,2),
    Amount int,
    FOREIGN key (supplierID) REFERENCES supplier(supplierID),
    foreign key (BookID) references book(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_STOREHOUSE =  """CREATE TABLE IF NOT EXISTS `storehouse` (
    BookID varchar(8),
    Price numeric(5,2),
    Amount int,
    foreign key (BookID) references supplyList(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_SALE =  """CREATE TABLE IF NOT EXISTS `sale` (
    SaleID varchar(8),
    BookID varchar(8),
    ConsumerName VARCHAR(20),
    Amount int,
    saleSum int,
    sellTime int, 
    PRIMARY key (SaleID),
    FOREIGN key (BookID) REFERENCES storehouse(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_REFUND =  """CREATE TABLE IF NOT EXISTS `refund` (
    SaleID varchar(8),
    Amount int,
    foreign key (SaleID) references sale(SaleID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""
