#! encoding=gbk
import pytest
import allure

@allure.feature("attach")
def test_attach_text():
    allure.attach("这是个纯文本附件",attachment_type=allure.attachment_type.TEXT)

@allure.feature("attach")
def test_attach_html():
    allure.attach("<body>this is html body !</body>","html模块",attachment_type=allure.attachment_type.HTML)

@allure.feature("attach")
def test_attach_jpg():
    allure.attach.file("./test_data/pic1.jpg","jpg_pic",attachment_type=allure.attachment_type.JPG)

# 错误异常截图，并将截图作为附件写入报告中。

if __name__ == '__main__':
    pytest.main(["-v","-s","test_attach.py"])