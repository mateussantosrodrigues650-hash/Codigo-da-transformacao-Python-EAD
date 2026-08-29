agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado/atualizado!")
    elif opcao == "2":
        nome = input("Digite o nome do contato a remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato {nome} removido com sucesso.")
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Digite o nome para buscar: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        print("Encerrando a agenda.")
        break
    else:
        print("Opção inválida.")