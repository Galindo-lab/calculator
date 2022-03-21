
# Warning: Codigo horrible

def bin(number,digits):
    # mejor formato de binario
    return "{0:0{1}b}".format(number,digits)

def gray(n):
    # Source: https://www.w3schools.com/python/ref_string_format.asp
    # genera una lista con los numeros de gray de 'n' bits 
    return [bin(i^(i>>1),n) for i in range(0,1<<n)]

def binary(n):
    # genera una lista con los numeros binarios de 'n' bits
    return [bin(i,n) for i in range(0,1<<n)]

def generate_values(variables, value):
    # divide el strig en cantidad de variables
    keys = variables.split(",")
    # mismas claves pero con una 'n' al inicio
    neg_keys = [ 'n' + x for x in keys ]
    # extrae el valor individual de cada bit
    values = [ bool(int(x)) for x in value ]
    # valores negados
    neg_values = [ not x for x in values ]
    # retorna un diccionario
    return dict(zip(keys+neg_keys+["n"],values+neg_values+[lambda x: not x]))

def eval_function(function, values):
    return eval( "int(bool(" + function.replace("-","n") + "))", values )

def tabla_verdad(variables, function, orden):
    for v in orden(len(variables.split(","))):
        print(v, eval_function(function, generate_values(variables,v)))

print("")
print("1. gray / 2.binario")
print("")
ordenado = int(input(" Ordenado: "))
variables =    input("Variables? ")
funcion =      input("  Funcion? ")
print("")

if(ordenado==1):
    tabla_verdad(variables, funcion, gray)
else:
    tabla_verdad(variables, funcion, binary)
