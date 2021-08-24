from math import *
from casioplot import *
def hat():
  p=192; q=100
  xp=144; xr=1.5*3.1415927
  yp=56; yr=1; zp=64
  xf=xr/xp; yf=yp/yr; zf=xr/zp
  for y in range(0,192):
    for x in range(0,384):
      set_pixel(x,y)
  for zi in range(-q,q):
    if zi>=-zp and zi<=zp:
      zt=zi*xp/zp; zz=zi
      xl=int(.5+sqrt(xp*xp-zt*zt)) # that first x is with lowercase L
      for xi in range(-xl,xl+1):  # That's two x's with a lowercase L after them
        xt=sqrt(xi*xi+zt*zt)*xf; xx=xi
        yy=(sin(xt)+.4*sin(3*xt))*yf
        x1=int(xx+zz+p) # That's x with a digit one after it
        y1=192-int(yy-zz+q) # That's y with a digit one after it
        set_pixel(x1,y1,(0,255,0)) # x with digit one after and y with digit one
        show_screen()
        for m in range(y1+1,y1+10): # Those are y with digit one after them
          set_pixel(x1,m) # That's x with digit one after it
