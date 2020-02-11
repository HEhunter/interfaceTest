#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

# 结果对比
import json
from filecmp import cmp


class CommonUtil:

    def is_contain(self, str_one, str_two):
        flag = None
        if isinstance(str_one, str):
            print(str_one+"这是字符串")
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self,dict_one,dict_two):
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)
            return cmp(dict_one,dict_two)
