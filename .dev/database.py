#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = {
        # id = address of Bus I2C
        'dataI2C':  {
                    1: {'id':"0x23",'name':"soil moisture sensor 1",'group':"SMS",'timestamp':55,'value':45},
                    2: {'id':"0x24",'name':"soil moisture sensor 2",'group':"SMS",'timestamp':66,'value':60},
                    3: {'id':"0x25",'name':"soil moisture sensor 3",'group':"SMS",'timestamp':77,'value':30},
                    4: {'id':"0x26",'name':"soil moisture sensor 4",'group':"SMS",'timestamp':22,'value':50},
                    5: {'id':"0x30",'name':"room temperature sensor 1",'group':"RTS",'timestamp':0,'value':0.0},
                    },
        # id = channel of Analog/Digital-Converter
        'dataADC':  {
                    1: {'id':0,'name':"light dependent resistor 1",'group':"LDR",'timestamp':0,'value':0},
                    2: {'id':1,'name':"light dependent resistor 2",'group':"LDR",'timestamp':0,'value':0},
                    3: {'id':2,'name':"water sensor 1",'group':"WS",'timestamp':0,'value':0},
                    4: {'id':3,'name':"water sensor 2",'group':"WS",'timestamp':0,'value':0},
                    5: {'id':4,'name':"rain sensor 1",'group':"RS",'timestamp':0,'value':0},
                    },
        # id = 
        'connections':  {
                    1: {'id':"wlan",'noFail_timestamp':0,'value':False},
                    2: {'id':"mqtt",'noFail_timestamp':0,'value':False},
                        },
       }
