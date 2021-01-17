#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ship.py
@Time    :   2021/01/17 15:56:55
@Author  :   GuoRuilong
@Version :   1.0
@Contact :   firelong.guo@hotmail.com
@Desc    :   None
'''

# here put the import lib
import pygame

class Ship():
    def __init__(self, screen, setting):
        """初始化飞船，并设置初始位置"""
        self.screen = screen
        self.setting = setting
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()    # 表示屏幕的矩形
        # 将每艘飞船放置在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 通过rect对象限制飞船的活动范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.setting.ship_speed_factor
        # 将self.center更新到rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)