#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-21 下午5:29
# @Author  : 闫继龙
# @File    : sqlite3_code.py
# @Software: PyCharm

import sqlite3

conn = sqlite3.connect('test.db')
'''
create_sql = 'create table company(emp_id int primary key  not null ,emp_name message_text not null )'
conn.execute(create_sql)
'''

insert_sql = 'insert into company values (?,?)'
conn.execute(insert_sql, (100, 'LY'))
conn.execute(insert_sql, (120, 'july'))

select_all_sql = 'select emp_id,emp_name from company'
cursors = conn.execute(select_all_sql)
for row in cursors:
    print(row[0], row[1])

conn.close()
