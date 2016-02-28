nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salario atual :"))
if salario >= 300:
	soma = salario + salario * 0.30
	print ("O novo salário de %s, será de R$%.2f ." %(nome, soma))
if salario <= 300:
	soma = salario + salario * 0.15
	print ("O novo salário de %s, será de R$%.2f ." %(nome, soma))