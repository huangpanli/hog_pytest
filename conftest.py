import os
import pytest
# ��ĿĿ¼����
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "\\test_report\\"
ALLURE_REPORT_DIR = BASE_DIR + "\\allure_report\\"
# ���в���������Ŀ¼���ļ�
cases_path = "./test_cases/"

@pytest.fixture()
def login():
    print("this is login fixture")
    print("close!!!")
