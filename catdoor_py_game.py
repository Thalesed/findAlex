import pygame
from random import *
from time import sleep
def catdoor():

    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Cat')
    win.fill((255, 255, 255))
    font = pygame.font.Font(None, 32)
    font1 = pygame.font.Font(None, 20)
    text = 'Onde o Gato está?'
    run = True
    katze = ['1', '2', '3']
    cat = choice(katze)
    man = False
    if cat == '1':
        catpos = 60
    elif cat == '2':
        catpos = 200
    elif cat == '3':
        catpos = 360
    d1 = d2 = d3 = True
    usertext = ''
    escolha = ''
    r = False
    trx = tri = 0
    m = t = False
    again = False
    vari = True
    poder = True
    op = randint(1, 2)
    print(op)

    while run:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()

                if poder:
                    if 10 <= xx <= 150 and 60 <= yy <= 210:

                        escolha = '1'
                        sleep(1)
                        poder = False

                    elif 160 <= xx <= 300 and 60 <= yy <= 210:

                        escolha = '2'
                        sleep(1)
                        poder = False

                    elif 310 <= xx <= 450 and 60 <= yy <= 210:

                        escolha = '3'
                        sleep(1)
                        poder = False

                if man:
                    if 300 <= xx <= 400 and 340 <= yy <= 370:
                        m = True
                        vari = False
                    elif 180 <= xx <= 280 and 340 <= yy <= 370:
                        t = True
                        vari = False
                if r:
                    if 100 <= xx <=200 and 450 <= yy <= 480:
                        again = True
            if '1' in escolha:
                con = False
                man = True
                if cat == '2':
                    d3 = False
                    usertext = 'O gato não está na porta 3. Deseja manter ou trocar? '
                    if m:
                        e = '1'
                        man = False
                        r = True
                    elif t:
                        e = '2'
                        r = True
                        man = False
                elif cat =='3':
                    d2 = False
                    usertext = 'O gato não está na porta 2. Deseja manter ou trocar?'
                    if m:
                        e = '1'
                        man = False
                        r = True
                    elif t:
                        e = '3'
                        r = True
                        man = False
                elif cat == '1':
                    if op == 1:
                        d2 = False
                        usertext = 'O gato não está na porta 2. Deseja manter ou trocar?  '
                        if m:
                            e = '1'
                            man = False
                            r = True
                        elif t:
                            e = '3'
                            r = True
                            man = False
                    elif op == 2:
                        d3 = False
                        usertext = 'O gato não está na porta 3. Deseja manter ou trocar?  '
                        if m:
                            e = '1'
                            man = False
                            r = True
                        elif t:
                            e = '2'
                            r = True
                            man = False
            if '2' in escolha:
                con = False
                man = True
                if cat == '1':
                    d3 = False
                    usertext = 'O gato não está na porta 3. Deseja manter ou trocar? '
                    if m:
                        e = '2'
                        man = False
                        r = True
                    elif t:
                        e = '1'
                        r = True
                        man = False
                elif cat == 3:
                    d1 = False
                    usertext = 'O gato não está na porta 1. Deseja manter ou trocar?  '
                    if m:
                        e = '2'
                        man = False
                        r = True
                    elif t:
                        e = '3'
                        r = True
                        man = False
                else:
                    if man:
                        d1 = False
                        usertext = 'O gato não está na porta 1. Deseja manter ou trocar?  '
                        if m:
                            e = '2'
                            man = False
                            r = True
                        elif t:
                            e = '3'
                            r = True
                            man = False

            if '3' in escolha:
                con = False
                man = True
                if cat == '1':
                    d2 = False
                    usertext = 'O gato não está na porta 2. Deseja manter ou trocar?'
                    if m:
                        e = '3'
                        man = False
                        r = True
                    elif t:
                        e = '1'
                        r = True
                        man = False
                elif cat == '2':
                    d1 = False
                    usertext = 'O gato não está na porta 1. Deseja manter ou trocar? '
                    if m:
                        e = '3'
                        man = False
                        r = True
                    elif t:
                        e = '2'
                        r = True
                        man = False
                elif cat == '3':
                    if op == 1:
                        d1 = False
                        usertext = 'O gato não está na porta 1. Deseja manter ou trocar?  '
                        if m:
                            e = '3'
                            man = False
                            r = True
                        elif t:
                            e = '2'
                            r = True
                            man = False
                    if op == 2:
                        d2 = False
                        usertext = 'O gato não está na porta 2. Deseja manter ou trocar?  '
                        if m:
                            e = '3'
                            man = False
                            r = True
                        elif t:
                            e = '1'
                            r = True
                            man = False
        door1 = pygame.image.load('./door.jpg')
        door2 = pygame.image.load('./door.jpg')
        door3 = pygame.image.load('./door.jpg')
        black = pygame.image.load('./black.jpg')
        tapi = pygame.image.load('./tapi1.png')
        win.fill((255, 255, 255))
        surface = font.render(text, True, (0, 0, 0))
        surface1 = font1.render(usertext, True, (0, 0, 0))
        win.blit(surface, (30, 50))
        win.blit(black, (35, 95))
        win.blit(black, (185, 95))
        win.blit(black, (335, 95))
        win.blit(tapi, (catpos, 120))
        if vari:
            win.blit(surface1, (30, 300))
        if d1:
            win.blit(door1, (10, 70))
        if d2:
            win.blit(door2, (160, 70))
        if d3:
            win.blit(door3, (310, 70))

        if man:
            pygame.draw.rect(win, (255, 0, 0), (300, 340, 100, 30))
            surface3 = font1.render('Manter', True, (255, 255, 255))
            win.blit(surface3, (320, 350))
            pygame.draw.rect(win, (0, 0, 255), (180, 340, 100, 30))
            surface4 = font1.render('Trocar', True, (255, 255, 255))
            win.blit(surface4, (200, 350))

        if r:
            if e == cat:
                word = 'ganhou'
            else:
                word = 'perdeu'
            surf = font1.render(f'Você {word}, sua última escolha foi a porta{e}.', True, (0, 0, 0))
            win.blit(surf, (100, 400))
            d1 = d2 = d3 = False
            pygame.draw.rect(win, (0, 255,0), (100, 450, 112, 30))
            surf1 = font1.render('Tentar novamente', True, (255, 255, 255))
            win.blit(surf1, (100, 460))
            if again:


                pygame.init()
                win = pygame.display.set_mode((500, 500))
                pygame.display.set_caption('Cat')
                win.fill((255, 255, 255))
                font = pygame.font.Font(None, 32)
                font1 = pygame.font.Font(None, 20)
                text = 'Onde o Gato está?'
                run = True
                katze = ['1', '2', '3']
                cat = choice(katze)
                man = False
                if cat == '1':
                    catpos = 60
                elif cat == '2':
                    catpos = 200
                elif cat == '3':
                    catpos = 360
                d1 = d2 = d3 = True
                usertext = ''
                escolha = ''
                r = False
                trx = tri = 0
                m = t = False
                again = False
                vari = True
                poder = True
                op = randint(1, 2)
catdoor()
