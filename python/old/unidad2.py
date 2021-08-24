

import math
#import numpy as np

def f(x):
    #return (x**2 + 1)**(1/2) + math.tan(math.radians(x))
    #return exp(-x)-x
    #return x**2 + 7 * x + 10
    #return x**3 + 6*(x**2) - x - 30
    #return exp(-x**3) - 2*x + 1
    return 4-x**2-x**3


def biseccion(xi,xu,f,n = 100):
    xr = 0
    xrant = 0
    ea  = 50
    es = Scarb(n)
    i = 0
    if (f(xi) * f(xu)) > 0:
        print("No existe raíz en el intervalo ",xi," ",xu)
        i+=1
    else:
        while ea > es:
            #print(i)
            print(i,xi,xu,xr,f(xi),f(xu),f(xr),ea)
            i += 1
            xrant = xr
            xr = (xi + xu)/2
            if f(xi) * f(xr) < 0:
                xu = xr
            if f(xu) * f(xr) < 0:
                xi = xr
            ea = ErrorA(xr, xrant)
    return xr


def falsa_pos(xi,xu,f,n = 100):
    xr = 0
    xrant = 0
    ea  = 50
    es = Scarb(n)
    i = 0
    if (f(xi) * f(xu)) > 0:
        i +=1
    else:
        while ea > es:
            #print(i)
            #print(i,xi,xu,xr,f(xi),f(xu),f(xr),ea)
            print(xi, xu, xr, f(xi),f(xu),f(xr),ea)
            i += 1
            xrant = xr
            xr = xu - (f(xu) * (xi - xu))/(f(xi) - f(xu))
            if f(xi) * f(xr) < 0:
                xu = xr
            if f(xu) * f(xr) < 0:
                xi = xr
            ea = ErrorA(xr, xrant)
    #print(i)
    return xr


def multiples_raices(xi,xu,m_flag):
    raices = []
    raiz = 0
    for i in range(xi,xu+1):
        #print(i,i+1)
        if m_flag == 1:
            raiz = falsa_pos(i,i+1)
        if m_flag == 2:
            print("metodo 2")
            raiz = biseccion(i,i+1)
            print(raiz)
            print("-----------------------")
        if f(raiz) == 0.0:
            raices.append(raiz)
    return raices


def MetodoIntervalo(xi,xu,n,opt,Fun):
    xr = 0
    ea = 50
    es = Scarb(n)
    n = 0
    if Fun(xi) * Fun(xu) > 0:
        #print("No existe raiz en el intervalo")
        dummi = 0
    else:
        while ea > es:
            xrant = xr
            if opt == 0:
                #biseccion
                xr = (xi+xu) / 2
            else:
                #falsa posicion
                xr = xu -Fun(xu)*(xi-xu) / (Fun(xi) - Fun(xu))
            if Fun(xi) * Fun(xr) < 0:
                xu = xr
            if Fun(xu) * Fun(xr) < 0:
                xi = xr
            ea = ErrorA(xr,xrant)
            n = n+1
    #print("n = ",n,"Interaciones y la raiz es:", xr)
    return xr


# def multiples_raices2(xi,xu,f,n=100):
#     raices = []
#     raiz = 0
#     for i in range(xi,xu+1):
#         raiz_biseccion = float(MetodoIntervalo(i,i+1,n,0,f))
#         raiz_posicion = float(MetodoIntervalo(i,i+1,n,1,f))
#         if ErrorA(f(raiz_biseccion),eps()) == 0.0 or f(raiz_biseccion) == 0:
#             print("biseccion")
#             raices.append(raiz_biseccion)
#         if ErrorA(abs(f(raiz_posicion)),eps()) == 0.0 or f(raiz_posicion) == 0:
#             print("falsa posiscion")
#             raices.append(raiz_posicion)
#     return raices


def multiples_raices2(xi,xu,f,n=100):
    raices = []
    raiz = 0
    for i in range(xi,xu+1):
        raiz_posicion = MetodoIntervalo(i,i+1,n,1,f)
        if ErrorA(abs(f(raiz_posicion)),eps()) == 0.0 or f(raiz_posicion) == 0:
            raices.append(raiz_posicion)
    if len(raices) == 0:
        print("biseccion")
        raiz_biseccion = MetodoIntervalo(xi,xu,n,0,f)
        raices.append(raiz_biseccion)
    else:
        print("falsa posicion")
    return list(set(raices))

