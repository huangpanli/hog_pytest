#! encoding=gbk
from conftest import REPORT_DIR,cases_path,ALLURE_REPORT_DIR
import pytest
import time,os
def init_env(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "/image")
if __name__ == '__main__':
    print(cases_path)
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    init_env(now_time)
    html_report = os.path.join(REPORT_DIR, now_time, "report.html")
    allure_report_raw_data = os.path.join(ALLURE_REPORT_DIR, now_time)  # 存放allure生成的结果数据文件json文件
    allure_report_html = os.path.join(allure_report_raw_data, "report")  # 存放依据json文件生成的报告文件
    # pytest.main(["-s", "-v", cases_path,"--html=" + html_report,"-n","auto"])
    # # 执行1个测试用例
    # pytest.main(["-s", "-v", cases_path,"--allure-stories","登录","--html=" + html_report,"--alluredir",allure_report_raw_data])
    # # # 执行2个测试用例
    # pytest.main(["-s", "-v", cases_path, "--allure-features", "登录", "--html=" + html_report,
    #              "--alluredir", allure_report_raw_data])
    # # 执行2个测试用例，可见两个结合使用，--allure-stories指定失效。
    # pytest.main(["-s", "-v", cases_path, "--allure-features", "登录","--allure-stories","登录", "--html=" + html_report,
    #              "--alluredir", allure_report_raw_data])
    # 指定功能模块运行，同时指定链接匹配规则，实际运行时通常是将id号替代{}的值。
    # pytest.main(["-v", "-s",cases_path,"--allure-features","link","--html=" + html_report,"--alluredir",allure_report_raw_data])
    # pytest.main(["-v", "-s", cases_path, "--allure-features", "link","--allure-link-pattern","issue:https://www.cnblogs.com/yoyoketang/p/{}.html", "--html=" + html_report, "--alluredir",
    #                  allure_report_raw_data])
    # pytest.main(["-v", "-s", cases_path, "--allure-severities","blocker,critical","--html=" + html_report, "--alluredir",
    #                               allure_report_raw_data])

    pytest.main(["-v", "-s", cases_path,"--allure-features","attach", "--html=" + html_report, "--alluredir",
                                  allure_report_raw_data])
    os.system("allure generate %s -o %s" % (allure_report_raw_data,allure_report_html))# 依据json文件生成报告，有趋势图但无数据。
    # os.system("allure open %s" % allure_report_html)#打开报告,用于在本地渲染和查看结果
