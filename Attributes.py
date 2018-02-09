# I learned to parse workbooks with https://www.sitepoint.com/using-python-parse-spreadsheet-data/


import xlrd

class Attributes:

    def __init__(self):
        self.inputs = []
        self.output = None

    def addInput(self, newInput):
        self.inputs.append(newInput)


    def parseInputs(self, workbook_file, row_index):
        workbook = xlrd.open_workbook(workbook_file, row_index)
        worksheet = workbook.sheet_by_index(0)
        for i in range(0,worksheet.row_len(row_index)-1):
            self.inputs.append(worksheet.cell(row_index, i))
        self.output = worksheet.cell(row_index, worksheet.row_len(row_index)-1)