# code/player.py
import pygame
import os
from .entity1 import Entity1
from .missile import Missile
from .settings import LARGURA_TELA, ALTURA_TELA


class Player(Entity1):
    def __init__(self, x: float, y: float, game_instance):
        # Localiza de forma segura a pasta ASSETS e a imagem do jogador
        pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        caminho_imagem = os.path.join(pasta_principal, "assets", "Player2.png")

        super().__init__(caminho_imagem, x, y)
        self.game = game_instance
        self.health = 100
        self.speed = 400.0
        self.fire_rate = 250  # Tempo entre os tiros em milissegundos
        self.last_shot = pygame.time.get_ticks()

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        self.velocity.xy = (0, 0)

        # Controles por Setas ou WASD
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  self.velocity.x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: self.velocity.x = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:    self.velocity.y = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  self.velocity.y = self.speed

    def shoot(self) -> None:
        keys = pygame.key.get_pressed()
        agora = pygame.time.get_ticks()

        # Atira ao pressionar ESPAÇO se o tempo de recarga passou
        if keys[pygame.K_SPACE] and (agora - self.last_shot > self.fire_rate):
            missil = Missile(self.rect.centerx, self.rect.top, owner="player")
            self.game.missiles.add(missil)
            self.last_shot = agora

    def update(self, dt: float) -> None:
        self.move()
        self.shoot()
        super().update(dt)

        # Impede a nave do jogador de sair das bordas da tela
        if self.rect.left < 0: self.position.x = 0
        if self.rect.right > LARGURA_TELA: self.position.x = LARGURA_TELA - self.rect.width
        if self.rect.top < 0: self.position.y = 0
        if self.rect.bottom > ALTURA_TELA: self.position.y = ALTURA_TELA - self.rect.height
        self.rect.topleft = (int(self.position.x), int(self.position.y))