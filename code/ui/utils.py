from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from PyQt5.QtCore import Qt


def make_middle(table: QTableWidget, other=None):
    row_cnt = table.rowCount()
    col_cnt = table.columnCount()

    if other is None:
        other = []

    for _j in range(col_cnt):
        if _j in other:
            continue
        for _i in range(row_cnt):
            item = table.item(_i, _j)
            item.setTextAlignment(Qt.AlignCenter)


def add_item_to_table(table: QTableWidget, lst: tuple):
    if len(lst) == 0 or len(lst[0]) == 0:
        return

    item_num = len(lst)
    item_attribute_num = len(lst[0])
    item_num_in_table = table.rowCount()

    for _i in range(item_num):
        table.insertRow(_i + item_num_in_table)
        for _j in range(item_attribute_num):
            table.setItem(_i + item_num_in_table, _j, QTableWidgetItem(lst[_i][_j]))


def remove_items_from_table(table: QTableWidget):
    item_lst = table.selectedItems()
    item_num = len(item_lst)

    if item_num == 0:
        return
    row_idx_lst = []

    for _i in range(item_num):
        if item_lst[_i].row() not in row_idx_lst:
            row_idx_lst.append(item_lst[_i].row())

    row_idx_lst.sort(reverse=True)
    for index in row_idx_lst:
        table.removeRow(index)


def refresh_all_in_table(table: QTableWidget, lst: tuple):
    if len(lst) == 0 or len(lst[0]) == 0:
        return

    item_num_in_table = table.rowCount()
    for _i in range(item_num_in_table):
        table.removeRow(0)
    add_item_to_table(table, lst)


def get_selected_items_in_table(table: QTableWidget, col_num: int):
    item_lst = table.selectedItems()
    item_num = len(item_lst)

    if item_num == 0:
        return []
    row_num = int(item_num / col_num)
    tmp_lst = []
    for _i in range(row_num):
        tmp_item_lst = []
        for _j in range(col_num):
            item = item_lst[_i * col_num + _j].text()
            tmp_item_lst.append(item)
        tmp_lst.append(tuple(tmp_item_lst))
    return tuple(tmp_lst)


def get_all_items_in_table(table: QTableWidget):
    row_num = table.rowCount()
    col_num = table.columnCount()
    items_lst = []

    for _i in range(row_num):
        item_lst = []
        for _j in range(col_num):
            item_lst.append(table.item(_i, _j).text())
        items_lst.append(tuple(item_lst))

    return items_lst


def add_demo_items_in_table(table: QTableWidget, row, col):
    tmp = []
    for _i in range(row):
        tmp2 = []
        for _j in range(col):
            tmp2.append('%d_%d' % ((_i + 1), (_j + 1)))
        tmp.append(tuple(tmp2))
    tmp = tuple(tmp)
    add_item_to_table(table, tmp)


def make_items_free(table: QTableWidget, col):
    row_num = table.rowCount()

    for _i in range(row_num):
        table.item(_i, col).setSelected(True)

def tuple_to_str_list(tuple):
    str_list = []
    for line in tuple:
        str_list.append([str(i) for i in line])
    return str_list


