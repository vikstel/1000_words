from openpyxl import load_workbook


wb = load_workbook('./1000_words.xlsx')
ws = wb['Лист1']

words_dict = {}
row_a = ws['A1': 'B2496']
for row in row_a:
    words_dict[row[0].value] = row[1].value

print(words_dict)