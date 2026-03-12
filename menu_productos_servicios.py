def menu_p():
    while True:
        print("\nHola! Bienvenid@ , aqui encontraras información sobre nuestros productos")
        print("1. Lista de productos\n2. Lista de servicios\n3. Contactar a un asesor\n4. PQR\n5. Salir")

        option=int(input("Digita el número de la opción que desea conocer: "))

        if option==1:   
            print("Lámparas, ceras para cuerina, alarmas, gadgets")
        elif option==2: 
            print("Overhauls, tapiforros, tapizados, polarizados")
        elif option==3: 
            print("Escribe al número 3245343788 para más información y cotizar el trabajo que desees")
        elif option==4:
            print("¿Posee una pregunta o desea hacer una petición o reclamo?")
            pqr= int(input("Digite 1. Para preguntas frecuentes, 2. Para petición o Para reclamo: "))
            if pqr==1:
                print("Dirección: calle 7 con 49 \n Horarios de atención: 8 am - 5 pm" )
            elif pqr==2:
                peticion= input("Qué reclamo o petición posee, deje también su contacto: ")
                print("Su petición o reclamo será atendida")
        elif option==5:
             print("Menú finalizado, un placer atenderl@")
             break
        else:
            print("La opción digitada no es válida")
menu_p()
