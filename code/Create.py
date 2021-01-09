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
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

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
    PRIMARY KEY (BookID),
    foreign key (BookID) references book(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_SALE = """CREATE TABLE IF NOT EXISTS `sale` (
    SaleID int,
    BookID varchar(8),
    Amount int,
    sellTime int, 
    saleSum NUMERIC(10,2),
    PRIMARY key (SaleID,BookID),
    FOREIGN key (BookID) REFERENCES book(BookID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""

CREAT_TABLE_REFUND =  """CREATE TABLE IF NOT EXISTS `refund` (
    SaleID INT,
    foreign key (SaleID) references sale(SaleID)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8;"""


DROP_PROCEDURE_GET_SUPPLIER = """DROP PROCEDURE IF EXISTS GetSupplier;"""
CREATE_PROCEDURE_GET_SUPPLIER = """create PROCEDURE GetSupplier()
begin
    select BookID, BookName, Author, Publisher, Price, Amount
    from book natural join supplier;
end"""

DROP_PROCEDURE_SUPPLY = """DROP PROCEDURE IF EXISTS supply;"""
CREATE_PROCEDURE_SUPPLY = """CREATE PROCEDURE supply(in BookID_IN varchar(8),
                        in Price_IN numeric(5,2),
                        in Amount_IN int) 
BEGIN 
    declare temp varchar(8);
    SELECT distinct storehouse.BookID into temp from storehouse WHERE storehouse.BookID = BookID_IN;
    if temp is null then
        INSERT INTO storehouse values(BookID,Price,Amount);
    else
        UPDATE storehouse
        set storehouse.Amount = storehouse.Amount + Amount_IN
        WHERE storehouse.BookID = BookID_IN;
    end if;
END"""

DROP_PROCEDURE_SALEBOOK = """DROP PROCEDURE IF EXISTS SaleBook;"""
CREATE_PROCEDURE_SALEBOOK = """CREATE PROCEDURE SaleBook(  in SaleID int,
                            in BookID varchar(8),
                            in Amount int,
                            in sellTime int)
BEGIN
	declare Price_book numeric(5,2);
    select Price into Price_book
    from storehouse
    where BookID = storehouse.BookID;
    INSERT INTO sale values(SaleID, BookID, Amount, sellTime, Price_book*Amount);
END"""

DROP_PROCEDURE_REFUNDBOOK = """DROP PROCEDURE IF EXISTS RefundBook;"""
CREATE_PROCEDURE_REFUNDBOOK = """CREATE PROCEDURE RefundBook(in SaleID_IN int)
BEGIN 
    if SaleID_IN not in (SELECT refund.SaleID
    from refund) then
         INSERT INTO refund values(SaleID_IN);
    end if;
END"""

# DROP_PROCEDURE_SELECT_BOOK = """DROP PROCEDURE IF EXISTS selectBook;"""
# CREATE_PROCEDURE_SELECT_BOOK = """create procedure selectBook(in bookname varchar(40))
# begin
#     select BookID, supplierID, price, amount
#     from book, supplierPrice
#     where book.BookID = supplierPrice.BookID and book.BookName = bookname;
# end"""

DROP_TRIGGER_TR_AFTER_IN_REFUND = """DROP TRIGGER IF EXISTS tr_after_in_refund;"""
CREATE_TRIGGER_TR_AFTER_IN_REFUND = """CREATE TRIGGER tr_after_in_refund AFTER INSERT on refund
    for each row
    BEGIN 
        update storehouse, (SELECT BookID, Amount 
			from sale
			where sale.SaleID = new.SaleID) as bookid_amount
        set storehouse.Amount = storehouse.Amount + bookid_amount.Amount
        where storehouse.BookID = bookid_amount.BookID;
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


