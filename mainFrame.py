import pygame , sys ,music ,thread


class MainFrame:
	check=True
	def __init__(self):
		pygame.init()
		self.DIS = pygame.display.set_mode((1600,900),pygame.RESIZABLE,32) 
		bg = pygame.image.load('Anna-and-Elsa-with-longer-background-frozen-34842649-500-211.png')
		pygame.display.set_icon(bg)
		pygame.display.set_caption("SEGA")
		if(self.check):
			self.call_music()
		self.DIS = pygame.display.set_mode((1600,900),pygame.RESIZABLE,32)
		self.DIS.blit(bg,(0,0))
		
	def call_music(self):
		thread.start_new_thread(music.playSong,('FROZEN - Let It Go Sing-along Official Disney HD.mp3',))

MainFrame()
		
