#Digite o nome do eletrodoméstico
Eletrodomestico = input("Eletrodoméstico: ")

#Digite a potência do aparelho em watts (W)
Potencia_eletrodomestico = int(input("Potência: "))

#Digite o tempo médio de uso diário em horas
Tempo_medio_de_uso = float(input("Tempo de consumo diário: "))

#Calcule o consumo mensal em kWh: consumoMensal = (potencia * horasDia * 30) / 1000
Consumo_mensal = (Potencia_eletrodomestico * Tempo_medio_de_uso * 30) / 1000

#Custo kWh em R$ em Sorocaba
Valor_medida = 0.70

#Cálculo de custo estimado
custo_estimado = (Consumo_mensal * Valor_medida)

#Mensagem na tela
print("Consumo mensal estimado: ", Consumo_mensal, "kWh/mês")
print("Custo estimado: R$", custo_estimado, "por kWh")