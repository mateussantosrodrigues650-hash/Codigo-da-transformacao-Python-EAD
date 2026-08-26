"""
>PO (como dono do negocio:quero um aplicativo de vendas para minha Hamburgueria
para que eu possa controlar as  e os produtos.)

>QA (como cliente: quero um sistema de vendas para minha Hamburgueria, 
para que eu possa comprar meus produtos de forma rápida e fácil.)

>Teach (como programador: quero um sistema de vendas para minha Hamburgueria,
para que eu possa desenvolver um aplicativo eficiente e funcional para o negocio.)

>Dev (como programador:quero um sistema de vendas para minha Hamburgueria,
para que eu possa implementar as funcionalidades necessarias para atender
as necessidades do negocio e dos clientes.)

>UX (como designer de experiencia do usario:Quero um sistema de 
vendas para minha Hamburgueria,para que eu possa criar uma interface
intuitiva e agradavel para os usuarios, garantindo uma experiencia
de compra satisfatoria.)

>IA (como analista de dados:Quero um sistema de vendas para minha
Hamburgueria, para que eu possa coletar e analisar os dados de vendas,
ajudando a identificar padrões de consumo e otimizar as
estrategias de marketing e estoque.)
"""

import tkinter as tk
from tkinter import messagebox, simpledialog

produtos = []
faturamento_total = 0.0
cupom_desconto = 0.0
taxa_entrega = 5.0
status_pedido = "Nenhum pedido feito"

def cadastrar_produto():
    nome = simpledialog.askstring("🍔 Cadastrar", "Digite o nome do produto (ex: X-Burger):")
    if not nome: return
    
    try:
        estoque = simpledialog.askinteger("📦 Estoque", f"Quantidade em estoque para {nome}:")
        if estoque is None: return
        
        preco_texto = simpledialog.askstring("💰 Preço", f"Preço de venda para {nome}: R$")
        if preco_texto is None: return
        preco_texto = preco_texto.replace(",", ".")
        preco = float(preco_texto)
        
        descricao = simpledialog.askstring("📝 Descrição", f"Descrição de {nome}:")
        if descricao is None: return
        
        novo_produto = {
            "nome": nome,
            "estoque": estoque,
            "preco": preco,
            "descricao": descricao
        }
        produtos.append(novo_produto)
        
        messagebox.showinfo("🎉 Sucesso", f"'{nome}' adicionado ao cardápio com sucesso!")
        atualizar_painel()
    except ValueError:
        messagebox.showerror("❌ Erro", "Preço inválido! Digite apenas números.")

def listar_produtos():
    if not produtos:
        messagebox.showinfo("📋 Cardápio", "Nenhum produto cadastrado até o momento.")
        return
    
    info = "✨ --- CARDÁPIO FABULOSO --- ✨\n\n"
    for p in produtos:
        preco_final = p["preco"] - cupom_desconto
        if preco_final < 0: preco_final = 0
        info += f"🍔 Produto: {p['nome']}\n💵 Preço: R$ {p['preco']:.2f} (Promo: R$ {preco_final:.2f})\n📦 Estoque: {p['estoque']} un\n📝 Descrição: {p['descricao']}\n-----------------------------------\n"
    
    messagebox.showinfo("📋 Cardápio Completo", info)

def realizar_venda():
    global faturamento_total, status_pedido
    if not produtos:
        messagebox.showerror("❌ Erro", "Não há produtos cadastrados para vender.")
        return
    
    lista_nomes = "\n".join([f"[{i}] {p['nome']} (Estoque: {p['estoque']})" for i, p in enumerate(produtos)])
    num_produto = simpledialog.askinteger("🛍️ Venda", f"Escolha o número do produto:\n\n{lista_nomes}")
    
    if num_produto is None: return
    
    if 0 <= num_produto < len(produtos):
        p = produtos[num_produto]
        if p["estoque"] <= 0:
            messagebox.showerror("❌ Erro", f"O estoque de {p['nome']} esgotou!")
            return
            
        qtd = simpledialog.askinteger("🛍️ Venda", f"Quantos {p['nome']} deseja vender?")
        if qtd is None: return
        
        if qtd <= p["estoque"]:
            p["estoque"] -= qtd
            preco_final = p["preco"] - cupom_desconto
            if preco_final < 0: preco_final = 0
            total = qtd * preco_final
            faturamento_total += total
            status_pedido = f"🔥 Na chapa: {qtd}x {p['nome']}"
            
            messagebox.showinfo("✅ Venda Realizada", f"🎉 Sucesso! Venda concluída!\n💰 Total: R$ {total:.2f}")
            atualizar_painel()
        else:
            messagebox.showerror("❌ Erro", f"Estoque insuficiente. Temos apenas {p['estoque']} unidades.")
    else:
        messagebox.showerror("❌ Erro", "Opção de produto inválida.")

