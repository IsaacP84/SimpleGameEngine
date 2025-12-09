import numpy as np, pygame, math
from entities.enemies.enemy import Enemy
from components.stats import Health

from components.physics import DoCollisions

from typing import override,Self

from physics import normalize


import config
# if it touches you, you die

class Fly(Enemy):
    def __init__(self):
        super().__init__()
        self.speed = 0.5
        self.max_speed = 1
        self.turn_speed = math.radians(3)
        
        self.width = 50
        self.height = 50
        
        
        self.move_direction = (0,0,0)
                
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
        
        p.components["Health"] = Health(10)
        p.components["DoCollisions"] = DoCollisions()

        # pygame.draw.rect(p.sprite, (255, 0, 0), (0,75,50,25))
        return p
    
    @override
    def _update(self):
        magnitude = np.linalg.norm(self.vel)
            
        if(magnitude > self.max_speed):
            self.vel = (self.vel / magnitude) * self.max_speed
            
        player = config.app.engine.entities.get(config.player_id)
        
        # search for player
        if self.alive_time % 20 == 0:
            
            move_force = np.array((0, 0, 0), dtype=np.float32)
            if player.pos[1] < self.pos[1]:
                move_force += (0, -1, 0)
        
            if player.pos[0] < self.pos[0]:
                move_force += (-1, 0, 0)

            if player.pos[1] > self.pos[1]:
                move_force += (0, 1, 0)
        
            if player.pos[0] > self.pos[0]:
                move_force += (1, 0, 0)

            move_force = normalize(move_force)
            self.move_direction = move_force
        self.applyForce(self.move_direction)
        
        
    @override
    def _damage(self, obj, amount):
        health = self.components.get("Health")
        health.value -= amount
        
    def onCollision(self, obj):
        # avoids circular dependency
        from entities.player import Player

        
        if(isinstance(obj, Enemy)):
           pass
        
        if(isinstance(obj, Player)):
            obj.damage(self, 1)
            # try damage
            # obj.damage(self, self._damage)
            pass
        
    # def shoot(self):
    #     pass
    
    def move(self, f):
        self.applyForce(f * self.speed)
