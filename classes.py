#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import abstractmethod
import pygame as p
from config import BG_SIZE

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

    def is_in_area(self, mouse_position: tuple):
        height = BG_SIZE[0] + (BG_SIZE[1]-BG_SIZE[0])/2
        if (self.x -1) * BG_SIZE[0]/8 < mouse_position[0] < self.x * BG_SIZE[0]/8 \
                and height - (self.y-1)*BG_SIZE[0]/8 > mouse_position[1] > height - self.y*BG_SIZE[0]/8:
            return True
        else:
            return False

