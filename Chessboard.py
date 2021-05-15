#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as p
from config import BG_SIZE
from Field import Field


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

