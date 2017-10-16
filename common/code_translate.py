#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Copyright (c) 2017 - xiongjiezk <xiongjiezk@163.com>

import sys
from xlwt import Workbook
import xlrd

__author__ = 'jie.xiong'

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file, write_file):
    data = open_excel(file)
    table = data.sheet_by_name(u'Sheet1')
    nrows = table.nrows  # 行数
    template_row =  table.row_values(0)  # 第一行
    if len(template_row) != 2:
        print("模板行长度不等于2，退出")
    template = table.row_values(0, 0, 2)

    style_template = template[1].strip('\n').split('\n\n')
    if len(style_template) != 2:
        print("代码格式错误,表头和表格内容之间用空行分隔，示例: \n <p><span><strong>%s</strong></span></p>\n\n<ul>\n<li><span>%s</span></li>\n</ul>\n程序退出.")
        sys.exit(-1)
    if "%s" not in style_template[0]:
        print("代码格式错误,表头缺少格式化串%s, 示例：\n<p><span><strong>%s</strong></span></p>\n程序退出.")
        sys.exit(-1)
    if "%s" not in style_template[1]:
        print("代码格式错误,表格内容缺少格式化串%s，示例：\n<li><span>%s</span></li>\n程序退出.")
        sys.exit(-1)
    title_template = style_template[0]
    body_template_x = style_template[1].split('\n')
    if len(body_template_x) != 3:
        print("代码格式错误, 表格内容为三行, 示例: \n<ul>\n<li><span>%s</span></li>\n</ul>\n程序退出.")
        sys.exit(-1)

    book = Workbook()
    sheet1 = book.add_sheet(u'Sheet1')
    for row in range(1, nrows):
        html_code = ''
        text = table.row_values(row, 0, 1)
        for item in text[0].split('\n\n'):
            item = item.replace("\"", "&quot;")
            content = item.split('\n')
            if len(content) == 0:
                continue
            html_code += title_template % content[0]
            html_code += '\n\n'
            if len(content) > 1:
                html_code += body_template_x[0]
                html_code += '\n'
                for i in range(1,len(content)):
                    html_code += body_template_x[1] % content[i]
                    html_code += '\n'
                html_code += body_template_x[2]
                html_code += '\n\n'
        print html_code
        sheet1.write(row-1, 0, text)
        sheet1.write(row-1, 1, html_code)

    book.save(write_file)


def main(read_file, write_file):
    excel_table_byname(read_file, write_file)

# args = sys.argv
# if len(args) == 3:
#     read_file = args[1]
#     write_file = args[2]
# else:
#     print('请输入模板文件和写入文件，形式 python code_translate.py read_file_path write_file_path')
#     sys.exit(-1)
read_file = "/Users/admin/data/code_translate.xlsx"
write_file = '/Users/admin/data/simple2.xls'
main(read_file, write_file)