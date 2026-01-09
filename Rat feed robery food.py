def RatcountHouse(r,units,n,arr):
  total=r*units
  bag=0
  for i in range (n):
    if arr[i]<=total:
      total-=arr[i]
      bag+=1
  return bag
RatcountHouse(7,2,len([2,3,5,7,4]),[2,3,5,7,4])
