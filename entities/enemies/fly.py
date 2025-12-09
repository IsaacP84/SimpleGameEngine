import numpy as np, pygame, math
from entities.entity import Entity
from typing import override,Self


class Fly(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 1.5
        self.max_speed = 7.4
        self.turn_speed = math.radians(3)
        
        self.width = 50
        self.height = 50
                
        # self.shoot_cooldown = 0
        # self.
        
        
    @classmethod
    @override
    def create(cls, loc=((0,0,0), 0), vel=(0,0,0)) -> Self:
        p = cls()
        p.pos = np.array(loc[0], dtype=np.float32)
        p.vel = np.array(vel, dtype=np.float32)
        p.heading = loc[1]
        
        p.sprite = pygame.Surface((p.width, p.height), pygame.SRCALPHA)
        p.sprite.fill((255, 255, 255))
        # pygame.draw.rect(p.sprite, (255, 0, 0), (0,75,50,25))
        return p
    def update(self):
        magnitude = np.linalg.norm(self.vel)
            
        if(magnitude > self.max_speed):
            self.vel = (self.vel / magnitude) * self.max_speed
            
    def shoot(self):
        pass
    
    def move(self, f):
        self.applyForce(f * self.speed)
