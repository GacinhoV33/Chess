from abc import abstractmethod

import pygame as p
import sys
import numpy as np

BG_SIZE = (800, 1000)


p.init()
screen = p.display.set_mode(BG_SIZE)
clock = p.time.Clock()

# ))chessboard_surface = p.image.load("images/chessboards/chessboard3.png").convert()
# # chessboard_surface = p.transform.scale(chessboard_surface, (BG_SIZE[0], BG_SIZE[0] Probably not important


class Figure:
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        self.color = color
        self.name = name
        self.start_pos = (x, y)
        self.actual_pos = (self.start_pos[0], self.start_pos[1])
        self.actual_display_pos = self.convert_to_display(self.start_pos[0], self.start_pos[1])
        self.image = p.image.load(image_path).convert_alpha()
        self.image = p.transform.scale(self.image, (int(BG_SIZE[0] / 8), int(BG_SIZE[0] / 8)))
        self.image_path = image_path
        self.figure_id = figure_id

    def show_figure(self):
        screen.blit(self.image, self.actual_display_pos)

    @abstractmethod
    def possible_moves(self):
        pass

    @classmethod
    def convert_to_display(cls, x: int, y: int):
        return int((BG_SIZE[0] / 8) * (x - 1)), int(BG_SIZE[0] - (BG_SIZE[0] / 8) * (y - 1))


class Pawn(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self):
        # super.__init__()
        pass

    def show_possible_moves_on_board(self):
        pass

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Knight(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self):
        # super.__init__()
        pass

    def show_possible_moves_on_board(self):
        pass

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Bishop(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self):
        # super.__init__()
        pass

    def show_possible_moves_on_board(self):
        pass

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Rook(Figure):
    def __init__(self, color: str, name:str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)


class King(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self):
        # super.__init__()
        pass

    def show_possible_moves_on_board(self):
        pass

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Queen(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self):
        # super.__init__()
        pass

    def show_possible_moves_on_board(self):
        pass

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (BG_SIZE[0]/8, BG_SIZE[0]/8)
        self.location = ((self.x-1) * BG_SIZE[0]/8, (self.y-1) * BG_SIZE[0]/8)
        self.is_free = True


class Chessboard:
    def __init__(self, image_path: str):
        self.surface = p.image.load(image_path).convert()
        self.surface = p.transform.scale(self.surface, (BG_SIZE[0], BG_SIZE[0]))
        self.matrix = np.zeros((8, 8))

    def init_chessboard(self):
        #TODO
        pass


    @classmethod
    def convert_to_display(cls, x: int, y: int):
        return (BG_SIZE[0] / 8) * (x - 1) + BG_SIZE[0] / 8 / 2, (BG_SIZE[0] / 8) * (y - 1) + BG_SIZE[0] / 8 / 2

Chessboard_classic = Chessboard("images/chessboards/chessboard3.png")
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

King1 = King("white", "KingE1", "images/figures/white_king.png", 25, 5, 1)
King2 = King("black", "KingE8", "images/figures/black_king.png", 26, 5, 8)
Queen1 = Queen("white", "QueenD1", "images/figures/white_queen.png", 27, 4, 1)
Queen2 = Queen("white", "QueenD8", "images/figures/black_queen.png", 28, 4, 8)

White_pawns = [Pawn1, Pawn2, Pawn3, Pawn4, Pawn5, Pawn6, Pawn7, Pawn8]
Black_pawns = [Pawn9, Pawn10, Pawn11, Pawn12, Pawn13, Pawn14, Pawn15, Pawn16]
White_knights = [Knight1, Knight2]
Black_knights = [Knight3, Knight4]
White_bishops = [Bishop1, Bishop2]
Black_bishops = [Bishop3, Bishop4]

All_figures = [Pawn1, Pawn2, Pawn3, Pawn4, Pawn5, Pawn6, Pawn7, Pawn8,
               Pawn9, Pawn10, Pawn11, Pawn12, Pawn13, Pawn14, Pawn15, Pawn16,
               Knight1, Knight2, Knight3, Knight4, Bishop1, Bishop2, Bishop3, Bishop4,
               Queen1, Queen2, King1, King2, Rook1, Rook2, Rook3, Rook4]


Chessboard_type = Chessboard_classic


while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            #TODO Show request: "Do you really wanna quit?"
            p.quit()
            sys.exit()
    screen.blit(Chessboard_type.surface, (0, (BG_SIZE[1] - BG_SIZE[0])/2))
    for figure in All_figures:
        figure.show_figure()
    # for pawn in White_pawns:
    #     pawn.show_figure()
    # for pawn in Black_pawns:
    #     pawn.show_figure()
    # for knight in White_knights:
    #     knight.show_figure()
    # for knight in Black_knights:
    #     knight.show_figure()
    # for bishop in White_bishops:
    #     bishop.show_figure()
    # for bishop in Black_bishops:
    #     bishop.show_figure()


    p.display.update()
    clock.tick(60)
