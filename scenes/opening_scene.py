import pygame
import sys

from const import WINDOW


class OpeningScene:
  def __init__(self):
    pass
    
  def init(self):
    self.start = True
  
  def run(self):
    self.init()
    while self.start:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      WINDOW.fill((255, 255, 255))

      pygame.display.flip()