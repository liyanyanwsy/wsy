
#coding:utf-8
#该代码未实现，后续研究
# from thrift import Thrift
# from thrift.transport import TSocket, TTransport
# from thrift.protocol import TBinaryProtocol
# from hbase import Hbase
# from hbase.ttypes import ColumnDescriptor, Mutation, BatchMutation, TRegionInfo
# from hbase.ttypes import IOError, AlreadyExists
def open_text(file_dir):
    with open(file_dir, "r") as f:
        s = f.readlines()
        print s
        print type(s)
        print s[0]
open_text("C:\\Users\\lyy\Desktop\\username.txt")






    # #server端地址和端口
# transport = TSocket.TSocket('10.42.2.32/root@1234', 2181)
# #可以设置超时
# transport.setTimeout(5000)
# #设置传输方式（TFramedTransport或TBufferedTransport）
# trans = TTransport.TBufferedTransport(transport)
# #设置传输协议
# protocol = TBinaryProtocol.TBinaryProtocol(trans)
# #确定客户端
# client = Hbase.Client(protocol)
# #打开连接
# transport.open()
# print "------"
# #获取表名
# print client.getTableNames()