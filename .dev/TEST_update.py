#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyDictDatabase import *
from database import data

DictDB = PyDictDatabase(database=data,settings={"ERROR_OUTPUT":True})
del data

### UPDATE ###
print("### UPDATE ###")
print("")

## EXAMPLE: commit / UPDATE one value
print('commit("UPDATE dataI2C SET name = {} WHERE id = {}".format("check with Space bar","0x23"))')
result = DictDB.commit("UPDATE dataI2C SET name = {} WHERE id = {}".format("check with Space bar","0x23"))
print("show return: " + str(result) + "        " + str(type(result)))
## check
result = DictDB.fetchall("SELECT name FROM dataI2C WHERE id = 0x23")
print("['name']: " + str(result["name"]) + "        " + str(type(result["name"])))

print("")
print("")

## EXAMPLE: commit / UPDATE one value
print('commit("UPDATE connections SET noFail_timestamp = {},value = {} WHERE id = {}".format(12345678,True,"wlan"))')
result = DictDB.commit("UPDATE connections SET noFail_timestamp = {},value = {} WHERE id = {}".format(12345678,True,"wlan"))
print("show return: " + str(result) + "        " + str(type(result)))
## check
result = DictDB.fetchall("SELECT noFail_timestamp,value FROM connections WHERE id = wlan")
print("['noFail_timestamp']: " + str(result["noFail_timestamp"]) + "        " + str(type(result["noFail_timestamp"])))
print("['value']: " + str(result["value"]) + "        " + str(type(result["value"])))

print("")
print("")
print("")



### SOME INTENTIONAL ERRORS ###
print("### SOME INTENTIONAL ERRORS ###")
print("")
