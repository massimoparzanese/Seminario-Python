lista =[ 2, 5, 6,8 , 1, 3, 10, 11 ]
lis_par = []
lis_impar = []
for i in lista:
    if( (i % 2) == 0):
         lis_par.append(i)
    else :
      lis_impar.append(i)
print("lista par:")
for i in lis_par:
    print(i)
print("\n")
print("lista impar")
for i in lis_impar:
    print(i)