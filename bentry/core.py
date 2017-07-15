# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.utils import column_index_from_string, get_column_letter
#import re
#from . import helpers

# def get_hmm():
#     """Get a thought."""
#     return 'hmmm...'
#
#
# def hmm():
#     """Contemplation..."""
#     if helpers.get_answer():
#         print(get_hmm())

wb = openpyxl.load_workbook('example.xlsx')

# Mock dictionary for testing single sheet entry
mockDict = [{'name':'item1','category': 'Food', 'price':10.93},
{'name':'item2','category': 'Entertainment', 'price':4.32},
{'name':'item3','category': 'Misc', 'price':1.00},
{'name':'item4','category': 'Food', 'price':45.3},
{'name':'item5','category': 'Transportation', 'price':23.40},
{'name':'item6','category': 'Transportation', 'price':2.29}]

categories = ['Food', 'Entertainment', 'Transportation', 'Misc']

firstRow = 9
categoryAnchors = {
    'Food': (firstRow, column_index_from_string('A')),
    'Entertainment': (firstRow, column_index_from_string('E')),
    'Transportation': (firstRow, column_index_from_string('I')),
    'Misc': (firstRow, column_index_from_string('M'))}

sheet1 = wb.get_sheet_by_name(wb.get_sheet_names()[0])


def findOpenCell(coordinate):
    """takes tuple cell coordinate and returns new tuple coordinate of first empty cell decending from origin"""
    rowIndex = row=coordinate[0]
    while sheet1.cell(row=rowIndex, column=coordinate[1]).value is not None:
        rowIndex += 1
    return (rowIndex, coordinate[1])

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
        sheet1.cell(row=cellAnchor[0]+idx, column=cellAnchor[1]).value = 'placholder date'
        sheet1.cell(row=cellAnchor[0]+idx, column=cellAnchor[1]+1).value = name
        sheet1.cell(row=cellAnchor[0]+idx, column=cellAnchor[1]+2).value = price
        idx += 1



for array in filterCategories(mockDict):
    # TODO handle error when category does not exist
    writeToCategory(array, array[0]['category'])





wb.save('example.xlsx')


 # proof of concept functionality:
 #    single sheet entry
 #    take a dictionary/data structure at the top of this file,
 #        entries: item, cost, category, opt:date
 #        if no date, use current date
 #    open example sheet
 #    write budget entries in corresponding sections
 #        this could also be an opportunity to change how I record budget, which makes the issue more complicated
 #        should I be matching the existing excel format, creating a new one, or meeting halfway?
 #        and later down the line I may even be cutting out the excel process entirely and writing direct to a database
