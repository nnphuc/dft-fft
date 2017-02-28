# dft-fft
simple dft fft understand

V = [w<sub>jk</sub>] = w<sup>ij</sup> with `w=nth-root(1) = exp(-2*PI/n*i)`

------------------
-  `DFT(a) = y <=> y=V*a`
-  `IDFT(y) = a <=> a=V`<sup>-1</sup>`*y/n`


# fft

A(x) = x*Aodd(x2) + Aeven(x2)
```py
odd=fft(x[1::2])
even=fft(x[::2])
x[i]=odd[i]+w*even[i]
x[i+n/2]=odd[i]-w*even[i]
```
visit at https://github.com/nnphuc/python-advanced-algorithms/blob/master/fft.py

