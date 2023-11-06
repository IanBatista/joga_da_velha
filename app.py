def verificar_ganhador(tab):
    for linha in range(3):
        if tab[linha][0] == tab[linha][1] == tab[linha][2] != 0:
            return tab[linha][0]

    for coluna in range(3):
        if tab[0][coluna] == tab[1][coluna] == tab[2][coluna] != 0:
            return tab[0][coluna]

    if tab[0][0] == tab[1][1] == tab[2][2] != 0:
        return tab[0][0]

    if tab[0][2] == tab[1][1] == tab[2][0] != 0:
        return tab[0][2]

    return 0

def verificar_empate(tab):
    for linha in range(3):
        for coluna in range(3):
            if tab[linha][coluna] == 0:
                return False

    return True

def main():
    jogadores = int(input("Quantos jogadores? "))

    tabuleiro = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

    while True:
        for linha in range(3):
            for coluna in range(3):
                print(tabuleiro[linha][coluna], end=' ')

            print()

        print("")

        if jogadores == 1:
            while True:
                posicao = int(input("Escolha uma posição (1-9): ")) - 1

                linha, coluna = divmod(posicao, 3)

                if tabuleiro[linha][coluna] == 0:
                    tabuleiro[linha][coluna] = 1
                    break
                else:
                    print("Posição ocupada. Tente novamente.")
        else:
            while True:
                posicao = int(input("Escolha uma posição (1-9): ")) - 1

                linha, coluna = divmod(posicao, 3)

                if tabuleiro[linha][coluna] == 0:
                    tabuleiro[linha][coluna] = 1
                    break
                else:
                    print("Posição ocupada. Tente novamente.")

            print("")
            print("É a vez do jogador 2.")

        if verificar_ganhador(tabuleiro) != 0:
            print("Parabéns! O jogador", verificar_ganhador(tabuleiro), "ganhou!")
            break
        elif verificar_empate(tabuleiro):
            print("O jogo terminou em empate!")
            break

main()