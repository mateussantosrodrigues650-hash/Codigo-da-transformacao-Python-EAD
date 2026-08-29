def maior_menor(numeros):
    if not numeros:
        return None, None
    
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

lista_numeros = [15, 3, 42, 8, 23, 1]
max_val, min_val = maior_menor(lista_numeros)
print(f"Maior valor: {max_val} | Menor valor: {min_val}")
