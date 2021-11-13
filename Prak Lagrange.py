# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 10:11:55 2021

@author: faris
"""
#Interpolasi Lagrage
import numpy as np
#Membaca Jumlah titik data
n = int(input('Masukan jumlah titik data: '))

#Membuat array ukuran n x n dan inisiasi
x = np.zeros((n))
y = np.zeros((n))

#Membaca titik data
print('Masukan data x dan y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))
    
#Membaca Interpolasi  titik
xp = float(input('Masukan x yang di inginkan: '))

#Inisiasi interpolasi titik
yp = 0

#Implementasi Interpolasi Lagrange
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]
    
#Displaying Output
print('Nilai Interpolasi untuk %.3f adalah %.3f.' % (xp, yp))