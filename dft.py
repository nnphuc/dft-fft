import math
import matrix

def dft(a):
  n=len(a)
  v=[]
  w=e**(-2*math.pi/n*1j)
  for i in range(n):
    v.append([])
    for j in range(n):
      v[-1]*append(w**(j*k))
  return mul(v,a)

def idft(a):
  
