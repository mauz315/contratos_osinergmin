#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from selenium import webdriver
import csv
# import unidecode
import urllib
from datetime import datetime


def date_fix(excel_date):
    dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date - 2)
    return dt.timetuple()


# Convirtiendo info en listas de listas
with open('datos.csv') as x:
    data = list([list(line) for line in csv.reader(x)])

url = "http://www.osinergmin.gob.pe/empresas/electricidad/DocumentosContratosDSE/"

# Codigo de prueba
# direc = "SDF_ACE_2017131_0_1463.pdf"
# urllib.urlretrieve(url+direc, "prueba.pdf")

count = 1
for i in data[1:]:
    # Eliminando acentos y corrigiendo fechas
    i[0] = date_fix(int(i[0]))

    if i[2][0] == " ":
        i[2] = i[2][1:]

    if i[3][0] == " ":
        i[3] = i[3][1:]

    # for j in range(1, 3):
    #    i[j] = unidecode.unidecode(j)
    # Descargando contratosr
    file_name = (str(count), i[2][:3], i[1][:3], str(i[0].tm_year), str(i[0].tm_mon), '.pdf')
    urllib.urlretrieve(url+i[3], '_'.join(file_name))
    count += 1
