from entities.entity import Entity
from entities.enemies.enemy import Enemy

from components.physics import DoCollisions

import config

import numpy as np, pygame
from typing import override,Self


class Bullet(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 15
        self.max_speed = 15
        
        self._damage_value = 1
        # self.turn_speed = math.radians(3)
        
        self.width = 10
        self.height = 10
        
        self.shooter_id = None
        
        
        self.max_alive_time = 120
        
        self.pierce_count = 0
        self.piece_limit = 1
        
        
    @classmethod
    @override
    def create(cls, loc=((0,0,0), 0), vel=(0,0,0)) -> Self:
        p = cls()
        p.pos = np.array(loc[0], dtype=np.float32)
        p.vel = np.array(vel, dtype=np.float32)
        p.heading = loc[1]
        
        p.sprite = pygame.Surface((p.width, p.height), pygame.SRCALPHA)
        p.sprite.fill((255, 255, 255))
        
        p.components["DoCollisions"] = DoCollisions()
        # pygame.draw.rect(p.sprite, (255, 0, 0), (0,75,50,25))
        return p
    
    @override
    def _update(self):
        magnitude = np.linalg.norm(self.vel)
            
        if(magnitude > self.max_speed):
            self.vel = (self.vel / magnitude) * self.max_speed
            
    @override
    def _damage(self, obj, amount):
        pass
    
    def move(self, f):
        self.applyForce(f * self.speed)
        
    def onCollision(self, obj:Entity):
        # avoids circular dependency
        from entities.player import Player
        
        # Cant shoot yourself
        if config.app.engine.getById(self.shooter_id) == obj:
            return
        
        if(self.pierce_count >= self.piece_limit):
            self.shouldDie = True
            return

        if(isinstance(obj, Bullet)):
            pass
        if(isinstance(obj, Enemy)):
            # try damage
            obj.damage(self, self._damage_value)
            self.pierce_count += 1
        
        if(isinstance(obj, Player)):
            # try damage
            obj.damage(self, self._damage_value)
            self.pierce_count += 1
            
        if self.pierce_count > self.piece_limit:
            self.shouldDie = True
            
        
