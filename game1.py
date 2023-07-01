import pygame

pygame.init() # 맨 처음에 선언하고 초기화 의미

# 게임의 배경화면 창 만들기
background = pygame.display.set_mode((480,200)) # 배경화면 창 크기
pygame.display.set_caption('good')


# 창 유지하기
play = True
while play:
    for envent in pygame.event.get():

        if envent.type == pygame.QUIT: # 게임을 종료 했을 때 play
            play = False

pygame.quit()