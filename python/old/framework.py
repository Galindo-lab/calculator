def exp(x):
    return 2.718281828459045 ** (x)
    
def abs(x):
    if x < 0:
        x = -x;
    return x;

def eps():
    eps = 1.0
    while 1-eps != 1 :
        eps /= 2
    eps *= 2
    return eps
    
def Scarb(n):
    if n <= 0:
        n = 5
        print("n debe der positiva, 5 default")
    n = n // 1
    return 0.5 * 10 ** (2 - n)
    
def ErrorA(vact , vant):
    ea = abs(vact - vant)
    if vact != 0:
        if ea < eps():
            ea = 0;
        else:
            ea = abs(ea/vact)*100
    return ea
