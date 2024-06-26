
import pygame
from pygame.locals import *
import random
pygame.init()

#creating the window
width = 500
height = 550
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

#colors
gray = (100,100,100)
green = (76,208,56)
red = (200,0,0)
white = (255,255,255)
yellow = (255,232,0)

#games settings
gameover = False
score = 0
speed = 2

#markers size
marker_width = 10
marker_height = 50

#road and edge markers
road = (100, 0, 300, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

#coordinates of lanes
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

#movement of lanes by y
lane_marker_move_y = 0

class Vehicle(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x, y)
        
player_x = 250
player_y = 400

player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

#gameloop
clock = pygame.time.Clock()
fps = 120
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    #grass
    screen.fill(green)

    #drawing the road
    pygame.draw.rect(screen, gray, road)

    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

        
        player_group.draw(screen)

















    pygame.display.update()
pygame.quit()