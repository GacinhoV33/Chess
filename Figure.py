#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as p
from config import BG_SIZE
from abc import abstractmethod


class Figure:
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        self.color = color
        self.name = name
        self.start_pos = (x, y)
        self.actual_pos = (self.start_pos[0], self.start_pos[1])
        self.actual_display_pos = self.convert_to_display(self.actual_pos[0], self.actual_pos[1])
        self.image = p.image.load(image_path).convert_alpha()
        self.image = p.transform.scale(self.image, (int(BG_SIZE[0] / 8), int(BG_SIZE[0] / 8)))
        self.field_frame = p.transform.scale(p.image.load("images/frame.png").convert_alpha(),(int(BG_SIZE[0] / 8), int(BG_SIZE[0] / 8)))
        self.image_path = image_path
        self.figure_id = figure_id
        self.circle_image = p.image.load("images/circle.png").convert_alpha()
        self.circle_image = p.transform.scale(self.circle_image, (int(BG_SIZE[0]/24), int(BG_SIZE[0]/24)))
        self.value = None

    def show_figure(self, screen):
        screen.blit(self.image, self.actual_display_pos)

    def show_possible_moves_on_board(self, chessboard, screen):
        for move in self.possible_moves(chessboard):
            if chessboard.matrix[move[0]-1][move[1]-1].is_free:
                screen.blit(self.circle_image, self.convert_to_display_circle(move[0], move[1]))
            else:
                if chessboard.matrix[move[0]-1][move[1]-1].figure.color != self.color:
                    screen.blit(self.field_frame, self.convert_to_display(move[0], move[1]))

    def make_move(self, x: int, y: int, chessboard, figures):
        if not chessboard.matrix[x - 1][y - 1].is_free and chessboard.matrix[x-1][y-1].figure.color != self.color:
            pop_figure = chessboard.matrix[x-1][y-1].figure
            for num, figure in enumerate(figures):
                if figure.figure_id == pop_figure.figure_id:
                    figures.pop(num)
        self.actual_pos = (x, y)
        self.actual_display_pos = self.convert_to_display(self.actual_pos[0], self.actual_pos[1])

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
