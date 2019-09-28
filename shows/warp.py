from randomcolor import random_color
from .showbase import ShowBase
from grid import Grid, inset


class Warp(ShowBase):
    def __init__(self, grid: Grid, frame_delay: float = 0.2):
        self.grid = grid
        self.frame_delay = frame_delay
        self.color = random_color(hue='purple')

        # Not sure of the proper formula for this, but allows running on normal or mega triangle.
        self.max_distance = 0
        while grid.select(inset(self.max_distance)):
            self.max_distance += 1


    def set_param(self, name, val):
        if name == 'color_hue':
            try:
                self.color = random_color(hue=val)
            except Exception as e:
                print("Bad Hue Value!", val)
                
    def next_frame(self):
        while True:
            for distance in range(self.max_distance):
                self.grid.clear()
                self.grid.set(inset(distance), self.color)
                self.grid.go()
                yield self.frame_delay
