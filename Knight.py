#!/usr/bin/python
# -*- coding: utf-8 -*-
from Figure import Figure


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
