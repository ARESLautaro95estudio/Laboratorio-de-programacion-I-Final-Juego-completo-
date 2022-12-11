from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
import pygame
import sys
from gui_widget import Widget
class FormMenu_09(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
       
        self.is_pause = False
        self.time = pygame.USEREVENT + 0
        pygame.time.set_timer(self.time,1000)  
        self.minuto=60     
        self.pausa = Button(master=self,x=0,y=0,w=90,h=40,color_background=None,color_border=None, on_click = self.on_click_boton ,on_click_param="Pausa",text="Pausa",font="Castellar",font_size=20,font_color=RED)    
        self.timer=Widget(master_form=self,x=100,y=0,w=50,h=40,color_background=None,color_border=NEGRO,image_background=None,text="{0}".format(self.minuto),font="Breadway",font_size=25,font_color=RED)
        self.lista_widget = [self.pausa,self.timer]

    def set_pausa(self,state):
        
        self.is_pause = state
        
    def on_click_boton(self, parametro):
        
        self.set_active(parametro)    
        self.is_pause = True
     