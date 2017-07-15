# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.utils import column_index_from_string, get_column_letter
import CLI_input

SAFE_MODE = False # prevents writing to excel

wb = openpyxl.load_workbook('example.xlsx')
sheet1 = wb.get_sheet_by_name(wb.get_sheet_names()[0])

# TODO standardize how I reference categories, etc. so I reduce refactoring difficulty

categories = ['Food', 'Entertainment', 'Transportation', 'Misc']

firstRow = 9
categoryAnchors = {
    'Food': (firstRow, column_index_from_string('A')),
    'Entertainment': (firstRow, column_index_from_string('E')),
    'Transportation': (firstRow, column_index_from_string('I')),
    'Misc': (firstRow, column_index_from_string('M'))}


def findOpenCell(coordinate):
    """takes tuple cell coordinate and returns new tuple coordinate of first empty cell decending from origin"""
    rowIndex = row=coordinate[0]
    while sheet1.cell(row=rowIndex, column=coordinate[1]).value is not None:
        rowIndex += 1
    return (rowIndex, coordinate[1])

# TODO move this to unit tests
# # findOpenCellUnit tests
# print findOpenCell((7,1)) # expect (12,1)
# print findOpenCell((2,3)) # expect (2,3)
# print findOpenCell((7,4)) # expect (9,4)

def filterCategories(inputDict):
    """returns array of dicts for each category"""
    return map(lambda category: filter(lambda entry: entry['category'] == category, inputDict), categories)

def writeToCategory(array, category):
    """writes all entries of a category to that category column"""
    cellAnchor = findOpenCell(categoryAnchors[category])
    idx = 0

    for entry in array:
        name = entry['name']
        price = entry['price']
        date = entry['date']

        sheet1.cell(row=cellAnchor[0]+idx, column=cellAnchor[1]).value = date
        sheet1.cell(row=cellAnchor[0]+idx, column=cellAnchor[1]+1).value = name
        sheet1.cell(row=cellAnchor[0]+idx, column=cellAnchor[1]+2).value = price
        idx += 1



for array in filterCategories(CLI_input.userInput()):
    if len(array) > 0:
        if not SAFE_MODE:
            writeToCategory(array, array[0]['category'])
        else:
            print array


wb.save('example.xlsx')
