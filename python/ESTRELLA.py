print((
"\n              RC \n"
"  \   /     --0---  \n"
"R1 0 0 R2   \    /  \n"
"    Y     RB 0  0 RA\n"
"    0 R3      \/    \n"
"    |"
))

ra = float(input("ra: "))
rb = float(input("rb: "))
rc = float(input("rc: "))
a = ra + rb + rc

print(" a = ", a)
print("R1 = ", (rc*rb)/a)
print("R2 = ", (rc*ra)/a) 
print("R3 = ", (ra*rb)/a)
