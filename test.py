import pygame , sys  ,thread
from pygame.locals import *
import SEGA


class MainFrame:
	mousex = 0
	mousey = 0
	mouseClicked1=False
	mouseClicked2=False
	game=[[1,2,3],[1,2,3],[1,2,3]]
	positionChoose1=9
	positionChoose2=9
	pos=0
	olfal = pygame.image.load("3.png")  # Olfal
	even = pygame.image.load('baby-sven-olaf-and-sven-fan-art-37071456-fanpop-tpMzEp-clipart.png')  # Even
	black = pygame.image.load('images.jpg')  # black
	gameXO=[[1,2,3],[1,2,3],[1,2,3]]
	win=False
	winner="o"


	dic={'x':False,'o':False,'x1':False ,'x2':False,'x3':False,'o1':False,'o2':False,'o3':False}


	"""
	def call_music(self):
		thread.start_new_thread(music.playSong,('FROZEN - Let It Go Sing-along Official Disney HD.mp3',))
	"""

	def convertGameToGameXO(self):
		for i in range(0,3):
			for j in range(0,3):
				if(self.game[i][j]==self.olfal):
					self.gameXO[i][j]="x"
				if(self.game[i][j]==self.even):
					self.gameXO[i][j]="o"
				if(self.game[i][j]==self.black):
					self.gameXO[i][j]=" "

