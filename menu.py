import pygame , sys ,test,time ,random



menuList = ["     Start",
			"     Score",
			"   Options",
			"      Help",
			"    About",
			"     Exit"]

class Menu ():
	global Text
	pygame.font.init()
	pygame.init()

	Text = pygame.font.SysFont("None",60)

	def drawBackGround(self):
		self.bg = pygame.image.load('Anna-and-Elsa-with-longer-background-frozen-34842649-500-211.png')
		self.img = pygame.image.load('938.png')
		self.mm.blit(pygame.transform.scale(self.bg, (500, 500)), (10, 230))
		self.mm.blit(pygame.transform.scale(self.img, (400, 400)), (950, 20))
		self.writeMenuList()


	def __init__(self):
		self.mm = pygame.display.set_mode((1400, 900), pygame.RESIZABLE, 32)
		self.drawBackGround()
		self.menuRun()

		
	def writeMenuList(self):
		k=0
		for i in menuList:
			self.mm.blit(Text.render(i, True, (255,0,255)), (500,100+100*k))#positions (700,100) (700,200)...
			k+=1
			pygame.display.update()

	def start(self):
		test.MainFrame()

	def high_Score(self):
		pass



	def options(self):
		pass
	 
	def player(slef):
		import help
		obj=help.helpHend()
		obj.work()

	def about(self):
		import about
		obj=about.aboutHend()
		obj.work()


	def exitt(self):
		sys.exit()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def Action(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.i -= 1
					if self.i > 5 or self.i < 0 :
						self.i = 0

					pygame.draw.rect(self.mm, (255, 255, 255), (490, 90 + 100 * self.i, 300, 60), 4)
					pygame.draw.rect(self.mm, (0, 0, 0), (490, 90 + 100 * (self.i+1), 300, 60), 4)

				elif event.key == pygame.K_DOWN:
					self.i += 1

					if self.i > 5 or self.i < 0:
						pygame.draw.rect(self.mm, (0, 0, 0), (490, 90 + 100 * (self.i-1), 300, 60), 4)
						self.i = 0
						#pygame.draw.rect(self.mm, (0, 0, 0), (490, 90 , 300, 60), 4)

					pygame.draw.rect(self.mm, (255, 255, 255), (490, 90 + 100 * self.i, 300, 60), 4)
					pygame.draw.rect(self.mm, (0, 0, 0), (490, 90 + 100 * (self.i-1), 300, 60), 4)


				elif event.key == pygame.K_RETURN:
					if self.i == 0:
						self.start()
					elif self.i == 1:
						self.high_Score()
					elif self.i == 2:
						self.options()
					elif self.i == 3:
						self.player()
					elif self.i == 4:
						self.about()

					elif self.i == 5:
						self.exitt()

	def menuRun(self):
		self.i = -1
		while True:
			self.Action()
			self.drawBackGround()
			pygame.display.update()

if __name__ == '__main__':
	obj = Menu()
	obj.menuRun()

