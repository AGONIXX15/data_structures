# Definir la lista de enteros
lista = [1, 2, 3, 4]

# Crear la lista de pares (x, y)
lista = [(x, y) for x in lista for y in lista]
print("Lista de pares:", lista)

# Filtrar pares donde y > x
r1 = list(filter(lambda x: x[1] > x[0], lista))
print("r1 (y > x):", r1)

# Filtrar pares donde y == x
r2 = list(filter(lambda x: x[1] == x[0], lista))
print("r2 (y == x):", r2)

# Filtrar pares donde y es múltiplo de x
r3 = list(filter(lambda x: x[1] % x[0] == 0, lista))
print("r3 (y es múltiplo de x):", r3)

# Filtrar pares donde la suma de x + y es menor o igual a 3
r4 = list(filter(lambda x: x[1] + x[0] <= 3, lista))
print("r4 (x + y <= 3):", r4)

# Crear r5 para encontrar relaciones simétricas
r5 = [(x, y) for (x, y) in lista if (y, x) in lista]
print("r5 (relaciones simétricas):", r5)