#here Comment and changes
	def CheckAllMove(self):
            if(self.dic['x3']==self.dic['x2'] and self.dic['x1']==self.dic['x2'] and self.dic['x1']==True):
                self.dic['x']=True;
            if (self.dic['o3'] == self.dic['o2'] and self.dic['o1'] == self.dic['o2'] and self.dic['o1'] == True):
            	self.dic['o'] = True







	def isWin(self,b):  # Board Win(state)
		for i in [0, 1, 2]:
			# horizontal lines
			if (b[i][0] == b[i][1]) and (b[i][0] == b[i][2]) and (b[i][0] != ' '):
				return b[i][0]
			# vertical lines
			if (b[0][i] == b[1][i]) and (b[0][i] == b[2][i]) and (b[0][i] != ' '):
				return b[0][i]
		# diagonal lines
		if (b[0][0] == b[1][1]) and (b[0][0] == b[2][2]) and (b[0][0] != ' '):
			return b[0][0]
		elif (b[0][2] == b[1][1]) and (b[0][2] == b[2][0]) and (b[0][2] != ' '):
			return b[0][2]
		else:
			return ' '


	def convert(self,value):
		if(value==0):
			return (0,0)
		if(value==1):
			return (0,1)
		if(value==2):
			return (0,2)
		if(value==3):
			return (1,0)
		if(value==4):
			return (1,1)
		if(value==5):
			return (1,2)
		if(value==6):
			return (2,0)
		if(value==7):
			return (2,1)
		if(value==8):
			return (2,2)

	def move(self,pos1,pos2):
		x,y=self.convert(pos1)
		x2,y2=self.convert(pos2)
		if (x == 2 and y == 0):
			self.CheckAllMove()
			self.dic['o1'] = True
		if (x == 2 and y == 1):
			self.CheckAllMove()
			self.dic['o2'] = True
		if (x == 2 and y == 2):
			self.CheckAllMove()
			self.dic['o3'] = True
		temp=self.game[x][y]
		self.game[x][y]=self.game[x2][y2]
		self.game[x2][y2]=temp
		#Comment And CHanges
		if (self.dic['o3'] == self.dic['o2'] and self.dic['o1'] == self.dic['o2'] and self.dic['o1'] == True):
			self.convertGameToGameXO()
			if (self.isWin(self.gameXO) == "o"):
				self.win = True
				self.winner = "o"

	def ConvertToList(self,game):
		x=""
		for i in [0, 1, 2]:
			for j in [0 , 1 , 2]:
				if(game[i][j]=='x'):
					x+="X"
				elif(game[i][j]=='o'):
					x+="O"
				else:
					x+=" "
		return x


	def swap(self):

		x,y=self.convert(self.positionChoose1)
		if(self.game[x][y]==self.olfal):

			x2,y2=self.convert(self.positionChoose2)
			# Check here eno 3ml swap le 3 items bto3 x
			# Hena bshof hwa 7rk anhi wa7da fehom

			if(self.game[x2][y2]==self.black):
				SEGA.count[self.positionChoose1] = 1
				if(x==0 and y==0):
					self.dic['x1']=True
				if(x==0 and y==1):
					self.dic['x2']=True
				if(x==0 and y==2):
					self.dic['x3']=True
				temp=self.game[x][y]
				self.game[x][y]=self.game[x2][y2]
				self.game[x2][y2]=temp
				self.draw_game()
				self.mouseClicked1=False
				self.mouseClicked2 = False
				self.CheckAllMove()
				if (self.dic['x'] == True):
					self.convertGameToGameXO()
					if (self.isWin(self.gameXO) == "x"):
						self.win = True
						self.winner = "x"
				self.convertGameToGameXO()
				list = self.ConvertToList(self.gameXO)
				Distination,poisionWillMoveFromIt= SEGA.computerMove(list)
				#print Distination , poisionWillMoveFromIt
				self.move(poisionWillMoveFromIt,Distination)
				SEGA.count[poisionWillMoveFromIt] = 1


	def draw_rectangle_around_button(self,pos,checkColor):
		if(checkColor):
			color=(255,0,0)
		else:
			color=(0, 0, 255)
		if(pos==0):
			pygame.draw.rect(self.DIS,color, (480, 170,120, 140), 2)
		if(pos==1):
			pygame.draw.rect(self.DIS, color, (480+120, 170, 120, 140), 2)
		if(pos==2):
			pygame.draw.rect(self.DIS,color, (480+120*2, 170, 110, 140), 2)
		if(pos==3):
			pygame.draw.rect(self.DIS, color, (480, 170+140, 120, 140), 2)
		if(pos==4):
			pygame.draw.rect(self.DIS, color, (480+120, 170+140, 120, 140), 2)
		if(pos==5):
			pygame.draw.rect(self.DIS, color, (480+120*2, 170+140, 110, 140), 2)
		if(pos==6):
			pygame.draw.rect(self.DIS, color, (480, 170+140*2, 120, 120), 2)
		if(pos==7):
			pygame.draw.rect(self.DIS, color, (480+120, 170+140*2, 120, 120), 2)
		if(pos==8):
			pygame.draw.rect(self.DIS, color, (480+120*2, 170+140*2, 110, 120), 2)

	def draw_game(self):
		#to draw back ground ella & anna & ice ^_^
		self.draw_backGround()

		#big rectangle
		pygame.draw.rect(self.DIS,(255,255,255), (480, 170, 350, 400),2)
		pygame.draw.rect(self.DIS,(255,255,255), (476, 166, 360, 410),2)

		pygame.draw.rect(self.DIS,(255,255,255),(480, 170, 120, 400),2)
		pygame.draw.rect(self.DIS, (255, 255, 255),(480, 170, 115, 400), 2)

		pygame.draw.rect(self.DIS,(255,255,255),(480, 170, 240, 400),2)
		pygame.draw.rect(self.DIS, (255, 255, 255),(480, 170, 235, 400), 2)

		#***************************
		pygame.draw.rect(self.DIS,(255,255,255), (480, 170, 350, 140),2)
		pygame.draw.rect(self.DIS,(255,255,255), (476, 166, 360, 150),2)

		pygame.draw.rect(self.DIS,(255,255,255), (480, 170, 350, 280),2)
		pygame.draw.rect(self.DIS,(255,255,255), (476, 166, 360, 290),2)




		#draw image in each button
		for i in range(3):
			for j in range(3):
				self.DIS.blit(pygame.transform.scale(self.game[i][j], (80, 100)),(500+(110*j),200+(130*i)))

		#to draw Rectangle Around button
		#click 1
		if(self.mouseClicked1==True and self.mouseClicked2==False):
			self.draw_rectangle_around_button(self.positionChoose1,False)

		#click 2
		if (self.mouseClicked1==False and self.mouseClicked2==True):
			self.draw_rectangle_around_button(self.positionChoose2,False)
			self.draw_rectangle_around_button(self.positionChoose1,False)


