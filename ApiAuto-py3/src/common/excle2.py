# coding:utf-8
import xlrd

class HandleExcel(object):
    """封装操作excel的方法"""
    def __init__(self, file=r'D:\xingit\wsy\ApiAuto\config\test.xlsx', sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet
    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        # t = self.get_data()  # 调用get_data()取得sheet对象(如果不在构造器获取sheet对象，就需要在方法内先获取sheet对象，再进行下一步操作，每个方法都要这样，所以还是写在构造器中方便)
        # rows = t.nrows
        return rows
    # 获取excel数据列数
    def get_cols(self):
        cols = self.data.ncols
        return cols
    # 获取某个单元格数据
    def get_value1(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_value(self):
        pass
    #根据列名，返回索引值
    def getColumnIndex(self, columnName):
        columnIndex = None
        for i in range(self.data.ncols):
            if(self.data.cell_value(0, i) == columnName):
                columnIndex = i
                break
        return columnIndex
    #根据行名，返回索引值
    def getRowIndex(self, RowName):
        RowIndex = None
        for i in range(self.data.nrows):
            if(self.data.cell_value(i, 0) == RowName):
                RowIndex = i
                break
        return RowIndex
    def get_value(self,row_name,col_name):
        row_index=self.getRowIndex(row_name)
        col_index=self.getColumnIndex(col_name)
        value=self.data.cell(row_index,col_index).value
        return  value


# # 封装excel的列名常量
# def get_caseseq():
#     """获取caseSeq"""
#     caseSeq = 0
#     return caseSeq
#
#
# def get_apitype():
#     """获取apiType"""
#     apiType = 1
#     return apiType
#
#
# def get_apiseq():
#     """获取apiSeq"""
#     apiSeq = 2
#     return apiSeq
#
#
# def get_apiName():
#     """获取apiName"""
#     apiName = 3
#     return apiName
#
#
# def get_priority():
#     """获取priority"""
#     priority = 4
#     return priority
#
#
# def get_url():
#     """获取url"""
#     url = 5
#     return url
#
#
# def get_method():
#     """获取method"""
#     method = 6
#     return method
#
#
# def get_header():
#     """获取header"""
#     header = 7
#     return header
#
#
# def get_purpose():
#     purpose = 8
#     return purpose
#
#
# def get_params():
#     """获取params"""
#     params = 9
#     return params
#
#
# def get_expectvalue():
#     """获取expectValue"""
#     expect = 10
#     return expect

if __name__ == '__main__':
    test = HandleExcel()
    print(test.get_rows())
    print(test.get_cols())
    # print(test.get_value(2, 2))
    print(test.getColumnIndex("path"))
    print(test.getRowIndex("plant_data"))
    print(test.get_value1(test.getRowIndex("plant_data"),test.getColumnIndex("url"),))
    print(test.get_value("plant_data","path"))