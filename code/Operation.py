INSERT_NEW_BOOK = """INSERT INTO book(BookID, BookName, Author, Publisher, sellPrice)
VALUES (%s, %s, %s, %s, %s);"""

INSERT_NEW_SUPPLIER = """INSERT INTO supplier(supplierID, supplierName)
VALUES (%s, %s);"""

INSERT_SUPPLIER_PRICE = """INSERT INTO supplierPrice(supplierID,BookID,Price)
VALUES (%s, %s, %s);"""

PURCHASE_BOOK = """INSERT INTO supplyList(supplierID,BookID,Price,Amount)
VALUES (%s, %s, %s, %s);"""

INSERT_NEW_BOOK_INTO_STORE ="""INSERT INTO storehouse(BookID,Price,Amount)
VALUES (%s, %s, %s)"""