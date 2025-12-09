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
        self.useCooldown = 2/60
        self.useCooldownTimer = 0
        
        
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
    def _update(self):
        magnitude = np.linalg.norm(self.vel)
            
        if(magnitude > self.max_speed):
            self.vel = (self.vel / magnitude) * self.max_speed
            
        self.useCooldownTimer = max(0, self.useCooldownTimer - 1)

    @override
    def _damage(self, obj, amount):
        pass
    def use(self):
        import config
        if(self.useCooldownTimer > 0):
            return

        print("Used gun")
        app = config.app
        if not app:
            return
        b, id = app.create_entity(Bullet.create, (self.pos, self.heading))
        cbh = self.components["CanBeHeld"]
        # holder_id = app.engine.getById(cbh.holder_id)
        b.shooter_id = cbh.holder_id
        
        
        b.applyForce((10,0,0))
        
        self.useCooldownTimer = self.useCooldown
    
 