cemento = 40
yeso = 30

costales_cemento = int(input("Número de costales de Cemento: "))
peso_cemento = costales_cemento * cemento
costales_yeso = int(input("Número de costales de Yeso: "))
peso_yeso = costales_yeso * yeso

peso_total = peso_cemento + peso_yeso

print("El peso total en kg es: ", peso_total)
print("¿Se puede realizar el envio?: ")

if peso_total > 1627 < 3254:
  print(True)
else:
  print(False)