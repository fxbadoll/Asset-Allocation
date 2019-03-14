# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:21:01 2019

@author: fuxuan
"""

from WindPy import w
import pandas as pd
import datetime
import matplotlib.pyplot as plt

w.start();

datestart = "2005-1-1"
dateend = "2019-3-14"

'中国国内宏观数据'
'1.GDP数据包括不变价的当季值和当季同比'

'GDP不变价当季值'
gdpabs = w.edb("M5567889", datestart, dateend,"Fill=Previous")
'GDP不变价第一产业当季值'
gdp1stabs = w.edb("M5567890", datestart, dateend,"Fill=Previous")
'GDP不变价第二产业当季值'
gdp2ndabs = w.edb("M5567891", datestart, dateend,"Fill=Previous")
'GDP不变价第三产业当季值'
gdp3rdabs = w.edb("M5567892", datestart, dateend,"Fill=Previous")
'GDP不变价当季同比'
gdptb = w.edb("M0039354", datestart, dateend,"Fill=Previous")
'GDP不变价第一产业当季同比'
gdp1tb = w.edb("M5567901", datestart, dateend,"Fill=Previous")
'GDP不变价第二产业当季同比'
gdp2ndtb = w.edb("M5567902", datestart, dateend,"Fill=Previous")
'GDP不变价第三产业当季同比'
gdp3rdtb = w.edb("M5567903", datestart, dateend,"Fill=Previous")
'GDP不变价金融产业当季同比'
gdpfintb = w.edb("M5567910", datestart, dateend,"Fill=Previous")
'GDP不变价房地产业当季同比'
gdpesttb = w.edb("M5567911", datestart, dateend,"Fill=Previous")


def wdtopd(wsd_data):
    fm=pd.DataFrame(wsd_data.Data,index=wsd_data.Fields,columns=wsd_data.Times)
    return fm

gdpabs = wdtopd(gdpabs).T
gdp1stabs = wdtopd(gdp1stabs).T
gdp2ndabs = wdtopd(gdp2ndabs).T
gdp3rdabs = wdtopd(gdp3rdabs).T


'GDP 第1、2、3产业占比'
gdp1stperc = gdp1stabs/gdpabs
gdp2ndperc = gdp2ndabs/gdpabs
gdp3rdperc = gdp3rdabs/gdpabs

gdpperclist = pd.concat([gdp1stperc,gdp2ndperc,gdp3rdperc],axis = 1,join_axes = [gdptbdf.index])
gdpperclist.columns = ['gdp1stperc','gdp2ndperc','gdp3rdperc']
gdpperclist.plot()

gdptbdf = wdtopd(gdptb).T
gdp1stbdf = wdtopd(gdp1tb).T
gdp2ndtbdf = wdtopd(gdp2ndtb).T
gdp3rdtbdf = wdtopd(gdp3rdtb).T


gdptblist = pd.concat([gdptbdf,gdp1stbdf,gdp2ndtbdf,gdp3rdtbdf],axis = 1,join_axes = [gdptbdf.index])
gdptblist.columns = ['gdptb','gdp1sttb','gdp2ndtb','gdp3rdtb']
gdptblist.plot()

