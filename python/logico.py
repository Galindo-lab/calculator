
variables = "a,b,c"
funcion = "-b * (-a + c)"
  
class Logic:
    def __init__(self, estatus: int):
        self.estatus = bool(estatus)

    def __add__(self, x):
        return Logic(self.estatus or x.estatus)

    def __sub__(self, x):
        return Logic( not(self.estatus) and x.estatus )

    def __neg__(self):
        return Logic( not(self.estatus) )

    def __mul__(self, x):
        return Logic( self.estatus and x.estatus )

    def __str__(self):
        return str(int(self.estatus))
        
        
def exp(elem,var,fun):
    keys = var.split(",")
    values = [ Logic(int(x)) for x in elem ]
    dic = dict(zip(keys, values))
    return eval("str("+fun+")",dic)


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

def geval( n, f ):
    for e in f(n):
        print(e,exp(e,variables,funcion))
