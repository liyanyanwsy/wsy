#coding:utf-8
import xlrd
class ExcelUtil():
    def __init__(self,excelpath,sheetName):
        self.data=xlrd.open_workbook(excelpath)
        self.table=self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys=self.table.row_values(0)
        print self.keys
        #获取总行数
        self.rowNum=self.table.nrows
        #获取总列数
        print self.rowNum
        self.colNum=self.table.ncols
        print self.colNum
    def dict_data(self):
        if self.rowNum <=1:
            print "总行数小于1"
        else:
            r=[]
            j=1
            for i in range(self.rowNum-1):
                s={}
                #第二行取对应value值
                values=self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
            return r
if __name__ == '__main__':
    filepath=r"D:\xingit\wsy\ApiAuto\config\test.xlsx"
    sheetName="Sheet1"
    data=ExcelUtil(filepath,sheetName)
    print data.dict_data()



