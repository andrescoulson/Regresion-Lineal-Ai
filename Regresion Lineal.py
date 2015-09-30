__author__ = 'Andres Bobadilla Fernando Herrera'


import numpy as np
import xlrd
from numpy.linalg import pinv

doc = xlrd.open_workbook("baseball_regression_data_set.xls")

sh = doc.sheet_by_index(0)
#------------inicializando el vector Y de valores realies -----------------
i = 0
y = np.zeros(shape=(27,1))
for i in range(27):
    y[i] = sh.cell_value(1+i,0)
#-------------------------------------------------

#------------------ matriz de valores de entrenamiento 45*.6 = 27 x 5 columnas------------------
x = np.zeros(shape=(27,5))
j=0
k=0
for j in range(27):
    for k in range(5):
        x[j][k] = sh.cell_value(j+1,k+1)

#--------------------------------------------------------------------

#--------------------------calculando la pseudo inversa-------------------

xSeudoinv = pinv(x)
o = np.dot(xSeudoinv,y)

#------------------------------------------------------

#----------------- calculando valot de theta i--------------------

def h(x1,x2,x3,x4,x5):
    prueba = x1*o[0] + x2*o[1] + x3*o[2] + x4*o[3]+x5*o[4]
    resultado = 0
    for i in range(prueba.size):
        resultado += prueba[i]
    return resultado

#--------------------------------------------------

#-------------------- valores de average reales de prueba-----------
z=0
j=28
yReal = np.zeros(shape=(18,1))
for z in range(18):
    yReal[z] = sh.cell_value(j,0)
    j += 1
#-----------------------------------------------------------------

#------------------------------matriz de valores de prueba-----------------
xPrueba = np.zeros(shape=(18,5))
j=0
l=27
k=0
for j in range(18):
    l += 1
    for k in range(5):
        xPrueba[j][k] = sh.cell_value(l,k+1)

#---------------------------------------------------------------

#--------------------calculando los y predecidos por la formula
yPredecido = np.zeros(shape=(18,1))
j=0
k=0
for j in range(18):
    yPredecido[j] = h(xPrueba[j][0],xPrueba[j][1],xPrueba[j][2],xPrueba[j][3],xPrueba[j][4])

#---------------------------------------------

j=0
mape = np.zeros(shape=(18,1))
acumMape = 0
for j in range(18):
    mape [j]= ((abs(yReal[j] - yPredecido[j])/yReal[j])/18)*100
    acumMape += ((abs(yReal[j] - yPredecido[j])/yReal[j])/18)*100

print mape

print ('acumulado Mape ',acumMape)