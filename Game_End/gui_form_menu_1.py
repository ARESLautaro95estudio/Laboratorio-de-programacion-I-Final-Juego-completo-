import pygame
import sys
from pygame.locals import *
from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_form_menu_2 import FormMenu_02
from gui_form_menu_4 import FormMenu_04

class FormMenu_01(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.niveles = Button(master=self,x=290,y=100,w=140,h=50,color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.menu_niveles ,on_click_param = "NIVELES", text = " Niveles " ,font="Castellar",font_size=25,font_color = BLUE)        
        self.opciones = Button(master=self,x=700,y=100,w=150,h=50,color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.menu_opciones ,on_click_param = "Opciones" , text = "OPCIONES" ,font="Castellar",font_size=25,font_color=BLUE)
        self.salir = Button(master=self,x=500,y=500,w=90,h=50,color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_L_04.png", on_click = self.on_click_boton_0 ,on_click_param = "Start" ,text="SALIR ",font="Castellar",font_size=25,font_color=BLUE)        
     
        self.lista_widget = [self.niveles,self.opciones,self.salir]

    def menu_niveles(self,parametro):

        FormMenu_02 ("NIVELES", self.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form=r"fondo_atardecer.png",active=False)       
        self.set_active("NIVELES")

    def menu_opciones(self,parametro):

        FormMenu_04 ("Opciones", self.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form=r"fondo_atardecer.png",active=False)       
        self.set_active("Opciones")

    def on_click_boton_0(self,parametro):
        pygame.quit()
        sys.exit() 
      