from manager_terreno import Terreno
from manager_materiales import Materiales
from manager_bullet import Manager_Bala
from player import Player
from Enemy_1 import Enemy_02
from Enemy_1 import Enemy_1
import pygame
from constantes import *
import random
from enemigo_03 import Enemigo_03
import pygame
from enemy_traps import Arma_mortal

class Stage:

    def __init__(self,json_data,screen):

        # self.enemigos.lista_balas
        self.json = json_data
        self.screen = screen        
        self.misiones = 0 
        self.player = 0     
        self.terreno = []            
        self.materiales = []              
        self.enemigos = []
        self.enemigo_static = []            
        self.scenario= []           
        self.portales = []      
        self.trampas=[]     
        self.bala= 0
        self.iniciador()
        self.json.clear()
        self.estado_juego2=True

    def iniciador(self):
     
        self.armado_de_terreno()
        self.objetivos()
        self.player = self.armado_de_personaje()
        self.armado_de_enemigos()
        self.armado_de_materiales()
        self.armado_de_balas()
        self.el_unificador()
        self.armado_de_trampas()

    def armado_de_trampas(self):

        cantidad=self.json["trampas"]["sierra"]["set_01"]["cantidad"]
        pos_x =self.json["trampas"]["sierra"]["set_01"]["pos_x"]
        pos_y =self.json["trampas"]["sierra"]["set_01"]["pos_y"]

        for i in range(cantidad):

            self.trampas.append(Arma_mortal(pos_x[i],pos_y[i]))

        cantidad=self.json["trampas"]["sierra"]["set_02"]["cantidad"]
        pos_x =self.json["trampas"]["sierra"]["set_02"]["pos_x"]
        pos_y =self.json["trampas"]["sierra"]["set_02"]["pos_y"]    
        
        for i in range(cantidad):

            self.trampas.append(Arma_mortal(pos_x[i],pos_y[i]))

    def armado_de_terreno(self):
        '''
        Llama a objeto Terreno creando una lista estos objetos tienen metodo(draw/update/colicion)
        Incluye(Muros/plataformas/Techos)
        '''
        self.terreno = Terreno(self.json["plataformas"],self.json["Muros"],self.json["Techos"],self.screen)

    def armado_de_materiales(self):
        '''
        Llama a objeto Materiales creando una lista estos objetos tienen metodo(draw/update/colicion)
        Incluye(Fruits/Portal)
        ''' 
        loot_config = self.json["loot"]
        portal_x = self.json["portal"]["pos_x"]
        portal_y = self.json["portal"]["pos_y"]
        self.materiales = Materiales(loot_config,portal_x,portal_y, self.misiones)
        loot_config.clear()
        
    def objetivos(self):

        for enemigos_eliminados in self.enemigos:
            if enemigos_eliminados.live == False:
                pass
           
    def update(self,screen,delta_ms,keys,lista_eventos):
        '''
        Recibe el screen , delta(tiempo),teclas(get_presed) desde el main
        Mantiene actualizado el objeto llamando a los metodos de los objetos involucrados.
        Ejecuta el metodo .draw y busca coliciones.
        '''      
        self.update_player(screen,keys,delta_ms)    
        self.update_materiales(screen)
        self.update_scenario(screen)  
        self.hud(screen)
        self.estado_juego(screen)
        self.update_enemy(delta_ms,screen,lista_eventos)
        self.bala.update(delta_ms,screen)
        self.update_trampas(screen,delta_ms)
       # self.update_enemy_Static(delta_ms,screen,lista_eventos)

    # def update_enemy_Static(self,delta_ms,screen,lista_eventos):
        
    #     for enemy in self.enemigo_static:
    #         if enemy.live:
    #             enemy.update(delta_ms,self.terreno.plataformas_lista,self.player.rect,screen,lista_eventos)        
    #             enemy.draw(screen)
            
    def update_materiales(self,screen):

        for fruta in self.materiales.lista_loot:
            fruta.draw(screen)
            fruta.colision(self.player.rect_pick_up_collition,fruta)

    def update_scenario(self,screen):
        
        for things in self.scenario:
            things.draw(screen)

    def update_player(self,screen,keys,delta_ms):
        
        self.player.draw(screen)      
        self.player.events(keys,self.terreno.plataformas_lista,self.terreno.muros_lista )
        self.player.update(delta_ms,self.terreno.plataformas_lista , self.terreno.muros_lista,self.terreno.techos_lista ,self.bala.lista_bulets,self.enemigos,self.materiales.lista_loot,self.trampas)
    
    def update_enemy(self,delta_ms,screen,lista_eventos):

        for enemy in self.enemigos:
            enemy.draw(screen)  
            enemy.update(delta_ms,self.terreno.plataformas_lista,self.player.rect,screen,lista_eventos)   
            enemy.move()
            if enemy.live == False:
                self.player.puntos+= 150
                self.misiones -=1
                self.enemigos.remove(enemy)
    
    def update_trampas(self,screen,delta_ms):

        for trampa in self.trampas:
            trampa.draw(screen)
            trampa.update(delta_ms)

    def el_unificador(self):
        '''
        Unifica todos los objetos en una sola lista para iterarla con .draw(screen)
        '''
        self.scenario+=self.terreno.plataformas_lista
        self.scenario+=self.terreno.techos_lista
        self.scenario+=self.terreno.muros_lista
        self.scenario+= self.materiales.lista_portal
        self.scenario+= self.enemigo_static
                 
    def armado_de_balas (self):
        '''
        Unifica objetos materiales,terrenos,enemigos y personaje
        (SUMA LISTAS Y LA DUPLICO UNA PARA DIBUJAR Y OTRA PARA RASTREAR COORDENADAS)
        '''
        self.bala = Manager_Bala(self.player,self.enemigos)

    def armado_de_personaje(self):
        x=self.json["Player"]["pos_x"]
        y=self.json["Player"]["pos_y"]

        return Player(x,y,speed_walk=6,gravity=8,jump_power=25,frame_rate_ms=40,move_rate_ms=10,jump_height=140,vidas=3)
        
    def armado_de_enemigos(self):

        cantidad=self.json["Enemigo"]["lagarto"]["cantidad"] 
        self.misiones = cantidad + self.json["Enemigo"]["pork"]["cantidad"]  +self.json["Enemigo"]["Hongo"]["cantidad"]  
        x=1
        pos_X =self.json["Enemigo"]["lagarto"]["pos_x"]
        
        for i in range(cantidad):
            if x < ANCHO_VENTANA :
                self.enemigos.append(Enemy_1 ( pos_X[i]+x ,self.json["Enemigo"]["lagarto"]["pos_y"][i] ,9,10,12,12))
            if cantidad > 2:  
                s = random.sample(range(40,800),1)
                x=s[0]     

       
        pos_X =self.json["Enemigo"]["pork"]["pos_x"]
        
        for i in range(self.json["Enemigo"]["pork"]["cantidad"]):
            if x < ANCHO_VENTANA :
                self.enemigos.append(Enemy_02 (pos_X[i]+x,self.json["Enemigo"]["pork"]["pos_y"][i],12,12,40))
            #     x+=180
            # if cantidad > 2:   
            #     s = random.sample(range(40,800),1)
            #     x=s[0]

        pos_X =self.json["Enemigo"]["Hongo"]["pos_x"]      
        x=1       
    
        for i in range(self.json["Enemigo"]["Hongo"]["cantidad"]):
            if x < ANCHO_VENTANA :
                
                self.enemigos.append(Enemigo_03 (pos_X[i]+x ,self.json["Enemigo"]["Hongo"]["pos_y"][i] ,12 ,12 ,13 ,40, self.json["Enemigo"]["Hongo"]["lista_preguntas"]))
                self.enemigo_static.append(Enemigo_03 (pos_X[i]+x ,self.json["Enemigo"]["Hongo"]["pos_y"][i] ,12 ,12 ,13 ,40, self.json["Enemigo"]["Hongo"]["lista_preguntas"]))
            if cantidad > 2:
                s = random.sample(range(50,800),1)
                x=s[0]
          
    def estado_juego(self,screen):
        
        if self.misiones==0:
            self.materiales.portal.open       
            if self.player.rect_pick_up_collition.colliderect(self.materiales.portal.rect_colition):
                
                self.estado_juego2=False
                #self.estado_juego2              
        if not(self.player.status_life):
            self.estado_juego2=False
                          
    def hud(self,screen):
        '''LLeva la cuenta '''     
        lifecont = pygame.font.Font(None,50)
        score = pygame.font.Font(None,50)
        life = lifecont.render("Vidas: {0}".format(self.player.vidas),0,(GREEN))
        screen.blit(life,(1000,10))
        puntos = score.render("SCORE: {0}".format(self.player.puntos),0,(GREEN))
        screen.blit(puntos,(10,10))
