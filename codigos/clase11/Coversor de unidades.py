import unidade



def Menu():

    print("CONVERSOR DE UNIDADES")
    print("Seleccione un opcion: ")
    print("1.Longuitud(metros a kilometros )")
    print("2.Masa (de gramos a kilogramos) ")
    print("3.Temperatura (de celcius a Fahrenheit)")
    
    print("4.Opcion no valida. Salir")
while True:
    Menu()


    opcion=int(input("Elige  su opcion: "))
    if opcion==4:
        print("Saliendo de el conversor")
        break

    dato=float(input("Ingrese el dato que desea convertir: "))

    if opcion==1 :
        print(f'Resultado:{unidade.longitud(dato)}')
    elif opcion==2:
        print(f'Resultado:{unidade.masa(dato)} k')
    else:
        print(f'Resultado: {unidade.temperatura(dato)}



