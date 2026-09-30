compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print(f"Itens atuais: {compras}")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        item = input("Digite o item para adicionar: ")
        compras.append(item)
        print(f"'{item}' foi adicionado.")
    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in compras:
            compras.remove(item)
            print(f"'{item}' foi removido.")
        else:
            print("Item não encontrado na lista.")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")