
import random
# manager = Manager_do_formularios(screen)      
# print(manager.lvl_config)  

from leer_json import Lector_json

data=Lector_json((r"C:/Users/Ares/Cursada Lab 1/Game_End/datas.json"))
lista_preguntas=data.importar_json()

prguntas=lista_preguntas["nivel_uno"] ["Enemigo"]["Hongo"]["lista_preguntas"]

s = random.choice(prguntas)

print(s)