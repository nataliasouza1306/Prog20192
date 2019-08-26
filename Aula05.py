'''
lista = ["carro", "peixe", 123, 111] # ordem dos elementos: 0, 1, 2, 3. 
novalista = ["pedra", lista]
#print(novalista)

#print(lista[1])
#print(novalista[1][2]) #o segundo operador vai respoder ao primeiro. Ou seja, acessar o local 2 da lista.

#print(lista[-1]) #lista ao contrário. 

#print(len(lista)) #tamanho da lista

#print(len(novalista[1])) # coloquei uma operação. Dentro de novalista procure o elemento 1. Retorne o tamanho desse resultado.

#print(lista+novalista) # anexa ao final da lista anterior o valor da nova lista

print(lista*3) # repete a lista 3x

print('peixe' in lista) #verifica a existência de algo dentro da lista

print('boneca' in lista)

numberlist = [1, 5, 9, 18, 16]
print(min(numberlist))
print(max(numberlist))
print(sum(numberlist))

if ('carro' in lista):
    print("Venci na vida!!")
else:
    print("Tristeza!")

if(not('carro' in lista)): #posso colocar operadores lógicos. Nesse caso, está tornando falso a existência de carro na lista. 
    print("Sou rica :)")

if(not('carro' in lista) and ('peixe' in lista)): 
    print("Sou pobre e estou com fome ")

livros = ["Java", "SqlServer", "Delphi", "Python"]
livros.append("Android") # insiro ao final da lista
print(livros) 

livros.insert(0, "Oracle") # na posição 0 insira a palavra Oracle
print(livros)

livros.pop() # exclui a última palavra ou adiciono a posição que quero retirar
print(livros)

livros.remove("SqlServer") # busca a palavra, encontra, remove. 
print(livros)

print(livros.index("Delphi")) # Diz a posição da palavra na lista

livros.sort() # ordem alfabética
print(livros)

livros.reverse() # espelha a ordem
print(livros)

print(livros.count("Java")) #Conta quantas vezes essa palavra aparece na lista


a = [33, 33, 33] 
b = [33, 33, 33]
print(a==b) #São iguais, mas não são a mesma coisa. Ocupam lugeres diferentes. 
print(a is b) #Confirma que eles não são a mesma coisa. 
b[0] = 3
print(a)

b = a # Agora torno a MESMA COISA, IGUAIS MESMO. Isso torna o programa mais  rápido.  
b[0] = 3
print(a) # Mudei b, refletiu em a. 

c = a[:] #Clona: tem os mesmos elementos, mas não é a mesma coisa. 
print(c)

a[1] = 4
print(c) #Mudei a, mas não refletiu em c. Ou seja, realmente não são a mesma coisa. 
'''
# TUPLA 

tupla = (1, 2, 3, 4); print(tupla)
tupla = (1,); print(tupla)
tupla = (); print(tupla) # tem que ter o ( ) para ele achar que é uma tupla


tuplinha = ("João", "e", "Maria")
print(tuplinha[0]) #Não posso modificar, mas posso acessar. 
print(tuplinha[0:2]) #A partir da posição zero mostre 2 elementos = FATIAMENTO. 

p = "PYTHON"
print(p[0:1])
print(p[0:2])
print(p[0:3])
print(p[0:4])

print(p[:]) # Mostro tudo
print(p[1:]) # Do final até o caractere 1
print(p[2:]) # Do final até o caractere 2

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1+t2) # Ele não muda as tuplas definidas anteriormente, mas cria uma terceira.

# DICIONÁRIO

agenda = {}; print(agenda)
agenda = {"Maria": [98885544, 988552211], "Pedro": [84458438758, 58754587]} #É a minha chave. Vou acessar pelo índice "Maria"
print(agenda)

print(agenda["Maria"]) #Mostra tudo que tiver depois dos 2 pontos. Associei Maria a uma lista, então mostra os elementos dessa lista. E dentro desas lista posso colocar o que eu quiser. 
print(agenda["Pedro"])


