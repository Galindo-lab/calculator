

# Matriz de 0
def zeros(ren,col):
    mtx = []
    for i in range(ren):
        aux = [0]*col
        mtx.append(aux)
    return(mtx)

def identity(n):
    mtx = zeros(n,n)
    for i in range(n):
        mtx[i][i] = 1
    return mtx

def MtxPrint(mtx):
    for r in range(len(mtx)):
        for c in range(len(mtx[0])):
            print("%5.1f" % (mtx[r][c]), end = ' ')
        print()

# Filas
def rows(mtx):
    return(len(mtx))

# columnas
def columns(mtx):
    return(len(mtx[0]))

# matriz cuadrada
def is_sqrmatrix(mtx):
    return rows(mtx) == columns(mtx)

# copiar matrix
def matcpy(aux):
    mtx = []
    for f in aux:
        mtx.append(f[:])
    return(mtx)

# Determiante
def det(a):
    aren = rows(a)
    acol = columns(a)
    d = 0
    if aren != acol:
        # print("\tLa matriz debe ser cuadrada")
        return None
    elif aren == 1:
        d = a[0][0]
    else:
        maux = zeros(aren - 1, acol - 1)
        for n in range(aren):
            r = 0
            for k in range(aren):
                if n != k:
                    for c in range(1,acol):
                        maux[r][c-1] = a[k][c]
                    r += 1
            d += a[n][0] * (-1) ** n * det(maux)
    return d


def test(name, expected, test):
    result = "ok" if expected == test else "fail"
    print( "%s ... %s"%(name, result) )
    
    
def run_test():
    sqrmtx = zeros(3,3);
    nosqrmtx = zeros(2,5);
    testmtx = [ [651,62,36], [4,65,66], [67,8,79] ]
    
    print("\n Matriz cuadrada ---------")
    test("is_sqrmatrix", False, is_sqrmatrix(nosqrmtx))
    test("is_sqrmatrix", True, is_sqrmatrix(sqrmtx))
    print("\n Determinante ------------")
    test("det", None, det(nosqrmtx))
    test("det", 0, det(sqrmtx))
    test("det", 3098101, det(testmtx))
    
run_test()
