
def mul(A,B):
  m=len(A)
  n=len(A[0])
  p=len(B)
  q=len(B[0])
  assert(n==p)
  
  C=[]
  for i in range(m):
    C.append([])
    for j in range(q):
      s=0
      for k in range(n):
        s+=A[i][k]*A[k][j]
       C[-1].append(s)
  return C
