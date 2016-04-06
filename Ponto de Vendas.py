#CENTRO UNIVERSITÁRIO DE JOÃO PESSOA - UNIPÊ
#CURSO: REDES DE COMPUTADORES - P2 2016.1
#PROFESSOR: JEFFERSON FERREIRA BARBOSA
#ALUNO: LEANDRO LOBO DO NASCIMENTO - 1520011349
#PROGRAMA: PONTO DE VENDAS

preco = [float(input("Digite o valor do Produto 1: ")), 
                  float(input("Digite o valor do Produto 2: ")), 
                  float(input("Digite o valor do Produto 3: ")), 
                  float(input("Digite o valor do Produto 4: ")), 
                  float(input("Digite o valor do Produto 5: "))]

ate_49 = 0
ate_80 = 0
maior_80 = 0

for valor in preco:
  if valor < 50:
     ate_49 = ate_49 + 1
  if (valor >= 50) and (valor <= 80): 
     ate_80 = ate_80 + 1
  if valor > 80:
     maior_80 = maior_80 + 1

print(" %d Produtos com preço abaixo de R$50,00" % ate_49)
print(" %d Produtos com preço entre R$50,00 e R$80,00" % ate_80)
print(" %d Produtos com preço maior que R$80,00" % maior_80)