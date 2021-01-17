#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   alien_invasion.py
@Time    :   2021/01/17 15:16:18
@Author  :   GuoRuilong
@Version :   1.0
@Contact :   firelong.guo@hotmail.com
@Desc    :   None
'''

# here put the import lib
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_hight))
    pygame.display.set_caption('Alien Invasion')
    # 创建一艘飞船
    ship = Ship(screen, setting)
    alien = Alien(screen, setting)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # bg_color = (230, 230, 230)
    # 游戏的主循环
    while True:
        # 监视键盘和鼠标事件 - 关闭时，退出游戏
        gf.check_events(setting, screen, ship, bullets)
        ship.update()       # 飞船的位置将在检测到键盘事件后（但在更新屏幕前）更新。
        gf.update_bullets(bullets)
        gf.update_screen(setting, screen, ship, bullets, alien)


if __name__ == "__main__":
    run_game()