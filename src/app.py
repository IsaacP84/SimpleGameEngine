import time, sys, pygame, math
from entities.player import Player
from entities.enemies.fly import Fly
from entities.weapons.gun import Gun
from engine import Engine
from globals import clock, Debug, screen_width, screen_height
import config

from typing import Callable
import numpy as np

import uuid

class App:
    def __init__(self):
        self.running = True
        self.paused = False
        self.engine = Engine(self)
        
       
        
        
        
        
    def create_entity(self, func: Callable, *args): 
        e = func(*args)
        id = uuid.uuid4()
        self.engine.entities[id] = e
        if config.SHOW_DEBUG:
            print(f"Created entity {id}")
        return e, id

    def setup(self):
        p, config.player_id = self.create_entity(Player.create, ((20,screen_height/2,0), 0))
        gun, _ = self.create_entity(Gun.create, ((0,0,0),0))
        p.components.get("CanHold").hold(p, gun)
        
        self.cam_pos = np.array([0,0,0], dtype=np.float32)
        
        self.game_score = 0
        
        for i in range(5):
            fly, _ = self.create_entity(Fly.create, ((screen_width-20,screen_height/2 + (i-2.5) * 50,0), 0))
            
            
    def run(self):
        # starts the 
        while(self.running):
            dt = clock.tick(60)
            self.engine.update()
            self.engine.render()
    def doGameWin(self):
        self.paused = True
        print("You win")
        for key, e in self.engine.entities.copy().items():
            # if e == self.engine.entities[config.player_id]:
            #     continue
            self.engine.kill(e)
            
        # put up some text
            
        
    def doGameOver(self):
        self.paused = True
        print("You died")
        for key, e in self.engine.entities.copy().items():
            if e == self.engine.entities[config.player_id]:
                continue
            self.engine.kill(e)
    
    
    def quit(self):
        self.running = False
        # stop systems






if __name__ == "__main__": 
    print("Hello, world!")
    pygame.init()
    config.app = App()
    config.app.setup()
    config.app.run()
    pygame.quit()
    print("good exit")
    sys.exit()