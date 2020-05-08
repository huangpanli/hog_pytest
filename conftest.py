import os
import pytest
# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "\\test_report\\"
ALLURE_REPORT_DIR = BASE_DIR + "\\allure_report\\"
# 运行测试用例的目录或文件
cases_path = "./test_cases/"

@pytest.fixture()
def login():
    print("this is login fixture")
    print("close!!!")
