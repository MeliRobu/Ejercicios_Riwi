numeros = [4, 2, 7, 2, 9, 1, 2]
numeros.index(7)
print(numeros.index(7))

a = [1, 2, 3]
b = [4, 5, 6]
c = a.copy()
c.extend(b)
print(c)

students = ["maria", "alberto", "isabel", "roberto"]
students.clear()
print(students)

person = {
    "name": "Ana",
    "age": 25,
    "city": "Bogotá"
}
print(person.values())
print(person.get("name"))
print(person.get("age"))
print(person.get("cellphone", "It does not exist"))
