import pygame
import random
import time
pygame.init()

textt_wrote= True
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Игра")
blue = (0,0,255)

hp = 100
sp = 1
w = 40
h = 40
rect_waters = [['пусто'for i in range(15)]for i in range(15)]
flag_ship = False

lgm = pygame.image.load("ship.png")
lgm = pygame.transform.scale(lgm, (40, 40))
jpg = pygame.draw.circle(screen, (255, 0, 0), (40, 40), 20)

# БЛОК ЗЕМЛИ
def earth(x, y):
    rus = pygame.draw.rect(screen, (150, 90, 30), (x, y, 40, 40))
    return rus

# ДЕРЕВО
def forest(x, y):
    res = pygame.draw.rect(screen, (100, 200, 100), (x, y, 40, 40))
    pygame.draw.rect(screen, (100, 200, 100), (x, y, 40, 40))
    pygame.draw.circle(screen, (50, 140, 50), (x + 10, y + 10), 6)
    pygame.draw.circle(screen, (50, 140, 50), (x + 30, y + 17), 6)
    pygame.draw.circle(screen, (50, 140, 50), (x + 19, y + 30), 6)
    return res


# ВОДА
def water(x, y):
    ras = pygame.draw.rect(screen, (0, 0, 250), (x, y, 40, 40))
    pygame.draw.rect(screen, (0, 0, 250), (x, y, 40, 40))
    return ras


# ПЕСОК
def sand(x, y):
    ris = pygame.draw.rect(screen, (240, 230, 140), (x, y, 40, 40))
    pygame.draw.rect(screen, (240, 230, 140), (x, y, 40, 40))
    return ris


def black(x, y):
    ras = pygame.draw.rect(screen, (0, 0, 0), (x, y, 40, 40))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 40, 40))
    return ras


def read_map():
    file = open("map.txt", "r+", encoding="utf-8")
    map = []
    for i in range(15):
        line = file.readline()
        data = line.split()
        map.append(data)
    return map


def draw_map(map):
    pos = [0, 0]
    global rect_waters
    rect_waters.clear()

    for k in range(15):
        for b in range(15):
            if map[k][b] == "Земля":
                earth(b * 40, k * 40)
            if map[k][b] == "Песок":
                sand(b * 40, k * 40)
            if map[k][b] == "Вода":
                water(b * 40, k * 40)
                a = water(b * 40, k * 40)
                rect_waters.append(a)
            if map[k][b] == "Лес":
                forest(b * 40, k * 40)
            if map[k][b] == "Ластик":
                black(b * 40, k * 40)
            if map[k][b] == "Персонаж":
                earth(b * 40, k * 40)
                player(b * 40, k * 40)
                map[k][b] = "Земля"
                pos = [k, b]
    return pos

def fght():
    if flag_menu:
        menu()

        oneknopka()
        if toknopkka:
            knopka()
        else:
            knopka()
            toknopka()
        twoknopka()
def draw_score():
    font = pygame.font.Font(None, 30)
    text = font.render(str(count_star), True, (255, 255, 255))
    screen.blit(text, (10, 10))


def player(x, y):
    global rect_ship
    if flag_ship == True:
        rus = screen.blit(lgm, (x, y))
    else:
        rus = pygame.draw.circle(screen, (255, 0, 0), (x + 20, y + 20), 20)
    return rus
def water_hp():
    global hp, sp
    for i in range(len(rect_waters)):
        if rect_player.colliderect(rect_waters[i]):

            hp = hp - sp

            break




def water_ship():
    global flag_ship, rect_player
    for i in range(len(rect_waters)):
        if rect_player.colliderect(rect_waters[i]):
            flag_ship = True
            break
    else:
        flag_ship = False
def menu():
    screen.fill(blue)
    font = pygame.font.Font(None, 50)
    text_font = font.render("Собиратель звёзд ", True, (255, 255, 255))
    screen.blit(text_font, (100, 60))


