#encoding:utf-8

# 思路：在userId.txt、type.txt文件中填写数据源，两个文件数据是一一对应的，通过readlines()读取，保存为一个列表，
# 通过list的索引读取数据，索引使用随机数
import random
class Readdata():
    # 随机数放在init方法中，保证只获取一次随机数，因为类只实例化一次
    def __init__(self):
        with open("./userId.txt") as f:
            userId = f.readlines()
            # 随机数范围0--（数组长度-1）为了和list下标一样，从0开始
        self.ran = random.randint(0,len(userId)-1)

    def readUserid(self):
        with open("./userId.txt") as f:
            userId = f.readlines()
        userIds = []
        # readlines获取每一行数据保存为list，每一行数据是一个元素，字符串形式，
        # 这里要遍历转为int可以去掉换行符号再append一个新数组。
        for i in userId:
            data = int(i)
            userIds.append(data)
        # 随机获取一个数
        userId = userIds[self.ran]
        return userId
    def readType(self):
        with open("./type.txt") as f1:
            type_ = f1.readlines()
        # 去掉list中的换行符号\n
        type1 = ''.join(type_).strip('\n')
        # 分割字符串，保存为list，
        type2 = type1.split(',')
        type3 = type2[self.ran]
        # print(type(type2))
        return type3
if __name__ == "__main__":
    rd = Readdata()
    print(rd.readType())
    print(rd.readUserid())
