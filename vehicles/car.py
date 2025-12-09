from vehicles.vehicle import Vehicle
import numpy as np, pygame,math

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.speed = 0.6
        self.max_speed = 7.4
        self.turn_speed = math.radians(3)
        
    @classmethod
    def create(cls, loc=((0,0,0), 0), vel=(0,0,0)):
        obj = cls()
        obj.pos = np.array(loc[0], dtype=np.float32)
        obj.vel = np.array(vel, dtype=np.float32)
        obj.heading = loc[1]
        
        
        obj.sprite = pygame.Surface((50, 100), pygame.SRCALPHA)
        obj.sprite.fill((255, 255, 255))
        pygame.draw.rect(obj.sprite, (255, 0, 0), (0,75,50,25))
        return obj
        
    def update(self):
        pass