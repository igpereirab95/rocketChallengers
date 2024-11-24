''' agenda deve conter:
        menu com todas as opções, são elas
            - adicionar contato - Nome, Telefone, Email e Favoritar (sim ou não)
            - visualizar toda a lista
            - editar contato
            - marcar/desmarcar como favorito
            - lista de favoritos
            - apagar um contato
            
'''
# instancionando lista vazia
contatos_lista = [{'nome': 'oaisdjaoids', 'telefone': '498489', 'email': '9498489@gmail.com', 'favorito': True}, {'nome': 'uioahsudiais', 'telefone': '987497978', 'email': 'igioajsdaoi@outlook.com', 'favorito': False}]

# funcao de adicionar, primeiro seco, depois com validacao
def adicionar_contato(contatos_lista, add_nome, add_telefone, add_email, add_favorito):
    
    status_favorito = True if add_favorito == "sim" else False
    contatos_dicio = {"nome": add_nome, "telefone": add_telefone, "email": add_email, "favorito": status_favorito}
    contatos_lista.append(contatos_dicio)   
    print("Contato adicionado com sucesso!")
    return

# visualizar lista de contatos
def visualizar_contatos(contatos_lista):
    print("\nLista de contatos")
    for indice_contato, contatos_dicio in enumerate(contatos_lista, start=1):
        status_favorito = " ☆ " if contatos_dicio["favorito"] else " "
        print(f''' 
            {indice_contato}. Nome: {contatos_dicio["nome"]}
            Telefone: {contatos_dicio["telefone"]}
            Email: {contatos_dicio["email"]}
            Favorito: {status_favorito}
              ''' )
    return

# editar contatos
def editar_contatos(contatos_lista, novo_nome, novo_telefone, novo_email, novo_status_favorito, numero_contato_edicao):

    # ajuste indice contatos_lista por causa do enumerate start
    indice_contatos_ajustado = numero_contato_edicao - 1

    # valor apenas inteiros positivos, validacao para não quebrar os valores da lista
    if indice_contatos_ajustado >= 0 and indice_contatos_ajustado < len(contatos_lista):        
        
        # verifica se vai alterar o nome, caso tenha alguma string sim, se não parmanece o antigo
        contatos_lista[indice_contatos_ajustado]["nome"] = novo_nome if novo_nome != "" else print("\nNome inalterado.")
        
        contatos_lista[indice_contatos_ajustado]["telefone"] = novo_telefone if novo_telefone != "" else print("\nTelefone inalterado.")
        
        contatos_lista[indice_contatos_ajustado]["email"] = novo_email if novo_email != "" else print("\nE-mail inalterado.")

        contatos_lista[indice_contatos_ajustado]["favorito"] = novo_status_favorito if novo_status_favorito != "" else print("\nStatus favorito mantido.")
        # até aqui para atualizar os valores

    return

# listar contatos favoritos
def listar_favoritos(contatos_lista):
    print(f"Os seguintes contatos são favoritos:")
    for indice_contato, contatos_dicio in enumerate(contatos_lista, start=1):
        status_favorito = contatos_dicio["favorito"]
        if status_favorito:
            print(f''' 
                {indice_contato}. Nome: {contatos_dicio["nome"]}
                Telefone: {contatos_dicio["telefone"]}
                Email: {contatos_dicio["email"]}
                ''' )
    return

# remover contato da agenda
def remove_contato(contatos_lista, numero_contato):
    print(numero_contato)
    indice_contato_remocao = numero_contato - 1
    contato_para_remover = contatos_lista[indice_contato_remocao]
    nome_contato_removido = contatos_lista[indice_contato_remocao]["nome"]
    contatos_lista.remove(contato_para_remover)
    print("Contato %s removido!" % nome_contato_removido)
    return

# função para mudar status para favorito de um contato
def mudar_status_favorito(contatos_lista, numero_selecionado):
    indice_contato_ajustado = numero_selecionado - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos_lista):
        valor_atual = contatos_lista[indice_contato_ajustado]["favorito"]
        if valor_atual:
            contatos_lista[indice_contato_ajustado]["favorito"] = False
            print("Desvaforitado!")
        else:
            contatos_lista[indice_contato_ajustado]["favorito"] = True
            print("Favoritado!")
    else:
        print("Não existe este contato na lista")
    return

# função para checar se é numero, para não abortar o código
def checa_mudanca_int(valor_digitado):
    try:
        valor_numerico = int(valor_digitado)
        return True
    except ValueError as erro:
        print("\nVocê não digitou um número.")
        return False

# menu com multiplas opções
while True:

    print(''' 
            Agenda de contatos 

                1 - Adicionar novo contato.
                2 - Visualizar contatos.
                3 - Editar contato.
                4 - Marcar/Desmarcar contato como favorito.
                5 - Listar contatos favoritos.
                6 - Apagar contato.
                7 - Sair.
          ''')
    
    selecao_menu = int(input("Selecione uma opção: "))

    if selecao_menu == 1:
        add_nome = input("Digite o nome do novo contato: ")
        add_telefone = input("Digite o telefone com ddd: ")
        add_email = input("Digite o email: ")
        add_favorito = input("Marcar ela como favorito (sim/não)? ")
        adicionar_contato(contatos_lista, add_nome, add_telefone, add_email, add_favorito)
    elif selecao_menu == 2:
        visualizar_contatos(contatos_lista)
    elif selecao_menu == 3:
        visualizar_contatos(contatos_lista)
        while True:
            numero_contato_edicao = input("Qual o número da lista de contatos alterar? ")
            if checa_mudanca_int(numero_contato_edicao):
                numero_checado_edicao = int(numero_contato_edicao)
                print("\nPressione Enter para manter o valor atual e pular para o próximo!")
                novo_nome = input("Informe o novo nome: ")
                novo_telefone = input("Informe o novo telefone: ")
                novo_email = input("Informe o novo email: ")
                novo_status_favorito = input("Marcar como favorito? ")
                break            
        editar_contatos(contatos_lista, novo_nome, novo_telefone, novo_email, novo_status_favorito, numero_checado_edicao)
        visualizar_contatos(contatos_lista)
    elif selecao_menu == 4:
        visualizar_contatos(contatos_lista)
        while True:
            marcar_favorito = input("Qual o número da lista de contatos quer marcar como favorito? ")
            if checa_mudanca_int(marcar_favorito):
                numero_favoritar_checado = int(marcar_favorito)
                break
        mudar_status_favorito(contatos_lista, numero_favoritar_checado)
    elif selecao_menu == 5:
        listar_favoritos(contatos_lista)
    elif selecao_menu == 6:
        visualizar_contatos(contatos_lista)
        while True:
            selecao_remove_contato = input("Qual o número da lista de contatos quer remover? ")
            if checa_mudanca_int(selecao_remove_contato):
                remover_numero_contato = int(selecao_remove_contato)
                break
        remove_contato(contatos_lista, remover_numero_contato)
    elif selecao_menu == 7:
        break
    elif selecao_menu not in range(1,7): #não digitar um número que não esteja informado
        print("\nNúmero de opção não informado.")