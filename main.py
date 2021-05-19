import sys

import pygame as p
from Pawn import Pawn
from Knight import Knight
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from King import King
from Chessboard import Chessboard
from Game import Game
from config import BG_SIZE, clock_tick_ratio
from Player import Player

game = Game()

p.init()
screen = p.display.set_mode(BG_SIZE)
clock = p.time.Clock()

Chessboard_classic = Chessboard("images/chessboards/chessboard3.png")

White_player = Player("white")
Black_player = Player("black")

#                                                       Szerokość---Wysokość
Pawn1 = Pawn("white", "PawnA2", "images/figures/white_pawn.png", 1, 1, 2)
Pawn2 = Pawn("white", "PawnB2", "images/figures/white_pawn.png", 2, 2, 2)
Pawn3 = Pawn("white", "PawnC2", "images/figures/white_pawn.png", 3, 3, 2)
Pawn4 = Pawn("white", "PawnD2", "images/figures/white_pawn.png", 4, 4, 2)
Pawn5 = Pawn("white", "PawnE2", "images/figures/white_pawn.png", 5, 5, 2)
Pawn6 = Pawn("white", "PawnF2", "images/figures/white_pawn.png", 6, 6, 2)
Pawn7 = Pawn("white", "PawnG2", "images/figures/white_pawn.png", 7, 7, 2)
Pawn8 = Pawn("white", "PawnH2", "images/figures/white_pawn.png", 8, 8, 2)
Pawn9 = Pawn("black", "PawnA7", "images/figures/black_pawn.png", 9, 1, 7)
Pawn10 = Pawn("black", "PawnB7", "images/figures/black_pawn.png", 10, 2, 7)
Pawn11 = Pawn("black", "PawnC7", "images/figures/black_pawn.png", 11, 3, 7)
Pawn12 = Pawn("black", "PawnD7", "images/figures/black_pawn.png", 12, 4, 7)
Pawn13 = Pawn("black", "PawnE7", "images/figures/black_pawn.png", 13, 5, 7)
Pawn14 = Pawn("black", "PawnF7", "images/figures/black_pawn.png", 14, 6, 7)
Pawn15 = Pawn("black", "PawnG7", "images/figures/black_pawn.png", 15, 7, 7)
Pawn16 = Pawn("black", "PawnH7", "images/figures/black_pawn.png", 16, 8, 7)
#repair rest
Knight1 = Knight("white", "KnightB1", "images/figures/white_knight.png", 17, 2, 1)
Knight2 = Knight("white", "KnightG1", "images/figures/white_knight.png", 18, 7, 1)
Knight3 = Knight("black", "KnightB8", "images/figures/black_knight.png", 19, 2, 8)
Knight4 = Knight("black", "KnightG8", "images/figures/black_knight.png", 20, 7, 8)
Bishop1 = Bishop("white", "BishopC1", "images/figures/white_bishop.png", 21, 3, 1)
Bishop2 = Bishop("white", "BishopF1", "images/figures/white_bishop.png", 22, 6, 1)
Bishop3 = Bishop("black", "BishopC8", "images/figures/black_bishop.png", 23, 3, 8)
Bishop4 = Bishop("black", "BishopF8", "images/figures/black_bishop.png", 24, 6, 8)
Rook1 = Rook("white", "Rook A1", "images/figures/white_rook.png", 25, 1, 1)
Rook2 = Rook("white", "Rook H1", "images/figures/white_rook.png", 26, 8, 1)
Rook3 = Rook("black", "Rook A8", "images/figures/black_rook.png", 27, 1, 8)
Rook4 = Rook("black", "Rook H8", "images/figures/black_rook.png", 28, 8, 8)

King1 = King("white", "KingE1", "images/figures/white_king.png", 29, 5, 1)
King2 = King("black", "KingE8", "images/figures/black_king.png", 30, 5, 8)
Queen1 = Queen("white", "QueenD1", "images/figures/white_queen.png", 31, 4, 1)
Queen2 = Queen("white", "QueenD8", "images/figures/black_queen.png", 32, 4, 8)

