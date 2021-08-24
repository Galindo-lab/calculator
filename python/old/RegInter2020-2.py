#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:02:18 2020

@author: Administrator
"""

from Matrices2020-2 import * 
from matplotlib import pyplot

def TblPrint(tabla):
    print("\t     x \t|  f(x)  ")
    print("\t----------------")
    for r in range(len(tabla)):
        print("\t%5.2f \t| %5.2f" % (tabla[r][0],tabla[r][1]))


def TblInput(n):
    n = int(n//1)
    if n <= 0:
        n = 0
    tabla = MtxZeros(n,2)
    print("\tCaptura de una tabla ejem 2, 5")
    for r in range(n):
            tabla[r][0] = float(input("x%d: " % (r+1)))
            tabla[r][1] = float(input("f(x%d): " % (r+1)))
    TblPrint(tabla)        
    return tabla

def TblInterLineal(tabla,x):
    ans = 0
    tren = mtx_ren(tabla)
    tcol = mtx_col(tabla)
    if (tcol != 2 or tren != 2):
        print("No se puede realizar la interpolacion lineal")
    else:
        m = (tabla[1][1] - tabla[0][1]) / (tabla[1][0] - tabla[0][0])
        ans = tabla[0][1] + m * (x - tabla[0][0])
        print("f(x) = %f + %f  (x - %f) " %(tabla[0][1], m, tabla[0][0]))
    return ans

def mtx_gauss(mtxa, mtxb):
    a = mtx_copy(mtxa)
    b = mtx_copy(mtxb)
    ren = mtx_ren(a)
    x = mtx_zeros(ren,1)
    if mtx_verifica(a,b,) == 1:
        for r in range(ren - 1):
            for k in range(r + 1, ren):
                piv = a[k][r] / a[r][r]
                for c in range(r, ren):
                    a[k][c] = a[k][c] - piv * a[r][c]
                b[k][0] -= piv * b[r][0]
        mtx_print(a)
        mtx_print(b)
        for i in range(ren - 1, -1, -1):
            x[i][0] = b[i][0]
            for k in range(i + 1, ren):
                x[i][0] -= a[i][k] * x[k][0]
            x[i][0] /= a[i][i]
    mtx_print(x)
    return x;

def mtx_gaussjordan(mtxa,mtxb):]
    a = mtx_copy(mtxa)
    b = mtx_copy(mtxb)
    ren = mtxRen(a)
    col = mtxCol(b)
    x = mtx_zeros(ren,1)
    if mtx_verifica(a,b,) == 1:
        for i in range(ren):
            dov = a[r][r]
            for c in range(r,ren):
                a[r][c] /= div
            for c in range(col):
                b[r][c] /= div
            for k in range(ren):
                if k != r:
                    mult = a[k][r]
                    for c in range(r,ren):
                        a[k][c] -= mult * a[r][c]
                    for c in range(col):
                        b[k][c] -= mult * b[r][c]
        mtx_print(a)
        mtx_print(b)
        x = mtx_copy(b)
    return(x);

def interlagrange(tabla, x):
    suma = 0
    tren = mtx_ren(tabla)
    tcol = mtx_col(tabla)
    if tren <= 1 or tcol != 2:
        print("No se puede realizar la interpolacion")
    else:
        for i in range(tren):
            Li = 1
            for j in range(tren):
                if j !=i:
                    if tabla[i][0] != tabla[j][0]:
                        Li = Li * (x-tabla[j][0]) / (tabla[i][0] - tabla[j][0])
                    else:
                        print("No se puede realizar la interpolacion, funcion Biyectiva")
                        suma = 0
                        break
            suma = suma + Li * tabla[i][1]
    return suma
