""" Uma nave espacial recebe as pessoas com uma mensagem de boas vindas de acordo com o nome que elas forneceram ao fazer o cadastro na recepção. 
Crie uma aplicação que imprima a mensagem de boas vindas de acordo com os nomes na lista: 
nomes = [‘Elysson’, ‘Giulia’, ‘Willian’, ‘Gileno’], com a seguinte mensagem: “Olá, NOME_PESSOA! Seja bem vindo à nave Imperial dos Siths.”. 
Crie um programa que faça a interpolação da string de boas vindas, 
substituindo o NOME_PESSOA pelo nome lido na lista e imprimindo a frase de boas vindas com o nome substituído.

Dica bônus: para resolver este código, basta você inserir os nomes Elysson, Giulia, Willian e Gileno 
dentro de uma lista e depois utilizar um for para percorrer cada um dos nomes. Você consegue resolver este código com apenas 03 linhas, 
então foque na simplicidade !

"""
nomes = ['Elysson', 'Giulia', 'Willian', 'Gileno']

for nome in nomes:
    print(f"Olá, {nome}! Seja bem vindo à nave Imperial dos Siths.")
  
    
