import pygame
import numpy as np
import math

from entities.player import Player

from globals import screen, clock, screen_height, screen_width, Debug
from physics import physics, applyFriction, cartesian_to_spherical, normalize

class Engine:
    def __init__(self, app):
        self.app = app
        self.entities = dict()
        
        
    def update(self):
        for event in pygame.event.get():
        # Check if the user clicked the close button
            if event.type == pygame.QUIT:
                self.app.quit()
            # if event.type == pygame.KEYDOWN:
                
        pressed = pygame.key.get_pressed()
        player = self.entities["player"]
        
        move_force = np.array((0,0,0), dtype=np.float32)
        if(pressed[pygame.K_w]):
            # player.moveUp()
            move_force += (0,-1,0)
        
            
        if(pressed[pygame.K_a]):
            # player.moveRight()
            move_force += (-1,0,0)
            
            
        if(pressed[pygame.K_s]):
            # player.moveDown()
            move_force += (0,1,0)
           
            
        if(pressed[pygame.K_d]):
            # player.moveLeft()
            move_force += (1,0,0)
        
        move_force = normalize(move_force)
        player.applyForce(move_force)
            
        if(pressed[pygame.K_SPACE]):
            player.shoot()
        
        for e in self.entities.values():
            e.heading = e.heading % (2 * np.pi)
            
        physics(self.entities.values())
        
        
        for e in self.entities.copy().values():
            e.alive_time += 1
            if e.max_alive_time:
                if(e.alive_time >= e.max_alive_time):
                    self.kill(e)
                    
        

   
    def render(self):
        screen.fill((0,0,0))
        # draw entities
        for key, e in self.entities.items():
            if(not e.shouldRender):
                continue
            # Rotate the image
            rotated_image = pygame.transform.rotate(e.sprite, math.degrees(e.heading))
            # Get the new rectangle, centered on the original center
            dest = rotated_image.get_rect(center=(0,0))
            dest.move_ip(float(e.pos[0]), float(e.pos[1]))
            screen.blit(rotated_image, dest)
            
            
        # debug
        player = self.entities["player"]
        active_object = player
        
        debug_strings = []
        debug_strings.append(f"Pos: {int(active_object.pos[0])}, {int(active_object.pos[1])}, {int(active_object.pos[2])}")
        debug_strings.append(f"Heading: {active_object.heading:.{3}g}")
        debug_strings.append(f"Vel: {active_object.vel[0]:.{3}g}, {active_object.vel[1]:.{3}g}, {active_object.vel[2]:.{3}g}")
        debug_strings.append(f"Entities: {len(self.entities)}")
        for i, string in enumerate(debug_strings):
            text_surface = Debug.font().render(string, True, (0, 122, 0))
            screen.blit(text_surface, (0,20*i,100,100))
            
            
        text_surface = Debug.font().render(str(int(clock.get_fps())), True, (0, 122, 0))
        screen.blit(text_surface, (0,screen_height-20,100,100))
        
        pygame.display.flip()
        
    def kill(self, e):
        for key, val in self.entities.copy().items():
            if e == val:
                self.entities.pop(key)