White_pawns = [Pawn1, Pawn2, Pawn3, Pawn4, Pawn5, Pawn6, Pawn7, Pawn8]
Black_pawns = [Pawn9, Pawn10, Pawn11, Pawn12, Pawn13, Pawn14, Pawn15, Pawn16]
White_knights = [Knight1, Knight2]
Black_knights = [Knight3, Knight4]
White_bishops = [Bishop1, Bishop2]
Black_bishops = [Bishop3, Bishop4]

All_figures = [Pawn1, Pawn2,  Pawn4,  Pawn6, Pawn7, Pawn8,
               Pawn9, Pawn10, Pawn11, Pawn12, Pawn13, Pawn14, Pawn15, Pawn16,
               Knight1, Knight2, Knight3, Knight4, Bishop1, Bishop2, Bishop3, Bishop4,
               Queen1, Queen2, King1, King2, Rook1, Rook2, Rook3, Rook4]

Board = Chessboard_classic
Board.init_chessboard(All_figures)
Actual_figure = None

screen.blit(Board.surface, (0, (BG_SIZE[1] - BG_SIZE[0]) / 2))
for figure in All_figures:
    figure.show_figure(screen)
p.display.update()

while True:
    All_figures = [Pawn1, Pawn2, Pawn4, Pawn6, Pawn7, Pawn8,
                   Pawn9, Pawn10, Pawn11, Pawn12, Pawn13, Pawn14, Pawn15, Pawn16,
                   Knight1, Knight2, Knight3, Knight4, Bishop1, Bishop2, Bishop3, Bishop4,
                   Queen1, Queen2, King1, King2, Rook1, Rook2, Rook3, Rook4]

    for event in p.event.get():
        if event.type == p.QUIT:
            #TODO Show request: "Do you really wanna quit?"
            p.quit()
            sys.exit()
        if event.type == p.MOUSEBUTTONDOWN:
            click_pos = p.mouse.get_pos()
            if game.state == 0:
                for column in Board.matrix:
                    for field in column:
                        if field.is_in_area(click_pos) and not field.is_free:
                            print("detected: ", field.x, ":", field.y)
                            if field.figure.color == game.player_turn:
                                Actual_figure = field.figure
                                game.state = 1

            elif game.state == 1:
                check_flag = True
                for column in Board.matrix:
                    for field in column:
                        if field.is_in_area(click_pos) and (field.x, field.y) in Actual_figure.possible_moves(Board):
                            Actual_figure.make_move(field.x, field.y)
                            game.update_chessboard(Board, All_figures)
                            Actual_figure = None
                            game.state = 0
                            check_flag = not check_flag
                if check_flag:
                    game.state = 0
                    Actual_figure = None
            else:
                raise ValueError("ERROR")
            # game.state = "figure_chosen"
            # click_pos = p.mouse.get_pos()
            # print(click_pos)
            # for column in Board.matrix:
            #     for field in column:
            #         if field.is_in_area(click_pos):
            #             print("detected: ", field.x, ":", field.y)
            #             field.figure.show_possible_moves_on_board(Board, screen)
            #             p.display.update()
            #             # p.time.wait(3000)
            #             game.end_of_turn = True
    screen.blit(Board.surface, (0, (BG_SIZE[1] - BG_SIZE[0])/2))

    for figure in All_figures:
        figure.show_figure(screen)

    if Actual_figure:
        Actual_figure.show_possible_moves_on_board(Board, screen)
    # King2.show_possible_moves_on_board(Board, screen)

    # if game.end_of_turn:
    p.display.update()
    clock.tick(clock_tick_ratio)





#TODO
# 1) Problem with assignig information to Board
# 2) Mechanics a lot to do :D