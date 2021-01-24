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
from alien import Alien

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

def update_screen(setting, screen, ship, bullets, aliens):
        # 每次循环时，都重绘屏幕
        screen.fill(setting.bg_color)
        # 在飞船和外星人图片的下面重绘子弹
        for bullet in bullets.sprites():    # bullets.sprites()返回一个列表，其中包括编组bullets中所有精灵
            bullet.draw_bullet()            # 在屏幕上，绘制发射的所有子弹
        ship.blitme()
        # alien.blitme()
        # 在屏幕上绘制编组中的每个外星人
        aliens.draw(screen)
        # 让最近绘制的屏幕可见，while每次执行时，都绘制一个空屏幕，并擦去旧屏幕
        pygame.display.flip()   # flip不断刷新屏幕

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()        # 将为编组bullets中的每颗子弹调用bullet.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():       # 不应从列表或编组中删除条目，因此必须遍历编组的副本
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(setting, alien_width):
    """计算每行可容纳多少外星人"""
    avaliable_space_x = setting.screen_width - (2 * alien_width)        # 可存放外星人的空间，去除左右边距
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))    # 该空间可存放外星人的数量
    return number_aliens_x

def get_number_rows(setting, ship_height, alien_hight):
    """计算屏幕可容纳多少行外星人"""
    # 将屏幕高度减去第一行外星人的上边距（外星人高度）、飞船的高度以及最初外星人高度加上外星人间距（外星人高度的两倍）
    avaliable_space_y = (setting.screen_hight - 
                        (3 * alien_hight) - ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_hight))
    return number_rows

def creat_alien(setting, screen, alien_number, aliens, row_number):
    # 创建一个外星人并将其加入到当前行
    alien = Alien(screen, setting)
    # 外星人间距为外星人宽度
    alien_width = alien.rect.width
    alien_hight = alien.rect.height
    # alien_width = alien.rect.x
    alien.x = alien_width + 2*alien_width * alien_number
    alien.y = alien_hight + 2*alien_hight * row_number 
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def creat_fleet(setting, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(screen, setting)
    number_aliens_x = get_number_aliens_x(setting, alien.rect.width)
    number_rows = get_number_rows(setting, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):   # 可创建的外星人行数
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入到当前行
            creat_alien(setting, screen, alien_number, aliens, row_number)
        
