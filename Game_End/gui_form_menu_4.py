from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
import pygame 
from gui_widget import Widget
from gui_form_menu_3 import FormMenu_03
class FormMenu_04(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        
        self.on = Button(master = self, x=353,y=210,w=140,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.on_sound , on_click_param = None, text = "ON" ,font="Castellar",font_size=25,font_color=RED)
        self.off = Button(master = self, x=740,y=210,w=140,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.off_sound , on_click_param = None , text = "OFF " ,font="Castellar",font_size=25,font_color=RED)        
        self.back_option = Button(master = self,x=0,y=540,w=100,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.back_boton ,on_click_param="Menu",text="BACK ",font="Castellar",font_size=25,font_color=RED)        
        self.puntaje =Button(master = self,x=500,y=50,w=240,h=70, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.crear_ranking ,on_click_param="High score",text="Puntaje ",font="Castellar",font_size=30,font_color=RED)  
        self.soudn_text = Widget(master_form = self, x=500,y=130,w=240,h=50, color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png",text="SONIDO",font="Castellar",font_size=30,font_color=RED)
    
        self.lista_widget = [self.back_option,self.on,self.off,self.soudn_text,self.puntaje]

    def back_boton(self,parametro):
        
        self.forms_dict.pop("Opciones")
        self.set_active(parametro)

    def crear_ranking(self,parametro):

        FormMenu_03 ("High score",self.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(GREEN_PERS),color_border=(None),image_background_form=r"fondo_atardecer.png",active=False)
        self.set_active("High score")

    def on_click_boton(self, parametro): 
          
        self.set_active(parametro)

    def off_sound(self,parametro):

        pygame.mixer.music.set_volume(0.0)

    def on_sound(self,parametro):
        sonido_fondo = pygame.mixer.music.load("bg.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(110.0)
        
   