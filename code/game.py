# code/game.py
import pygame
import random
import sys
import os

from .settings import LARGURA_TELA, ALTURA_TELA, COR_BRANCA, COR_VERMELHA, COR_VERDE, TEMPO_ALVO
from .background import Background
from .player import Player
from .enemy import Enemy
from .energy import Energy
from .menu import Menu


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Space Survivor")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "MENU"  # Requisito: Começar fixamente na Tela de Menu

        # Mapeamento do caminho absoluto para evitar quebras no .exe do professor
        pasta_principal = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.background = Background()
        self.player = Player(400, 500, self)
        self.interface_menu = Menu()

        self.enemies = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        self.energy_items = pygame.sprite.Group()

        self.score = 0
        self.lives = 3
        self.spawn_timer = pygame.time.get_ticks()
        self.tempo_de_jogo = 0.0

        # Carregamento seguro da trilha sonora para não travar se o som falhar
        try:
            pygame.mixer.init()
            caminho_musica = os.path.join(pasta_principal, "assets", "Score.mp3")
            pygame.mixer.music.load(caminho_musica)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Aviso: Áudio desativado ({e})")

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Requisito: ESC fecha o jogo imediatamente em qualquer tela
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                # Requisito: ENTER inicia a gameplay
                if self.state == "MENU" and event.key == pygame.K_RETURN:
                    self.state = "GAMEPLAY"
                    self.tempo_de_jogo = 0.0

                # Reiniciar após o fim da partida
                elif self.state in ["GAMEOVER", "VITORIA"] and event.key == pygame.K_r:
                    self.reset_game()

    def spawn_enemy(self) -> None:
        if self.state != "GAMEPLAY": return
        agora = pygame.time.get_ticks()
        if agora - self.spawn_timer > 1200:
            self.enemies.add(Enemy(random.randint(50, 750), -40))
            # Gera os itens de energia necessários para cumprir o objetivo
            if random.random() < 0.25:
                self.energy_items.add(Energy(random.randint(50, 750), -40))
            self.spawn_timer = agora

    def check_collisions(self) -> None:
        # Colisões básicas (Míssil destrói inimigo)
        pygame.sprite.groupcollide(self.enemies, self.missiles, True, True)

        # Requisito de Derrota: Vidas chegam a 0 ao colidir com o desafio (inimigos)
        bateram = pygame.sprite.spritecollide(self.player, self.enemies, True)
        for inimigo in bateram:
            self.player.health -= inimigo.damage
            if self.player.health <= 0:
                self.lives -= 1
                self.player.health = 100
                if self.lives < 0:
                    self.state = "GAMEOVER"  # ESTADO DE DERROTA

        # Requisito de Objetivo: Coletar energia espalhada
        coletados = pygame.sprite.spritecollide(self.player, self.energy_items, True)
        for item in coletados:
            self.score += 50
            self.player.health = min(100, self.player.health + item.value)

    def update(self, dt: float) -> None:
        self.background.update(dt)
        if self.state == "GAMEPLAY":
            self.player.update(dt)
            self.enemies.update(dt)
            self.missiles.update(dt)
            self.energy_items.update(dt)
            self.spawn_enemy()
            self.check_collisions()

            # Requisito de Vitória: Contagem regressiva até completar 60 segundos
            self.tempo_de_jogo += dt
            if self.tempo_de_jogo >= TEMPO_ALVO:
                self.state = "VITORIA"  # ESTADO DE VITÓRIA

    def draw(self) -> None:
        self.background.draw(self.screen)

        if self.state == "MENU":
            self.interface_menu.draw(self.screen)

        elif self.state == "GAMEPLAY":
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            self.missiles.draw(self.screen)
            self.energy_items.draw(self.screen)

            # HUD Dinâmico
            tempo_restante = max(0, int(TEMPO_ALVO - self.tempo_de_jogo))
            self.interface_menu.draw_text(self.screen, f"Tempo Restante: {tempo_restante}s", 20, 20, COR_BRANCA)
            self.interface_menu.draw_text(self.screen, f"Vidas: {self.lives}", 20, 55, COR_VERMELHA)
            self.interface_menu.draw_text(self.screen, f"Energia (HP): {self.player.health}%", 20, 90, COR_VERDE)

        elif self.state == "GAMEOVER":
            self.interface_menu.draw_text(self.screen, "GAME OVER", 330, 230, COR_VERMELHA)
            self.interface_menu.draw_text(self.screen, "Pressione 'R' para Reiniciar", 250, 290, COR_BRANCA)
            self.interface_menu.draw_text(self.screen, "Pressione 'ESC' para Sair", 265, 330, COR_BRANCA)

        elif self.state == "VITORIA":
            self.interface_menu.draw_text(self.screen, "VICTORIA! REQUISITO CUMPRIDO", 190, 230, COR_VERDE)
            self.interface_menu.draw_text(self.screen, "Pressione 'R' para Jogar Novamente", 210, 290, COR_BRANCA)
            self.interface_menu.draw_text(self.screen, "Pressione 'ESC' para Sair", 265, 330, COR_BRANCA)

        pygame.display.flip()

    def reset_game(self) -> None:
        self.score = 0
        self.lives = 3
        self.tempo_de_jogo = 0.0
        self.player.health = 100
        self.player.position = pygame.Vector2(400, 500)
        self.enemies.empty()
        self.missiles.empty()
        self.energy_items.empty()
        self.state = "GAMEPLAY"

    def run(self) -> None:
        while self.running:
            dt = max(self.clock.tick(60) / 1000.0, 0.001)
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()
        sys.exit()
