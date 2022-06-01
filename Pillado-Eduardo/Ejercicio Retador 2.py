municipio1 = input("Ingresa un municipio:")
habitantes1 = int(input("Ingresa su cantidad de habitantes:"))
municipio2 = input("Ingresa otro municipio:")
habitantes2 = int(input("Ingresa su cantidad de habitantes:"))
municipio3 = input("Ingresa un ultimo municipio:")
habitantes3 = int(input("Ingresa su cantidad de habitantes:"))

municipios = [municipio1, municipio2, municipio3]
habitantes = [habitantes1, habitantes2, habitantes3]

total_habitantes = habitantes1 + habitantes2 + habitantes3

promedio_habitantes = total_habitantes / 3

print(municipios)
print(habitantes)
print("El total de habitantes es:", total_habitantes)
print("El promedio de habitantes es:", promedio_habitantes)