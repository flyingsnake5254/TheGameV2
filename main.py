import pygame
# pygame 初始化
pygame.init()

import const, fonts.font_config, colors.color_config
from scenes.opening_scene import OpeningScene



'''
初始化
'''
# 視窗名稱
pygame.display.set_caption(const.CAPTION)


'''
遊戲場景
'''
openingScene = OpeningScene().run()