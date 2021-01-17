#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   alien.py
@Time    :   2021/01/17 22:17:08
@Author  :   GuoRuilong
@Version :   1.0
@Contact :   firelong.guo@hotmail.com
@Desc    :   None
'''

# here put the import lib
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, screen, setting):
        """初始化外星人并设置起始位置"""
        super(Alien, self).__init__()  # 继承Sprite类，2.x版本写法
        self.setting = setting
        self.screen = screen
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)