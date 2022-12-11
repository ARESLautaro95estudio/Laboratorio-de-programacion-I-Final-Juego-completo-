from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_widget import Widget
import pygame
import sys
from sqlite_funciones import insertRow

class FormMenu_10(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active,puntos,lvl_actual):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        
        self.puntos = puntos
        self.lvl_actual = lvl_actual    
        self.menu_principal = Button(master=self,x=500,y=200,w=160,h=40,color_background = None ,color_border = None, image_background=r"set_gui_01\Comic\Buttons\Button_M_04.png",on_click = self.on_click_boton ,on_click_param="Menu",text="menu principal",font="Cooper",font_size=25,font_color=BLUE)                     
        self.next_lvl=self.iniciar_next_lvl()
        self.salir = Button(master=self,x=550,y=260,w=100,h=50,color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_M_04.png", on_click = self.on_click_boton_0 ,on_click_param = "Start" ,text="SALIR ",font="Castellar",font_size=25,font_color=BLUE)  
        self.score = Widget(master_form=self,x=550,y=100,w=100,h=50,color_background = None ,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_M_04.png",text="{0}".format(self.puntos),font="Castellar",font_size=30,font_color=NEGRO)
        self.load_name = TextBox(master=self,x=500,y=45,w=200,h=50,color_background = None ,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_M_04.png",text ="Name",font="Castellar",font_size=21,font_color=NEGRO,on_click=None,on_click_param=None)
        self.guardar = Button(master=self,x=650,y=100,w=75,h=25,color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_M_04.png", on_click = self.guardar_puntaje_nombre ,on_click_param = None,text="Guardar ",font="Castellar",font_size=12,font_color=BLUE)  
        self.lista_widget = [self.menu_principal,self.salir,self.score,self.load_name,self.guardar,self.next_lvl] #self.lvl_select,
    
    def iniciar_next_lvl(self):

        if self.lvl_actual == "nivel_uno":
            proximo_nivel = "nivel_dos"
        elif self.lvl_actual=="nivel_dos":
            proximo_nivel = "nivel_tres"
        elif self.lvl_actual=="nivel_tres":
            proximo_nivel ="Menu"       
       
        return Button(master=self,x=550,y=320,w=100,h=50,color_background=None,color_border=None,image_background=r"set_gui_01\Comic\Buttons\Button_M_04.png", on_click = self.nuevo_nivel ,on_click_param = proximo_nivel ,text="Next level ",font="Castellar",font_size=12,font_color=BLUE)
        
    def nuevo_nivel(self,parametro):

        self.forms_dict.pop(self.lvl_actual)
        self.forms_dict.pop("FIN")    
        if parametro =="Menu":
            self.forms_dict.pop("NIVELES")
            
            self.set_active(parametro)
        else:
            self.forms_dict["NIVELES"].crear_nivel(parametro)

    def on_click_boton_0(self,parametro):

        pygame.quit()
        sys.exit() 

    def on_click_boton(self, parametro):

        self.forms_dict.pop("NIVELES")
        self.forms_dict.pop("FIN")
        self.forms_dict.pop(self.lvl_actual)
        self.set_active(parametro)

    def guardar_puntaje_nombre(self,parametro):

        insertRow(self.load_name._text,self.puntos,self.lvl_actual)
            