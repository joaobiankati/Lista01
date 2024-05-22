salario = float(input("Informe o valor do salário: "))
porcentagem_aumento = float(input("Informe o valor do aumento: "))

aumento = salario * (porcentagem_aumento / 100)

salario_novo = salario + aumento

print(f"O novo salário é de R$ {salario_novo:.2f}")