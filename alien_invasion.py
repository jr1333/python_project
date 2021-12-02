# alien_invasion.py
# import sys
from pygame.sprite import Group
import pygame
from setting import Setting
from game_stats import GameStats
from ship import Ship
from alien import Alien
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象,setting initial
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 注意这里是元组
    pygame.display.set_caption("Alien Invasion")
    # create play
    play_button = Button(ai_settings, screen, "Play")
    # create shili
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 设置背景色
    # bg_color = (230, 230, 230)
    # chuangjian alien
    alien = Alien(ai_settings, screen)
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # bullet
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # print(len(bullets))
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()

