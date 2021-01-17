#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bullet.py
@Time    :   2021/01/17 20:38:59
@Author  :   GuoRuilong
@Version :   1.0
@Contact :   firelong.guo@hotmail.com
@Desc    :   None
'''

# here put the import lib
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, setting, screen, ship):
        """在飞船所处位置的顶部创建一个子弹对象"""
        super(Bullet, self).__init__()  # 继承Sprite类
        self.screen = screen
        # 在(0,0)处创建一个表示子弹的矩形
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_hight)
        # 将子弹设置正确的位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数点表示的子弹位置
        self.y = float(self.rect.y)
        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor
        # 

    def update(self):
        """子弹向上移动"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
    
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)