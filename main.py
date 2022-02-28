from tkinter import *
from time import sleep
from random import randint


class Player:
    def __init__(self, c, x, y, size, color="RED"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.c = c
        self.body = self.c.create_oval(self.x - self.size / 2,
                                       self.y - self.size / 2,
                                       self.x + self.size / 2,
                                       self.y + self.size / 2,
                                       fill=self.color)

    def moveto(self, x, y):
        self.mx = x
        self.my = y
        self.dx = (self.mx - self.x) / 50
        self.dy = (self.my - self.y) / 50
        self.draw()

    def draw(self):
        self.x += self.dx
        self.y += self.dy
        self.c.move(self.body, self.dx, self.dy)

        print(f"x position of {self.color} is {abs(self.x)}")
        if abs(self.mx - self.x) > 2:
            self.c.after(100, self.draw)

    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5


class Hero(Player):
    def __init__(self, c, x, y, size, color="BLACK"):
        super().__init__(c, x, y, size, color)
        self.boostrate = 2
        self.stamina = 10

    def moveto(self, x, y):
        super().moveto(x, y)
        self.dx = (self.mx - self.x) / 50 * self.boostrate
        self.dy = (self.my - self.y) / 50 * self.boostrate


root = Tk()
root.geometry("400x400")
c = Canvas(root, width=400, height=400)
c.pack()

p1 = Player(c, 25, 25, 20, "GREEN")
p2 = Player(c, 375, 25, 20, "RED")
h1 = Hero(c, 375, 375, 20)

p1.moveto(200, 200)
p2.moveto(200, 200)
h1.moveto(200, 200)

root.mainloop()