print("Vamos fazer uma lista de compras!!")
lista_compras = [] 
def lstar_compras(lista_compras): # Função para enumerar os itens da lista de compras
    for item in range (len(lista_compras)):
        print(f"{1 + item}. {lista_compras[item]} []")
while True: # Estrutura de repetição principal, que contém as funcionalidades do programa
    item = input("Digite o nome de um item para ele ser adicionado, digite 'saia', para sair ou 'remova' para remover o item: ") 
    if item.lower() == "saia":
        break
    elif item in lista_compras:
        print("O item", item, "já está na lista de compras.") 
    elif item.lower() == "remova":
        item_para_remover = input("Que item você deseja remover? ")
        if item_para_remover in lista_compras:
            lista_compras.remove (item_para_remover)
            print("O item", item_para_remover ,"foi removido da lista com sucesso! ")
        else:
            print("O item", item_para_remover, "não está na lista de compras.")
    else:
        lista_compras.append(item)
        print("O item", item, "foi adicionado à lista com sucesso!")
    print("Sua lista atual é:",)
    lstar_compras(lista_compras)
    print("-"*20)
print("Sua lista final é:")
lstar_compras(lista_compras)
print("-"*20)
print("Obrigado por usar nosso sistema de lista de compras!")
 