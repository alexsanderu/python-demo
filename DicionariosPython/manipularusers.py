from pythonProject.DicionariosPython.Funcoes import *

usuarios = {}
opcao = perguntar()
while opcao =="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao =="I":
        inserir(usuarios)
    opcao = perguntar()
    if opcao =="P":
        pesquisachave = input("Digite o usuario a pesquisar: ").upper()
        pesquisar(usuarios, pesquisachave)
    if opcao =="E":
        excluiruser = input("Digite o usuario a excluir: ").upper()
        excluir(usuarios, excluiruser)
    if opcao == "L":
        listar(usuarios)
        opcao = perguntar()


