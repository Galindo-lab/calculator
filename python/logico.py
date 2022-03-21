
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

def positive_values(variables, values): # string a diccionario
    keys = [ char for char in variables ]
    values = [ bool(int(char)) for char in values ]
    return dict(zip(keys, values))

def negative_values(variables, values): # string a diccionario negado
    keys = [ 'n'+char for char in variables ]
    values = [ not bool(int(char)) for char in values ]
    return dict(zip(keys, values))

def function_values():
    return { "n": lambda x: not x }

def generate_values(variables, values): # unir los 3 diccionarios
    return { **positive_values(variables, values),
             **negative_values(variables, values),
             **function_values() }

def eval_function(function, values):
    return str(eval( "int(bool(" + function.replace("-","n") + "))", values ))

def tabla_verdad(variables, function, orden):
    for v in orden(len(variables)):
        print(v, "|", eval_function(function, generate_values(variables,v)))

def x():
    print("")
    print("Tablas de verdad")
    print("")
    print("1.gray / 2.binario")
    print("")
    print("Ordenado?")
    ordenado = int(input())
    print("Variables?")
    variables = input()
    print("Funcion?")
    funcion = input()
    print("")
    print(variables,"| o")
    print("-" * len(variables) + "-+---" )
    if(ordenado==1):
        tabla_verdad(variables, funcion, gray)
    else:
        tabla_verdad(variables, funcion, binary)

x()
