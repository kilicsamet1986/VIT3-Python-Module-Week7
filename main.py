import gspread
from PyQt6.QtWidgets import QApplication, QTableWidgetItem


def connection_hub(credentials, table):
    gc = gspread.service_account(filename=credentials)
    spreadsheet = gc.open(table)
    worksheet = spreadsheet.get_worksheet(0)
    items = worksheet.get_all_values()
    return items


def write2table(page, a_list):
    table_widget = page.tableWidget
    table_widget.clearContents()  # Clear table
    table_widget.setColumnCount(len(a_list[0]))  # Add title to table
    table_widget.setHorizontalHeaderLabels(a_list[0])
    table_widget.setRowCount(len(a_list[1:]))  # Fill in the table
    for i, row in enumerate(a_list[1:]):
        for j, col in enumerate(row):
            item = QTableWidgetItem(str(col))
            table_widget.setItem(i, j, item)
    return True


def list_exclude(a_list, excluded_column_indexes):
    n_list = []
    for i, row in enumerate(a_list):
        item = []
        for j, col in enumerate(row):
            # if "column index" is inside our exclude list, come inside "if code block" and pass the loop.
            # don't add anything to item
            if j in excluded_column_indexes:
                continue
            # Otherwise add column to the item, which will become a row for new list
            item.append(col)
        n_list.append(item)     # add new item(row) to the new list
    return n_list


if __name__ == '__main__':
    from login import LoginPage

    app = QApplication([])
    window = LoginPage()
    window.show()
    app.exec()
