import pygame,sys,menu


class MainFrame:
    global Text
    pygame.font.init()
    pygame.init()
    Text = pygame.font.SysFont("None", 60)
    def __init__(self,win):
        self.DIS = pygame.display.set_mode((1400, 900), pygame.RESIZABLE, 32)
        if(win=='o'):
            self.DIS.blit(Text.render("Computer is Winner ^__^", True, (255, 0, 255)), (500, 100))
        else:
            self.DIS.blit(Text.render("Congratulation ^__^", True, (255, 0, 255)), (500, 100))
        pygame.display.set_caption("SEGA")
        while True:
            if(self.Action()):
                menu.Menu()
                break
            self.drawBackGround(win)
            pygame.display.update()

    def Action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
            return False

    def drawBackGround(self,win):
        if(win=="o"):
            bg = pygame.image.load('laughing smiley face Vector.png')#laught
            img=pygame.image.load('disney-frozen-sad.png')#olfal
        else:
            img = pygame.image.load('fc54c943fc1d678b797f67cbbbf298cd.png')
            bg = pygame.image.load('7iaKE6AjT.png')
        self.DIS.blit(pygame.transform.scale(bg, (400, 400)), (100, 250))
        self.DIS.blit(pygame.transform.scale(img, (400, 400)), (900, 250))



