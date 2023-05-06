import pygame as pg


class Air:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = pg.image.load("./images/air.png")
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pg.draw.rect(screen, (0,0,0), (self.x,self.y,self.size, self.size))
        # TEMP #
        font = pg.font.SysFont(None, 24)
        img = font.render("Air", True, "white")
        screen.blit(img, (self.x, self.y))


class Fire:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = pg.image.load("./images/fire.png")
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pg.draw.rect(screen, (0,0,0), (self.x,self.y,self.size, self.size))
        # TEMP #
        font = pg.font.SysFont(None, 24)
        img = font.render("Fire", True, "white")
        screen.blit(img, (self.x, self.y))

class Earth:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = pg.image.load("./images/dirt.png")
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pg.draw.rect(screen, (0,0,0), (self.x,self.y,self.size, self.size))
        # TEMP #
        font = pg.font.SysFont(None, 24)
        img = font.render("Earth", True, "white")
        screen.blit(img, (self.x, self.y))

class Water:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = pg.image.load("./images/water.png")
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pg.draw.rect(screen, (0,0,0), (self.x,self.y,self.size, self.size))
        # TEMP #
        font = pg.font.SysFont(None, 24)
        img = font.render("Water", True, "white")
        screen.blit(img, (self.x, self.y))