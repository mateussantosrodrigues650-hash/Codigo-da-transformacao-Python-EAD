'''
pensamento projeto seunome <-nome da pasta

Um Bloco de Comentarios. 
Para explicar o que o código faz, ou para deixar anotações para o programador.
>>projeto hamburgueria:

>PO (Como dono do negocio: Quero um sistema de vendas para minha hamburgueria, 
para que eu possa controlar as vendas e os produtos.)

>QA (Como cliente: Quero um sistema de vendas para minha hamburgueria,
para que eu possa comprar meus lanches favoritos de forma rápida e fácil.)

>Tech (Como programador: Quero um sistema de vendas para minha hamburgueria,
para que eu possa desenvolver um software eficiente e funcional para o negócio.)

>Dev (Como programador: Quero um sistema de vendas para minha hamburgueria,
para que eu possa implementar as funcionalidades necessárias para 
atender as necessidades do negócio e dos clientes.)

>UX (Como designer de experiência do usuário: Quero um sistema de 
vendas para minha hamburgueria, para que eu possa criar uma 
interface intuitiva e agradável para os usuários, 
garantindo uma experiência de compra satisfatória.)

>IA (Como analista de dados: Quero um sistema de vendas para minha 
hamburgueria, para que eu possa coletar e analisar os dados de vendas, 
ajudando a identificar padrões de consumo e otimizar as 
estratégias de marketing e estoque.)


Ciclo de vida do projeto:
1. Planejamento: Definir os requisitos do sistema, identificar as necessidades do negócio e dos clientes, 
e criar um plano de desenvolvimento.
2. Análise: Analisar os requisitos e criar um modelo de dados e um design de sistema.
3. Desenvolvimento: Escrever o código para implementar as funcionalidades do sistema.
4. Testes: Testar o sistema para garantir que ele funcione corretamente e atenda aos requisitos.
5. Implantação: Implantar o sistema em um ambiente de produção e garantir que ele esteja funcionando 
corretamente.
6. Manutenção: Realizar manutenção contínua para corrigir bugs, adicionar novas funcionalidades e garantir 
que o sistema continue atendendo às necessidades do negócio e dos clientes.

>>Criar um aplicativo, sistema em CLI - Command Line Interface, ou seja, um sistema que funcione no terminal, sem interface gráfica.
>>Complementar e implementar o app / sistema em GUI - Graphical User Interface, ou seja, um sistema com interface gráfica, 
para que os usuários possam interagir de forma mais intuitiva e agradável.

'''

# Inicializando as variáveis para o Produto 1
p1_nome = "x-burger clássico"
p1_estoque = 50
p1_preco = 22.90
p1_validade = "15/09/2026"
p1_descricao = "Pão artesanal, hambúrguer bovino 160g, queijo prato e maionese da casa."

# Inicializando as variáveis para o Produto 2
p2_nome = "x-bacon artesanal"
p2_estoque = 35
p2_preco = 28.90
p2_validade = "15/09/2026"
p2_descricao = "Pão brioche, hambúrguer bovino 160g, muito bacon crocante e queijo cheddar."

# Inicializando as variáveis para o Produto 3
p3_nome = "batata frita especial"
p3_estoque = 80
p3_preco = 14.50
p3_validade = "30/11/2026"
p3_descricao = "Porção de batatas palito crocantes com tempero da casa."

# Loop principal do sistema CLI
while True: 
    print('-' * 48 + '\n')
    print('🍔 Bem-vindo ao Sistema de Vendas - Hamburgueria!\n')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Realizar venda')
    print('0 - Sair')
    print('\n--------------------------------------\n')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Cadastrando produtos...\n')
        
        if p1_nome == "":
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_validade = input('Digite a validade do lote: ')    
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')            
        elif p2_nome == "":
            p2_nome = input('Digite o nome do produto: ')
            p2_estoque = int(input('Digite a quantidade em estoque: '))
            p2_preco = float(input('Digite o preço do produto: '))
            p2_validade = input('Digite a validade do lote: ')    
            p2_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
        elif p3_nome == "":
            p3_nome = input('Digite o nome do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            p3_validade = input('Digite a validade do lote: ')    
            p3_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')
        else:
            print('❌ Sistema cheio! Limite de 3 produtos atingido.')

    elif opcao == '2':
        print('Listando produtos do Cardápio...\n')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print('Nenhum produto cadastrado no sistema ainda.')
        else:
            # Mostra o Produto 1 se existir
            if p1_nome != "":
                print(f"Lanche/Item: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")
                print(f"Validade Lote: {p1_validade} | Descrição: {p1_descricao}")
                print('🔥' * 30)
                
            # Mostra o Produto 2 se existir
            if p2_nome != "":
                print(f"Lanche/Item: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")
                print(f"Validade Lote: {p2_validade} | Descrição: {p2_descricao}")
                print('🔥' * 30)
                
            # Mostra o Produto 3 se existir
            if p3_nome != "":
                print(f"Lanche/Item: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")
                print(f"Validade Lote: {p3_validade} | Descrição: {p3_descricao}")
                print('🔥' * 30)

    elif opcao == '3':
        print('Realizando venda...\n')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print('Não há produtos cadastrados para realizar vendas.')
        else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')
            
            # Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
            
            # Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                    
            # Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
            
            else:
                print('🔥 Erro: Produto não encontrado!')

    elif opcao == '0':
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente.')