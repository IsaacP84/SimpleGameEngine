import numpy as np, pygame, math
from entities.entity import Entity
from entities.bullets.bullet import Bullet

from typing import override,Self


from components.holding import CanBeHeld



class Gun(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 1.5
        self.max_speed = 7.4
        self.turn_speed = math.radians(3)
        
        self.width = 40
        self.height = 20                
        # self.shoot_cooldown = 0
        # self.
        
        
    @classmethod
    @override
    def create(cls, loc=((0,0,0), 0), vel=(0,0,0)) -> Self:
        e = cls()
        e.pos = np.array(loc[0], dtype=np.float32)
        e.vel = np.array(vel, dtype=np.float32)
        e.heading = loc[1]
        
        e.sprite = pygame.Surface((e.width, e.height), pygame.SRCALPHA)
        e.sprite.fill((127, 127, 127))
        
        e.components["CanBeHeld"] = CanBeHeld()
        
        # pygame.draw.rect(p.sprite, (255, 0, 0), (0,75,50,25))
        return e
    def update(self):
        magnitude = np.linalg.norm(self.vel)
            
        if(magnitude > self.max_speed):
            self.vel = (self.vel / magnitude) * self.max_speed

            
    def use(self):
        import config

        print("Used gun")
        app = config.app
        if not app:
            return
        b = app.create_entity(None, Bullet.create, ((0,0,0), 0))
        b.applyForce((10,0,0))
        pass
    
 