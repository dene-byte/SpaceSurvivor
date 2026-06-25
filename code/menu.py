# code/menu.py
import pygame
from .settings import LARGURA_TELA, COR_BRANCA, COR_VERDE


class Menu:
    def __init__(self):
        self.font_titulo = pygame.font.SysFont("Arial", 55, bold=True)
        self.font_opcoes = pygame.font.SysFont("Arial", 26, bold=True)
        self.font_subtitulos = pygame.font.SysFont("Arial", 24, bold=True)
        self.font_texto = pygame.font.SysFont("Arial", 20)

    def draw_text(self, screen: pygame.Surface, text: str, x: int, y: int, color: tuple) -> None:
        surface = self.font_subtitulos.render(text, True, color)
        screen.blit(surface, (x, y))

    def draw(self, screen: pygame.Surface) -> None:
        # Requisito: Exibição exata do Menu da Faculdade
        txt_titulo = self.font_titulo.render("SPACE SURVIVOR", True, COR_VERDE)
        screen.blit(txt_titulo, (LARGURA_TELA // 2 - txt_titulo.get_width() // 2, 60))

        txt_jogar = self.font_opcoes.render("ENTER - Jogar", True, COR_BRANCA)
        txt_sair = self.font_opcoes.render("ESC - Sair", True, COR_BRANCA)
        screen.blit(txt_jogar, (LARGURA_TELA // 2 - txt_jogar.get_width() // 2, 160))
        screen.blit(txt_sair, (LARGURA_TELA // 2 - txt_sair.get_width() // 2, 200))

        txt_cap_controles = self.font_subtitulos.render("CONTROLES", True, COR_VERDE)
        txt_movimentar = self.font_texto.render("↑ ↓ ← → Movimentar", True, COR_BRANCA)
        screen.blit(txt_cap_controles, (LARGURA_TELA // 2 - txt_cap_controles.get_width() // 2, 280))
        screen.blit(txt_movimentar, (LARGURA_TELA // 2 - txt_movimentar.get_width() // 2, 315))

        txt_cap_objetivo = self.font_subtitulos.render("Objetivo:", True, COR_VERDE)
        txt_obj1 = self.font_texto.render("Sobreviva por 60 segundos", True, COR_BRANCA)
        txt_obj2 = self.font_texto.render("e colete a energia.", True, COR_BRANCA)

        screen.blit(txt_cap_objetivo, (LARGURA_TELA // 2 - txt_cap_objetivo.get_width() // 2, 380))
        screen.blit(txt_obj1, (LARGURA_TELA // 2 - txt_obj1.get_width() // 2, 415))
        screen.blit(txt_obj2, (LARGURA_TELA // 2 - txt_obj2.get_width() // 2, 445))
