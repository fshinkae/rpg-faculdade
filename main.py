import os
import time
import sys
from random import randint

name = input("diga o nome do seu aventureiro(a): ")
jogador = {'nome': name, 'level': 0, 'vida': 3, 'exp': 0, 'gold': 0, 'atributos': {'ataque': 3, 'defesa': 1}}

def status_jogador():
    os.system('clear')
    print(f"Seu status atual é: {jogador}")

def print_typing(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def desafio_bau():
    while True:
        print(f'{"-" * 5} Você encontrou um Bau! {"-" * 5}')
        dado_um = randint(1, 6)
        dado_dois = randint(1, 6)
        dado_tres = randint(1, 6)
        codigo_cofre = randint(1, 18)
        soma_dos_dados = dado_um + dado_dois + dado_tres

        print_typing(f"Código do baú: {codigo_cofre}\n")
        time.sleep(1)
        print("Rolando os dados...\n")
        time.sleep(1)
        print(f"Seus dados: {soma_dos_dados}\n")
        time.sleep(1)

        if soma_dos_dados == codigo_cofre:
            jogador['gold'] += 10
            jogador['exp'] += 2

            if jogador['exp'] == 4:
                jogador['level'] += 1
                jogador['exp'] = 0
                print_typing("Você ganhou!\n")
                time.sleep(0.5)
        else:
            print_typing("Você perdeu.\n")
            time.sleep(0.5)

        print('Deseja continuar explorando ou voltar?')
        print('1. Continuar explorando')
        print('2. Voltar')
        option = input('Escolha uma opção (1 ou 2): ')

        if option == '1':
            masmorra_sort()
            return
        elif option == '2':
            break
        else:
            print('Opção inválida! Tente novamente')

def desafio_monstro():
    while True:
        sorted_dice = randint(0, 100)
        if 0 <= sorted_dice <= 39:
            monstro = {'nome': 'goblin', 'vida': 5, 'ataque': 2, 'defesa': 0, 'xp': 1, 'gold': 1}
        elif 40 <= sorted_dice <= 69:
            monstro = {'nome': 'morto_vivo', 'vida': 10, 'ataque': 4, 'defesa': 1, 'xp': 3, 'gold': 3}
        elif 70 <= sorted_dice <= 89:
            monstro = {'nome': 'orc', 'vida': 15, 'ataque': 6, 'defesa': 2, 'xp': 10, 'gold': 10}
        elif 90 <= sorted_dice <= 100:
            monstro = {'nome': 'Rei Dragao', 'vida': 50, 'ataque': 10, 'defesa': 5, 'xp': 100, 'gold': 100}

        print_typing(f"Você encontrou um {monstro['nome']}!")
        print(f'{"-" * 5} Atributos Monstro {"-" * 5}')
        print(f"Vida do monstro: {monstro['vida']} | Ataque: {monstro['ataque']} | Defesa: {monstro['defesa']}")
        time.sleep(0.5)

        while monstro['vida'] > 0 and jogador['vida'] > 0:
            print('Escolha sua ação:')
            print('1. Atacar')
            print('2. Fugir')
            action = input('Escolha uma opção (1 ou 2): ')

            if action == '1':
                os.system('clear')
                damage = max(jogador['atributos']['ataque'] - monstro['defesa'], 0)
                monstro['vida'] -= damage
                print(f"Você atacou o {monstro['nome']} e causou {damage} de dano")
                print(f"Vida restante do monstro: {monstro['vida']}")

                if monstro['vida'] <= 0:
                    os.system('clear')
                    jogador['exp'] += monstro['xp']
                    jogador['gold'] += monstro['gold']
                    print(f"Você derrotou o {monstro['nome']}!")
                    print(f"Você ganhou {monstro['xp']} de experiência e {monstro['gold']} moedas")

                    xp_needed = (jogador['level'] + 1) * 1.1
                    while jogador['exp'] >= xp_needed:
                        jogador['level'] += 1
                        jogador['vida'] += 2
                        jogador['atributos']['ataque'] += 1 if jogador['level'] % 2 == 1 else 0
                        jogador['atributos']['defesa'] += 1 if jogador['level'] % 2 == 1 else 0
                        print(f"Parabéns! Você subiu para o nível {jogador['level']}!")
                        print(f"Sua vida máxima agora é {jogador['vida']}")
                        print(f"Seu ataque é {jogador['atributos']['ataque']} e sua defesa é {jogador['atributos']['defesa']}")
                        xp_needed = (jogador['level'] + 1) * 1.1
                    break

                damage = max(monstro['ataque'] - jogador['atributos']['defesa'], 0)
                jogador['vida'] -= damage
                print(f"{monstro['nome']} atacou você e causou {damage} de dano")
                print(f"Sua vida restante: {jogador['vida']}")

            elif action == '2':
                os.system('clear')
                print(f"Você fugiu da batalha contra o {monstro['nome']}")
                print(f"Cagao...")
                return

            else:
                print('Opção inválida! Tente novamente')

def masmorra_sort():
    dado_masmorra = randint(1, 8)
    if dado_masmorra < 3:
        desafio_bau()
    else:
        desafio_monstro()

if __name__ == '__main__':
    while True:
        os.system('clear')
        print("1. Ver status")
        print("2. Entrar na Masmorra")
        print("3. Sair do jogo")
        option = input("Escolha uma opção: ")
        if option == '1':
            status_jogador()
        elif option == '2':
            masmorra_sort()
        elif option == '3':
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida! Tente novamente.")