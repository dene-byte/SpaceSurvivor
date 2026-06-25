# code/missile.py
import pygame
from .entity1 import Entity1


class Missile(Entity1):
    def __init__(self, x: float, y: float, owner: str):
        self.speed = 600.0
        self.owner = owner
        self.damage = 10
        speed_y = -self.speed if owner == "player" else self.speed

        # INCLUSÃO DE IMAGEM: Substitua 'missil_pequeno.png' pelo nome do seu arquivo de projétil
        # code/missile.py -> Dentro do __init__
        import os
        pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        super().__init__(os.path.join(pasta_principal, "ASSETS", "missil_pequeno.png"), x, y, speed_y=speed_y)

        self.rect.centerx = x

    def update(self, dt: float) -> None:
        super().update(dt)
        # Remove o míssil da memória se ele sair dos limites visíveis da tela
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()