def newton(xi,f,fd,n = 5):
    x0 = xi
    x1 = 0
    ea = 50
    es = Scarb(n)
    i = 0
    while ea > es:
        print(i,xi,x1,x0,f(x0),fd(x0),ea)
        i += 1
        x1 = x0 - f(x0) / fd(x0)
        ea = ErrorA(x1, x0)
        x0 = x1
    print(i,xi,x1,x0,f(x1),fd(x0),ea)
    return x0

def newton_multiple(xi,f,fd,fdd,n = 100):
    x0 = xi
    x1 = 0
    ea = 50
    es = Scarb(n)
    i = 0
    while ea > es:
        print(i,xi,x1,x0,f(x1),fd(x0),fdd(x0),ea)
        i += 1
        x1 = x0 - (f(x0) * fd(x0))/( fd(x0)**2 - f(x0)*fdd(x0) )
        ea = ErrorA(x1, x0)
        x0 = x1
    print(i,xi,x1,x0,f(x1),fd(x0),ea)
    return x0

def pol_eval(a,x):
    ans = 0.0
    agrado = len(a)-1
    if agrado >= 0:
        for i in range(agrado, -1, -1):
            ans = ans * x + a[i]
    return ans

def pol_deriv(a):
    b = []
    agrado = len(a)
    if agrado <= 1:
        b.append(0)
    else:
        for i in range(0,agrado-1):
            b.append(a[i + 1] * (i+1))
    return b

def pol_div_sint(a,root):
    b = []
    agrado = len(a)
    if agrado <= 1:
        print("no se puede realiar la divicion sintetica")
        b.append(0)
    else:
        for n in range(agrado - 1):
            b.append(0)
        bgrado = agrado - 1
        b[bgrado-1] = a[agrado-1]
        for i in range(bgrado-1, 0, -1):
            b[i - 1] = a[i] + root * b[i]
        residuo = a[0]+root*b[0]
        #print("El residuo es = %f"%(residuo))
    return(b)

def pol_newton_r(a,x0,n = 100):
    ad = []
    ad = pol_deriv(a)
    ea = 50
    es = Scarb(n)
    while ea > es:
        x1= x0 - pol_eval(a,x0) / pol_eval(ad,x0)
        ea = ErrorA(x1,x0)
        x0 = x1
    return x1

def pol_birge_vietta(a):
    x0 = 0
    while len(a) > 1:
        x0 = pol_newton_r(a, x0)
        a = pol_div_sint(a, x0)
        print(x0)

def pol_print(a):
    n = len(a)
    if n < 0:
        print("no es un polinomio")
    else:
        print("%5.3f "%(a[0]),end = " ")
        for i in range(1,n):
            if i == 1:
                if a[i] >= 0:
                    print("+ %5.3f X "%(a[i]),end = " ")
                else:
                    print("- %5.3f X "%(-a[i]),end  =" ")
            else:
                if a[i] >= 0:
                    print("+ %5.3f X^%d"%(a[i], i), end = " ")
                else:
                    print("- %5.3f X^%d"%(-a[i], i), end = " ")
        print("")

def horner(coeficientes,x):
    #coeficientes es un array
    valorX=x or 0;
    resultado=0;
    for i in range(0,len(coeficientes)):
        resultado = resultado * valorX + coeficientes[i]
    return resultado

def derivada(coeficientes,x):
    valorX = x or 0
    resultado = 0
    coeficientes.pop()
    for i in range(0, len(coeficientes)):
        exponente = len(coeficientes) - i
        resultado += (coeficientes[i] * exponente) * x**(exponente - 1)
        print((coeficientes[i] * exponente),x,(exponente - 1))
    return resultado

def exp(x):
    return 2.718281828459045 ** (x)

def abs(x):
    if x < 0:
        x = -x;
    return x;

def eps():
    eps = 1.0
    while 1-eps != 1 :
        eps /= 2
    eps *= 2
    return eps

def Scarb(n):
    if n <= 0:
        n = 5
        print("n debe der positiva, 5 default")
    n = n // 1
    return 0.5 * 10 ** (2 - n)

def ErrorA(vact, vant):
    ea = abs(vact - vant)
    if vact != 0:
        if ea < eps():
            ea = 0;
        else:
            ea = abs(ea/vact)*100
    return ea

if __name__ == "__main__":
    #a = [-7.5, 30.25, -30.75, 0, 1]
    #print(pol_print(a))
    #print(pol_birge_vietta(a))
    print(newton(0,lambda x: math.sin(x)-x+1, lambda x: math.cos(x)-1))
