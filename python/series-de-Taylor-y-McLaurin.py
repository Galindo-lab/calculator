# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:57:27 2020

@author: mingf
"""
import matplotlib.pyplot as pyplot
from math import *

def tblprint(tabla):
    print("\t     x \t|  f(x) ")
    print("\t-----------------")
    for r in range(len(tabla)):
        print("\t%5.2f \t| %5.2f" % (tabla[r][0],tabla[r][1]))
        
def tblinput(n):
    n = int(n//1)
    if n <= 0:
        n = 0
    tabla = mtxzeros(n,2)
    print("\tcaptura de una tabla ejem 2,5")
    for r in range(n):
        tabla[r][0] = float(input("x%d: " % (r+1)))
        tabla[r][1] = float(input("f(x%d): " % (r+1)))
    tblprint(tabla)
    return tabla

def mtxprint(mtx):
    print()
    for r in range(len(mtx)):
        for c in range(len(mtx[0])):
            print("\t%6.2f" % (mtx[r][c]), end = '')
        print()
        


#regresion lineal
def reglin(tabla,x):
    sx = 0.0
    sy = 0.0
    sx2 =0.0
    sy2 = 0.0
    sxy = 0.0
    n = len(tabla)
    for i in range(n):
        sx = sx + tabla[i][0]
        sy = sy + tabla[i][1]
        sx2 = sx2 + tabla[i][0] **2
        sy2 = sy2 + tabla[i][1] **2
        sxy = sxy + tabla[i][0] * tabla[i][1]
    a1 = (n * sxy - sx * sy) / (n * sx2 - sx * sx)
    a0 = (sy - a1 * sx) / n
    r = (n * sxy - sx * sy) / (sqrt(n * sx2 - sx ** 2) * sqrt(n * sy2 - sy **2))
    print("n = ", n)
    print("suma de x =",sx)
    print("suma de y =",sy)
    print("suma de x^2 =", sx2)
    print("suma de y^2 =", sy2)
    print("suma de xy =", sxy)
    print("a0 =",a0)
    print("a1 =",a1)
    print("y = %f + %f X" %(a0,a1))
    print("y(%f) = %f + %f X=%f" %(x,a0,a1,a0+a1*x))
    tablat = MtxTraspuesta(tabla)
    y = []
    for i in range(n):
        y.append(a0 * exp( a1 * tabla[i][0]))
    pyplot.plot(tablat[0],tablat[1],"*",tablat[0],y)
    pyplot.grid()
    pyplot.title("Regresion lineal y = a0 + a1 x")
    pyplot.xlabel("Eje x")
    pyplot.ylabel("Eje y")
    pyplot.show()

#interpolacion
def interlagrange(tabla, x):
    suma = 0
    tren = mtxren(tabla)
    tcol = mtxcol(tabla)
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

def mtxren(mtx):
    return(len(mtx))

def mtxcol(mtx):
    return(len(mtx[0]))

def mtxzeros(ren,col):
    mtx = []
    for i in range(ren):
        aux = [0]*col
        mtx.append(aux)
    return(mtx)

def mtxcopy(aux):
    mtx = []
    for f in aux:
        mtx.append(f[:])
    return(mtx) 

def MtxIdent(n):
    mtx = mtxzeros(n,n)
    for i in range(n):
        mtx[i][i] = 1
    return mtx 

def MtxTraspuesta(mtx):
    m = mtxren(mtx)
    n = mtxcol(mtx)
    mtxt = mtxzeros(n,m)
    for r in range(n):
        for c in range(m):
            mtxt[r][c] = mtx[c][r]
    return mtxt

def MtxOper(mtxa,mtxb,opt):
    aren = mtxren(mtxa)
    acol = mtxcol(mtxa)
    bren = mtxren(mtxb)
    bcol = mtxcol(mtxb)
    if aren == bren and acol == bcol:
       mtxc = mtxzeros(aren, acol)
       for r in range(aren):
           for c in range(acol):
               if opt == 1:
                   mtxc[r][c] = mtxa[r][c] + mtxb[r][c]
               if opt == 0:
                   mtxc[r][c] = mtxa[r][c] - mtxb[r][c]
       return mtxc

def MtxSuma(mtxa, mtxb):
    return MtxOper(mtxa, mtxb, 1)

def MtxResta(mtxa, mtxb):
    return MtxOper(mtxa, mtxb, 0)

def mtxdet(a):
    aren = mtxren(a)
    acol = mtxcol(a)
    d = 0
    if aren != acol:
        print("\tLa matriz debe ser cuadrada")
    elif aren == 1:
        d = a[0][0]
    else:
        maux = mtxzeros(aren - 1, acol - 1)
        for n in range(aren):
            r = 0
            for k in range(aren):
                if n != k:
                    for c in range(1,acol):
                        maux[r][c-1] = a[k][c]
                    r += 1
            #MtxPrint(maux)        
            d += a[n][0] * (-1) ** n * mtxdet(maux)
    return d 

def MtxVerifica(mtxa, mtxb):
    aren = mtxren(mtxa)
    acol = mtxcol(mtxa)
    bren = mtxren(mtxb)
    bcol = mtxcol(mtxb)
    adet = mtxdet(mtxa)
    opt = 1
    if aren != acol:
        print("La matriz A debe ser cuadrada")
        opt = 0
    if aren != bren:
        print("La matriz A y B tienen diferente numero de renglones")
        opt = 0
    if adet == 0:
        print("La matriz es singular")
        opt = 0
    return opt

def mtxinput(n,m):
    n = int(n//1)
    m = int(m//1)
    if n <= 0:
        n = 0
    if m <= 0:
        m = 0
    mtx = mtxzeros(n,m)
    for r in range(n):
        for c in range(m):
            mtx[r][c] = float(input("MTX[%d][%d]: " % (r+1,c+1)))
    mtxprint(mtx)
    return mtx

def printlagrange(tabla,xi,xu):
    #Valores de eje x o variable independiente
    n =20
    h = (xu-xi)/n
    x=[]
    y=[]
    for i in range(n):
        x.append(xi + h * i)
        y.append(interlagrange(tabla,xi+h*i))
    t1 = MtxTraspuesta(tabla)
    pyplot.plot(t1[0],t1[1],"*", x, y)
    pyplot.grid()
    pyplot.title("Lagrange")
    pyplot.xlabel("Eje x")
    pyplot.ylabel("Eje y")
    pyplot.show()
    
    

def regExp(tabla,x):
    sx = 0.0
    sy = 0.0
    sx2 =0.0
    sy2 = 0.0
    sxy = 0.0
    n = len(tabla)
    for i in range(n):
        sx = sx + tabla[i][0]
        sy = sy + log(tabla[i][1])
        sx2 = sx2 + tabla[i][0] **2
        sy2 = sy2 + log(tabla[i][1]) **2
        sxy = sxy + tabla[i][0] * log(tabla[i][1])
    a1 = (n * sxy - sx * sy) / (n * sx2 - sx * sx)
    a0 = exp((sy - a1 * sx) / n)
    r = (n * sxy - sx * sy) / (sqrt(n * sx2 - sx ** 2) * sqrt(n * sy2 - sy **2))
    for i in range(n):
        y.append(a0 * exp( a1 * tabla[i][0]))
    r = (n * sxy - sx * sy) / (sqrt(n * sx2 - sx **2) * aqrt(n * sy2 - sy ** 2))
    tablat = MtxTraspuesta(tabla)
    pyplot.plot(tablat[0],tablat[1],"*",tablat[0],y)
    pyplot.grid()
    pyplot.title("Regresion exponencial y = a0 * Exp(a1 x)")
    pyplot.xlabel("Eje x")
    pyplot.ylabel("Eje y")
    pyplot.show()
    print("n = ", n)
    print("suma de x =",sx)
    print("suma de y =",sy)
    print("suma de x^2 =", sx2)
    print("suma de y^2 =", sy2)
    print("suma de xy =", sxy)
    print("correlacion =",r)
    print("a0 =",a0)
    print("a1 =",a1)
    print("y = %f + %f x" %(a0,a1))
    print("y = %f +%f * %f = %f" %(a0,a1,x,a0+a1*x))
    
          

    
def MtxGauss(a,b):
    ren = mtxren(b)
    x = mtxzeros(ren,1)
    if MtxVerifica(a,b) == 1:
        for r in range(ren-1):
            for k in range(r+1,ren):
                piv = a[k][r] / a[r][r]
                for c in range(r,ren):
                    a[k][c] = a[k][c] - piv * a[r][c]
                b[k][0] = b[k][0] - piv * b[r][0]
        for i in range(ren-1,-1,-1):
            x[i][0] = b[i][0]
            for k in range(i+1,ren):
                x[i][0] = x[i][0] - a[i][k] * x[k][0]
            x[i][0] = x[i][0] / a[i][i]
    return x

def MtxGaussJordan(a,b):
    ren = mtxren(b)
    col = mtxcol(b)
    x = mtxzeros(ren,col)
    if MtxVerifica(a,b) == 1:
        for r in range(ren):
            div = a[r][r]
            for c in range(r,ren):
                a[r][c] = a[r][c] / div
            for c in range(col):
                b[r][c] = b[r][c] / div
            for k in range(ren):
                if k != r:
                    mult = a[k][r]
                    for c in range(r,ren):
                        a[k][c] = a[k][c] - mult * a[r][c]
                    for c in range(col):
                        b[k][c] = b[k][c] - mult * b[r][c]
        x = mtxcopy(b)
        return x
    
def MtxInver(A):
    a = mtxcopy(A)
    ren = mtxren(A)
    I = MtxIdent(ren)
    return MtxGaussJordan(a,I)
#matriz
def MtxMult(Amtx,Bmtx):
    aren = mtxren(Amtx)
    bren = mtxren(Bmtx)
    acol = mtxcol(Amtx)
    bcol = mtxzeros(aren,bcol)
    if acol != bren:
        print("\n\tNo se puede realizar la multiplicacion")
    else:
        for r in range(aren):
            for c in range(bcol):
                for k in range(bren):
                    Cmtx[r][c] += Amtx[r][k] * Bmtx
    return(Cmtx)


#integracion
def irt_traprecio(a,b,n,f):
    ans = 0
    if n <= 1:
        n = 2 ** 9
    h = (b-a) / n
    suma = 0
    for i in range(1,n):
        x = a + i * h
        suma = suma + f(x)
    print("suma = ",suma)
    ans = (f(a) + 2 * suma + f(b)) * h / 2
    print("La integral es: ", ans)
    return ans
#integrar

def irs_simpson3(a,b,n):
    ans = 0
    if n <= 1:
        n = n ** 9
    n = n + n % 2
    h = (b-a)/n
    print(n," ",h)
    snon = 0
    spar = 0
    for i in range(1,n,2):
        x = a + i * h
        snon += f(x)
        print("f(%f) = %f " % (x, f(x)))
    for i in range(2,n-1,2):
        x = a + i * h
        spar += f(x)
        print("f(%f) = %f" %(x,f(x)))
    print("suma non = %f, suma par = %f" %(snon, spar))
    print("fa:",f(a)," fb:",f(b))
    ans = (f(a) + 4 * snon + 2 * spar + f(b)) * h/3
    print("La integral es: ", ans)
    return ans

def f(x):
    return (1 / sqrt(2 * pi)) * exp(- x**2/2)

def derivadas(x0):
    h = 2 ** -8
    h = .0001
    fp = (f(x0+h)-f(x0-h))/(2*h)
    fp2 = (f(x0+h)-2*f(x0)+f(x0-h))/(h**2)
    fp3 = (f(x0+2*h)-2*f(x0+h)+2*f(x0-h)-f(x0-2*h))/(2*h**3)
    fp4 = (f(x0+2*h)-4*f(x0+h)+6*f(x0)-4*f(x0-h)+f(x0-2*h))/(h**4)
    print("f1(x):",fp)
    print("f2(x):",fp2)
    print("f3(x):",fp3)
    print("f4(x):",fp4)
    
        
    
        