def calcular_media(notas):
    if not notas:
        print("Nenhuma nota fornecida.")
        return
    
    media = sum(notas) / len(notas)
    
    if media >= 7.0:
        print(f"Média: {media:.2f} - Status: Aprovado!")
    else:
        print(f"Média: {media:.2f} - Status: Reprovado.")

calcular_media([8.0, 7.5, 6.0])