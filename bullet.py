import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理 子弹"""
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0,0）处设置一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # store 子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_speed_factor
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """up"""
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        """draw"""
        pygame.draw.rect(self.screen, int(self.color), self.rect)
