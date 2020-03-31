#encoding:utf-8
import random
class Readdata():
    def __init__(self):
        with open("accout.txt") as f:
            account = f.readlines()
            # 随机数范围0--（数组长度-1）为了和list下标一样，从0开始
        self.ran = random.randint(0,len(account)-1)

    def readAccount(self):
        with open("accout.txt") as f:
            account = f.readlines()
            # print (account)
        accounts = []
        # readlines获取每一行数据保存为list，每一行数据是一个元素，字符串形式，
        # 这里要遍历转为int可以去掉换行符号再append一个新数组。
        for i in account:
            data = int(i)
            accounts.append(data)
            print (accounts)
        # 随机获取一个数
        account = accounts[self.ran]
        return account

if __name__ == "__main__":
    rd = Readdata()
    print (rd)



