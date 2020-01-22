import pygame
import random

import game_constants

print(game_constants.FPS)

vector = pygame.math.Vector2

class grid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		self.obstacles = []

		self.left = vector(-1, 0)
		self.right = vector(1, 0)
		self.up = (0, -1)
		self.down = (0, 1)
		self.possible_directions = [
			self.left, 
			self.right,
			self.up,
			self.down
		]
	def find_neighbours(self, node):
		possible_neighbours = []
		neighbours = []
			
		for edges in self.possible_directions:
			possible_neighbours.append(node + edges)
		for neighbour in possible_neighbours:
			if neighbour not in self.obstacles:
				if 0 <= neighbour.x < self.width: #can write " and 0<= neighbour.y < self.height ""
					if 0 <= neighbour.y < self.height: #instead of a second if statement
						neighbours.append(neighbour)
		return neighbours
	
	def add_random_obstacles(self, num_obstacles):
		count = 0
		while count <= num_obstacles:
			x = random.randint(0, game_constants.GRIDWIDTH - 1 )
			y = random.randint(0, game_constants.GRIDHEIGHT - 1)
			new_obstacle = vector(x, y)
			if new_obstacle not in self.obstacles:
				self.obstacles.append(new_obstacle)
			else:
				count -= 1
			count += 1
	def draw(self, screen):
		for x in range(0, game_constants.GRIDWIDTH_PX, game_constants.TILESIZE):
			pygame.draw.line(screen, game_constants.LIGHT_GRAY, (x, 0), (x, game_constants.GRIDHEIGHT_PX))
		for y in range(0, game_constants.GRIDHEIGHT_PX, game_constants.TILESIZE):
			pygame.draw.line(screen, game_constants.LIGHT_GRAY, (0, y), (game_constants.GRIDWIDTH_PX, y))
		for obstacle in self.obstacles:
			rect = pygame.Rect(obstacle * game_constants.TILESIZE, (game_constants.TILESIZE, game_constants.TILESIZE))
			pygame.draw.rect(screen, game_constants.LIGHT_GRAY, rect)

class player:
	def __init__(self, starting_position = vector(0,0), colour = game_constants.BLUE):
		self.colour = colour 
		self.position = starting_position
		self.path = []
	def draw(self, screen):
		rect = pygame.Rect(self.position * game_constants.TILESIZE, (game_constants.TILESIZE, game_constants.TILESIZE))
		pygame.draw.rect(screen, self.colour, rect)	
	def move_up(self, screen, map):
		new_position = self.position + vector(0,-1)
		if 0 <= new_position.y < map.height:#game_constants.GRIDHEIGHT:
			if new_position.y not in map.obstacles:
				self.position = new_position
				self.draw(screen)
	def move_down(self, screen, map):
		new_position = self.position + vector(0,1)
		if 0 <= new_position.y < map.height:
			if new_position.y not in map.obstacles:
				self.position = new_position
				self.draw(screen)
	def move_left(self, screen, map):
		new_position = self.position + vector(-1,0)
		if 0 <= new_position.x < map.width:
			if new_position.x not in map.obstacles:
				self.position = new_position
				self.draw(screen)
	def move_right(self, screen, map):
		new_position = self.position + vector(1, 0)
		if 0 <= new_position.x < map.width:
			if new_position.x not in map.obstacles:
				self.position = new_position
				self.draw(screen)

class game(grid, player):
	def __init__(self, width=game_constants.GRIDWIDTH, height=game_constants.GRIDHEIGHT):
		self.width = width
		self.height = height 
		self.map = grid(self.width, self.height)
		self.screen = pygame.display.set_mode((game_constants.GRIDWIDTH_PX, game_constants.GRIDHEIGHT_PX))
		#game runs			
		self.game_loop = True
		self.game_clock = pygame.time.Clock()
		#player
		self.player = player()
	def draw(self):
		self.map.draw(self.screen)
		self.player.draw(self.screen)

	def play(self):
		self.map.add_random_obstacles(10)

		while self.game_loop:
			#game runs until user says quit
			pygame.display.set_caption("Game Title")
			self.game_clock.tick(game_constants.FPS)
			for event in pygame.event.get():
				#since event based actions
				if event.type == pygame.QUIT: 
					self.game_loop = False
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					mouse_position = vector(pygame.mouse.get_pos()) // game_constants.TILESIZE
					if event.button == 1: 
						if mouse_position in self.map.obstacles:
							self.map.obstacles.remove(mouse_position)
						else:
							self.map.obstacles.append(mouse_position)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.player.move_up(self.screen, self.map)
					elif event.key == pygame.K_DOWN:
						self.player.move_down(self.screen, self.map)
					elif event.key == pygame.K_LEFT:
						self.player.move_left(self.screen, self.map)
					elif event.key == pygame.K_RIGHT:
						self.player.move_right(self.screen, self.map)


				#if A/B = some exact number, A//B == just the int number, no decimals
			self.screen.fill(game_constants.DARK_GRAY)
			self.draw()
			pygame.display.flip() #doesn't actually flip, just displays... 

test_game = game()
test_game.play()



