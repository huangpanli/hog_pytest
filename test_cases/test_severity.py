#! encoding=gbk
import pytest
import allure

'''
@allure.severityװ�����������Լ��������case������
ִ��ָ���������� --allure-severities blocker
BLOCKER = 'blocker'��������ȱ��
CRITICAL = 'critical'������ȱ��
NORMAL = 'normal'����  һ��ȱ��
MINOR = 'minor'����    ��Ҫȱ��
TRIVIAL = 'trivial'������΢ȱ�ݡ�
'''


@allure.severity(allure.severity_level.NORMAL)
def test_case_1():
    '''this is nomorl testcase'''
    print("test case normal")


@allure.severity(allure.severity_level.CRITICAL)
def test_case_2():
    '''this is critical testcase'''
    print("test case critical")


@allure.severity(allure.severity_level.MINOR)
def test_case_3():
    '''this is minor testcase'''
    print("test case minor")


@allure.severity(allure.severity_level.BLOCKER)
def test_case_4():
    '''this is blocker testcase'''
    print("test case blocker")

@allure.severity(allure.severity_level.TRIVIAL)
def test_case_5():
    '''this is trival testcase'''
    print("test case trivial")