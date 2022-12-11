from gui_button import Button
from constantes_gui import *
from constantes import *
from gui_form import FormMenu
from gui_textbox import TextBox
from gui_widget import Widget
import re

class Quest(FormMenu):
    
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active,ask,ask_seg_reg=None):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        self.w=w
        self.respuesta = False   
        self.ask = ask
        self.question = self.ask.keys()        
        self.crea_answ()
        self.sanitizacion_datos()
        self.opcion_a = Button (master=self,x=80,y=120,w=50,h=75,color_background=None,color_border=None, image_background=r"set_gui_01\Comic\Elements\Element12.png",on_click = self.on_click_boton1 , on_click_param = self.respuesta_a , text="A",font="Castellar",font_size = 18 , font_color = NEGRO)
        self.opcion_b = Button(master=self,x=240,y=120,w=50,h=75,color_background=None,color_border=None, image_background=r"set_gui_01\Comic\Elements\Element12.png",on_click = self.on_click_boton1 , on_click_param = self.respuesta_b , text="B",font="Castellar",font_size = 18 , font_color = NEGRO)
        self.opcion_c =Button (master=self,x=380,y=120,w=50,h=75,color_background=None,color_border=None, image_background=r"set_gui_01\Comic\Elements\Element12.png",on_click = self.on_click_boton1 , on_click_param = self.respuesta_c , text="C",font="Castellar",font_size = 18 , font_color = NEGRO)
        self.surface.set_colorkey(NEGRO)   
        self.pregunta = Widget(master_form=self,x=15,y=0,w=self.w,h=75,color_background = None ,color_border= None,image_background=None, text = self.question ,font="Castellar",font_size=22,font_color=NEGRO)
        
        # if self.ask_seg_reg!=None:
        #     self.ask_seg_reg = ask_seg_reg
        #     self.question_2 = ask_seg_reg.keys()
        
        #     self.pregunta_2 = Widget(master_form=self,x=15,y=75,w=self.w,h=75,color_background = None ,color_border= None,image_background=None, text = self.question_2 ,font="Castellar",font_size=22,font_color=NEGRO)
        
        self.lista_widget = [self.pregunta,self.opcion_a,self.opcion_b,self.opcion_c]
        
        self.acierto = False
        self.error = False
        
    
    def on_click_boton1(self, parametro):

        if parametro == 0:
            self.error=True
            return self.error

        if  parametro ==1:
            self.acierto = True
            self.forms_dict.pop("Pregunta")
            return self.acierto
        #super().on_click_boton1(parametro)
        self.set_active(parametro)


    def update_r(self, lista_eventos,key=[],delta_ms=0,screen=None):
        for widget in self.lista_widget:
            widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for widget in self.lista_widget:
            widget.draw()

    def sanitizacion_datos(self):

        llave_dict = str(self.question)
        string_sucio = re.split( "'",llave_dict)
        palabra=""
        for letra in string_sucio[1]:
            if letra == "/":
                letra = ("\n")
            palabra+=letra
        self.question = str(palabra)   
        return  self.question    
                 
    def sanitizacion_datos_2(self):
        
        llave_dict = str(self.question_2)
        string_sucio = re.split( "'",llave_dict)
        palabra=""
        for letra in string_sucio[1]:
            if letra == "/":
                letra = ("\n")
            palabra+=letra
        self.question_2 = str(palabra)   
        return  self.question_2
       
    def crea_answ(self):
        answer = self.ask.values()
        

        self.respuesta_a=(list(answer)[0][0])
        self.respuesta_b=(list(answer)[0][1])
        self.respuesta_c=(list(answer)[0][2])
        answer = []       
        # if self.ask_seg_reg != None:
        #     answer = self.ask_seg_reg.values()
        #     self.respuesta_a=(list(answer)[0][0])
        #     self.respuesta_b=(list(answer)[0][1])
        #     self.respuesta_c=(list(answer)[0][2])
        #     answer = []
        