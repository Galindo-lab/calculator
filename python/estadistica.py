

#arreglo
datos = [18,20,20,22,20,20,22,22,22]


def media(datos):
    media = 0
    for dato in datos:
        media += dato
    media /= len(datos)
    return media

def mediana(datos):
    datos2 = datos.copy()
    datos2.sort()
    n = len(datos2)
    mediana = 0
    if n % 2 == 1:
        mediana = datos2[n//2]
    else:
        mediana = (datos2[n//2 -1] + datos2[n//2])/2
    return mediana

def varianza(datos):
    media_ = media(datos)
    n = len(datos)
    varianza = 0
    sumatoria = 0
    for dato in datos:
        sumatoria += float((dato - media_)**2)
    varianza = sumatoria /n
    return varianza

def desviacion_estandar(datos):
    return varianza**(1/2)

def rango(datos):
    datos_ordenados = datos.copy()
    datos_ordenados.sort()
    print("rango ",datos_ordenados[0]," hasta ",datos_ordenados[-1])

def moda(l):
    repeticiones = 0
    for i in l:
        apariciones = l.count(i)
        if apariciones > repeticiones:                                                       
            repeticiones = apariciones
    modas = []
    for i in l:                                                                              
        apariciones = l.count(i)
        if apariciones == repeticiones and i not in modas:
            modas.append(i)
    print("moda:", modas)