def ver_faturamento():
    messagebox.showinfo("📈 Faturamento", f"💰 O faturamento total acumulado é: R$ {faturamento_total:.2f}")

def adicionar_estoque():
    if not produtos:
        messagebox.showerror("❌ Erro", "Não há produtos cadastrados.")
        return
        
    lista_nomes = "\n".join([f"[{i}] {p['nome']} (Estoque: {p['estoque']})" for i, p in enumerate(produtos)])
    num_produto = simpledialog.askinteger("📦 Reabastecer", f"Escolha o número do produto:\n\n{lista_nomes}")
    
    if num_produto is None: return
    
    if 0 <= num_produto < len(produtos):
        qtd = simpledialog.askinteger("📦 Reabastecer", f"Quantas unidades deseja adicionar ao {produtos[num_produto]['nome']}?")
        if qtd is None: return
        produtos[num_produto]["estoque"] += qtd
        messagebox.showinfo("✅ Sucesso", f"Estoque de {produtos[num_produto]['nome']} reabastecido!")
        atualizar_painel()
    else:
        messagebox.showerror("❌ Erro", "Produto não encontrado.")

def alterar_preco():
    if not produtos:
        messagebox.showerror("❌ Erro", "Não há produtos cadastrados.")
        return
        
    lista_nomes = "\n".join([f"[{i}] {p['nome']} (Preço: R$ {p['preco']:.2f})" for i, p in enumerate(produtos)])
    num_produto = simpledialog.askinteger("💵 Mudar Preço", f"Escolha o número do produto:\n\n{lista_nomes}")
    
    if num_produto is None: return
    
    if 0 <= num_produto < len(produtos):
        novo_preco = simpledialog.askfloat("💵 Mudar Preço", f"Digite o novo preço para {produtos[num_produto]['nome']}: R$")
        if novo_preco is None: return
        produtos[num_produto]["preco"] = novo_preco
        messagebox.showinfo("✅ Sucesso", "Preço atualizado com sucesso!")
        atualizar_painel()
    else:
        messagebox.showerror("❌ Erro", "Produto não encontrado.")

def criar_cupom():
    global cupom_desconto
    valor = simpledialog.askfloat("🎟️ Cupom", "Digite o valor em R$ do desconto para o cardápio:")
    if valor is None: return
    cupom_desconto = valor
    messagebox.showinfo("🎟️ Cupom Ativado", f"Desconto de R$ {cupom_desconto:.2f} aplicado em todos os produtos!")
    atualizar_painel()

def consultar_entrega():
    global taxa_entrega
    mudar = messagebox.askyesno("Taxa de Entrega", f"A taxa de entrega atual é R$ {taxa_entrega:.2f}.\nDeseja alterar?")
    if mudar:
        nova_taxa = simpledialog.askfloat("Taxa", "Digite a nova taxa de entrega: R$")
        if nova_taxa is None: return
        taxa_entrega = nova_taxa
        messagebox.showinfo("✅ Sucesso", "Taxa do motoboy atualizada!")

def ver_status():
    global status_pedido
    nova_op = simpledialog.askstring("👨‍🍳 Status do Pedido", 
        f"Status Atual: {status_pedido}\n\nDigite o número do novo status:\n1 - 🍳 Na Cozinha / Chapa\n2 - 🏍️ Saiu para Entrega\n3 - 🤝 Entregue com Sucesso")
    
    if nova_op == '1': status_pedido = "🍳 Na Cozinha / Chapa"
    elif nova_op == '2': status_pedido = "🏍️ Saiu para Entrega"
    elif nova_op == '3': status_pedido = "🤝 Entregue com Sucesso"
    
    atualizar_painel()

def atualizar_painel():
    lbl_prod.config(text=f"🍔 Itens Diferentes Cadastrados: {len(produtos)}")
    lbl_status.config(text=f"Status Atual: {status_pedido}")
    
    txt_cardapio.config(state=tk.NORMAL)
    txt_cardapio.delete("1.0", tk.END)
    if not produtos:
        txt_cardapio.insert(tk.END, "⚠️ Nenhum hambúrguer ou acompanhamento cadastrado. Clique no botão 1 para começar!")
    else:
        for p in produtos:
            txt_cardapio.insert(tk.END, f"👑 {p['nome']}  |  💵 R$ {p['preco']:.2f}  |  📦 Estoque: {p['estoque']} un  ({p['descricao']})\n")
    txt_cardapio.config(state=tk.DISABLED)

# Cores Fabulosas da Identidade Visual
COR_FUNDO = "#FFF8F0"        
COR_TITULO = "#D9381E"       
COR_BOTOES_GERAIS = "#FFB000" 
COR_TEXTO = "#4A2E2B"        
COR_PAINEL = "#F7E6D4"       

janela = tk.Tk()
janela.title("Hamburgueria Fabulosa - Painel de Vendas")
janela.geometry("800x650")
janela.configure(bg=COR_FUNDO)

