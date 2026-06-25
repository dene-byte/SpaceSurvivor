# code/background.py
# code/background.py
import pygame
from .settings import LARGURA_TELA, ALTURA_TELA


class Background:
    def __init__(self):
        import os
        # Descobre o caminho da pasta principal do jogo automaticamente
        pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # CORREÇÃO: Aponta exatamente para dentro da pasta ASSETS
        caminho_imagem = os.path.join(pasta_principal, "ASSETS", "space bg game.png")

        # Carrega a imagem usando o caminho seguro do sistema
        imagem_original = pygame.image.load(caminho_imagem).convert()
        self.imagem = pygame.transform.scale(imagem_original, (LARGURA_TELA, ALTURA_TELA))
        self.y = 0.0
        self.speed = 80.0

    def update(self, dt: float) -> None:
        self.y += self.speed * dt
        if self.y >= ALTURA_TELA:
            self.y = 0

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.imagem, (0, int(self.y)))
        screen.blit(self.imagem, (0, int(self.y) - ALTURA_TELA))
