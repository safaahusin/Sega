import pygame
import sys

class aboutHend():
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
  pygame.display.set_caption("About US")

  background = pygame.image.load('938.png').convert()
  t = '  Programmer By : - '
  t1 = '- Amal Tarek '

  t2 = '- Asmaa Mostafa'

  t3 = '- Safaa EL-Shafe\'y'

  t4 = '- Mahmoud Ahmad'

  t5 = '- Hend Mohammad'

  t6 = '- Abdelrahman Mohammad'

  while True:
   self.Action()
   screen.blit(pygame.transform.scale(background, (400, 400)), (950, 300))

   screen.blit(font.render('* About US *', True, (225, 0, 255)), (550, 10))

   screen.blit(font2.render(t, True, (225, 0, 0)), (50, 100))
   screen.blit(font2.render(t1, True, (225, 225, 225)), (50, 175))

   screen.blit(font2.render(t2, True, (225, 225, 225)), (50, 250))

   screen.blit(font2.render(t3, True, (225, 225, 225)), (50, 325))
   screen.blit(font2.render(t4, True, (225, 225, 225)), (50, 400))

   screen.blit(font2.render(t5, True, (225, 225, 225)), (50, 475))
   screen.blit(font2.render(t6, True, (225, 225, 225)), (50, 550))

   pygame.display.update()






