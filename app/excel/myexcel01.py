#coding:utf-8
import xlrd
#简单的excel操作
#打开excel表格，参数是文件路径
data=xlrd.open_workbook("D:\\Program Files\\Git\\11\\test.xlsx")
#通过名称获取工作表
table=data.sheet_by_name(u'Sheet1')
#获取总行数
nrows=table.nrows
#获取总列数
ncols=table.ncols
#打印首行
print table.row_values(0)
#打印首列
print table.col_values(0)


