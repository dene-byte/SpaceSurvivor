# main.py
import pygame
from code.game import Game

if __name__ == "__main__":
    pygame.init()
    jogo = Game()
    jogo.run()
