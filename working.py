from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

#inset rows of data

ws.append(['Sean', 'Is', 'Awesome', '!!!'])

wb.save('Book2.xlsx')

