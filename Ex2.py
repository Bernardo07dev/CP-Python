def ler_voto():
    while True:
        voto = input("Digite o número e escolha o melhor sistema:\n"
                    "1 - Windows Server\n"
                    "2 - Unix\n"
                    "3 - Linux\n"
                    "4 - Netware\n"
                    "5 - Mac OS\n"
                    "6 - Outro\n")
        if not voto.isnumeric():
            print("Apenas números de 1 a 6 são válidos")
        else:
            voto = int(voto)
            if voto > 6:
                print("Apenas números de 1 a 6 são válidos")
            else:
                return voto
            

sistemas = ("Windows Server", "Unix", "Linux", "Netware", "MAC Os", "Outro")
votos = [0,0,0,0,0,0]

while True:
    print("---CLIQUE EM 0 PARA FINALIZAR A VOTAÇÃO---")
    voto = ler_voto()
    if voto == 0:
        break
    else:
        votos[voto - 1] += 1

indice_vencedor = votos.index(max(votos))

print("---RESULTADO VOTAÇÃO---")

for i in range(0,6):
    print(f"{sistemas[i]} - {votos[i]}")

print(f"O vencedor foi {sistemas[indice_vencedor]} com {votos[indice_vencedor]} votos")

