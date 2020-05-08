#! encoding=gbk
import pytest
import allure

@allure.feature("attach")
def test_attach_text():
    allure.attach("���Ǹ����ı�����",attachment_type=allure.attachment_type.TEXT)

@allure.feature("attach")
def test_attach_html():
    allure.attach("<body>this is html body !</body>","htmlģ��",attachment_type=allure.attachment_type.HTML)

@allure.feature("attach")
def test_attach_jpg():
    allure.attach.file("./test_data/pic1.jpg","jpg_pic",attachment_type=allure.attachment_type.JPG)

# �����쳣��ͼ��������ͼ��Ϊ����д�뱨���С�

if __name__ == '__main__':
    pytest.main(["-v","-s","test_attach.py"])