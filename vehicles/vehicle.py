from entity import Entity
import numpy as np, pygame,math

class Vehicle(Entity):
    def __init__(self):
        Entity.__init__(self)
        
        self.speed = 0
        self.max_speed = 0
        self.turn_speed = 0
        
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
        
    def moveForward(self):
        self.applyForce((np.sin(self.heading) * self.speed,
                         np.cos(self.heading) * self.speed,
                         0))
    
    def moveBackward(self):
        self.applyForce((np.sin(self.heading) * -self.speed,
                         np.cos(self.heading) * -self.speed,
                         0))
        
    def turnLeft(self):
        self.heading += self.turn_speed
        
        
    def turnRight(self):
        self.heading -= self.turn_speed