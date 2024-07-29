import pygame

'''
視窗相關配置
'''
# 視窗顯示遊戲名稱
CAPTION = '聽說是遊戲'

# 縮放比例
SCALE_FACTOR = 0.5

# 視窗大小
WINDOW_WIDTH = 4096
WINDOW_HEIGHT = 1714
WINDOW_SIZE = (WINDOW_WIDTH * SCALE_FACTOR, WINDOW_HEIGHT * SCALE_FACTOR)

# 視窗 
WINDOW = pygame.display.set_mode(WINDOW_SIZE)