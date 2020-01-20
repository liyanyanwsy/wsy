#encoding:utf-8
class SolarmanCacheKeyword(object):
    # def getDeviceType(self,devicename):
        # if devicename=='逆变器':
        #     devicetype='01'
        # elif devicename=='汇流箱':
        #     devicetype='02'
        # elif devicename=='电池(储能)':
        #     devicetype='03'
        # elif devicename=='气象站':
        #     devicetype='04'
        # elif devicename=='电表':
        #     devicetype='05'
        # elif devicename=='空调':
        #     devicetype='06'
        # elif devicename=='离网机':
        #     devicetype='07'
        # elif devicename=='谐波表':
        #     devicetype='08'
        # elif devicename=='质量监控（水、空气等':
        #     devicetype='09'
        # elif devicename=='智能家居':
        #     devicetype='10'
        # elif devicename=='太阳能跟踪器控制器':
        #     devicetype='11'
        # elif devicename=='微逆':
        #     devicetype='15'
        #
        # return devicetype
#返回设备的类型，根据不同的设备名来定义设备类型
    def getDeviceType(self,devicename):
        device_type={
            '逆变器':'01',
            '汇流箱':'02',
            '电池(储能)':'03',
            '气象站':'04',
            '电表':'05',
            '空调':'06',
            '离网机':'07',
            '谐波表':'08',
            '质量监控（水、空气等':'09',
            '智能家居':'10',
            '太阳能跟踪器控制器':'11',
            '微逆':'15'
        }
        #添加default错误，后期优化
        devicetype=device_type.get(devicename)
        return  devicetype
    # a=getDeviceType('智能家居')
    # print(a)
    #定义数据类型
    def getDataType(self,dataname):
        data_type={
            '信息帧':'01',
            '数据帧':'02'
        }
        datatype=data_type.get(dataname)
        return datatype
    # a=getDataType('数据帧')
    # # print(a)
    #定义传输的数据形式
    def getDataTransType(self,dataTransName):
        trans_type={
            '普通实时':'01',
            '普通历史':'81',
            '精简实时':'11',
            '精简历史':'91'
        }
        transtype=trans_type.get(dataTransName)
        return transtype
    # a=getDataTransType('普通实时')
    # print(a)
#

