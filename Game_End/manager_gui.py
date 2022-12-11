from pygame.locals import *
from constantes_gui import *
from gui_form_menu_1 import FormMenu_01
from gui_form_menu_5 import FormMenu_05
from gui_form_menu_10 import FormMenu_10

class Manager_do_formularios:
   
    def __init__(self,screen):
        
        self.screen = screen
       
        self.iniciador()

    def iniciador(self):
               
        self.menu = FormMenu_01 ("Menu",  self.screen , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form=r"fondo_atardecer.png",active=True )                        
          
    def update(self,screen,delta_ms,keys,lista_eventos):
        
        for aux_form in self.menu.forms_dict.values():
            if aux_form.active:
                aux_form.update(lista_eventos,keys,delta_ms,screen)
                aux_form.draw()
                break         
    