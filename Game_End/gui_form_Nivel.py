from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_widget import Widget
import pygame
from leer_json import Lector_json
from manager_nivel import Stage
from gui_form_menu_10 import FormMenu_10
from gui_form_menu_5 import FormMenu_05

class FormNivel(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        self.name = name
        self.is_pause = False
        self.time = pygame.USEREVENT + 0
        pygame.time.set_timer(self.time,1000)  
        self.minuto = 60     
        self.pausa = Button(master=self,x=0,y=0,w=90,h=40,color_background=None,color_border=None, on_click = self.pausa_on ,on_click_param="Pausa",text="Pausa",font="Castellar",font_size=20,font_color=RED)    
        self.timer=Widget(master_form=self,x=100,y=0,w=50,h=40,color_background=None,color_border=NEGRO,image_background=None,text="{0}".format(self.minuto),font="Breadway",font_size=25,font_color=RED)
        self.lista_widget = [self.pausa,self.timer]

        json_full = Lector_json((r"C:\Users\Ares\Cursada Lab 1\Game_End\datas.json"))
        self.data_lvl = json_full.importar_json()  
        self.lvl = Stage(self.data_lvl[self.name],self.master_surface)
        self.data_lvl.clear()

    def set_pausa(self,state):
        
        self.is_pause = state
        
    def pausa_on(self, parametro):

        FormMenu_05 ("Pausa", self.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form=r"fondo_atardecer.png",active=False,lvl=self.name)    
        self.set_active(parametro)    
        
 
    def update(self,lista_eventos,keys,delta_ms,screen):

        if  self.minuto<=0: #
            self.lvl.player.status_life=False
               
        if self.lvl.estado_juego2==False:
             
            FormMenu_10("FIN",self.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form=r"fondo_atardecer.png",active=False,puntos=self.lvl.player.puntos,lvl_actual=self.name)                                                                                                                                                                       
            self.set_active("FIN")
        for evento in lista_eventos:
            if evento.type ==  self.time:
                self.minuto-=1
        if self.minuto >-1:
            self.timer._text="{0}".format(self.minuto)       
        if not (self.is_pause):
            for aux_widget in self.lista_widget:               
                aux_widget.update(lista_eventos)
        self.lvl.update(screen,delta_ms,keys,lista_eventos)
   