from cgitb import reset
from math import sqrt
from pdb import Restart
from tracemalloc import stop

while True:

 a= int(input("Digite o valore de a:"))
 b= int(input("Digite o valor de b:"))
 c= int(input("Digite o valor de c:"))

 delta=b*b-4*a*c
 if delta < 0: 
   print("Delta negativo, logo não possui raizes reais")
 elif delta == 0:
   r1=(-b + sqrt(delta))/(2*a)
   r2=(-b - sqrt(delta))/(2*a)
   print("Delta igual a zero e possui apenas uma raiz:{}".format(r1))
 else:
   r1=(-b + sqrt(delta))/(2*a)
   r2=(-b - sqrt(delta))/(2*a)
   print("As raizes da equação são {} e {}".format(r1,r2))

 out=input("Aperte enter se quiser continuar, se quiser sair digite sair: ")
 if out == "sair":
  break