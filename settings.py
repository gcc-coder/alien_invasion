#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2021/01/17 15:30:05
@Author  :   GuoRuilong
@Version :   1.0
@Contact :   firelong.guo@hotmail.com
@Desc    :   None
'''

# here put the import lib
class Settings():
    """存储《Alien Invasion》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1000
        self.screen_hight = 600
        self.bg_color = (230, 230, 230)     # 浅蓝色：187 255 255
        self.ship_speed_factor = 1.5
        # 设置子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3     # 限制子弹在屏幕中显示的数量
