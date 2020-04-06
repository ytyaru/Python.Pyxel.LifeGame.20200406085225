#!/usr/bin/env python3
# coding: utf8
import numpy, random, pyxel

class App:
    def __init__(self):
        self.window = Window()
        self.world = World(self.window.Width, self.window.Height)
        pyxel.run(self.update, self.draw)
    def update(self):
        self.world.update()
    def draw(self):
        self.window.draw()
        self.world.draw()

class Window:
    def __init__(self):
        pyxel.init(self.Width, self.Height, border_width=self.BorderWidth, caption=self.Caption, fps=5)
    @property
    def Width(self): return 64
    @property
    def Height(self): return 48
    @property
    def Caption(self): return "Life game"
    @property
    def BorderWidth(self): return 0
    def update(self): pass
    def draw(self): pyxel.cls(0)

class World:
    def __init__(self, w=32, h=24):
        self.__w = w
        self.__h = h
        self.__colors = (0, 11)
        self.__init_cells()
    @property
    def Width(self): return self.__w
    @property
    def Height(self): return self.__h
    @property
    def Cells(self): return self.__cells
    @property
    def Colors(self): return self.__colors
    def __init_cells(self):
        self.__cells = numpy.array([(1 if random.randint(0, 10) == 0 else 0) for x in range(self.Width * self.Height)]).reshape(self.Height, self.Width)
    def update(self): self.proceed()
    def draw(self):
        pyxel.cls(0)
        for y in range(self.Height):
            for x in range(self.Width):
                pyxel.rect(x, y, 1, 1, self.Colors[1] if self.Cells[y][x] else self.Colors[0])
    def proceed(self):
        next_cells = numpy.zeros((self.Height, self.Width))
        for y in range(self.Height):
            for x in range(self.Width):
                cnt = self.__count_adjacent_cells(x, y)
                if self.__is_birth(x, y, cnt): next_cells[y][x] = 1
                elif self.__is_alive(x, y, cnt): next_cells[y][x] = 1
                elif self.__is_depopulation(x, y, cnt): next_cells[y][x] = 0
                elif self.__is_overcrowding(x, y, cnt): next_cells[y][x] = 0
                else: next_cells[y][x] = self.Cells[y][x]
        self.__cells = next_cells
    def __is_birth(self, x, y, adjs_alive_cells_num):
        if 0 == self.Cells[y][x] and 3 == adjs_alive_cells_num: return True
        else: return False
    def __is_alive(self, x, y, adjs_alive_cells_num):
        if 1 == self.Cells[y][x] and 2 <= adjs_alive_cells_num <= 3: return True
        else: return False
    def __is_depopulation(self, x, y, adjs_alive_cells_num): # 過疎
        if 1 == self.Cells[y][x] and adjs_alive_cells_num <= 1: return True
        else: return False
    def __is_overcrowding(self, x, y, adjs_alive_cells_num): # 過密
        if 1 == self.Cells[y][x] and 4 <= adjs_alive_cells_num: return True
        else: return False
    def __count_adjacent_cells(self, x, y):
        return numpy.count_nonzero(self.__get_adjacent_cells(x, y))
    def __get_adjacent_cells(self, x, y):
        adjs = []
        relatives = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for r in relatives:
            if -1 < x + r[1] < self.Width and -1 < y + r[0] < self.Height:
                adjs.append(self.Cells[y+r[0], x+r[1]])
        return adjs
#        self.Cells[y+-1:y+1+1, x+-1:x+1+1]

App()
