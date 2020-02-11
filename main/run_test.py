#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mai = SendEmail()

    # 程序执行入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.get_is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData()
                    # 获取的依赖响应数据
                    depend_resonse_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    data[depend_key] = depend_resonse_data
                res = self.run_method.run_main(method,url,data,header)

                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,"pass")
                    pass_count.append(i)
                else:
                    self.data.write_result(i,res)
                    fail_count.append(i)

        self.send_mai.send_main(pass_count,fail_count)

if __name__ == "__main__":
    run = RunTest()
    print(run.go_on_run())