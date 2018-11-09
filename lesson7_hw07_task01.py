import random, copy

barrel_num = 90
card_digits = 15
line_digits = 5

def gen_card():
    num_comb = random.sample(range(1, barrel_num + 1), card_digits)
    card = [sorted(num_comb[i:i + line_digits]) for i in range(0, len(num_comb), line_digits)]
    return card

def gen_barr_list():
    return random.sample(range(1, barrel_num + 1), 90)

def get_barrel(barr_list):
    return barr_list.pop()

def show_card(card):
    card = copy.deepcopy(card)
    placeholders = ' '.join(['{:>2}' for i in range(9)])
    for line in card:
        for space in ' ' * 4:
            line.insert(random.randint(0, len(line) - 1), space)
    return [placeholders.format(*line) for line in card]

def update_card(card, barrel):
    for line in card:
        yield ['-' if x == barrel else x for x in line]

def is_empty(card):
    for line in card:
        for elt in line:
            if elt != '-':
                return False
    return True

def barr_in_card(card, barrel):
    return barrel in [barrel for line in card for barrel in line]

def game():
    player_card, comp_card = gen_card(), gen_card()
    barrels = gen_barr_list()
    while True:
        next_barrel = get_barrel(barrels)
        print('Новый бочонок: {}. Оставшиеся бочонки: {}'.format(next_barrel, len(barrels)))
        print("{0} Карточка пользователя {0}\n{1}\n{2}\n{3}".format('-' * 6, *show_card(player_card)))
        print("{0} Карточка компьютера {0}\n{1}\n{2}\n{3}".format('-' * 5, *show_card(comp_card)))
        answ = 'a'
        while answ not in 'ynq':
            answ = input("Номер бочонка есть в карточке пользователя? Наберите y/n или q для выхода из игры: ")
        if answ == 'q':
            break
        elif (answ == 'y' and barr_in_card(player_card, next_barrel)) or (answ == 'n' and not barr_in_card(player_card, next_barrel)):
            print("Вы угадали!!! \n\nСледующий ход")
        else:
            print("Вы проиграли!!!")
            break
        player_card = list(update_card(player_card, next_barrel))
        comp_card = list(update_card(comp_card, next_barrel))
        if is_empty(player_card):
            print('Ты заполнил всю карточку!!!')
            break
        if is_empty(comp_card):
            print('Компьютер заполнил всю карточку')
            break

game()