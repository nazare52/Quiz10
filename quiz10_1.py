#Sergio Andrade Nieves
def findthrees(a):
 n = 0
 t = 0
 for item in a:
  if a[n]%3 == 0: 
   t = t+a[n]
  n += 1
 return t

lista = [0,4,2,6,9,8,3,12]
z = findthrees(lista)
print (z)