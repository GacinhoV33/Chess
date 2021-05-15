#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import BG_SIZE


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
