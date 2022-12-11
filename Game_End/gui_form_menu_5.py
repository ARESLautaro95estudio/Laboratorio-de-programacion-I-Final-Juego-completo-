from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
import pygame
import sys
from gui_widget import Widget

class FormMenu_05(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active,lvl):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        
        # self.is_pause = is_pause
        self.nivel_actual = lvl     
        self.menu_principal = Button(master = self,x=500,y=190,w=150,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.on_click_boton ,on_click_param="Menu",text="Menu principal ",font="Castellar",font_size=16,font_color=BLUE)      
        self.reanudar = Button(master = self,x=500,y=135,w=150,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.on_click_boton_2 ,on_click_param=None,text="Reanudar ",font="Castellar",font_size=18,font_color=BLUE)               
        self.salir = Button(master=self,x=525,y=400,w=90,h=50,color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.on_click_boton_0 ,on_click_param = "Start" ,text="SALIR ",font="Castellar",font_size=25,font_color=BLUE)      
        self.high = Button(master = self, x=730,y=310,w=140,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.high_sound , on_click_param = None, text = "HIGH" ,font="Castellar",font_size=25,font_color=BLUE)
        self.low = Button(master = self, x=500,y=310,w=140,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.low_sound , on_click_param = None, text = "LOW" ,font="Castellar",font_size=25,font_color=BLUE)
        
        self.off = Button(master = self, x=343,y=310,w=140,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.off_sound , on_click_param = None , text = "OFF " ,font="Castellar",font_size=25,font_color=BLUE)        
        self.soudn_text = Widget(master_form = self, x=475,y=250,w=240,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png",text="SONIDO",font="Castellar",font_size=30,font_color=BLUE)
        self.lista_widget = [ self.menu_principal,self.salir, self.reanudar,self.soudn_text,self.off,self.high,self.low  ]

    def off_sound(self,parametro):

        pygame.mixer.music.set_volume(0.0)

    def high_sound(self,parametro):

        sonido_fondo = pygame.mixer.music.load("bg.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(110.0)
        
    def low_sound(self,parametro):

        sonido_fondo = pygame.mixer.music.load("bg.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

    def on_click_boton(self, parametro): 
        self.forms_dict.pop("Pausa")
        self.set_active(parametro)

    def on_click_boton_2(self,parametro,):

        self.forms_dict.pop("Pausa")
        # self.is_pause(False) 
        self.set_active(self.nivel_actual)
               
    def on_click_boton_0(self,parametro):
        pygame.quit()
        sys.exit() 
