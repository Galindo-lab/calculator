
import math

def table_print(tabla):
    print("\t   x \t|  f(x)    ")
    print("\t---------------")
    for r in range(len(tabla)):
        for c in range(len(tabla[0])):
            print("\t%5.2f \t| %5.2f" % (tabla[r][0],tabla[r][1]))

def mtx_print(mtx):
    print()
    for r in range(len(mtx)):
        for c in  range(len(mtx[0])):
            print("\t%6.2f" % (mtx[r][c]), end=" ")
        print()

def mtx_input(n, m):
    n = int(n//1)
    if n <= 0:
        n = 0
    if m <= 0:
        m = 0
    mtx = mtx_zeros(n, m)
    for r in range(n):
        for c in range(m):
            mtx[r][c] = float(input("mtx[%d][%d]: " % (r+1, c+1)))
    mtx_print(mtx)
    return mtx

def mtx_ren(mtx):
    return len(mtx)

def mtx_col(mtx):
    return len(mtx[0])

def mtx_zeros(ren,col):
    mtx = []
    for i in range(ren):
        aux = [0]*col
        mtx.append(aux)
    return(mtx)

def regresion_lineal(n, mtx, debug=False):
    if mtx_col(mtx) == 2 and mtx_ren(mtx) > 1:
        x = 0
        y = 1
        sumatoria_xy = 0.0
        sumatoria_x = 0.0
        sumatoria_y = 0.0
        sumatoria_x_2 = 0.0
        sumatoria_y_2 = 0.0
        a_1 = 0
        a_0 = 0
        for par in mtx:
            # Σxy
            sumatoria_xy += par[x] * par[y]
            # Σx
            sumatoria_x += par[x]
            # Σy
            sumatoria_y += par[y]
            # Σx²
            sumatoria_x_2 += par[x]**2
            #
            sumatoria_y_2 += par[y]**2
        a_1 = (n * (sumatoria_xy) - (sumatoria_y*sumatoria_x))/(n*(sumatoria_x_2)-sumatoria_x**2)
        a_0 = (sumatoria_y/n) - a_1 * (sumatoria_x/n)
        if debug == True:
            print("\n === debug ===")
            print("  Σxy: ", sumatoria_xy)
            print("  Σx : ", (sumatoria_x) )
            print("  Σy : ", (sumatoria_y) )
            print("  Σx²: ", sumatoria_x_2)
            print("  Σy²: ", sumatoria_y_2,"\n")
        print("%6.2f + %6.2fx" % (a_0, a_1))
        error_estandar = math.sqrt(sumatoria_x_2 - (a_0 * sumatoria_y) - (a_1 * sumatoria_xy) / len(mtx) - 2)
        print("error estandar: ", error_estandar)
        numerador = (a_0 * sumatoria_y) + (a_1 * sumatoria_xy) - (len(mtx) * (sumatoria_y/len(mtx))**2)
        denominnador = sumatoria_y_2 - (sumatoria_y/len(mtx))**2
        coeficiente_determinacion = numerador / denominnador
        print("coeficiente ", coeficiente_determinacion)
    else:
        print("no se puede ejecutar esa operacion")

def InterLagrange(tabla, x):
    suma = 0
    tren = mtx_ren(tabla)
    tcol = mtx_col(tabla)
    if tren <= 1 or tcol != 2:
        print("no se puede realizar la interpolacion")
    else:
        for i in range(tren):
            Li = 1
            for j in range(tren):
                if j != i:
                    Li *= (x - tabla[j][0]) / (tabla[i][0] - tabla[j][0])
            suma += Li * tabla[i][1]
    return suma

def gtx_gaussjordan(a,b):
    ren = mtx_ren(b)
    col = mtx_col(b)
    x = mtx_zeros(ren,col)
