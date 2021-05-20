"""
This class represnts mechanics of game

States:
0 - beggining state, figure not chosen
1 - figure chosen


Mechanics:

State 0:
if figure that's belong to player chosen:
    go to state 1 and mark chosen figure
else:
    stay in state 0

State 1:
if clicked on figure that's belong to player:
    stay in state 1 - change figure #TODO
elif clicked on place where figure cannot go
    back to state 0
elif clicked on figure which may be attacek or on free space where figure might go
    go to state 0 and make move and update chessboard

"""


class Game:
    def __init__(self):
        self.player_turn = "white"
        self.end_of_turn = False
        self.is_game_started = False
        self.state = 0

    def update_chessboard(self, chessboard, figures):
        for i in range(8):
            for j in range(8):
                chessboard.matrix[i][j].is_free = True
                chessboard.matrix[i][j].figure = None

        for figure in figures:
            chessboard.matrix[figure.actual_pos[0] - 1][figure.actual_pos[1] - 1].is_free = False
            chessboard.matrix[figure.actual_pos[0] - 1][figure.actual_pos[1] - 1].figure = figure

        if self.player_turn == "white":
            self.player_turn = "black"
        elif self.player_turn == "black":
            self.player_turn = "white"
