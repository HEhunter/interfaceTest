#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

import xlrd

from xlutils import copy
# data = xlrd.open_workbook('../dataconfig/测试用例.xlsx')
# print(data)
#
# tables = data.sheets()[0]
# print(tables.nrows)
# print(tables.cell_value(2,3))


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            #self.data = self.get_data()
        else:
            self.file_name = "../dataconfig/测试用例.xlsx"
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取行数
    def get_lines(self):
        return self.data.nrows

    # 获取单元格的到内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    # 写入数据
    def write_value(self,row,col,value):

        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy.copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据对应caseid，找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_cell_value(row_num)
        return row_data

    #根据对应的caseid，找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num += 1


    # 根据行号，找到行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self,col_id = None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols




if __name__ == "__main__":
    opens = OperationExcel()
    print(opens.get_cell_value(2,2))
    print(opens.get_lines())
