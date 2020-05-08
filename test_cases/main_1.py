#! encoding=gbk
print('main1.py的__name__的value: ', __name__)
def hello1():
    print("hello1")
# hello1()

if __name__ == '__main__':
    hello1()
    print("测试main1.py文件被其他模块导入时，这个main函数是否被执行")
