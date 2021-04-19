import pygame as p
import sys

BG_SIZE = (800, 1000)


p.init()
screen = p.display.set_mode(BG_SIZE)
clock = p.time.Clock()

chessboard_surface = p.image.load("images/chessboard.jpg").convert()
chessboard_surface = p.transform.scale(chessboard_surface, (BG_SIZE[0], BG_SIZE[0]))


while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            #TODO Show request: "Do you really wanna quit?"
            p.quit()
            sys.exit()

    screen.blit(chessboard_surface, (0, (BG_SIZE[1] - BG_SIZE[0])/2))
    p.display.update()
    clock.tick(60)
