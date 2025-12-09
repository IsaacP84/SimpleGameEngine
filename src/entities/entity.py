import numpy as np, pygame, math

from abc import ABC, abstractmethod
from typing import Self
import config

class Entity(ABC):
    def __init__(self):
        self.pos = np.array([0,0,0], dtype=np.float32)
        self.vel = np.array([0,0,0], dtype=np.float32)
        self.heading = 0
                
        self.sprite = None
        self.shouldRender = True
        
        self.components = dict()
        
        self.alive_time = 0
        self.max_alive_time = None
        
        self.width = 0
        self.height = 0
        
        self.shouldDie = False
        
        self._immunity_timer = 0
        self._immunity_frames = 10
        
    @classmethod
    @abstractmethod
    def create(cls,loc: tuple[tuple[float,float,float],float], vel:tuple[float,float,float]=(0,0,0)) -> Self | None:
        pass
    
    @abstractmethod
    def _update(self):
        pass
    
    def update(self):
        self._update()
        self._immunity_timer = max(0, self._immunity_timer - 1)
    
    @abstractmethod
    def _damage(self, obj, amount):
        pass
    
    def damage(self, obj, amount):
        from entities.bullets.bullet import Bullet
        if self._immunity_timer > 0:
            return
        self._immunity_timer = self._immunity_frames
        self._damage(obj, amount)
        if config.SHOW_DEBUG:
            if isinstance(obj, Bullet):
                shooter = config.app.engine.getById(obj.shooter_id)
                print(f"Damaged by {obj.__class__.__name__}:{config.app.engine.getId(obj)}, from {shooter.__class__.__name__}:{obj.shooter_id}")
            else:
                print(f"Damaged by {obj.__class__.__name__}:{config.app.engine.getId(obj)}")
    
    def applyForce(self, f=(0,0,0)):
        f = np.array(f, dtype=np.float32)
        self.vel += f