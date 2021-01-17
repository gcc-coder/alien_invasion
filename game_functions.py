#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   game_functions.py
@Time    :   2021/01/17 16:36:40
@Author  :   GuoRuilong
@Version :   1.0
@Contact :   firelong.guo@hotmail.com
@Desc    :   None
'''

# here put the import lib
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, setting, screen, ship, bullets):
    """响应按下"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting, screen, ship, bullets)
    elif event.key == pygame.K_q:       # 设置快捷键，按q退出游戏
        sys.exit()

def fire_bullet(setting, screen, ship, bullets):
    """如果没到达限制的子弹数，就可发射"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)     # 将新子弹存储到编组bullets中

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(setting, screen, ship, bullets):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(setting, screen, ship, bullets, alien):
        # 每次循环时，都重绘屏幕
        screen.fill(setting.bg_color)
        # 在飞船和外星人图片的下面重绘子弹
        for bullet in bullets.sprites():    # bullets.sprites()返回一个列表，其中包括编组bullets中所有精灵
            bullet.draw_bullet()
        ship.blitme()
        alien.blitme()
        # 让最近绘制的屏幕可见，while每次执行时，都绘制一个空屏幕，并擦去旧屏幕
        pygame.display.flip()   # flip不断刷新屏幕

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()        # 将为编组bullets中的每颗子弹调用bullet.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)