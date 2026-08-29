
nome_arquivo = "dados_arquivo.txt"


conteudo = [
    "Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com\n",
    "Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com\n",
    "Eric Renan;17 anos;089880-100;98799;ericrenan@gmail.com\n"
]

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(conteudo)
#
print(f"✅ Arquivo '{nome_arquivo}' criado e escrito com sucesso!")


print("\n--- Lendo o conteúdo do arquivo TXT ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    print(texto)