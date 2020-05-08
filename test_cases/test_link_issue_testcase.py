#! encoding=gbk
import allure

LINK = "https://www.cnblogs.com/yoyoketang/p/12203778.html"
@allure.feature("link")
@allure.link('https://www.baidu.com')
def test_with_link():
    print("this is 直接使用地址做链接的测试用例")

@allure.feature("link")
@allure.link(LINK, name='点击我看一看youtube吧')
def test_with_named_link():
    print("this is 使用名称做链接，连接到知道的地址，测试用例")

@allure.feature("link")
@allure.issue('12203778', name='我是个bug，点击看看吧')
def test_with_issue():
    print("这个测试用例是在演示：链接到测试用例对应的bug地址")

@allure.feature("link")
@allure.testcase(LINK, name='我是个测试用例，点击看看吧')
def test_with_testcase():
    print("这个测试用例是在演示：链接到测试用例对应的测试用例地址")