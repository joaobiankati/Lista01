dia_semana = int(input("Informe o dia da semana, sendo (1) para segunda-feira, (2) para terça-feira e etc: "))

dias_fim_semana = (5 - dia_semana)
if dia_semana > 5:
    print("Você ja esta no final de semana!")

else:
    print(f"Faltam {dias_fim_semana} para o final de semana! ")