def es_numerico(value: str) -> bool:
    """
    Verificar si un string contine un valor 
    HACK: micropython no tiene la funcion 
          is_numeric.
    numerico
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def captura_list(message="", separator=",") -> list:
    """ 
    Captura una lista de enteros
    """
    foo = input(message + "?\n").split(separator)
    return [int(e) for e in foo if es_numerico(e)]

def d(valor):
    return "%0.4f"%(valor)

def mediana():
    x.sort()
    m = x[N // 2]

    if N % 2 == 0:
        m = (m + x[N // 2 - 1]) / 2

    return m


def frecuencias():
    return {v: x.count(v) for v in x}


def moda(freq):
    mx = max(freq.values())
    return [k for k, v in freq.items() if v == mx]


def desviacion_absoluta():
    media = 1 / N * sum(x)
    return {v: abs(v - media) for v in x}


print("")
print("---------------------")
print("      ANALISIS       ")
print("  ESTADISTICO SIMP.  ")
print("---------------------")
print("")

x = captura_list("lista de terminos")
N = len(x)  # cantidad de elementos


frecuencia = frecuencias()
desviacion = desviacion_absoluta()

# d.m.m desviacion media absoluta
# print(" Valor | Freq. | d.m.a. ")
print("")
for i in x:
    print(i, frecuencia[i], d(desviacion[i]))
print("")

# elementos
print("term.:", N)


media = 1 / N * sum(x)
# media
print("media:", d(media))

# varianza
varianza = 1 / N * sum([(a - media)**2 for a in x])
print(" var.:", d(varianza))

# desviacion estandar
print(" d.s.:", d(varianza**(1 / 2)))

# desviacion media
print(" m.d.:", d(1 / N * sum([abs(v - media) for v in x])))

# modas
print(" moda:", moda(frecuencia))
