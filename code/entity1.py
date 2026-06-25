# code/entity1.py
import pygame

class Entity1(pygame.sprite.Sprite):
    def __init__(self, image_path: str, x: float, y: float, speed_y=0.0):
        super().__init__()
        # INCLUSÃO DE IMAGEM: O caminho do arquivo é passado por parâmetro pelas classes filhas
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(x, y)
        self.rect.topleft = (int(self.position.x), int(self.position.y))
        self.velocity = pygame.Vector2(0, speed_y)

    def update(self, dt: float) -> None:
        # Lógica de movimentação física baseada no Delta Time
        self.position += self.velocity * dt
        self.rect.topleft = (int(self.position.x), int(self.position.y))

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
