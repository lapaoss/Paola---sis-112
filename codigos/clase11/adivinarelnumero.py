
import random
contador=0
numeroaleratorio= random.randint(1,100)

print("Bienvenido a el juego de adivinar un numero"))
while True:
  numero=int(input("Ingrese su intento:"))
  contador+=1        
  if  numero < numeroaleratorio:
    print("Demasiado bajo. Intente de nuevo.")
  if numero >numeroaleratorio:
    print("Demasiado Alto. Intente de nuevo")
  if numero == numeroaleratorio:
    print("Felicidades adivino el numero, en el intento numero {}".format(contador))
    break














