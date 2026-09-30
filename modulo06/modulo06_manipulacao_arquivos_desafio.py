import os
import shutil

def realizar_backup(pasta_origem, pasta_destino):
    os.makedirs(pasta_origem, exist_ok=True)
    os.makedirs(pasta_destino, exist_ok=True)

    arquivos = os.listdir(pasta_origem)

    if not arquivos:
        print("Nenhum arquivo encontrado para realizar backup.")
        return

    for arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)

        if os.path.isfile(caminho_origem):
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"✓ Backup de '{arquivo}' concluído com sucesso!")

origem = "meus_documentos"
destino = "backup_documentos"

realizar_backup(origem, destino)