
def vtc_add(a,b):
    size = vtc_dimension(a,b)
    aux = [0]*size
    for i in range(size):
        aux[i] = a[i] + b[i]
    return aux

def vtc_sub(a,b):
    size = vtc_dimension(a,b)
    aux = [0]*size
    for i in range(size):
        aux[i] = a[i] - b[i]
    return aux

def dot(a,b):
    size = vtc_dimension(a,b)
    aux = 0
    for i in range(size):
        aux += a[i]*b[i]
    return aux

def cross(a,b):
    size = vtc_dimension(a,b)
    aux = [0] * size
    aux[0] = a[1]*b[2]-a[2]*b[1]
    aux[1] = a[2]*b[0]-a[0]*b[2]
    aux[2] = a[0]*b[1]-a[1]*b[0]
    return aux
        
def norm(a):
    aux = 0
    for i in range(size):
        aux = a[i]**2
    return aux**(0.5)

def vtc_dimension(a,b):
    assert( True if len(a) == len(b) else "Error Dimensión" )
    return len(a)