def drugaya_knopka():
    rect_buton_save = pygame.draw.rect(screen, (255, 255, 255), (209, 200, 170, 50),border_radius=10)
    font = pygame.font.Font(None, 36)
    text_save = font.render("Продолжить", True, (255, 0, 0))
    rect_text = text_save.get_rect()
    rect_text.center = rect_buton_save.center
    screen.blit(text_save, rect_text)
    return rect_buton_save

def knopka():
    rect_buton_save = pygame.draw.rect(screen, (255, 255, 255), (209, 200, 140, 50),border_radius=10)
    font = pygame.font.Font(None, 36)
    text_save = font.render("Новая игра", True, (255, 0, 0))
    rect_text = text_save.get_rect()
    rect_text.center = rect_buton_save.center
    screen.blit(text_save, rect_text)
    return rect_buton_save
def oneknopka():
    rect_buton_save = pygame.draw.rect(screen, (255, 255, 255), (209, 280, 140, 50),border_radius=10)
    font = pygame.font.Font(None, 36)
    text_save = font.render("об авторе ", True, (255, 0, 0))
    rect_text = text_save.get_rect()
    rect_text.center = rect_buton_save.center
    screen.blit(text_save, rect_text)
    return rect_buton_save
def twoknopka():
    rect_buton_save = pygame.draw.rect(screen, (255, 255, 255), (209, 360, 140, 50),border_radius=10)
    font = pygame.font.Font(None, 36)
    text_save = font.render("Выйти", True, (255, 0, 0))
    rect_text = text_save.get_rect()
    rect_text.center = rect_buton_save.center
    screen.blit(text_save, rect_text)
    return rect_buton_save

def xopoшya_knopka():
    rect_buton_save = pygame.draw.rect(screen, (255, 255, 255), (209, 400, 170, 50),border_radius=10)
    font = pygame.font.Font(None, 36)
    text_save = font.render("Назад", True, (255, 0, 0))
    rect_text = text_save.get_rect()
    rect_text.center = rect_buton_save.center
    screen.blit(text_save, rect_text)
    return rect_buton_save


def new_game():
    global position_player, rect_player, count_star, rect_stars,hp
    draw_map(map)
    position_player = pos.copy()
    rect_player = player(position_player[1] * 40, position_player[0] * 40)

    count_star = 0
    hp = 100

    rect_stars = []

    for i in range(10):
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        rect_star = img.get_rect()
        rect_star.topleft = (x * 40, y * 40)
        rect_stars.append(rect_star)


map = read_map()
position_player = draw_map(map)

pos = position_player.copy()

rect_player = player(position_player[1] * 40, position_player[0] * 40)

img = pygame.image.load("star.png")
img = pygame.transform.scale(img, (40, 40))

count_star = 0

rect_stars = []
for i in range(10):
    x = random.randint(0, 14)
    y = random.randint(0, 14)
    rect_star = img.get_rect()
    rect_star.topleft = (x * 40, y * 40)
    rect_stars.append(rect_star)

def lose():
    pygame.draw.rect(screen, (0, 0, 255), (200, 120, 190, 350), border_radius=10)
    font = pygame.font.Font(None, 50)
    text_font = font.render("YOU LOSE", True, (255, 0, 0))
    screen.blit(text_font, (208, 130))
    font = pygame.font.Font(None, 50)
    text_font = font.render("В этом раунде", True, (255, 0, 0))
    screen.blit(text_font, (208, 180))
    font = pygame.font.Font(None, 50)
    text_font = font.render("Ты собрал", True, (255, 0, 0))
    screen.blit(text_font, (208, 230))
    font = pygame.font.Font(None, 50)
    text_font = font.render(str(count_star) , True, (255, 0, 0))
    screen.blit(text_font, (208, 280))
    font = pygame.font.Font(None, 50)
    text_font = font.render("Звёзд", True, (255, 0, 0))
    screen.blit(text_font, (208, 330))
    xopoшya_knopka()


