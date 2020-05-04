#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyDictDatabase import *
from database import data

DictDB = PyDictDatabase(database=data,settings={"ERROR_OUTPUT":True})
del data

### SELECT ###
print("### SELECT ###")
print("")

# EXAMPLE: fetchone / SELECT a string
print('fetchone("SELECT name FROM dataI2C WHERE id = {}".format("0x23"))')
result = DictDB.fetchone("SELECT name FROM dataI2C WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))

print("")
print("")

# EXAMPLE: fetchone / SELECT a integer
print('fetchone("SELECT value FROM dataI2C WHERE id = {}".format("0x23"))')
result = DictDB.fetchone("SELECT value FROM dataI2C WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))

print("")
print("")

# EXAMPLE: fetchone / SELECT a boolean
print('fetchone("SELECT value FROM connections WHERE id = {}".format("wlan"))')
result = DictDB.fetchone("SELECT value FROM connections WHERE id = {}".format("wlan"))
print(str(result) + "          " + str(type(result)))

print("")
print("")

# EXAMPLE: fetchall / SELECT one value
print('fetchall("SELECT timestamp FROM dataI2C WHERE id = {}".format("0x23"))')
result = DictDB.fetchall("SELECT timestamp FROM dataI2C WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))
print("['timestamp']: " + str(result["timestamp"]) + "     " + str(type(result["timestamp"])))

print("")
print("")

# EXAMPLE: fetchall / SELECT more then one value
print('fetchall("SELECT group,timestamp,value FROM dataI2C WHERE id = {}".format("0x23"))')
result = DictDB.fetchall("SELECT group,timestamp,value FROM dataI2C WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))
print("['group']: " + str(result["group"]) + "        " + str(type(result["group"])))
print("['timestamp']: " + str(result["timestamp"]) + "     " + str(type(result["timestamp"])))
print("['value']: " + str(result["value"]) + "         " + str(type(result["value"])))

print("")
print("")
print("")



### SOME INTENTIONAL ERRORS ###
print("### SOME INTENTIONAL ERRORS ###")
print("")

# EXAMPLE: SELECT key that don't exist
print("# EXAMPLE: SELECT key that don't exist")
result = DictDB.fetchone("SELECT dontexist FROM dataI2C WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))
result = DictDB.fetchall("SELECT dontexist,value FROM dataI2C WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))

print("")

# EXAMPLE: SELECT table that don't exist
print("# EXAMPLE: SELECT table that don't exist")
result = DictDB.fetchone("SELECT timestamp FROM dontexist WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))
result = DictDB.fetchall("SELECT timestamp,value FROM dontexist WHERE id = {}".format("0x23"))
print(str(result) + "          " + str(type(result)))

print("")

# EXAMPLE: use fetchone instead of fetchall
print("# EXAMPLE: use fetchone instead of fetchall")
result = DictDB.fetchone("SELECT timestamp,value FROM connections WHERE id = {}".format("wlan"))
print(str(result) + "          " + str(type(result)))
