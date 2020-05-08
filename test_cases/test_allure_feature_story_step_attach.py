#! encoding=gbk
import pytest
import allure
import os

@allure.feature('登录')
class TestAllure:

    @allure.story('登录')
    # @allure.title('Title登录')
    def test_login_success(login):
        '''this is login case'''
        with allure.step("输入用户名"):
            print("输入用户名")
        with allure.step("输入密码"):
            print("输入密码")
        print("测试用例_登录")

    @allure.story('退出')
    # @allure.title('Title退出')
    def test_login_failure(login):
        '''this is logout case'''
        print("测试用例_退出")
