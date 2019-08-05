# coding:utf-8
import xlrd
# class ExcleHelper(object):
#     def __init__(self):
#         self.file_name=r'D:\xingit\wsy\ApiAuto\config\test.xlsx'
#         self.sheet_name="Sheet1"
#         self.data=xlrd.open_workbook(self.file_name)
#         self.table=self.data.sheet_by_name(self.sheet_name)
#     def get_value(self,row_name,col_name):
#
#         rows=self.table.row_values(0)
#         cols=self.table.col_values(0)
#         row_index=cols.index(unicode(row_name))
#         col_index=rows.index(unicode(col_name))
#         value=self.table.cell(row_index,col_index).value
#         return value
#
# print(ExcleHelper().get_value("plant_data","path"))

# class ExcleHelper(object):
#     def __init__(self,filename=r'D:\xingit\wsy\ApiAuto\config\test.xlsx',sheetname="Sheet1"):
#         self.file_name=filename
#         self.sheet_name=sheetname
#         self.data=xlrd.open_workbook(self.file_name)
#         self.table=self.data.sheet_by_name(self.sheet_name)
#     def get_value(self,row_name,col_name):
#         rows=self.table.row_values(0)
#         cols=self.table.col_values(0)
#         row_index=cols.index(unicode(row_name))
#         col_index=rows.index(unicode(col_name))
#         value=self.table.cell(row_index,col_index).value
#         return value

class ExcleHelper(object):
    def __init__(self,filename,sheetname):
        self.file_name=filename
        self.sheet_name=sheetname
        self.data=xlrd.open_workbook(self.file_name)
        self.table=self.data.sheet_by_name(self.sheet_name)
    def get_value(self,row_name,col_name):
        rows=self.table.row_values(0)
        cols=self.table.col_values(0)
        # row_index=cols.index(unicode(row_name))
        # col_index=rows.index(unicode(col_name))
        row_index=cols.index(row_name)
        col_index=rows.index(col_name)
        value=self.table.cell(row_index,col_index).value
        return value
# print(ExcleHelper().get_value("plant_data","path"))
























