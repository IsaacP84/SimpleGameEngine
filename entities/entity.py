import numpy as np, pygame, math

from abc import ABC, abstractmethod
from typing import Self

class Entity(ABC):
    def __init__(self):
        self.pos = np.array([0,0,0], dtype=np.float32)
        self.vel = np.array([0,0,0], dtype=np.float32)
        self.heading = 0
                
        self.sprite = None
        self.shouldRender = True
        
        self.components = dict()
        
        
    @classmethod
    @abstractmethod
    def create(cls,loc: tuple[tuple[float,float,float],float], vel:tuple[float,float,float]=(0,0,0)) -> Self | None:
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    def applyForce(self, f=(0,0,0)):
        f = np.array(f, dtype=np.float32)
        self.vel += f