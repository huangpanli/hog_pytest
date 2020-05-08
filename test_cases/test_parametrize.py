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
    print(f"�û�����{user} ���룺{pwd}")
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize(["user","pwd"],[("lily","123456"),("roy","789")])
def test_param2(user, pwd):
    print(f"�û�����{user} ���룺{pwd}")
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize(("user","pwd"),[("lily","123456"),("roy","789")])
def test_param3(user, pwd):
    print(f"�û�����{user} ���룺{pwd}")

user_list = [('wangxiao', '123'), ('chengzi', '123456')]
@pytest.fixture(scope="module")
def login(request):
    req = request.param
    user = req[0]
    pwd =  req[1]
    print("�û�����%s,���룺%s" % (user, pwd))
    return user, pwd
@pytest.mark.skip("no execute skip")
@pytest.mark.parametrize("login", user_list, indirect=True)
def test_login(login):
    user,pwd =login
    print("�˴δ���Ĳ���ֵ��",login,"user",user,"pwd",pwd)

# def test_yaml():
#     with open("../test_data/test_data.yaml","rb") as fp:
#         print(yaml.safe_load(fp))

# ��yaml�ļ����ȡyaml���ݣ�yaml.safe_load��yaml����ת��python�������ݣ�python����������Ϊ�������@pytest.mark.parametrize���в����������������������
# @pytest.mark.parametrize("data",yaml.load(open("../test_data/test_data.yaml","rb"),Loader=yaml.FullLoader))
# @pytest.mark.parametrize("data",yaml.safe_load(open("../test_data/test_data.yaml","rb")))#�����ļ�����ʹ�õ�·��
@pytest.mark.parametrize("data",yaml.safe_load(open("./test_data/test_data.yaml","rb")))#run_tests.py����ʹ��
def test_datadriven(data):
    print(type(data))
    print("�˴δ���������ǣ�",data,data["user"],data["pwd"])

if __name__ == '__main__':
    pytest.main(["-v","-s"])