from random import randint
import os

name = ""
level = 0
xp = 0
life = 3
gold = 0
number_tentatives = 0

name = input("Digite o nome do seu aventureiro: \n")

print(f'Ficha de {name}')
print(f'Nível: {level}')
print(f'Vida: {life}')
print(f'Experiência: {xp}')

print(f'Bem-vindo, {name}! Sua jornada começa agora. \n')

while True:

    if life == 0:
        os.system('cls')
        print(f'Ficha de {name}')
        print(f'Nível: {level}')
        print(f'Experiência: {xp}')
        print(f'Vida: {life}')
        print("Você Perdeu \n")
        break

    print("Faça sua escolha:")
    print("1 - Entrar na masrmorra")
    print("2 - Sair do Jogo")
    print("Digite sua opção: ")
    option = int(input())

    if option == 1:
        while True:
            if life == 0:
                os.system('cls')
                print("Você Perdeu \n")
                break

            if number_tentatives == 2:
                os.system('cls')
                print(f'Você perdeu uma vida, vidas restantes: {life}')
                number_tentatives = 0
                life -= 1

            dice_one = randint(1, 6)
            dice_two = randint(1, 6)
            dice_three = randint(1, 6)
            safe_code = randint(1, 18)
            sum_of_dices = dice_one + dice_two + dice_three

            if sum_of_dices == safe_code:
                gold += 10
                xp += 2

                if xp == 4:
                    level += 1
                    xp == 0

                os.system('cls')
                print(
                    f"Você ganhou, código do baú: {safe_code}, Seus dados: {sum_of_dices}, Numero deTentativas {number_tentatives} \n")
                print(f"Tentar de novo? 1 - Sim ; 2 - Não")

                option_game = int(input())
                if option_game == 2:
                    break
            else:
                os.system('cls')
                print(
                    f"Você perdeu, código do baú: {safe_code}, Seus dados: {sum_of_dices}, Numero deTentativas {number_tentatives} \n")
                number_tentatives += 1
                print(f"Tentar de novo? 1 - Sim ; 2 - Não")
                option_game = int(input())

                if option_game == 2:
                    break

    if option == 2:
        os.system('cls')
        print(f'Ficha de {name}')
        print(f'Nível: {level}')
        print(f'Experiência: {xp}')
        print(f'Vida: {life}')
        print("Você saiu do jogo... \n")
        break