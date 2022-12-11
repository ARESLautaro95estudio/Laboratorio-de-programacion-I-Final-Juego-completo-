from constantes import *
from auxiliarjoa import *
import pygame

class Bala():

    def __init__(self,x,y,direction,objetos):
        
        self.bullet_r = Auxiliar.getSurfaceFromSpriteSheet("Recursos\Items\Fruits\Apple.png",17,1)[:]
        self.bullet_l = Auxiliar.getSurfaceFromSpriteSheet("Recursos\Items\Fruits\Apple.png",17,1,True)[:]
        self.direction = direction
        self.frame = 0
        self.animation = self.bullet_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
        self.rect_weakpoint = self.rect 
        self.move_x = 12
        self.move_y = 0.3
        self.live = True
        self.coldown = 0 
        self.objetos = objetos
        
    def draw(self,screen):

        screen.blit(self.image,self.rect)

    def update(self):
        
        if self.coldown > 0:
            self.coldown -= 1
            self.movement()
            if self.direction == DIRECTION_R:
                self.animation = self.bullet_r
            else:
                self.animation =self.bullet_l
        self.colition()

    def movement(self):

        if self.live:
            self.add_x(self.move_x)
            self.add_y(self.move_y)
            if self.rect.x > ANCHO_VENTANA:
                self.live=False
            if self.rect.x < 0 :
                self.live=False
        
    def add_x(self,delta_x):

        if self.direction==DIRECTION_L:
            self.rect.x -= delta_x
        elif self.direction==DIRECTION_R:
            self.rect.x += delta_x
       
    def add_y(self,delta_y):
        
        self.rect.y += delta_y  
    
    def colition(self):

        for objeto in self.objetos:
            if self.rect_weakpoint.colliderect(objeto.rect):
                self.live = False
