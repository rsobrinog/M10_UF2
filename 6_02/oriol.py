######################################### EXERCICI 14 ###########################33
#aLTERNATIVA

entrada_usuario = input("Introduce 10 números separados por espacio: ")

numeros = sorted(tuple(int(x) for x in entrada_usuario.split()))

print(f"Tupla ordenada de menor a mayor: {numeros}")