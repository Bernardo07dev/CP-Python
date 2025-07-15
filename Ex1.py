count = 0

def ler_nome():
    per_nome = input(f"Atleta {count}:")
    return per_nome

def ler_saltos(count_sal):
        per_salto = input(f"Salto {count_sal + 1}:\n")
        while not per_salto.isnumeric():
            print("Apenas números são permitidos")
            per_salto = input(f"Salto {count_sal + 1}:\n")
        per_salto = float(per_salto)
        return per_salto

def calcula_media(saltos):
    media = sum(saltos) / len(saltos)
    return sum(saltos)

def exclui_extremos(saltos):
    menor = min(saltos)
    maior = max(saltos)
    saltos.remove(menor)
    saltos.remove(maior)
    return saltos
        

medias = []
geral = []
nomes = []

while True:
    saltos = []
    count += 1
    print("---CLQIUE ENTER PARA VER OS RESULTADOS---")
    atleta = ler_nome()
    if atleta == "":
        break
    nomes.append(atleta)
    for i in range(0,5):
        salto = ler_saltos(i)
        saltos.append(salto)
    saltos_final = exclui_extremos(saltos)
    geral.append(saltos_final)
    media = calcula_media(saltos_final)
    medias.append(media)

index_campeao = medias.index(max(medias))

for i  in range(count - 1):
     print(f"{nomes[i]}\n"
           f"Saltos Considerados: {geral[i]}\n"
           f"Média: {medias[i]}\n")
    
print(f"---O campeão foi:---\n"
      f"{nomes[index_campeao].upper()}\n")
