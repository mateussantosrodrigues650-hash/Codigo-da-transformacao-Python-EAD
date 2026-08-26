# 🍔 Hamburgueria Fabulosa - Sistema de Vendas v2.0

![Python](https://img.shields.io/badge/Python-3.x-URGENT?style=for-the-badge&logo=python&logoColor=white&color=FFB000)
![Tkinter](https://img.shields.io/badge/Interface-Tkinter-blue?style=for-the-badge&logo=python&logoColor=white&color=D9381E)

Um sistema completo de gerenciamento e faturamento para balcão e delivery, desenvolvido com interface gráfica (GUI) em Python utilizando a biblioteca *Tkinter*. 

Este aplicativo foi estruturado com base nas metodologias ágeis de desenvolvimento, atendendo aos requisitos e visões de múltiplos envolvidos no negócio (PO, QA, Tech/Dev, UX e IA).

---

## 🎯 Visão do Projeto (Histórias de Usuário)

O projeto foi construído para satisfazer as seguintes necessidades:
* *👑 Product Owner (PO):* Ter controle total do estoque de produtos e monitorar o faturamento do negócio em tempo real.
* *🛍️ Cliente (QA):* Um sistema rápido e fácil de usar para selecionar produtos e fazer compras sem complicações.
* *👨‍💻 Dev / Instructor (Teach):* Desenvolver um código limpo, eficiente, bem estruturado com tratamento de dados e uso de listas de dicionários.
* *🎨 Designer (UX):* Proporcionar uma interface atraente, intuitiva e com cores temáticas de lanchonete (Vermelho Catchup e Amarelo Mostarda).
* *📈 Analista de Dados (IA):* Coletar dados operacionais de vendas para planejar estratégias futuras de estoque e marketing.

---

## ✨ Funcionalidades do Sistema

1. **🍔 Cadastro Inteligente de Produtos:** Permite adicionar vários itens ao cardápio definindo nome, estoque, descrição e preço (com tratamento automático para aceitar tanto pontos quanto vírgulas!).
2. **📋 Monitoramento em Tempo Real:** Painel superior e visor de texto central atualizados instantaneamente a cada ação.
3. **🛍️ Realização de Vendas:** Venda baseada no índice do produto, dando baixa automática no estoque.
4. **📈 Controle de Faturamento:** Acumula os valores vendidos para exibir o faturamento total da lanchonete.
5. **📦 Gestão de Estoque:** Opção direta para reabastecer as unidades de qualquer item cadastrado.
6. **🎟️ Cupons de Desconto:** Aplicação de cupons de desconto (em R$) aplicados de forma geral em todo o cardápio.
7. **🏍️ Configuração de Delivery:** Consulta e alteração rápida do valor da taxa de entrega do motoboy.
8. **👨‍🍳 Atualização do Status do Pedido:** Alteração visual do progresso do pedido (Na Chapa, Saiu para Entrega, Entregue).

---

## 🎨 Identidade Visual (Design de Interface)

A interface utiliza elementos visuais focados na experiência do usuário (UX):

* **Fundo Principal (`#FFF8F0`):** Tom creme claro para dar conforto visual.
* **Título Principal (`#D9381E`):** Vermelho Catchup em destaque com fonte robusta (Impact).
* **Botões de Comando (`#FFB000`):** Amarelo Ouro de alta visibilidade com Emojis indicativos.
* **Caixa do Cardápio (`#FFFFFF`):** Visor limpo com fonte estilo máquina de escrever (Courier New) para simular uma comanda real.

---

## 🛠️ Como Executar o Projeto

Como o sistema utiliza apenas bibliotecas nativas do Python (*Tkinter*), não há necessidade de instalar dependências externas via pip.

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Salve o código Python do sistema na mesma pasta (ex: `main.py`).
3. Abra o terminal ou prompt de comando na pasta e execute:

```bash
python main.py