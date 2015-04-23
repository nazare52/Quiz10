#Sergio Andrade Nieves
def dotproduct(a,b):
 x = 0
 n = 0
 for item in a:
  x = x+(a[n]*b[n])
  n += 1
 return x

list01 = [2,4,5,6]
list02 = [1,2,3,4]
r = dotproduct(list01,list02)
print (r)