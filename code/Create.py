CREATE_DATABASE = """CREATE DATABASE IF NOT EXISTS bookManagement DEFAULT CHARSET utf8 COLLATE utf8_general_ci;"""
USE_DATABASE = """use bookManagement;"""

CREAT_TABLE_BOOK =  """CREATE TABLE IF NOT EXISTS `book` (
    BookID varchar(8),      
    BookName varchar(40),
    Author varchar(40),
    Publisher varchar(40),
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
)NGINE=InnoDB  DEFAULT CHARSET=utf8;"""

# CREAT_TABLE_SUPPLY_LIST =  """CREATE TABLE IF NOT EXISTS `supplyList` (
#     supplierID varchar(8),
#     BookID varchar(8),
#     Price numeric(5,2),
#     Amount int,
#     FOREIGN key (supplierID) REFERENCES supplier(supplierID),
#     foreign key (BookID) references book(BookID)
# )ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_STOREHOUSE =  """CREATE TABLE IF NOT EXISTS `storehouse` (
    BookID varchar(8),
    Amount int,
    Price NUMERIC(5,2),
    foreign key (BookID) references book(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_SALE =  """CREATE TABLE IF NOT EXISTS `sale` (
    SaleID int,
    BookID varchar(8),
    Amount int,
    sellTime int, 
    PRIMARY key (SaleID,BookID),
    FOREIGN key (BookID) REFERENCES storehouse(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_REFUND =  """CREATE TABLE IF NOT EXISTS `refund` (
    SaleID INT,
    BookID varchar(8),
    foreign key (SaleID,BookID) references sale(SaleID,BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""


DROP_PROCEDURE_GET_SUPPLIER = """DROP PROCEDURE IF EXISTS GetSupplier;"""
CREATE_PROCEDURE_GET_SUPPLIER = """create PROCEDURE GetSupplier()
begin
    select BookID, BookName, Author, Publisher, Price, Amount
    from book natural join supplier;
end"""

DROP_PROCEDURE_SUPPLY = """DROP PROCEDURE IF EXISTS supply;"""
CREATE_PROCEDURE_SUPPLY = """CREATE PROCEDURE supply(in BookID varchar(8), in Price numeric(5,2), in Amount int) 
BEGIN 
    declare temp varchar(8);
    SELECT BookID into temp from storehouse;
    if temp is null then
        INSERT INTO storehouse values(BookID,Price,Amount);
    else
        UPDATE storehouse
        set storehouse.Amount = storehouse.Amount + Amount
        WHERE storehouse.BookID = BookID;
    end if;
END"""

DROP_PROCEDURE_SALEBOOK = """DROP PROCEDURE IF EXISTS SaleBook;"""
CREATE_PROCEDURE_SALEBOOK = """CREATE PROCEDURE SaleBook(  in SaleID int,
                            in BookID varchar(8),
                            in Amount int,
                            in sellTime int)
BEGIN 
    INSERT INTO sale values(SaleID, BookID,Amount,sellTime);
END"""

DROP_PROCEDURE_REFUNDBOOK = """DROP PROCEDURE IF EXISTS RefundBook;"""
CREATE_PROCEDURE_REFUNDBOOK = """CREATE PROCEDURE RefundBook(in SaleID int, in BookID varchar(8), out status int)
BEGIN 
    declare bookid varchar(8);
    declare amount int;
    SELECT Bookid, Amount into bookid, amount
    from sale 
    where sale.SaleID = SaleID and sale.BookID = BookID;
    if isnull(bookid) then
        set status = 1;
    else set status = 0;
    end if;
    INSERT INTO refund values(SaleID,BookID);
    DELETE FROM sale 
    WHERE sale.SaleID = SaleID and sale.BookID = BookID;
END"""

DROP_PROCEDURE_SELECT_BOOK = """DROP PROCEDURE IF EXISTS RefundBook;"""
CREATE_PROCEDURE_SELECT_BOOK = """create procedure selectBook(in bookname varchar(40))
begin
    select BookID, supplierID, price, amount 
    from book, supplierPrice 
    where book.BookID = supplierPrice.BookID and book.BookName = bookname;
end"""

DROP_TRIGGER_TR_AFTER_IN_REFUND = """DROP TRIGGER IF EXISTS tr_after_in_refund;"""
CREATE_TRIGGER_TR_AFTER_IN_REFUND = """CREATE TRIGGER tr_after_in_refund
    AFTER INSERT on refund
    for each row
    BEGIN 
        declare bookid varchar(8);
        declare amount int;
        SELECT BookID, Amount into bookid, amount
        from sale
        where sale.SaleID = new.SaleID and sale.BookID = new.BookID;
        update storehouse
        set storehouse.Amount = storehouse.Amount + amount
        where storehouse.BookID = bookid;
    END"""

DROP_TRIGGER_TR_AFTER_IN_SALE= """DROP TRIGGER IF EXISTS tr_after_in_sale;"""
CREATE_TRIGGER_TR_AFTER_IN_SALE = """CREATE TRIGGER tr_after_in_sale
    AFTER INSERT ON sale
    for each row
    BEGIN 
        update storehouse 
        set storehouse.Amount = storehouse.Amount - new.Amount 
        where storehouse.BookID = new.BookID;
    END"""


