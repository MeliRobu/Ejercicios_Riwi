#Menu iterativo / condiciones sin condicionales

print("elije tu pet: ")
#Creación de lista
pets = ["dog","cat","rabbit"]
#Creación de diccionario
mensaje = {
    "dog":"comida para perro",
    "cat":"comida para gto",
    "rabbit":"comida para conejo"
}
#metodo enumerate para "creacion de menú" (enumeración de los datos de una lista)
for i,pet in enumerate(pets):
    print(f"{i+1} - {pet}")

indce = int(input("elije tu pet"))

print(f"{mensaje[pets[indce-1]]}")
