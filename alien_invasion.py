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
# from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_hight))  # 设置游戏屏幕布局尺寸
    pygame.display.set_caption("Alien Invasion's Game")     # Title
    # 创建一艘飞船
    ship = Ship(screen, setting)
    # 创建一个外星人
    # alien = Alien(screen, setting)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()
    # 创建外星人群
    gf.creat_fleet(setting, screen, ship, aliens)
    # bg_color = (230, 230, 230)
    # 游戏的主循环
    while True:
        # 监视键盘和鼠标事件 - 关闭时，退出游戏
        gf.check_events(setting, screen, ship, bullets)
        ship.update()       # 飞船的位置将在检测到键盘事件后（但在更新屏幕前）更新。
        gf.update_bullets(bullets)
        gf.update_screen(setting, screen, ship, bullets, aliens)


if __name__ == "__main__":
    run_game()