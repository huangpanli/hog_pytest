#! encoding=gbk

import pytest
import yaml
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize("test_data1,test_data2,expected",[(1,1,2),(2,2,4),(3,3,6)])
def test_parametrize(test_data1,test_data2,expected):
    assert test_data1 + test_data2 == expected
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize("user,pwd",[("lily","123456"),("roy","789")])
def test_param1(user, pwd):
    print(f"用户名：{user} 密码：{pwd}")
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize(["user","pwd"],[("lily","123456"),("roy","789")])
def test_param2(user, pwd):
    print(f"用户名：{user} 密码：{pwd}")
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize(("user","pwd"),[("lily","123456"),("roy","789")])
def test_param3(user, pwd):
    print(f"用户名：{user} 密码：{pwd}")

user_list = [('wangxiao', '123'), ('chengzi', '123456')]
@pytest.fixture(scope="module")
def login(request):
    req = request.param
    user = req[0]
    pwd =  req[1]
    print("用户名：%s,密码：%s" % (user, pwd))
    return user, pwd
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize("login", user_list, indirect=True)
def test_login(login):
    user,pwd =login
    print("此次传入的参数值：",login,"user",user,"pwd",pwd)

# def test_yaml():
#     with open("../test_data/test_data.yaml","rb") as fp:
#         print(yaml.safe_load(fp))

# 从yaml文件里读取yaml数据，yaml.safe_load将yaml数据转成python对象数据，python对象数据作为参数结合@pytest.mark.parametrize进行参数化，这就是数据驱动。
# @pytest.mark.parametrize("data",yaml.load(open("../test_data/test_data.yaml","rb"),Loader=yaml.FullLoader))
# @pytest.mark.parametrize("data",yaml.safe_load(open("../test_data/test_data.yaml","rb")))#单个文件调试使用的路径
@pytest.mark.parametrize("data",yaml.safe_load(open("./test_data/test_data.yaml","rb")))#run_tests.py调试使用
def test_datadriven(data):
    print(type(data))
    print("此次传入的数据是：",data,data["user"],data["pwd"])

if __name__ == '__main__':
    pytest.main(["-v","-s"])