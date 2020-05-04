#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyDictDatabase import *
from database import data

import time

DictDB = PyDictDatabase(database=data,settings={"ERROR_OUTPUT":True})
del data


test_range = 1000
test_list = []

for x in range(0,test_range):
    time1 = time.time()

    ''' CHOOSE ONE TEST '''
    result = DictDB.fetchone("SELECT timestamp FROM dataI2C WHERE id = 0x23")
#    result = DictDB.fetchall("SELECT timestamp FROM dataI2C WHERE id = 0x23")
#    result = DictDB.fetchall("SELECT group,timestamp,value FROM dataI2C WHERE id = 0x23")
#    result = DictDB.commit("UPDATE connections SET noFail_timestamp = 12345678 WHERE id = wlan")
#    result = DictDB.commit("UPDATE connections SET noFail_timestamp = 12345678,value = True WHERE id = wlan")

    time2 = time.time()
    test_list.append(round(float(time2-time1)*1000,5))

test_list.sort()

print("sum of all queries: " + str(round(sum(test_list),5)) + " ms")
print("time average: " + str(round(sum(test_list)/test_range,5)) + " ms")
print("shortest query: " + str(test_list[0]) + " ms")
print("longest query: " + str(test_list[len(test_list)-1]) + " ms")