def toknopka():
    rect_buton_save = pygame.draw.rect(screen, (255, 255, 255), (209, 120, 140, 50),border_radius=10)
    font = pygame.font.Font(None, 36)
    text_save = font.render("продолжить", True, (255, 0, 0))
    rect_text = text_save.get_rect()
    rect_text.center = rect_buton_save.center
    screen.blit(text_save, rect_text)
    return rect_buton_save
toknopkka = True
rect_butttonn_save = toknopka()
flag_menu = True
rect_button_save = knopka()
rect_buton_save = oneknopka()
rect_buttton_save = twoknopka()
rect_buttonnn_save = xopoшya_knopka()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_button_save.collidepoint(event.pos):
                flag_menu = False
                new_game()
                toknopkka = False



            if rect_buton_save.collidepoint(event.pos):
                flag_menu = "автор"
            if rect_buttton_save.collidepoint(event.pos):
                flag_menu = "Выйти"
            if rect_butttonn_save.collidepoint(event.pos):
                flag_menu = False
            if rect_butttonn_save.collidepoint(event.pos):
                flag_menu = False
            if rect_buttonnn_save.collidepoint(event.pos):
                flag_menu = True
            if rect_button_save.collidepoint(event.pos):
                flag_menu = False








    if flag_menu:
        fght()


    else:

        for i in range(len(rect_stars)):
            if rect_player.colliderect(rect_stars[i]):
                rect_stars.pop(i)
                count_star += 1
                break





        draw_map(map)
        draw_score()
        keys = pygame.key.get_pressed()
        water_ship()
        water_hp()
        font = pygame.font.Font(None, 30)
        text_font = font.render(str(hp), True, (255, 255, 255))
        screen.blit(text_font, (550, 10))


        if keys[pygame.K_ESCAPE]:
            flag_menu = True



        if keys[pygame.K_s]:
            position_player[0] += 1
        if keys[pygame.K_w]:
            position_player[0] -= 1
        if keys[pygame.K_d]:
            position_player[1] += 1
        if keys[pygame.K_a]:
            position_player[1] -= 1



        rect_player = player(position_player[1] * 40, position_player[0] * 40)

        for i in range(len(rect_stars)):
            screen.blit(img, rect_stars[i])

        if count_star == 10:
            font = pygame.font.Font(None, 50)
            text_font5 = font.render("Молодец, прошёл игру", True, (255, 0, 0))
            screen.blit(text_font5, (140, 215))
        if hp == 0:
            sp = 0

            lose()
    if flag_menu == "автор":
        screen.fill((0,255,0))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            flag_menu = True

        font = pygame.font.Font(None, 30)
        text_font = font.render("Автора этой замечательной игры зовут Слава", True, (255, 255, 255))
        screen.blit(text_font, (30, 50))

        font = pygame.font.Font(None, 30)
        text_font = font.render("Родился он в Санк Петербурге ", True, (255, 255, 255))
        screen.blit(text_font, (30, 100))
        font = pygame.font.Font(None, 30)
        text_font = font.render("А сейчас проживает в посёлке Вознесенье", True, (255, 255, 255))
        screen.blit(text_font, (30, 150))
        font = pygame.font.Font(None, 30)
        text_font = font.render("учится в 6 классе в школе МБУ СОШ №7", True, (255, 255, 255))
        screen.blit(text_font, (30, 200))
        font = pygame.font.Font(None, 30)
        text_font = font.render("У славы 2 собаки Чет и Нюша", True, (255, 255, 255))
        screen.blit(text_font, (30, 250))
        font = pygame.font.Font(None, 30)
        text_font = font.render("И 2 кошки Мотя и Буся ,но Слава её называет Бусинатор", True, (255, 255, 255))
        screen.blit(text_font, (25, 300))
        ont = pygame.font.Font(None, 30)
        text_font = font.render("Слава играет в игры:ксго и фаркрай 2 и 3 часть", True, (255, 255, 255))
        screen.blit(text_font, (25, 350))
        xopoшya_knopka()
    if flag_menu == "Выйти":
       run = False





    pygame.display.update()
    pygame.time.Clock().tick(50)
