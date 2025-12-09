print("Vamos fazer uma lista!!")
lista = [] 
def list_num(lista): # Função para enumerar os itens da lista
    for item in range(len(lista)):
        print(f"{1 + item}. {lista[item]} []")
while True: # Estrutura de repetição principal, que contém as funcionalidades do programa
    item = input("Digite o nome de um item para ele ser adicionado, digite 'saia', para sair ou 'remova' para remover o item: ") 
    if item.lower() == "saia":
        break
    elif item in lista:
        print("O item", item, "já está na lista.") 
    elif item.lower() == "remova":
        item_para_remover = input("Que item você deseja remover? ")
        if item_para_remover in lista:
            lista.remove (item_para_remover)
            print("O item", item_para_remover ,"foi removido da lista com sucesso! ")
        else:
            print("O item", item_para_remover, "não está na lista.")
    else:
        lista.append(item)
        print("O item", item, "foi adicionado à lista com sucesso!")
    print("Sua lista atual é:",)
    list_num(lista)
    print("-"*20)
print("Sua lista final é:")
list_num(lista)
print("-"*20)
print("Obrigado por usar nosso sistema de lista!")

with open("lista.txt", "w", encoding="utf-8") as arquivo: # Salvando a lista em um arquivo de texto
    for i, item in enumerate(lista, start=1):
        arquivo.write(f"{i}. {item} []\n")
 