from os import system
from random import randint

lvl = 1
xp_player = 0
life = 5
attack = 3
defense = 1
gold_player = 0
actual_life = life
monster_name = ""
life_monster = 0
attack_monster = 0
defense_monster = 0

print("Digite seu nome, Jogador: ")
name = str(input())
system('clear')
print(f'Nome: {name}')
print(f'Nível: {lvl}')
print(f'{"-"*5} Atributos Jogador {"-"*5}')
print(f'Vida: {life}')
print(f'Ataque: {attack}')
print(f'Defesa: {defense}')

while life > 0:
    system('clear')
    print(f'Bem-vindo à Caverna, {name}!')
    print('1. Entrar na caverna')
    print('2. Sair da caverna')
    option = input('Escolha uma opção (1 ou 2): ')

    if option == '2':
        break

    if option == '1':
        sorted_dice = randint(0, 100)
        if 0 <= sorted_dice <= 39:
            monster_name = "Monstro Fraco"
            life_monster = 5
            attack_monster = 2
            defense_monster = 0
            xp = 1
            gold = 1

        elif 40 <= sorted_dice <= 69:
            monster_name = "Monstro Médio"
            life_monster = 10
            attack_monster = 4
            defense_monster = 1
            xp = 3
            gold = 3

        elif 70 <= sorted_dice <= 89:
            monster_name = "Monstro Difícil"
            life_monster = 15
            attack_monster = 6
            defense_monster = 2
            xp = 10
            gold = 10

        elif 90 <= sorted_dice <= 100:
            monster_name = "Boss"
            life_monster = 50
            attack_monster = 10
            defense_monster = 5
            xp = 100
            gold = 1

        system('clear')
        print(f'Você encontrou um {monster_name}!')
        print(f'{"-"*5} Atributos Monstro {"-"*5}')
        print(f'Vida do monstro: {life_monster} | Ataque: {attack_monster} | Defesa: {defense_monster}')

        while life_monster > 0 and life > 0:
            print('Escolha sua ação:')
            print('1. Atacar')
            print('2. Fugir')
            action = input('Escolha uma opção (1 ou 2): ')

            if action == '1':
                system('clear')
                damage = max(attack - defense_monster, 0)
                life_monster -= damage
                print(f'Você atacou o {monster_name} e causou {damage} de dano')
                print(f'Vida restante do monstro: {life_monster}')

                if life_monster <= 0:
                    system('clear')
                    xp_player += xp
                    gold_player += gold
                    print(f'Você derrotou o {monster_name}!')
                    print(f'Você ganhou {xp} de experiência e {gold} moedas')

                    xp_needed = (lvl + 1) * 1.1
                    while xp_player >= xp_needed:
                        lvl += 1
                        life += 2
                        attack += 1 if lvl % 2 == 1 else 0
                        defense += 1 if lvl % 2 == 1 else 0
                        print(f'Parabéns! Você subiu para o nível {lvl}!')
                        print(f'Sua vida máxima agora é {life}')
                        print(f'Seu ataque é {attack} e sua defesa é {defense}')
                        xp_needed = (lvl + 1) * 1.1

                    actual_life = life
                    break

                damage = max(attack_monster - defense, 0)
                life -= damage
                print(f'{monster_name} atacou você e causou {damage} de dano')
                print(f"Sua vida restante: {life}")

            elif action == '2':
                system('clear')
                print(f'Você fugiu da batalha contra o {monster_name}')
                break

            else:
                print('Opção inválida! Tente novamente')

        if life > 0:
            system('clear')
            print(f'{"-"*5} Atributos Jogador {"-"*5}')
            print(f'Nome: {name}')
            print(f'Nível: {lvl}')
            print(f'Vida: {actual_life}/{life}')
            print(f'Ataque: {attack}')
            print(f'Defesa: {defense}')
            print(f'Experiência: {xp_player}')
            print(f'Moedas: {gold_player}')
            print('{"-"*5}Deseja continuar explorando ou sair da caverna?{"-"*5}')
            print('1. Continuar explorando')
            print('2. Sair da caverna')
            option = input('Escolha uma opção (1 ou 2): ')

            if option == '2':
                break
    else:
        print('Opção inválida! Tente novamente')

system('clear')
print('Jogo encerrado')
print(f'{"-"*5} Atributos Jogador {"-"*5}')
print(f'Nome: {name}')
print(f'Nível: {lvl}')
print(f'Vida: {actual_life}/{life}')
print(f'Ataque: {attack}')
print(f'Defesa: {defense}')
print(f'Experiência: {xp_player}')
print(f'Moedas: {gold_player}')