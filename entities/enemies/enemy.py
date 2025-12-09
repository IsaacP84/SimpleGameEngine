import numpy as np, pygame, math
from entities.entity import Entity
from typing import override,Self


import config
# if it touches you, you die

class Enemy(Entity):
    def __init__(self):
        super().__init__()
