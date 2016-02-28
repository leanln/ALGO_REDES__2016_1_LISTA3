codigo = int(input("Coloque 1 para adição ou 2 para subtração : "))
if codigo == 1:
 print ("Vamos lá, você escolheu ADIÇÃO")
 um = float(input("Digite o primeiro numéro : "))
 dois = float(input("Digite o segundo numéro : "))
 soma = float(um) + float(dois)
 print ("O resultado da adição é %.2f" %(soma))
if codigo == 2:
 print ("Vamos lá, você escolheu SUBTRAÇÃO")
 um = float(input("Digite o primeiro numéro : "))
 dois = float(input("Digito o segundo numéro : "))
 soma = um - dois
 print ("O resultado da subtração é %.2f " %(soma))
if codigo >= 3:
	print("Apenas coloque 1 ou 2")
if codigo <= 0:
	print("Apenas coloque 1 ou 2")