#check  postion of mouse and call function draw rectangle around button
	def check_position(self):
		if((self.mousex>=480 and self.mousex<=480+120) and(self.mousey>=170 and self.mousey<=170+140)):
			self.pos=0
			self.draw_rectangle_around_button(0,True)
		if((self.mousex>=480+120 and self.mousex<=480+120*2) and(self.mousey>=170 and self.mousey<=170+140)):
			self.pos=1
			self.draw_rectangle_around_button(1,True)
		if((self.mousex>=480+120*2 and self.mousex<=480+120*3) and(self.mousey>=170 and self.mousey<=170+140)):
			self.pos=2
			self.draw_rectangle_around_button(2,True)
		if((self.mousex>=480 and self.mousex<=480+120) and(self.mousey>=170+140 and self.mousey<=170+140*2)):
			self.pos=3
			self.draw_rectangle_around_button(3,True)
		if((self.mousex>=480+120 and self.mousex<=480+120*2) and(self.mousey>=170+140 and self.mousey<=170+140*2)):
			self.pos=4
			self.draw_rectangle_around_button(4,True)
		if((self.mousex>=480+120*2 and self.mousex<=480+120*3) and(self.mousey>=170+140 and self.mousey<=170+140*2)):
			self.pos=5
			self.draw_rectangle_around_button(5,True)
		if((self.mousex>=480 and self.mousex<=480+120) and(self.mousey>=170+140*2 and self.mousey<=170+140*3)):
			self.pos=6
			self.draw_rectangle_around_button(6,True)
		if ((self.mousex >= 480+120 and self.mousex <= 480 + 120*2) and (self.mousey >= 170+140*2 and self.mousey <= 170 + 140*3)):
			self.pos = 7
			self.draw_rectangle_around_button(7,True)
		if((self.mousex>=480+120*2 and self.mousex<=480+120*3) and(self.mousey>=170+140*2 and self.mousey<=170+140*3)):
			self.pos=8
			self.draw_rectangle_around_button(8,True)





	def Action(self):

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			#hover
			elif event.type == MOUSEMOTION:
				self.mousex,self.mousey = event.pos
				self.check_position()

			#click
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos

				self.check_position()

				x=8
				if(self.mouseClicked1==False):
					x=9
					self.mouseClicked1=True
					self.mouseClicked2=False
					self.positionChoose1 = self.pos

				if(self.mouseClicked1==True and x==8):
					self.mouseClicked2 = True
					self.mouseClicked1 = False
					self.positionChoose2=self.pos
					self.swap()




	#inital State
	def start_game(self):
		for i in range(0,3):
			self.game[0][i]=self.olfal
		for i in range(3):
			self.game[2][i]=self.even
		for i in range(3):
			self.game[1][i]=self.black




	#just draw BackGround Ellsa & Anna & ice
	def draw_backGround(self):
		bg = pygame.image.load("FR-detalhe-esq.png")#ellsa
		img = pygame.image.load('frames_frozen_char_3_mob.png') #Anna
		pygame.display.set_icon(bg)
		self.DIS.blit(bg,(10,230))
		self.DIS.blit(img,(800,20))
		ice = pygame.image.load("771e9ca721c6cc8412fe8674dbc2554b.jpg")#ice
		self.DIS.blit(pygame.transform.scale(ice, (200, 200)),(1050,500))

	def return_to_default(self):
		self.game = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
		self.pos = 0
		self.gameXO = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
		self.win = False
		SEGA.count = [0, 0, 0, 1, 1, 1, 0, 0, 0]
		self.dic = {'x': False, 'o': False, 'x1': False, 'x2': False, 'x3': False, 'o1': False, 'o2': False, 'o3': False}

	#constructor class start from here
	def __init__(self):

		pygame.init()

		self.return_to_default()

		self.DIS = pygame.display.set_mode((1400,900),pygame.RESIZABLE,32)
		pygame.display.set_caption("SeGa")
		#self.call_music()
		self.start_game()
		while True:
			self.draw_game()
			#self.draw_backGround()
			self.Action()
			if(self.win):
				Text = pygame.font.SysFont("None", 60)
				self.draw_game()
				self.DIS.blit(Text.render("Losser :P", True, (255, 0, 255)), (500, 100))
				pygame.display.update()
				pygame.time.wait(2000)
				import win
				win.MainFrame(self.winner)
			pygame.display.update()

#MainFrame()
