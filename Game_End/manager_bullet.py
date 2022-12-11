import pygame
from bullet import Bala

class Manager_Bala :

    def __init__(self,data_player,lista_enemigos):

        self.player = data_player
        self.enemy_list=[]
        self.enemy_list += lista_enemigos
        self.lista_bulets= []
        #self.get_balas()

    def update(self,delta_ms,screen,lista_muros=[],lista_plataformas=[]):

        stage = lista_muros+lista_plataformas
        self.get_balas(screen,delta_ms)
       # self.bullet_update(screen)
        self.balas_state(stage)
        self.player_update(screen)
        self.enemigo_update(delta_ms)
         
    def balas_state(self,stage):

        for bullet in self.lista_bulets:        
            for block in stage:
                if bullet.colliderect(block.rect):
                    bullet.live=False             
                    self.lista_bulets.remove(bullet)
      
    # def bullet_update(self,screen):
        
    #     for bala in self.lista_bulets: 

    #         if  bala.live:
    #                     bala.draw(screen)
    #                     bala.movement() 
    #                     bala.update()
            # if bala.live == False:
            #     self.lista_bulets.remove(bala)

    def enemigo_update(self,delta_ms):

        for enemigo in self.enemy_list:

            self.player.colition(self.lista_bulets,delta_ms)

    def player_update(self,screen):

        for balas in self.player.lista_balas:
            if balas.live:
                balas.draw(screen)
                balas.movement() 
                balas.update()
                for enemigo in self.enemy_list:
                    enemigo.colision(balas.rect,screen)
                    
    def get_balas(self,screen,delta_ms):
      
        for enemigo in self.enemy_list:
            self.lista_bulets=enemigo.lista_balas
            self.player.colition(self.lista_bulets,delta_ms)
            for bala in self.lista_bulets:
                if  bala.live:
                        bala.draw(screen)
                        bala.movement() 
                        bala.update()

                elif not(bala.live):
                    self.lista_bulets.remove(bala)
            #     print(bala.live)
            # print(len(self.lista_bulets))
              
    def draw(self,screen):
        pass