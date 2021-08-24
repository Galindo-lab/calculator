
def MtxZeros(ren,col):
    mtx = []
    for i in range(ren):
        aux = [0]*col
        mtx.append(aux)
    return(mtx) 

def MtxDet(a):
    aren = MtxRen(a)
    acol = MtxCol(a)
    d = 0
    if aren != acol:
        print("\tLa matriz debe ser cuadrada")
    elif aren == 1:
        d = a[0][0]
    else:
        maux = MtxZeros(aren - 1, acol - 1)
        for n in range(aren):
            r = 0
            for k in range(aren):
                if n != k:
                    for c in range(1,acol):
                        maux[r][c-1] = a[k][c]
                    r += 1
            #MtxPrint(maux)
            d += a[n][0] * (-1) ** n * MtxDet(maux)
    return d

def MtxRen(mtx):
    return(len(mtx))

def MtxCol(mtx):
    return(len(mtx[0]))

def MtxVerifica(mtxa, mtxb):
    aren = MtxRen(mtxa)
    acol = MtxCol(mtxa)
    bren = MtxRen(mtxb)
    bcol = MtxCol(mtxb)
    adet = MtxDet(mtxa)
    opt = 1
    if aren != acol:
        print("La matriz A debe ser cuadrada")
        opt = 0
    if aren != bren:
        print("La matriz A y B tienen diferente numero de renglones")
        opt = 0
    if adet == 0:
        print("La matriz es singular")
        opt = 0
    return opt

def irt_traprecio(a,b,n,f):
    ans = 0
    if n <= 1:
        n = 2 ** 9
    h = (b-a) / n
    suma = 0
    for i in range(1,n):
        x = a + i * h
        suma = suma + f(x)
    print("suma = ",suma)
    ans = (f(a) + 2 * suma + f(b)) * h / 2
    print("La integral es: ", ans)
    return ans

def irs_simpson3(a,b,n,f):
    ans = 0
    if n <= 1:
        n = n ** 9
    n = n + n % 2
    h = (b-a)/n
    print(n," ",h)
    snon = 0
    spar = 0
    for i in range(1,n,2):
        x = a + i * h
        snon += f(x)
        print("f(%f) = %f " % (x, f(x)))
    for i in range(2,n-1,2):
        x = a + i * h
        spar += f(x)
        print("f(%f) = %f" %(x,f(x)))
    print("suma non = %f, suma par = %f" %(snon, spar))
    print("fa:",f(a)," fb:",f(b))
    ans = (f(a) + 4 * snon + 2 * spar + f(b)) * h/3
    print("La integral es: ", ans)
    return ans

def derivadas(x0,f):
    h = 2 ** -8
    h = .0001
    fp  = ( f(x0+h)   -   f(x0-h))           /(2*h)
    fp2 = ( f(x0+h)   - 2*f(x0)   + f(x0-h)) /(h**2)
    fp3 = ( f(x0+2*h) - 2*f(x0+h) + 2*f(x0-h) - f(x0-2*h))/(2*h**3)
    fp4 = ( f(x0+2*h) - 4*f(x0+h) + 6*f(x0)   - 4*f(x0-h)+f(x0-2*h))/(h**4)
    print("f1(x):",fp)
    print("f2(x):",fp2)
    print("f3(x):",fp3)
    print("f4(x):",fp4)

def mtx_copy(aux):
    mtx = []
    for f in aux:
        mtx.append(f[:])
    return(mtx)

def MtxPrint(mtx):
    print( )
    for r in range(len(mtx)):
        for c in range(len(mtx[0])):
            print("\t%6.2f" % (mtx[r][c]), end = ' ')
        print()

def mtx_Gauss(mtxa, mtxb):
    a = mtx_copy(mtxa)
    b = mtx_copy(mtxb)
    ren = MtxRen(a)
    x = MtxZeros(ren,1);
    if MtxVerifica(a,b) == 1:
        for r in range(ren - 1):
            for k in range(r + 1, ren):
                piv = a[k][r] / a[r][r]
                for c in range(r, ren):
                    a[k][c] = a[k][c] - piv * a[r][c]
                b[k][0] = b[k][0] - piv * b[r][0]
        MtxPrint(a)
        MtxPrint(b)
        for i in range(ren - 1,-1,-1):
            x[i][0] = b[i][0]
            for k in range(i+1, ren):
                x[i][0] = x[i][0] - a[i][k] * x[k][0]
            x[i][0] = x[i][0] / a[i][i]
    MtxPrint(x)
    return x

def mtx_gauss_jordan(mtxa, mtxb):
    a = mtx_copy(mtxa)
    b = mtx_copy(mtxb)
    ren = MtxRen(a)
    col = MtxCol(b)
    x = MtxZeros(ren, 1)
    if MtxVerifica(a,b) == 1:
        for r in range(ren):
            div = a[r][r]
            for c in range(r, ren):
                a[r][c] = a[r][c] / div
            for c in range(col):
                b[r][c] = b[r][c] / div
            for k in range(ren):
                if k != r:
                    mult = a[k][r]
                    for c in range(r, ren):
                        a[k][c] = a[k][c] - mult * a[r][c]
                    for c in range(col):
                        b[k][c] = b[k][c] - mult * b[r][c]
        MtxPrint(a)
        MtxPrint(b)
        x = mtx_copy(b)
    return(x)

def MtxIdent(n):
    mtx = MtxZeros(n,n)
    for i in range(n):
        mtx[i][i] = 1
    return mtx

def MtxInver(A):
    a = mtx_copy(A)
    ren = MtxRen(A)
    I = MtxIdent(ren)
    return mtx_gauss_jordan(a, I)
