"""
# 1. Agregar y eliminar elementos de una lista

Crea una lista con 5 frutas. Luego:

- agrega una fruta al final con append()
- inserta una fruta en la posición 2 con insert()
- elimina una fruta con remove()
- elimina el último elemento con pop()
- Objetivo: practicar modificación básica de listas.

# 2. Ordenar y contar elementos en una lista

Dada esta lista:

```py
numeros = [4, 2, 7, 2, 9, 1, 2]
```

Haz lo siguiente:

- ordénala con sort()
- invierte el orden con reverse()
- cuenta cuántas veces aparece el número 2 con count()
- busca en qué posición aparece el número 7 con index()
- Objetivo: usar métodos de búsqueda y ordenamiento.

# 3. Copiar y extender listas

Crea dos listas:

```py
a = [1, 2, 3]
b = [4, 5, 6]
```

Luego:

- copia a en otra lista usando copy()
- une b a la copia usando extend()
- muestra la lista final
- Objetivo: entender la diferencia entre copiar y modificar.
"""
import os
os.system("clear")

#lists
#Practice 1
fruit_list= ['grape','orange','banana','watermelon', 'pineapple']
fruit_list.append('apple')
fruit_list.insert(2,'pear')
fruit_list.remove('orange')
fruit_list.pop()
print(fruit_list)

#practice 2
numbers= [4, 2, 7, 2, 9, 1, 2]
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers.reverse)

#practice 3
a = [1, 2, 3]
b = [4, 5, 6]
c = a.copy()
c.extend(b)
print(c)

#practice 4
students=['marie','shary','marlon','valery']
students.clear()
print(students)

#practice 4

person = {
    "name" : "Ana",
    "age" : 25,
    "city" : "Bogotá"
}
print(person["name"])
print(person.get("age"))
print(person.get("cellphone number","It does not exist"))

#practice 6

person["ocuppation"] = "Accounter"
person["age"]= 30
city_remove= person.pop("city")
print(city_remove)
print(person)

#practice 7
products= {
    "bread" : 1500,
    "milk" : 3200,
    "eggs" : 9000
}
print(products.keys())
print(products.values())
print(products.items())

#practice 8

prices= {
    "towel" : 20000,
    "hairbrush" : 150000,
    "wipes" : 10000,
    "jeans" : 50000
}
price_remove= prices.popitem()
print(price_remove)
print(prices)

#practice 10
student_s= [
    {"name" : "Luis","score" : 4.5},
    { "name" : "Marta", "score" : 3.8},
    { "name" : "Carlos","score" : 4.2 }
    ]

print(sum(e['score'] for e in student_s)/len(student_s))

for students_dic in student_s:
    print(students_dic["name"])
    if students_dic["score"]> 4:
        print(students_dic['score'])



