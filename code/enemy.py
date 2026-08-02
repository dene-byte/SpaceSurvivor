# code/enemy.py
import pygame
import random
from .entity1 import Entity1

class Enemy(Entity1):
    def __init__(self, x: float, y: float):
        self.speed = random.uniform(120.0, 240.0)
        # INCLUSÃO DE IMAGEM: substitua 'nave_inimiga_pequena.png' pelo nome do seu arquivo do inimigo
        # code/enemy.py -> Dentro do __init__
        import os
        pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(os.path.join(pasta_principal, "ASSETS", "nave_inimiga_pequena.png"), x, y, speed_y=self.speed)

        self.damage = 20
        self.score_value = 100

    def update(self, dt: float) -> None:
        super().update(dt)
        # Se passar da borda inferior da tela, apaga o objeto para poupar memória
        if self.rect.top > 600:
            self.kill()
