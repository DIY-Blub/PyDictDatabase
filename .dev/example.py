#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyDictDatabase import *

data = {
        'table1':  {
                    1: {'id':1,'key':"value"},
                    2: {'id':2,'key':"value"},
                    },
        'table2':  {
                    1: {'id':1,'name':"name1",'status':True},
                    2: {'id':2,'name':"name2",'status':False},
                    },
       }

DictDB = PyDictDatabase(database=data,settings={"ERROR_OUTPUT":True})
del data

result = DictDB.fetchone("SELECT status FROM table2 WHERE id = 1")
print(result)
result = DictDB.fetchall("SELECT status FROM table2 WHERE id = 1")
print(result)
result = DictDB.fetchall("SELECT name,status FROM table2 WHERE id = 1")
print(result)
result = DictDB.commit("UPDATE table2 SET status = False WHERE id = 1")
print(result)

DictDB.close()      # not yet necessary but useful for the future
