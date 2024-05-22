potencia = float(input("Informe a potência de seu aparelho eletrônico: "))
tempo = float(input("Informe o tempo que o aparelho ficou ligado: "))
custo = float(input("Informe o custo por kWh: "))

consumo_kWh = (potencia * tempo) / 1000

custo_total = consumo_kWh * custo

print(f"O custo total para deixar o aparelho ligado por {tempo}, é {custo_total} kWh!")