from colorama import Fore, Style, init
from time import sleep as t
import pyautogui as p
import os
def limpiar_consola():
 so=os.name
 if so == 'nt':
  os.system("cls")
 else:
  os.system("clear")

init(autoreset=True)
def automatizar():
 limpiar_consola()
 n=1
 try:
  cantidad_palabras=int(input(" -Cantidad de palabras ---> "))
  cantidad_principal=int(input(" -Cantidad de repeticiones ---> "))
  tiempo=int(input(" -Tiempo de espera dentro del bucle: "))
 except:
  print("\n Campo Invalido , introduzca un numero")
  t(2)
  automatizar()

 print("")
 palabras=[]
 for i in range(1,cantidad_palabras+1):
  x=input(f" -Palabra Numero [{n}]: ")
  palabras.append(x)
  n=n+1

 def sin_orden():
  t(5)
  for i in range(0, cantidad_principal):
   for d  in palabras:
    p.write(d)
    p.press("enter")
    t(tiempo)

 def ordenados():
  t(5)
  for i in palabras:
   for d in range(0, cantidad_principal):
    p.write(i)
    p.press("enter")
    t(tiempo)

 print(f"""
  [1] Sin orden de palabras
  [2] Ordenados bucle
 """)

 X=input(" SELECCIONE SU OPCION ---> ")

 if X == "1":
  sin_orden()
 elif X == "2":
  ordenados()
 else:
  print(" Opcion Invalida...")
  automatizar()

 fin=input(f"\n HA FINALIZADO EL PROGRAMA")
 automatizar()
automatizar()
