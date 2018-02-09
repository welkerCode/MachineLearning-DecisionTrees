import xlrd

from Example import Example

class Dataset:

    def __init__(self,filename):
        self.filename = filename
        self.exampleList = []

    def parseDatasheet(self):
        workbook = xlrd.open_workbook(self.filename)
        worksheet = workbook.sheet_by_index(0)
        num_rows = worksheet.nrows
        for i in range(0, num_rows):
            newExample = Example()
            newExample.parseAttributes(self.filename, i)
            self.exampleList.append(newExample)

    def getExampleList(self):
        return self.exampleList