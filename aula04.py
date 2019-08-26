'''
varLogica = int(input("Você é uma pessoa inteligente? ")) #Se você digitar 1, o programa entende como TRUE. Se digitar 0, o programa entende como FALSE. Por isso a variável inteira. 

if(varLogica):
    print("Não deixe o trabalho pra depois!") #Lembrar do tab. O que estiver com espaço tá dentro do if.

print("Fim de programa!")

--

botao1apertado = int(input("O rato apertou o botão 1? ")) # Da mesma forma que o exemplo anterior, responder com 0 e 1.
botao2apertado = int(input("O rato apertou o botão 2? "))

if (not botao1apertado and not botao2apertado):
    print("Nenhuma comida foi adicionada")
if (botao1apertado and not botao2apertado): # O operador lógico and considera verdadeiro quando as duas situações forem verdadeiras ao mesmo tempo. Por isso o not foi acrescentado.
    print("Foram adicionados 10g de comida")
if (not botao1apertado and botao2apertado):
    print("Foram adicionados 20g de comida")
if (botao1apertado and botao2apertado):
    print("Foram adicionados 40g de comida")

print("Fim de programa!")


# String + operadores lógicos (and, or ou not) e relacionais (==. <=, >=)

strLazy = input("Você é uma pessoa preguiçosa? ")
strItelligent = input("Você é uma pessoa inteligente? ")

if(strLazy == "s" or "sim" and strItelligent == "n"): # O resultado de um operador relacional é um resultado lógico, então consigo aplicar operador lógico como o and.
    print("Você é preguiçoso(a) e não é muito inteligente.")

if(strLazy == "n" and strItelligent == "n"): # Ele compara se o que eu digitei é == a "n" ou se é == "s"
    print("Você não é preguiçoso(a) e não é muito inteligente.")

if(strLazy == "s" and strItelligent == "s"):
    print("Você é preguiçoso(a) e inteligente.")

if(strLazy == "n" and strItelligent == "s"):
    print("Você não é preguiçoso(a) e é inteligente.")

print("FIM!")


# Usando IF e ELSE

logicValue = int(input("Você é inteligente? "))
if(logicValue):
    print("Você é inteligente!")
else:
    print("Você não é inteligente!")

print("FIM")


# Usando IF e ELSE junto com operadores relacionais

numeroMenor = int(input('Digite um número menor que 5: '))

if numeroMenor > 5:
    print('Ops!')
    print('O número digitado é maior que 5.')
else:
    print("O número digitado foi: ", numeroMenor)

print('FIM')
'''
# Usando IF, ELIF e ELSE

strLazy = input("Você é uma pessoa preguiçosa? ")
strItelligent = input("Você é uma pessoa inteligente? ")

if(strLazy == "s" or "sim" and strItelligent == "n"): # O resultado de um operador relacional é um resultado lógico, então consigo aplicar operador lógico como o and.
    print("Você é preguiçoso(a) e não é muito inteligente.")

elif(strLazy == "n" and strItelligent == "n"): # Ele compara se o que eu digitei é == a "n" ou se é == "s"
    print("Você não é preguiçoso(a) e não é muito inteligente.")

elif(strLazy == "s" and strItelligent == "s"):
    print("Você é preguiçoso(a) e inteligente.")

else: #não coloca condição do else
    print("Você não é nada.")

print("FIM!")

# Não erro semanticamente usando IF para tudo, mas irei tomar mais tempo de processamento, pois ele irá verificar todas as condições. 
