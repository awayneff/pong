
import pygame
from pygame.locals import *
from paddle import Player
from ball import Ball


'''def gm(inp):
    if inp == '':
        return False
    if inp == 'M':
        return True
    else:
        inp = input('Неверная команда. Введите ещё раз')'''


def showScore():
    font = pygame.font.Font(None, 50)
    text1 = font.render(str(score1), 1, white)
    text2 = font.render(str(score2), 1, white)

    screen.blit(text1, (10, 10))

    if mp:
        screen.blit(text2, (600, 10))


def pMenu(screen):
    global running, mainMenu

    showScore()
    inMenu = True

    font = pygame.font.Font(None, 40)
    tFont = pygame.font.Font(None, 55)

    # Title
    tText = tFont.render('bpong', 1, white)
    tTextW = tText.get_width()

    # Continue button
    cText = font.render('Continue', 1, white)

    cTextW = cText.get_width()
    cTextH = cText.get_height()

    cBtnPos = ((screen.get_width() - cTextW) // 2, 200)

    # Main menu button
    mText = font.render('Main menu', 1, white)

    mTextW = mText.get_width()
    mTextH = mText.get_height()

    mBtnPos = ((screen.get_width() - mTextW) // 2, 250)

    # Quit button
    qText = font.render('Quit', 1, white)

    qTextW = qText.get_width()
    qTextH = qText.get_height()

    qBtnPos = ((screen.get_width() - qTextW) // 2, 300)

    while inMenu:
        screen.fill(black)

        screen.blit(cText, cBtnPos)
        screen.blit(qText, qBtnPos)
        screen.blit(mText, mBtnPos)
        screen.blit(tText, ((screen.get_width() - tTextW) // 2, 50))

        pygame.draw.line(screen, white, (0, 100), (screen.get_width(), 100))

        for event in pygame.event.get():
            # ESC button mechanic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inMenu = False

            # Mouse click mechanics
            if event.type == pygame.MOUSEBUTTONUP:
                # Continue button mechanic
                if cBtnPos[0] < pygame.mouse.get_pos()[0] < cBtnPos[0] + cTextW and\
                        cBtnPos[1] < pygame.mouse.get_pos()[1] < cBtnPos[1] + cTextH:
                    inMenu = False

                # Quit button mechanic
                if qBtnPos[0] < pygame.mouse.get_pos()[0] < qBtnPos[0] + qTextW and\
                        qBtnPos[1] < pygame.mouse.get_pos()[1] < qBtnPos[1] + qTextH:
                    running = False
                    return running

                # Main menu button mechanic
                if mBtnPos[0] < pygame.mouse.get_pos()[0] < mBtnPos[0] + mTextW and\
                        mBtnPos[1] < pygame.mouse.get_pos()[1] < qBtnPos[1] + mTextH:
                    mainMenu = True
                    inMenu = False

        clock.tick(60)
        pygame.display.update()


def mMenu(screen):
    global mp, mainMenu, score1, score2

    font = pygame.font.Font(None, 40)
    tFont = pygame.font.Font(None, 55)

    # Title
    tText = tFont.render('bpong', 1, white)
    tTextW = tText.get_width()

    # Quit button
    qText = font.render('Quit', 1, white)

    qTextW = qText.get_width()
    qTextH = qText.get_height()

    qBtnPos = ((screen.get_width() - qTextW) // 2, 400)

    # Singleplayer button
    sText = font.render('Singleplayer', 1, white)

    sTextW = sText.get_width()
    sTextH = sText.get_height()

    sBtnPos = ((screen.get_width() - sTextW) // 2, 200)

    # Multiplayer button
    mText = font.render('Multiplayer', 1, white)

    mTextW = mText.get_width()
    mTextH = mText.get_height()

    mBtnPos = ((screen.get_width() - mTextW) // 2, 270)

    while mainMenu:
        screen.fill(black)

        screen.blit(qText, qBtnPos)
        screen.blit(sText, sBtnPos)
        screen.blit(mText, mBtnPos)
        screen.blit(tText, ((screen.get_width() - tTextW) // 2, 50))

        pygame.draw.line(screen, white, (0, 100), (screen.get_width(), 100))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # Quit button mechanic
                if qBtnPos[0] < pygame.mouse.get_pos()[0] < qBtnPos[0] + qTextW and\
                        qBtnPos[1] < pygame.mouse.get_pos()[1] < qBtnPos[1] + qTextH:
                    pygame.quit()

                # Singleplayer button mechanic
                if sBtnPos[0] < pygame.mouse.get_pos()[0] < sBtnPos[0] + sTextW and\
                        sBtnPos[1] < pygame.mouse.get_pos()[1] < sBtnPos[1] + sTextH:
                    mainMenu = False
                    score1, score2 = 0, 0

                # Multiplayer button mechanic
                if mBtnPos[0] < pygame.mouse.get_pos()[0] < mBtnPos[0] + mTextW and\
                        mBtnPos[1] < pygame.mouse.get_pos()[1] < mBtnPos[1] + mTextH:
                    score1, score2 = 0, 0
                    mainMenu = False
                    mp = True

        clock.tick(60)
        pygame.display.update()


def dScreen(screen):
    global score1, score2, mainMenu, running
    inScreen = True

    font = pygame.font.Font(None, 40)
    tFont = pygame.font.Font(None, 55)

    # Restart button
    sText = font.render('Play again', 1, white)

    sTextW = sText.get_width()
    sTextH = sText.get_height()

    sBtnPos = ((screen.get_width() - sTextW) // 2, 230)

    # Main menu button
    mText = font.render('Main menu', 1, white)

    mTextW = mText.get_width()
    mTextH = mText.get_height()

    mBtnPos = ((screen.get_width() - mTextW) // 2, 270)

    # Title
    tText = tFont.render('Game over!', 1, white)
    tTextW = tText.get_width()

    # Quit button
    qText = font.render('Quit', 1, white)

    qTextW = qText.get_width()
    qTextH = qText.get_height()

    qBtnPos = ((screen.get_width() - qTextW) // 2, 400)

    while inScreen:
        screen.fill(black)

        screen.blit(tText, ((screen.get_width() - tTextW) // 2, 50))
        screen.blit(sText, sBtnPos)
        screen.blit(mText, mBtnPos)
        screen.blit(qText, qBtnPos)

        # Final score display
        if score1 > score2:
            scoreText = font.render('Player 1 won!', 1, white)
        if score1 < score2:
            scoreText = font.render('Player 2 won!', 1, white)
        screen.blit(
            scoreText, ((screen.get_width() - scoreText.get_width()) // 2, 150))

        pygame.draw.line(screen, white, (0, 100), (screen.get_width(), 100))

        showScore()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # Quit button mechanic
                if qBtnPos[0] < pygame.mouse.get_pos()[0] < qBtnPos[0] + qTextW and\
                        qBtnPos[1] < pygame.mouse.get_pos()[1] < qBtnPos[1] + qTextH:
                    pygame.quit()

                # Restart button mechanic
                if sBtnPos[0] < pygame.mouse.get_pos()[0] < sBtnPos[0] + sTextW and\
                        sBtnPos[1] < pygame.mouse.get_pos()[1] < sBtnPos[1] + sTextH:
                    running = True
                    score1, score2 = 0, 0
                    return

                # Main menu button mechanic
                if mBtnPos[0] < pygame.mouse.get_pos()[0] < mBtnPos[0] + mTextW and\
                        mBtnPos[1] < pygame.mouse.get_pos()[1] < mBtnPos[1] + mTextH:
                    mainMenu = True
                    inScreen = False
                    return

        clock.tick(60)
        pygame.display.update()


# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Screen size
size = W, H = 640, 640

# Main loop, multiplayer, main menu variable
running = True
mp = False
mainMenu = True

pygame.init()

screen = pygame.display.set_mode(size)

pygame.display.set_caption('bpong')

clock = pygame.time.Clock()

mMenu(screen)

# Player1 initialization
pl1 = Player(white, 5, 50)
pl1.rect.x = 50
pl1.rect.y = 0

# Player2 initialization
if mp:
    pl2 = Player(white, 5, 50)
    pl2.rect.x = 550
    pl2.rect.y = 0

# Ball initialization
ball = Ball(white, 5, 5)
ball.rect.x = screen.get_width() // 2
ball.rect.y = screen.get_height() // 2

score1, score2 = 0, 0
speed1, speed2 = 6, 6

spritesList = pygame.sprite.Group()

spritesList.add(pl1)
spritesList.add(ball)
if mp:
    spritesList.add(pl2)

collSound = pygame.mixer.Sound('sounds/coll.mp3')
zSound = pygame.mixer.Sound('sounds/scs.mp3')

while running:
    mMenu(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            if event.key == pygame.K_r:
                score1, score2 = 0, 0
            if event.key == pygame.K_ESCAPE:
                pMenu(screen)
                if mp:
                    pl2.rect.x = 550
                    pl2.rect.y = 0

            if event.key == pygame.K_LSHIFT:
                speed1 = 15
            if event.key == pygame.K_RSHIFT:
                speed2 = 15

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed1 = 6
            if event.key == pygame.K_RSHIFT:
                speed2 = 6

    # Players movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        pl1.moveUp(speed1)
    if keys[pygame.K_s]:
        pl1.moveDown(speed1)

    if mp:
        if keys[pygame.K_UP]:
            pl2.moveUp(speed2)
        if keys[pygame.K_DOWN]:
            pl2.moveDown(speed2)

    spritesList.update()

    # Ball move
    if ball.rect.x > screen.get_width() or ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y >= screen.get_height() or ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # Score handler
    if ball.rect.x <= 0:
        zSound.play()
        score2 += 1
    
        if not mp:
            score1 -= 1

    if ball.rect.x >= screen.get_width() and mp:
        zSound.play()
        score1 += 1

    # End screen
    if mp:
        if score1 >= 30 or score2 >= 30:
            dScreen(screen)

    # Collision detection
    if pygame.sprite.collide_mask(ball, pl1):
        collSound.play()
        ball.bounce()

    if mp and pygame.sprite.collide_mask(ball, pl2):
        collSound.play()
        ball.bounce()

    screen.fill(black)

    spritesList.draw(screen)

    showScore()

    pygame.display.flip()

    clock.tick(60)
