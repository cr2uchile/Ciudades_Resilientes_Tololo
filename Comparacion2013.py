# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:51:56 2021

@author: Sebastián
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os as os
from datetime import date
from datetime import timedelta
from datetime import datetime as dt
import pandas as pd

orig_ebas = os.getcwd()
fn_ebas = orig_ebas+'\\DATA\\'+'EBAS-O3H-2013-2019.csv'
df_ebas = pd.read_csv(fn_ebas)
df_ebas.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
df_orig_ebas = df_ebas

orig_dmc = os.getcwd()
fn_dmc = orig_dmc+'\\DATA\\'+'DMC-O3_RH_15m_dmc-1995-2013.csv'
df_dmc = pd.read_csv(fn_dmc, index_col=0, parse_dates=True)
df_orig_dmc = df_dmc
Fecha_ebas = []
Fecha_ebas_2013 = []
O3_ebas_2013 = []
fechas_dmc = df_orig_dmc.index
Fecha_dmc = []
Fecha_dmc_2013 = []
O3_dmc_2013 = []

for i in range(61344):
    Fecha_ebas.append(dt.strptime(df_orig_ebas['Date'][i],
                                  '%Y-%m-%d %H:%M:%S'))
for i in range(61344):
    if Fecha_ebas[i].year == 2013:
        Fecha_ebas_2013.append(Fecha_ebas[i])
        O3_ebas_2013.append(df_orig_ebas['O3_ppbv'][i].astype(float))

for i in range(len(fechas_dmc)):
    if fechas_dmc[i].year == 2013:
        Fecha_dmc_2013.append(fechas_dmc[i])
        O3_dmc_2013.append(df_orig_dmc['O3_ppbv'][i].astype(float))
for i in range(len(O3_dmc_2013)):
    if O3_dmc_2013[i] < 10:
        O3_dmc_2013[i] = np.nan
    if O3_dmc_2013[i] > 65:
        O3_dmc_2013[i] = np.nan

fig1 = plt.figure(1)
fig1.clf()
ax1 = fig1.add_subplot(211)
ax2 = fig1.add_subplot(212)
ax1.plot(Fecha_dmc_2013, O3_dmc_2013, color='b',
         label='Mediciones equipo Teco')
ax2.plot(Fecha_ebas_2013, O3_ebas_2013, color='r',
         label='Mediciones equipo Picarro')
ax1.set_ylabel('Concentración $O_{3}$ [ppbv]', fontsize=12)
ax2.set_ylabel('Concentración $O_{3}$ [ppbv]', fontsize=12)
fig1.legend()
fig1.show()

fig2 = plt.figure(2)
fig2.clf()
ax3 = fig2.add_subplot(111)
ax3.plot(Fecha_dmc_2013, O3_dmc_2013, label='Mediciones equipo Teco')
ax3.plot(Fecha_ebas_2013, O3_ebas_2013, label='Mediciones equipo Picarro')
ax3.set_ylabel('Concentración $O_{3}$ [ppbv]', fontsize=15)
fig2.legend()
fig2.show()
