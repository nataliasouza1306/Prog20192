# Opção 1 sem exponeciação 
'''
peso = 60
altura = 1.70

num = (peso/altura)
imc = (num/altura)  
print(imc)
'''
# Opção 2 com exponenciação 
peso = 60
altura = 1.70**2
imc = (peso/altura)
print("O resultado do IMC é: ", imc)

MuitoAbaixo = (imc<17)
print("Muito abaixo: ", MuitoAbaixo)

BaixoPeso = (imc>17 and imc<18.5)
print("Baixo peso normal: ", BaixoPeso)

PesoNormal = (imc>18.5 and imc<25.0)
print("Peso normal: ", PesoNormal)

AcimaPeso = (imc>25.0 and imc<30)
print("Acima do peso normal: ", AcimaPeso)

MuitoAcima = (imc>30)
print("Muito acima do peso: ", MuitoAcima)