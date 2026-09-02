# ============================================================
# DESAFIO EXTRA: CALCULADORA INTERATIVA
# ============================================================
while True:
    print("\n--- MENU CALCULADORA ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '3':
        print("Saindo do programa... Até mais!")
        break
    elif opcao in ['1', '2']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            print(f"Resultado da Soma: {num1 + num2}")
        elif opcao == '2':
            print(f"Resultado da Subtração: {num1 - num2}")
    else:
        print("Opção inválida! Tente novamente.")
