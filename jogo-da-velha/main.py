import time
import apresent as ap
import os

def tabuleiro2(elemento: list) -> None:
    # os.system("clear")
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print('-'*10)
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print('-'*10)
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")

# teste de tabuleiro gerado
def tabuleiro(elemento: list) -> None:
    tabuleiro_mont = ""
    for i in range(0,9):
        if(i == 2 or i == 5 or i == 8):
            pula = " \n"
            if(i ==2 or i == 5):
                print('-'*10)
        else:
            pula = " | "
        tabuleiro_mont += f"{elemento[i]} {pula}"
        print(tabuleiro_mont)

# apresenta o jogo
print(ap.apresentacao)

# comando para carregamento do jogo
input("Pressione Enter para começar:")
os.system("clear")
print("carregando...")
time.sleep(1)

def nome_jogador(simbolo: str, numero: int) -> str:
    # verifica jogador valido
    while True:
        nome_jogador = str(input(f"\nJogador {numero}({simbolo}), digite seu nome: ").title())
        if nome_jogador != "":
            os.system("clear")
            return [nome_jogador, numero, simbolo]
        print("Nome invalido, digite novamente:")

os.system("clear")
jogadores = nome_jogador(" O ", 1),nome_jogador(" X ", 2)

def checar_resultado(elemento: list) -> bool:
    # Vitória na horizontal
    for i in range(len(elemento) - 6, len(elemento), 3):
        if(elemento[i - 2] == elemento[i - 1]):
            if(elemento[i - 1] == elemento[i] != " "):
                return True
            
    # Vitória na vertical            
    for i in range(len(elemento) - 6,len(elemento) - 3):
        if(elemento[i - 3] == elemento[i]):
            if(elemento[i] == elemento[i + 3] != " "):
                return True
            
    # Vitórias na diagonal
    if elemento[0] == elemento[4] == elemento[8] != " ":
        return True

    if elemento[2] == elemento[4] == elemento[6] != " ":
        return True

    return False

def checar_empate(elemento: list) -> bool:
    """Se existe um elemento em branco no tabuleiro, há um empate"""
    return " " not in elemento


def rodada(elemento: list, num_jogador: int, num_rodada: int, jogador: list) -> None:
    """Método "principal" que recebe inúmeros argumentos e
    implementa as outras funções"""
    simbolo = "O" if num_jogador == 1 else "X"

    complemento = ""
    while(True):
        tabuleiro(elemento)
        print(complemento)
        jogada = input(f"Rodada {num_rodada}! {jogador[0], jogador[2]}, digite o número da casa que deseja jogar: ")
        os.system("clear")

        if(jogada.isnumeric()):
            jogada = int(jogada)

            # É usado o range(1, 10) e não o range(9), pois o tabuleiro começa em 0
            if jogada in range(1, 10):

                # O -1 é usado, pois, o range começa em 1, e a lista começa em 0.
                if elemento[jogada - 1] == " ":
                    elemento[jogada - 1] = simbolo
                    break
                else:
                    complemento = "Casa ocupada, escolha outra"

            else:
                complemento = "Jogada inválida, escolha outra"
        else:
            complemento = " \" {} \": não é um numero inteiro".format(jogada)


elemento_do_jogo = [" "] * 9

# Se o contador for par, é a vez do jogador 1, senão, é a vez do jogador 2
for num_rodada_atual in range(1, 10):
    contador_jogador = num_rodada_atual - 1

    # O operador not serve para inverter o valor entre 0 e 1,
    # ou seja, se o contador for par, o número do jogador é 1, e vice-versa
    jogador_atual = jogadores[num_rodada_atual % 2]
    
    
    rodada(elemento_do_jogo, jogador_atual[1], num_rodada_atual, jogador_atual)

    # if checar_vitoria(elemento_do_jogo):
    if checar_resultado(elemento_do_jogo):
        tabuleiro(elemento_do_jogo)

        print(f"{jogador_atual[0], jogador_atual[2]} venceu!, Parabéns você venceu na {num_rodada_atual}ª rodada!")

        time.sleep(2)
        break

    if checar_empate(elemento_do_jogo):
        print("Empate!")
        break

    time.sleep(0.5)

print(ap.finalizacao)
print("Obrigado por jogar")