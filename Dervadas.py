

#derivadas 1,2,3,4
def diff(x, f, debug = False, h = 2 ** -8):
    #Precalcular las funciones
    fx = f(x)
    fxph = f(x+h)
    fxmh = f(x-h)
    fxp2h = f(x+2*h)
    fxm2h = f(x-2*h)
    #primerda derivada
    fp1 = (fxph - fxmh) / (2*h)
    #segunda derivada
    fp2 = (fxph - 2*fx + fxmh) / (h**2)
    #tercera derivada
    fp3 = (fxp2h - 2*fxph + 2*fxmh - fxm2h) / (2*h**3)
    #mostrar resultados
    fp4 = (fxp2h - 4*fxph + 6*fx - 4*fxmh + fxm2h) / (h**4)
    if debug:
        print("   x | %.4f" % (x))
        print(" f(x)| %.4f" % (fx))
        print("-----+-------------")
    print(" 1 | %.4f" % (fp1))
    print(" 2 | %.4f" % (fp2))
    print(" 3 | %.4f" % (fp3))
    print(" 4 | %.4f" % (fp4))
