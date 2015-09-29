__author__ = 'JuanyAndres'


import numpy as np
import xlrd
from numpy.linalg import pinv

doc = xlrd.open_workbook("mlr07.xls")

sh = doc.sheet_by_index(0)

i = 0
y = np.zeros(shape=(31,1))
for i in range(31):
    y[i] = sh.cell_value(1+i,0)

x = np.zeros(shape=(31,4))
j=0
k=0
for j in range(31):
    for k in range(4):
        x[j][k] = sh.cell_value(j+1,k+1)

xSeudoinv = pinv(x)
o = np.dot(xSeudoinv,y)


def h(x1,x2,x3,x4):
    prueba = x1*o[0] + x2*o[1] + x3*o[2] + x4*o[3]
    resultado = 0
    for i in range(prueba.size):
        resultado += prueba[i]
    return resultado

z=0
j=32
yReal = np.zeros(shape=(22,1))
for z in range(22):
    yReal[z] = sh.cell_value(j,0)
    j += 1


xPrueba = np.zeros(shape=(22,4))
j=0
l=31
k=0
for j in range(22):
    l += 1
    for k in range(4):
        xPrueba[j][k] = sh.cell_value(l,k+1)

yPredecido = np.zeros(shape=(22,1))
j=0
k=0
for j in range(22):
    yPredecido[j] = h(xPrueba[j][0],xPrueba[j][1],xPrueba[j][2],xPrueba[j][3])

j=0
mape = 0
for j in range(22):
    mape += ((abs(yReal[j] - yPredecido[j])/yReal[j])/22)*100

print mape