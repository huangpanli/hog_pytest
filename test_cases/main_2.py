#! encoding=gbk
from  test_cases import main_1
print('main2.py的__name__的value: ', __name__)
def hello2():
    print("hello2")

if __name__ == '__main__':
    hello2()