# Título Principal Estilizado
lbl_titulo = tk.Label(janela, text="🍔 HAMBURGUERIA FABULOSA ✨", font=("Impact", 28), fg=COR_TITULO, bg=COR_FUNDO)
lbl_titulo.pack(pady=15)

# Container do topo com Resumos
frame_info = tk.LabelFrame(janela, text=" 📊 Monitoramento em Tempo Real ", font=("Arial", 11, "bold"), fg=COR_TEXTO, bg=COR_PAINEL, padx=15, pady=10)
frame_info.pack(fill="x", padx=20, pady=5)

lbl_prod = tk.Label(frame_info, text="🍔 Itens Diferentes Cadastrados: 0", font=("Arial", 12, "bold"), fg=COR_TEXTO, bg=COR_PAINEL)
lbl_prod.pack(anchor="w")

lbl_status = tk.Label(frame_info, text="Status Atual: Nenhum pedido feito", font=("Arial", 12, "bold"), fg="#1E6B7B", bg=COR_PAINEL)
lbl_status.pack(anchor="w")

# Visor do Cardápio
lbl_visor_titulo = tk.Label(janela, text="📋 Nosso Cardápio Atual:", font=("Arial", 12, "bold"), fg=COR_TEXTO, bg=COR_FUNDO)
lbl_visor_titulo.pack(anchor="w", padx=20, pady=(10, 0))

txt_cardapio = tk.Text(janela, height=6, font=("Courier New", 11, "bold"), fg=COR_TEXTO, bg="#FFFFFF", bd=2, relief="groove", state=tk.DISABLED)
txt_cardapio.pack(fill="x", padx=20, pady=5)

# Seção de Botões em Grid
frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack(pady=10)

# Botões com comandos ativados (command=...)
tk.Button(frame_botoes, text="➕ 1 - Cadastrar Produto", width=34, height=2, font=("Arial", 11, "bold"), bg=COR_BOTOES_GERAIS, fg="black", activebackground="#E69D00", relief="raised", command=cadastrar_produto).grid(row=0, column=0, padx=15, pady=8)
tk.Button(frame_botoes, text="📋 2 - Detalhes do Cardápio", width=34, height=2, font=("Arial", 11, "bold"), bg=COR_BOTOES_GERAIS, fg="black", activebackground="#E69D00", relief="raised", command=listar_produtos).grid(row=0, column=1, padx=15, pady=8)

tk.Button(frame_botoes, text="🛍️ 3 - Realizar Venda", width=34, height=2, font=("Arial", 12, "bold"), bg="#28A745", fg="white", activebackground="#218838", relief="raised", command=realizar_venda).grid(row=1, column=0, padx=15, pady=8)
tk.Button(frame_botoes, text="📈 4 - Faturamento Total", width=34, height=2, font=("Arial", 11, "bold"), bg=COR_BOTOES_GERAIS, fg="black", activebackground="#E69D00", relief="raised", command=ver_faturamento).grid(row=1, column=1, padx=15, pady=8)

tk.Button(frame_botoes, text="📦 5 - Reabastecer Estoque", width=34, height=2, font=("Arial", 11, "bold"), bg=COR_BOTOES_GERAIS, fg="black", activebackground="#E69D00", relief="raised", command=adicionar_estoque).grid(row=2, column=0, padx=15, pady=8)
tk.Button(frame_botoes, text="💵 6 - Alterar Preço do Item", width=34, height=2, font=("Arial", 11, "bold"), bg=COR_BOTOES_GERAIS, fg="black", activebackground="#E69D00", relief="raised", command=alterar_preco).grid(row=2, column=1, padx=15, pady=8)

tk.Button(frame_botoes, text="🎟️ 7 - Ativar Cupom de Desconto", width=34, height=2, font=("Arial", 11, "bold"), bg=COR_BOTOES_GERAIS, fg="black", activebackground="#E69D00", relief="raised", command=criar_cupom).grid(row=3, column=0, padx=15, pady=8)
tk.Button(frame_botoes, text="🏍️ 8 - Taxa do Motoboy", width=34, height=2, font=("Arial", 11, "bold"), bg=COR_BOTOES_GERAIS, fg="black", activebackground="#E69D00", relief="raised", command=consultar_entrega).grid(row=3, column=1, padx=15, pady=8)

tk.Button(frame_botoes, text="👨‍🍳 9 - Atualizar Status do Pedido", width=34, height=2, font=("Arial", 11, "bold"), bg="#17A2B8", fg="white", activebackground="#138496", relief="raised", command=ver_status).grid(row=4, column=0, columnspan=2, pady=8)

# Botão Sair
tk.Button(janela, text="❌ 0 - Fechar Sistema", width=28, height=2, font=("Arial", 12, "bold"), bg="#DC3545", fg="white", activebackground="#C82333", relief="solid", command=janela.quit).pack(pady=10)

atualizar_painel()
janela.mainloop()