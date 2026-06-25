# code/energy.py
import pygame
from .entity1 import Entity1

class Energy(Entity1):
    def __init__(self, x: float, y: float):
        # INCLUSÃO DE IMAGEM: Substitua 'sprite_nave_pequena.png' ou use uma imagem de poção/energia aqui
        # code/energy.py -> Dentro do __init__
        import os
        pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(os.path.join(pasta_principal, "ASSETS", "sprite_nave_pequena.png"), x, y, speed_y=120.0)

        self.value = 25

    def update(self, dt: float) -> None:
        super().update(dt)
        if self.rect.top > 600:
            self.kill()
