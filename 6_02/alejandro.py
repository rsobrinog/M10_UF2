
############################# EXERCICI 18 ####################################

# palabra1 = input("Introduce la primera palabra: ")
# palabra2 = input("Introduce la segunda palabra: ")

# tupla_palabras = (palabra1, palabra2)

# frecuencia_letras = {}
# for palabra in tupla_palabras:
#     for letra in palabra:
#         if letra in frecuencia_letras:
#             frecuencia_letras[letra] += 1
#         else:
#             frecuencia_letras[letra] = 1

# print("Frecuencia de cada letra:")
# for letra, frecuencia in frecuencia_letras.items():
#     print(f"{letra}: {frecuencia} veces")


############################# EXERCICI 17 ####################################

# frase_usuario = input("Introduce una frase: ")

# frase_sin_espacios = tuple(frase_usuario.replace(" ", ""))
# frase_sin_repetidos = tuple(set(frase_sin_espacios))

# print(f"Tupla sin espacios y sin caracteres repetidos: {frase_sin_repetidos}")



############################# EXERCICI 15 ##########################################

# numeros = []

# while True:
#     entrada_usuario = input("Introduce un número (o 0 para terminar): ")
#     numero = int(entrada_usuario)

#     if numero == 0:
#         break

#     numeros.append(numero)

#     print(type(numeros))

# tupla_ordenada = tuple(sorted(numeros))

# print(f"Tupla ordenada de menor a mayor: {tupla_ordenada}")


############################# EXERCICI 14 ###########################################

# entrada_usuario = input("Introduce 10 números separados por espacio: ")

# numeros = [int(x) for x in entrada_usuario.split()]

# print(type(numeros))

# tupla_ordenada = tuple(sorted(numeros))

# print(type(tupla_ordenada))

# print(f"Tupla ordenada de menor a mayor: {tupla_ordenada}")

entrada_usuario = input("Introduce 10 números separados por espacio: ")

numeros = tuple(int(x) for x in entrada_usuario.split())

numeros = sorted(numeros)

print(f"Tupla ordenada de menor a mayor: {numeros}")