#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

'''
PyDictDatabase.py is licensed under the GNU General Public License v3.0
OPEN SOURCE CODE: https://github.com/DIY-Blub/PyDictDatabase
'''

# The Python Dictionary Database class
class PyDictDatabase():
    def __init__(self,database,settings=dict()):
        self.__settings(settings)
        self.__database(database)
        self.command = ""
        del database,settings

    def fetchone(self,command):
        self.command = command.split(" ")
        if len(self.command) == 8:
            resultat = self.__SELECT(self.command[3],self.command[5],self.command[7],[self.command[1]])
            if resultat:
                return resultat[self.command[1]]
            else:
                return None
        else:
            self.__ERROR(["syntax of",command,"incorrect!","see documentation"])
            return None

    def fetchall(self,command):
        self.command = command.split(" ")
        if len(self.command) == 8:
            return self.__SELECT(self.command[3],self.command[5],self.command[7],self.command[1].split(","))
        else:
            self.__ERROR(["syntax of",command,"incorrect!","see documentation"])
            return None

    def commit(self,command):
        regex = re.findall('(?<=SET\s).*(?=\sWHERE)',command)
        updates = regex[0].split(",")
        regex = re.sub('(?<=SET).*(?=\sWHERE)',"",command)
        self.command = regex.split(" ")
        listofTuples = []
        for update in updates:
            split = update.split("=")
            listofTuples += [(split[0].strip(),split[1].strip())]
        return self.__UPDATE(self.command[1],self.command[len(self.command)-3],self.command[len(self.command)-1],dict(listofTuples))

    def close(self):
        if self.__EXPORT_DATABASE:
            pass        # TODO / will be needed in a later version

    def __SELECT(self,search_in_table,search_in_key,search_value,getDataFromKeys):
        ID = self.__getDBdataID(search_in_table,search_in_key,search_value)
        if ID:
            listofTuples = []
            for key in getDataFromKeys:
                if key in self.__database_data[search_in_table][ID]:
                    listofTuples += [(key,self.__database_data[search_in_table][ID][key])]
                else:
                    self.__ERROR(["key",key,"not found!"])
                    return None
            return dict(listofTuples)
        return None

    def __UPDATE(self,search_in_table,search_in_key,search_value,update):
        ID = self.__getDBdataID(search_in_table,search_in_key,search_value)
        if ID:
            updates = {}
            simulation = True
            # simulation and obtain the key
            for key in update.keys():
                if key in self.__database_data[search_in_table][ID]:
                    if type(update[key]) == type(self.__database_data[search_in_table][ID][key]):
                        updates[key] = update[key]
                    else:
                        convert = self.__tryToConvert(str(update[key]),type(self.__database_data[search_in_table][ID][key]))
                        if convert is not None:
                            updates[key] = convert
                        else:
                            self.__ERROR([key,update[key],"could not converted to target type! target type is:",str(type(self.__database_data[search_in_table][ID][key]).__name__)])
                            simulation = False
                else:
                    self.__ERROR(["key",key,"not found!"])
                    simulation = False
            if simulation:
                # start updates
                for key in updates.keys():
                    self.__database_data[search_in_table][ID][key] = updates[key]
                return 20
            else:
                # simulation failed
                return 40
        return 44


    def __getDBdataID(self,search_in_table,search_in_key,search_value):
        if search_in_table in self.__database_data:
            id_list = []
            for key in self.__database_data[search_in_table].keys():
                if search_value == str(self.__database_data[search_in_table][key][search_in_key]):
                    return key
            self.__ERROR(["value",search_value,"not found!"])
            return None
        self.__ERROR(["table",search_in_table,"not found!"])
        return None

    def __tryToConvert(self,string,target):
        if target == int:
            try:
                int(string)
            except ValueError:
                return None
            else:
                if str(int(string)) == string:
                    return int(string)
                else:
                    return None
        elif target == float:
            try:
                float(string)
            except ValueError:
                return None
            else:
                if str(float(string)) == string:
                    return float(string)
                else:
                    return None
        elif target == bool:
            try:
                bool(string)
            except ValueError:
                return None
            else:
                if str(bool(string)) == string:
                    return bool(string)
                else:
                    return None
        elif target == str:
            try:
                str(string)
            except ValueError:
                return None
            else:
                if str(string) == string:
                    return str(string)
                else:
                    return None
        else:
            return None

    def __database(self,database):
        self.__database_data = database
        del database

    def __settings(self,settings):
        self.__EXPORT_DATABASE = settings.get('EXPORT_DATABASE', False)     # will be needed in a later version
        self.__ERROR_OUTPUT = settings.get('ERROR_OUTPUT', False)
        self.__ERROR_EXIT = settings.get('ERROR_EXIT', False)
        del settings

    def __ERROR(self,array):
        if self.__ERROR_OUTPUT:
            array[1] = "'"+str(array[1])+"'"
            print("PyDictDB-ERROR: " + str(' '.join(array)))
        if self.__ERROR_EXIT:
            exit(1)


if __name__ == '__main__':

    ''' EXAMPLE '''
    example_var = 100

    data = {
            'table1':  {
                        1: {'id':1,'name':"name1",'value':example_var},
                        },
           }

    DictDB = PyDictDatabase(database=data)
    del data

    ## EXAMPLE: fetchone / SELECT one value
    result = DictDB.fetchone("SELECT value FROM table1 WHERE id = {}".format(1))
    print(str(result) + "     " + str(type(result)))

    print("")

    ## EXAMPLE: fetchall / SELECT more than one value
    result = DictDB.fetchall("SELECT name,value FROM table1 WHERE id = {}".format("1"))
    print(str(result) + "     " + str(type(result)))

    print("")

    ## EXAMPLE: commit / UPDATE
    result = DictDB.commit("UPDATE table1 SET name = {},value = {} WHERE id = 1".format("something amazing",42))
    print("status code: " + str(result) + "        " + str(type(result)))


    DictDB.close()      # not yet necessary but useful for the future
