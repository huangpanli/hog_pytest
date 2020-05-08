#! encoding=gbk
from conftest import REPORT_DIR,cases_path,ALLURE_REPORT_DIR
import pytest
import time,os
def init_env(now_time):
    """
    ��ʼ�����Ա���Ŀ¼
    """
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "/image")
if __name__ == '__main__':
    print(cases_path)
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    init_env(now_time)
    html_report = os.path.join(REPORT_DIR, now_time, "report.html")
    allure_report_raw_data = os.path.join(ALLURE_REPORT_DIR, now_time)  # ���allure���ɵĽ�������ļ�json�ļ�
    allure_report_html = os.path.join(allure_report_raw_data, "report")  # �������json�ļ����ɵı����ļ�
    # pytest.main(["-s", "-v", cases_path,"--html=" + html_report,"-n","auto"])
    # # ִ��1����������
    # pytest.main(["-s", "-v", cases_path,"--allure-stories","��¼","--html=" + html_report,"--alluredir",allure_report_raw_data])
    # # # ִ��2����������
    # pytest.main(["-s", "-v", cases_path, "--allure-features", "��¼", "--html=" + html_report,
    #              "--alluredir", allure_report_raw_data])
    # # ִ��2�������������ɼ��������ʹ�ã�--allure-storiesָ��ʧЧ��
    # pytest.main(["-s", "-v", cases_path, "--allure-features", "��¼","--allure-stories","��¼", "--html=" + html_report,
    #              "--alluredir", allure_report_raw_data])
    # ָ������ģ�����У�ͬʱָ������ƥ�����ʵ������ʱͨ���ǽ�id�����{}��ֵ��
    # pytest.main(["-v", "-s",cases_path,"--allure-features","link","--html=" + html_report,"--alluredir",allure_report_raw_data])
    # pytest.main(["-v", "-s", cases_path, "--allure-features", "link","--allure-link-pattern","issue:https://www.cnblogs.com/yoyoketang/p/{}.html", "--html=" + html_report, "--alluredir",
    #                  allure_report_raw_data])
    # pytest.main(["-v", "-s", cases_path, "--allure-severities","blocker,critical","--html=" + html_report, "--alluredir",
    #                               allure_report_raw_data])

    pytest.main(["-v", "-s", cases_path,"--allure-features","attach", "--html=" + html_report, "--alluredir",
                                  allure_report_raw_data])
    os.system("allure generate %s -o %s" % (allure_report_raw_data,allure_report_html))# ����json�ļ����ɱ��棬������ͼ�������ݡ�
    # os.system("allure open %s" % allure_report_html)#�򿪱���,�����ڱ�����Ⱦ�Ͳ鿴���
