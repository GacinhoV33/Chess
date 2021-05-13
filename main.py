from abc import abstractmethod

import pygame as p
import sys
import numpy as np

BG_SIZE = (800, 1000)


p.init()
screen = p.display.set_mode(BG_SIZE)
clock = p.time.Clock()


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
        self.circle_image = p.image.load("images/circle.png").convert_alpha()
        self.circle_image = p.transform.scale(self.circle_image, (int(BG_SIZE[0]/24), int(BG_SIZE[0]/24)))

    def show_figure(self):
        screen.blit(self.image, self.actual_display_pos)

    def show_possible_moves_on_board(self, chessboard):
        for move in self.possible_moves(chessboard):
            if chessboard.matrix[move[0]-1][move[1]-1].is_free:
                screen.blit(self.circle_image, self.convert_to_display_circle(move[0], move[1]))
            else:
                #TODO highlight attacked figure
                pass

    @abstractmethod
    def possible_moves(self, chessboard):
        """
        function returns every possible positon on the board where figure might go
        This not consider whether it's collide with other figures or not
        :return: List[(x:int, y:int)]
        """
        pass

    @classmethod
    def convert_to_display(cls, x: int, y: int):
        """
        Function convert coordinates to coordinates on chessboard
        The coordinates are placed in the left-top corner of one chessboard field
        :param x:
        :param y:
        :return: Tuple(int, int)
        """
        return int((BG_SIZE[0] / 8) * (x - 1)), int(BG_SIZE[0] - (BG_SIZE[0] / 8) * (y - 1))

    @classmethod
    def convert_to_display_circle(cls, x: int, y: int):
        """
        Function convert coordinates to coordinates on chessboard
        The middle of converted coordinates has place in the middle of one chessboard field
        :param x:
        :param y:
        :return: Tuple(int, int)
        """
        return int((BG_SIZE[0] / 8) * (x - 1) + BG_SIZE[0]/24), int(BG_SIZE[0] - (BG_SIZE[0] / 8) * (y - 1) + BG_SIZE[0]/24)

    @classmethod
    def is_on_board(cls, x: int, y: int):
        """
        Function chceck whether given coordinates are inside the chessboard area
        :param x:
        :param y:
        :return: Bool
        """
        if 1 <= x <= 8 and 1 <= y <= 8:
            return True
        else:
            return False


class Pawn(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self, chessboard):
        if self.color == "white":
            #TODO add attacking opponent
            #TODO add limit of boards
            if self.actual_pos == self.start_pos:
                return [(self.actual_pos[0], self.actual_pos[1]+1), (self.actual_pos[0], self.actual_pos[1]+2)]
            else:
                return [(self.actual_pos[0], self.actual_pos[1] + 1)]
        elif self.color == "black":
            if self.actual_pos == self.start_pos:
                return [(self.actual_pos[0], self.actual_pos[1]-1), (self.actual_pos[0], self.actual_pos[1]-2)]
            else:
                return [(self.actual_pos[0], self.actual_pos[1]-1)]
        else:
            raise ValueError("Wrong color type assigned")

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Knight(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self, chessboard):
        poss_moves = list()
        if self.is_on_board(self.actual_pos[0] + 2, self.actual_pos[1] + 1):
            poss_moves.append((self.actual_pos[0] + 2, self.actual_pos[1] + 1))
        if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1] + 2):
            poss_moves.append((self.actual_pos[0] + 1, self.actual_pos[1] + 2))
        if self.is_on_board(self.actual_pos[0] + 2, self.actual_pos[1] - 1):
            poss_moves.append((self.actual_pos[0] + 2, self.actual_pos[1] - 1))
        if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1] - 2):
            poss_moves.append((self.actual_pos[0] + 1, self.actual_pos[1] - 2))
        if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] - 2):
            poss_moves.append((self.actual_pos[0] - 1, self.actual_pos[1] - 2))
        if self.is_on_board(self.actual_pos[0] - 2, self.actual_pos[1] - 1):
            poss_moves.append((self.actual_pos[0] -2, self.actual_pos[1] - 1))
        if self.is_on_board(self.actual_pos[0] - 2, self.actual_pos[1] + 1):
            poss_moves.append((self.actual_pos[0] -2, self.actual_pos[1] + 1))
        if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] + 2):
            poss_moves.append((self.actual_pos[0] - 1, self.actual_pos[1] + 2))
        return poss_moves

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Bishop(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self, chessboard):
        poss_moves = list()
        i = 1
        while self.is_on_board(self.actual_pos[0] + i, self.actual_pos[1] + i) and chessboard.matrix[self.actual_pos[0] + i - 1][self.actual_pos[1] + i - 1].is_free:
            poss_moves.append((self.actual_pos[0] + i, self.actual_pos[1] + i))
            i += 1

        i = 1
        while self.is_on_board(self.actual_pos[0] - i, self.actual_pos[1] - i) and chessboard.matrix[self.actual_pos[0] - i - 1][self.actual_pos[1] - i - 1].is_free:
            poss_moves.append((self.actual_pos[0] - i, self.actual_pos[1] - i))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0] + i, self.actual_pos[1] - i) and \
                chessboard.matrix[self.actual_pos[0] + i - 1][self.actual_pos[1] - i - 1].is_free:
            poss_moves.append((self.actual_pos[0] + i, self.actual_pos[1] - i))
            i += 1

        i = 1

        while self.is_on_board(self.actual_pos[0] - i, self.actual_pos[1] + i) and \
                chessboard.matrix[self.actual_pos[0] - i - 1][self.actual_pos[1] + i - 1].is_free:
            poss_moves.append((self.actual_pos[0] - i, self.actual_pos[1] + i))
            i += 1
        return poss_moves

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Rook(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self, chessboard):
        poss_moves = list()
        i = 1
        while self.is_on_board(self.actual_pos[0] + i, self.actual_pos[1]) and \
                chessboard.matrix[self.actual_pos[0] + i - 1][self.actual_pos[1] - 1].is_free:
            poss_moves.append((self.actual_pos[0] + i, self.actual_pos[1]))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0] - i, self.actual_pos[1]) and \
                chessboard.matrix[self.actual_pos[0] - i - 1][self.actual_pos[1] - 1].is_free:
            poss_moves.append((self.actual_pos[0] - i, self.actual_pos[1]))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0], self.actual_pos[1] + i) and \
                chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1] + i - 1].is_free:
            poss_moves.append((self.actual_pos[0], self.actual_pos[1] + i))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0], self.actual_pos[1] - i) and \
                chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1] - i - 1].is_free:
            poss_moves.append((self.actual_pos[0], self.actual_pos[1] - i))
            i += 1
        return poss_moves

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class King(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self, chessboard):
        poss_moves = list()
        if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1] + 1):
            poss_moves.append((self.actual_pos[0] + 1, self.actual_pos[1] + 1))
        if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1]):
            poss_moves.append((self.actual_pos[0] + 1, self.actual_pos[1]))
        if self.is_on_board(self.actual_pos[0], self.actual_pos[1] + 1):
            poss_moves.append((self.actual_pos[0], self.actual_pos[1] + 1))
        if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1] - 1):
            poss_moves.append((self.actual_pos[0] + 1, self.actual_pos[1] - 1))
        if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] + 1):
            poss_moves.append((self.actual_pos[0] - 1, self.actual_pos[1] + 1))
        if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] - 1):
            poss_moves.append((self.actual_pos[0] - 1, self.actual_pos[1] - 1))
        if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1]):
            poss_moves.append((self.actual_pos[0] - 1, self.actual_pos[1]))
        if self.is_on_board(self.actual_pos[0], self.actual_pos[1] - 1):
            poss_moves.append((self.actual_pos[0], self.actual_pos[1] - 1))
        return poss_moves

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Queen(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)

    def possible_moves(self, chessboard):
        poss_moves = list()
        i = 1
        while self.is_on_board(self.actual_pos[0] + i, self.actual_pos[1]) and \
                chessboard.matrix[self.actual_pos[0] + i - 1][self.actual_pos[1] - 1].is_free:
            poss_moves.append((self.actual_pos[0] + i, self.actual_pos[1]))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0] - i, self.actual_pos[1]) and \
                chessboard.matrix[self.actual_pos[0] - i - 1][self.actual_pos[1] - 1].is_free:
            poss_moves.append((self.actual_pos[0] - i, self.actual_pos[1]))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0], self.actual_pos[1] + i) and \
                chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1] + i - 1].is_free:
            poss_moves.append((self.actual_pos[0], self.actual_pos[1] + i))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0], self.actual_pos[1] - i) and \
                chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1] - i - 1].is_free:
            poss_moves.append((self.actual_pos[0], self.actual_pos[1] - i))
            i += 1
        while self.is_on_board(self.actual_pos[0] + i, self.actual_pos[1] + i) and \
                chessboard.matrix[self.actual_pos[0] + i - 1][self.actual_pos[1] + i - 1].is_free:
            poss_moves.append((self.actual_pos[0] + i, self.actual_pos[1] + i))
            i += 1

        i = 1
        while self.is_on_board(self.actual_pos[0] - i, self.actual_pos[1] - i) and \
                chessboard.matrix[self.actual_pos[0] - i - 1][self.actual_pos[1] - i - 1].is_free:
            poss_moves.append((self.actual_pos[0] - i, self.actual_pos[1] - i))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0] + i, self.actual_pos[1] - i) and \
                chessboard.matrix[self.actual_pos[0] + i - 1][self.actual_pos[1] - i - 1].is_free:
            poss_moves.append((self.actual_pos[0] + i, self.actual_pos[1] - i))
            i += 1
        i = 1
        while self.is_on_board(self.actual_pos[0] - i, self.actual_pos[1] + i) and \
                chessboard.matrix[self.actual_pos[0] - i - 1][self.actual_pos[1] + i - 1].is_free:
            poss_moves.append((self.actual_pos[0] - i, self.actual_pos[1] + i))
            i += 1
        return poss_moves

    def make_move(self):
        pass

    def remove_figure(self):
        pass


class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (BG_SIZE[0]/8, BG_SIZE[0]/8)
        self.location = ((self.x-1) * BG_SIZE[0]/8, BG_SIZE[0] + (BG_SIZE[1] - BG_SIZE[0])/2 - (self.y-1) * BG_SIZE[0]/8)
        self.is_free = True
        self.figure = None
        # self.area = TODO detect clicking here


class Chessboard:
    def __init__(self, image_path: str):
        self.surface = p.image.load(image_path).convert()
        self.surface = p.transform.scale(self.surface, (BG_SIZE[0], BG_SIZE[0]))
        self.matrix = [[Field(i+1, j+1) for i in range(8)] for j in range(8)]

    def init_chessboard(self, figures):
        """
        Function fill chessboard matrix with figures
        It assigns specific figure to specific field on board and change status of field to not_free
        :param figures:
        :return:
        """
        for figure in figures:
            self.matrix[figure.actual_pos[0]-1][figure.actual_pos[1]-1].is_free = False
            self.matrix[figure.actual_pos[0]-1][figure.actual_pos[1]-1].figure = figure



    @classmethod
    def convert_to_display(cls, x: int, y: int):
        """
        Function convert coordinates to coordinates on chessboard
        The middle of converted coordinates has place in the middle of one chessboard field
        :param x:
        :param y:
        :return: Tuple(int, int)
        """
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
Chessboard_type.init_chessboard(All_figures)

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            #TODO Show request: "Do you really wanna quit?"
            p.quit()
            sys.exit()
        if event.type == p.MOUSEBUTTONUP:
            click_pos = p.mouse.get_pos()
            print(click_pos)
    screen.blit(Chessboard_type.surface, (0, (BG_SIZE[1] - BG_SIZE[0])/2))



    for figure in All_figures:
        figure.show_figure()

    King2.show_possible_moves_on_board(Chessboard_type)

    p.display.update()
    clock.tick(60)
