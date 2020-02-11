#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

import unittest
import json
from interfaceTest.base.HttpMethon import RunMain
import HTMLTestRunner
import os
import time
import mock
from mock_demo import mock_test


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()
        self.uuid = self.test01()

    def test01(self):
        url = "https://www.kuaidi100.com/query?type=yunda&postid=4303562980128&temp=0.89132139814984&phone="
        data = ""
        res = self.run.run_math("get",url,data)
        print(res)
        result = json.loads(res)
        self.assertEquals(result["status"],"200","测试通过")

        global uuidd

        uuidd = 3000
        self.uuid = 300
        return self.uuid

    #@unittest.skip("test02")
    def test02(self):
        print(self.uuid)
        print(uuidd)

        url = "https://www.kuaidi100.com/query?type=yunda&postid=4303562980128&temp=0.89132139814984&phone="
        data = ""
        res = self.run.run_math("get", url, data)
        result = json.loads(res)
        self.assertEquals(result["message"],"ok","测试失败")

    def test03(self):
        print(self.uuid)
        print(uuidd)

        url = "https://www.kuaidi100.com/query?type=yunda&postid=4303562980128&temp=0.89132139814984&phone="
        data = ""
        res = mock_test(self.run.run_math,data,url,"get",data)
        print(res)

        #res = self.run.run_math("get", url, data)
        result = json.loads(res)

        self.assertEquals(result["message"],"ok","测试失败")


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.join(os.getcwd(), 'report')
    print(report_path)
    #filepath = os.path.join()"../report/htmlreport.html"
    report_abspath = os.path.join(report_path, "result_" + now + ".html")
    fp = open(report_abspath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test01'))
    suite.addTest(TestMethod('test02'))
    suite.addTest(TestMethod('test03'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="这是测试报告")
    runner.run(suite)

    #unittest.TextTestRunner().run(suite)
