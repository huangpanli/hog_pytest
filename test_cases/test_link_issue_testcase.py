#! encoding=gbk
import allure

LINK = "https://www.cnblogs.com/yoyoketang/p/12203778.html"
@allure.feature("link")
@allure.link('https://www.baidu.com')
def test_with_link():
    print("this is ֱ��ʹ�õ�ַ�����ӵĲ�������")

@allure.feature("link")
@allure.link(LINK, name='����ҿ�һ��youtube��')
def test_with_named_link():
    print("this is ʹ�����������ӣ����ӵ�֪���ĵ�ַ����������")

@allure.feature("link")
@allure.issue('12203778', name='���Ǹ�bug�����������')
def test_with_issue():
    print("�����������������ʾ�����ӵ�����������Ӧ��bug��ַ")

@allure.feature("link")
@allure.testcase(LINK, name='���Ǹ��������������������')
def test_with_testcase():
    print("�����������������ʾ�����ӵ�����������Ӧ�Ĳ���������ַ")