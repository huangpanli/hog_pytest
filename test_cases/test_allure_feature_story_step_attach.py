#! encoding=gbk
import pytest
import allure
import os

@allure.feature('��¼')
class TestAllure:

    @allure.story('��¼')
    # @allure.title('Title��¼')
    def test_login_success(login):
        '''this is login case'''
        with allure.step("�����û���"):
            print("�����û���")
        with allure.step("��������"):
            print("��������")
        print("��������_��¼")

    @allure.story('�˳�')
    # @allure.title('Title�˳�')
    def test_login_failure(login):
        '''this is logout case'''
        print("��������_�˳�")
