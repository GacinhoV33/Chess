#!/usr/bin/python
# -*- coding: utf-8 -*-


class Player:

    def __init__(self, color: str):
        self.score = self.get_score()
        self.color = color
        self.is_on_move = True if self.color == "white" else False
        self.player_figures = list()

    def get_figures_on_chessboard(self, chessboard):
        for row in chessboard.matrix:
            for figure in row:
                if figure.color == self.color:
                    self.player_figures.append(figure)

    def make_move(self, flag):
        pass

    def get_score(self):
        score = 0
        for figure in self.player_figures:
            score += figure.value
        return score

