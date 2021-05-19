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
                poss_moves = list()
                if chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1]].is_free:
                    poss_moves.append((self.actual_pos[0], self.actual_pos[1] + 1))
                if chessboard.matrix[self.actual_pos[0] -1][self.actual_pos[1] + 1].is_free:
                    poss_moves.append((self.actual_pos[0], self.actual_pos[1]+2))
                if self.is_on_board(self.actual_pos[0]+1, self.actual_pos[1]+1):
                    if not chessboard.matrix[self.actual_pos[0]][self.actual_pos[1]].is_free and chessboard.matrix[self.actual_pos[0]][self.actual_pos[1]].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0]+1, self.actual_pos[1]+1))
                if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] + 1):
                    if not chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]].is_free and chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0]-1, self.actual_pos[1]+1))
                return poss_moves
            else:
                poss_moves = list()
                if chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1]].is_free:
                    poss_moves.append((self.actual_pos[0], self.actual_pos[1] + 1))
                if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1] + 1):
                    if not chessboard.matrix[self.actual_pos[0]][self.actual_pos[1]].is_free and chessboard.matrix[self.actual_pos[0]][self.actual_pos[1]].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0]+1, self.actual_pos[1]+1))
                if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] + 1):
                    if not chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]].is_free and chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0]-1, self.actual_pos[1]+1))
                return poss_moves

        elif self.color == "black":
            if self.actual_pos == self.start_pos:
                poss_moves = list()
                if chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1]-2].is_free:   #TODO add is_on_board to first if
                    poss_moves.append((self.actual_pos[0], self.actual_pos[1] - 1))
                if chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1] - 3].is_free:
                    poss_moves.append((self.actual_pos[0], self.actual_pos[1] - 2))
                if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] - 1):
                    if not chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]-2].is_free and chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]-2].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0]-1, self.actual_pos[1]-1))
                if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1] - 1):
                    if not chessboard.matrix[self.actual_pos[0]][self.actual_pos[1]-2].is_free and chessboard.matrix[self.actual_pos[0]][self.actual_pos[1]-2].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0]+1, self.actual_pos[1]-1))
                return poss_moves
            else:
                poss_moves = list()
                if chessboard.matrix[self.actual_pos[0] - 1][self.actual_pos[1] - 2].is_free:
                    poss_moves.append((self.actual_pos[0], self.actual_pos[1] - 1))
                if self.is_on_board(self.actual_pos[0] - 1, self.actual_pos[1] - 1):
                    if not chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]-2].is_free and chessboard.matrix[self.actual_pos[0]-2][self.actual_pos[1]-2].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0]-1, self.actual_pos[1]-1))
                if self.is_on_board(self.actual_pos[0] + 1, self.actual_pos[1] - 1):
                    if not chessboard.matrix[self.actual_pos[0]][self.actual_pos[1] - 2].is_free and \
                            chessboard.matrix[self.actual_pos[0]][self.actual_pos[1] - 2].figure.color != self.color:
                        poss_moves.append((self.actual_pos[0] + 1, self.actual_pos[1] - 1))
                return poss_moves

        else:
            raise ValueError("Wrong color type assigned")

    def remove_figure(self):
        pass