#!/usr/bin/python
# -*- coding: utf-8 -*-
from Figure import Figure


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


