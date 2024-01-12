def perguntar():
    return input("o que deseja realizar?\n" +
                  " <i> para inserir um usuário\n" +
                  " <p> para pesquisar um usuario\n" +
                  " <e> para excluir um usuario\n" +
                  " <l> para listar um usuario: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                                                     input("Digite o aniversário: "),
                                                     input("Digite o estado: ").upper()]
    salvar(dicionario)

def pesquisar(dicionario, pesquisachave):
    if pesquisachave in dicionario:
        return print(dicionario[pesquisachave])
    else:
        return print("O usuário não existe.")

def excluir(dicionario, excluiruser):
    if excluiruser in dicionario:
        del dicionario[excluiruser]
        return print("Usuário excluído com sucesso")
    else:
        return print("O usuário não pôde ser excluído.")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)
    
def salvar(dicionario): 
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
            
