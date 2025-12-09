import time, sys, pygame, math
from entities.player import Player
from engine import Engine
from globals import clock, Debug

from typing import Callable
import numpy as np

class App:
    def __init__(self):
        self.running = True
        self.engine = Engine(self)
        
        p = self.create_entity("player", Player.create, ((0,0,0), 0))
        
        self.cam_pos = np.array([0,0,0], dtype=np.float32)
        
        self.game_score = 0
        
        
        
        
    def create_entity(self, id: str, func: Callable, *args): 
        e = func(*args)
        self.engine.entities[id] = e
        return e

    def run(self):
        # starts the 
        while(self.running):
            dt = clock.tick(60)
            self.engine.update()
            self.engine.render()
            
            
    
    
    def quit(self):
        self.running = False
        # stop systems






if __name__ == "__main__": 
    print("Hello, world!")
    pygame.init()
    
    
    app = App()

    app.run()
    pygame.quit()
    print("good exit")
    sys.exit()