import pygame
import sys,time,random

class helpHend():
 def Action(self):
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    sys.exit()
   if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RETURN:
     import menu
     obj = menu.Menu()
     obj.menuRun()

 def work(self):

  pygame.init()
  pygame.font.init()
  screen = pygame.display.set_mode((1400, 900))
  font = pygame.font.SysFont("Forte", 60);
  font2 = pygame.font.SysFont("Georgia", 40);
  pygame.display.set_caption("Help")

  background = pygame.image.load('Anna-and-Elsa-with-longer-background-frozen-34842649-500-211.png').convert()

  t = '* user is olfa and should move all'
  t1 = '* pictures to specific position and will win when'

  t2 = '* the three pictures moves and be in horizontal or vertical or diagonal'

  t3 = '* the three pictures moves and be in horizontal'
  t4 = '* or vertical or diagonal'
  while True:
   screen.blit(background, (1000, 400))

   screen.blit(font.render('* Help *', True, (225, 0, 155)), (600, 10))

   screen.blit(font2.render(t, True, (225, 255, 255)), (30, 100))
   screen.blit(font2.render(t1, True, (225, 225, 225)), (30, 175))
   screen.blit(font2.render(t2, True, (225, 225, 225)), (30, 250))
   screen.blit(font2.render(t3, True, (225, 225, 225)), (30, 325))
   screen.blit(font2.render(t4, True, (225, 225, 225)), (30, 400))
   self.Action()
   pygame.display.update()






