import csv
import os
import shutil


def sistema_notas_csv():
    print("\n--- 3. Sistema de Notas em CSV ---")
    arquivo_csv = "notas_alunos.csv"
    
   
    if not os.path.exists(arquivo_csv):
        with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nome", "Disciplina", "Nota"])
            
    while True:
        print("\n[1] Adicionar Nota | [2] Exibir Notas Cadastradas | [3] Voltar")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            nome = input("Nome do aluno: ").strip()
            disciplina = input("Disciplina: ").strip()
            try:
                nota = float(input("Nota: "))
                with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([nome, disciplina, nota])
                print(f"Nota de {nome} salva com sucesso em '{arquivo_csv}'!")
            except ValueError:
                print("Por favor, insira um valor numérico válido para a nota.")
                
        elif opcao == '2':
            print("\n--- NOTAS CADASTRADAS ---")
            if os.path.exists(arquivo_csv):
                with open(arquivo_csv, mode="r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    linhas = list(reader)
                    if len(linhas) <= 1:
                        print("Nenhuma nota cadastrada até o momento.")
                    else:
                        for row in linhas:
                            print(f"{row[0]:<20} | {row[1]:<15} | {row[2]}")
            else:
                print("Arquivo de notas não encontrado.")
                
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")

def sistema_backup():
    print("\n--- Desafio Extra: Backup Automático ---")
    pasta_origem = input("Digite o caminho/nome da pasta de ORIGEM: ").strip()
    pasta_destino = input("Digite o caminho/nome da pasta de DESTINO (Backup): ").strip()
    
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe.")
        return
        
   
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    arquivos_copiados = 0
    
    for item in os.listdir(pasta_origem):
        caminho_item = os.path.join(pasta_origem, item)
        if os.path.isfile(caminho_item):
            shutil.copy2(caminho_item, pasta_destino)
            print(f"Copiado: {item} -> {pasta_destino}")
            arquivos_copiados += 1
            
    print(f"\nBackup concluído! Total de {arquivos_copiados} arquivo(s) copiado(s).")


def main():
    while True:
        print("\n=================================")
        print("    MANIPULAÇÃO DE ARQUIVOS     ")
        print("=================================")
        print("1 - Sistema de Notas (CSV)")
        print("2 - Desafio Extra (Backup Automático)")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            sistema_notas_csv()
        elif escolha == '2':
            sistema_backup()
        elif escolha == '0':
            print("Encerrando o programa!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()