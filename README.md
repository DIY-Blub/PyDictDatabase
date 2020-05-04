# PyDictDatabase [![Build Status](https://travis-ci.org/DIY-Blub/PyDictDatabase.svg?branch=master)](https://travis-ci.org/github/DIY-Blub/PyDictDatabase)

Python Dictionary based database for tiny databases.

**useful for**

* matrix or very small database

* static database structure (more or less)

**useless for**

* collecting data

* growing databases

**comment:**

I am using this type of database in two of my projects:

1. for my plant watering system to collect my last status data

2. for my SmartPi as manageable & clear structure for matrixes

> The SmartPi also uses a MySQL database to collect data. As there are many read/write cycles for some attributes. It makes more sense to leave them in memory which is also gentler on the memory card (RasPi).




## features

* use SELECT and UPDATE like MySQL

* existing data types are retained

* SELECT methods: fetchone & fetchall

* UPDATE methods: commit


## usage example

You have to save the file PyDictDatabase.py in your project directory.

### setup database

```
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

DictDB = PyDictDatabase(database=data)
```
### use options

```
DictDB = PyDictDatabase(database=data,settings={"ERROR_OUTPUT":True})
```

**options:**
* "EXPORT_DATABASE":True for new feature, available soon (default: False)
* "ERROR_OUTPUT":True for error output, DEBUG-MODE (default: False)
* "ERROR_EXIT":True to stop script with exit(1), if an error occurs with select/update (default: False)

### SELECT Data (short instruction)

```
result = DictDB.fetchone("SELECT status FROM table2 WHERE id = name1")
result = DictDB.fetchall("SELECT id,status FROM table2 WHERE id = name1")
```

### UPDATE Data (short instruction)

```
result = DictDB.commit("UPDATE table2 SET status = False WHERE id = name1")
```

## rules

* dict must start with 1, instead of 0

* use the same keys per table (so it is also common with MySQL)


## return codes

### fetchone / fetchall (SELECT)

**None** - no entry found

### commit (UPDATE)

**20 SUCCESS** - nothing amiss

**40 ERROR** - for further information activate ERROR_OUTPUT

**44 NOT FOUND** - name of the table/key not found


## SYNTAX

**SYNTAX fetchone:**
```
SELECT `KEY` FROM `TABLE` WHERE `KEY` = `VALUE`
```

**SYNTAX fetchall:**
```
SELECT `KEY` FROM `TABLE` WHERE `KEY` = `VALUE`

SELECT `KEY`,`KEY`,`KEY` FROM `TABLE` WHERE `KEY` = `VALUE`
```

**SYNTAX commit:**
```
UPDATE `TABLE` SET `KEY` = `VALUE` WHERE `KEY` = `VALUE`

UPDATE `TABLE` SET `KEY` = `VALUE`,`KEY` = `VALUE`,`KEY` = `VALUE` WHERE `KEY` = `VALUE`
```


## in progress

* option to export the last status data to a file and reload it during initialization (method close)

* implement a findall method for chaining

* INSERT option to add a new entry

## Changelog

### v1.0.0 (04.05.2020)

* initial release
