#!/usr/bin/python
# -*- coding: utf-8 -*-
from Figure import Figure


class Pawn(Figure):
    def __init__(self, color: str, name: str, image_path: str, figure_id: int, x: int, y: int):
        super().__init__(color, name, image_path, figure_id, x, y)
        self.value = 1

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