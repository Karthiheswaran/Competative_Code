def nbase(num,n):
  res = ""
  while (num!=0):
    rem = num%n
    if rem>=10:
      val = hex(rem)
      res = res+val[2].upper()
    else:
      res = res+str(rem)
    num = num//n
  return res
nbase(718,12)
