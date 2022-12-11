from auxiliarjoa import Auxiliar



class  Arma_mortal:

    def __init__(self,x,y):

        self.stay=Auxiliar.getSurfaceFromSpriteSheet(r"Saw\On (38x38).png",8,1)[:]
        self.frame = 0
        self.animation=self.stay
        self.image=self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect_weakpoint = self.rect
        self.rect.x = x
        self.rect.y = y 
        self.tiempo_transcurrido = 0
        self.frame_rate_ms = 40
        
    def draw(self,screen):

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
           
    def update(self,delta_ms):

       # self.tiempo_transcurrido += delta_ms
        #if self.tiempo_transcurrido > self.frame_rate_ms:  
            if(self.frame < len(self.animation) - 1):
                self.frame += 1               
            else: 
                self.frame = 0   
    
