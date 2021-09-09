print((
"\n              RC \n"
"  \   /     --0---  \n"
"R1 0 0 R2   \    /  \n"
"    Y     RB 0  0 RA\n"
"    0 R3      \/    \n"
"    |"
))

r1 = float(input("r1: "))
r2 = float(input("r2: "))
r3 = float(input("r3: "))
a = r1*r2 + r2*r3 + r3*r1

print(" a = ", a)
print("RA = ", a/r1)
print("RB = ", a/r2)
print("RC = ", a/r3)
