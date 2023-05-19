import os

# colored text
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

def showDescription():
    os.system('cls')
    print("| / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / |")
    print("|                                                                                                                       |")
    print(f'|        🍀 O {Fore.GREEN}Lucky Numbers {Fore.WHITE}é um jogo de tabuleiro no qual o jogador precisa de formar uma sequência crescente          |\n|         de números, tanto na horizontal quanto na vertical. A cada jogada é fornecido um novo número, exceto          |\n|         quando o jogador não coloca o número atribuído na jogada anterior ou troca com um número já presente          |\n|         no tabuleiro. Quando isso acontece, o número substituído é colocado em uma mesa separada, que  ambos          |\n|         os jogadores têm acesso e podem utilizar para futuras trocas, caso seja conveniente.                          |')
    print("|                                                                                                                       |")
    print("| / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / |")
    input("Pressione uma tecla para continuar...")
    os.system('cls') 