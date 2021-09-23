
import sys
import random

import noise
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

tile_outline = 1
tile_outline_beclick = 3

tile_size = 35
boarder = 64

tilemap = []

freq = 9
octaves = 12

mouse_pos = [0,0]

window_fps = 60

window_level = 80
window_size  = [16*window_level,9*window_level]

window_title = 'SUGT09'

screen = pygame.display.set_mode((window_size),pygame.RESIZABLE)

tile_outline_surface = pygame.Surface((window_size)).convert_alpha()
tilemap_surface = pygame.Surface((window_size)).convert_alpha()
country_surface = pygame.Surface((window_size)).convert_alpha()
gui_surface = pygame.Surface((window_size)).convert_alpha()

clock = pygame.time.Clock()

font1 = pygame.font.Font('assets/font/LockClock.ttf', 15)

pygame.display.set_caption(window_title)
#pygame.display.set_icon(G.tl6)
pygame.display.flip()

def tilemap_builder():
    global tilemap

    seed = random.randint(100000, 999999)

    # 0 land 1 army 2 country 3 dv_code
    tilemap = [[[int(noise.pnoise2((x/freq)+seed,(y/freq)+seed,octaves)*100+50),0,0,0] for x in range(0,boarder,1)] for y in range(0,boarder,1)]

    return tilemap

def tilemap_loarder():

    tilemap_n = len(tilemap)
    tilemap_m = len(tilemap[0])

    for tilemap_x in range(tilemap_n):
        for tilemap_y in range(tilemap_m):

            tile_info = tilemap[tilemap_x][tilemap_y]

            if tile_info[3] == 0:

                # 0 =================================================================

                if -100 <=tile_info[0]<= 15:
                    tile_info[0] = 1
                    
                if 16 <=tile_info[0]<= 35:
                    tile_info[0] = 2
                    
                if 36 <=tile_info[0]<= 45:
                    tile_info[0] = 3
                    
                if 46 <=tile_info[0]<= 58:
                    tile_info[0] = 4
                    
                if 59 <=tile_info[0]<= 70:
                    tile_info[0] = 5
                    
                if 70 <=tile_info[0]<= 110:
                    tile_info[1] = 6
                    tile_info[2] = random.randint(0,100)

                # 1 =================================================================

                if tile_info[0] == 1 or tile_info[0] == 2 or tile_info[0] == 3:
                    tile_info[1] = 0
                    
                tile_info[3] = 1

            if tile_info[3] == 1:

                # 0 =================================================================

                if tile_info[0] == 1:
                    pygame.draw.rect(tilemap_surface,(100,149,237),(tilemap_x*tile_size,tilemap_y*tile_size,tile_size,tile_size))

                if tile_info[0] == 2:
                    pygame.draw.rect(tilemap_surface,(135,206,235),(tilemap_x*tile_size,tilemap_y*tile_size,tile_size,tile_size))

                if tile_info[0] == 3:
                    pygame.draw.rect(tilemap_surface,(176,224,230),(tilemap_x*tile_size,tilemap_y*tile_size,tile_size,tile_size))

                if tile_info[0] == 4:
                    pygame.draw.rect(tilemap_surface,(240,230,140),(tilemap_x*tile_size,tilemap_y*tile_size,tile_size,tile_size))

                if tile_info[0] == 5:
                    pygame.draw.rect(tilemap_surface,(0,179,113),(tilemap_x*tile_size,tilemap_y*tile_size,tile_size,tile_size))

                if tile_info[0] == 6:
                    pygame.draw.rect(tilemap_surface,(46,139,87),(tilemap_x*tile_size,tilemap_y*tile_size,tile_size,tile_size))
                    pygame.draw.rect(country_surface,(255,0,0,100),(tilemap_x*tile_size,tilemap_y*tile_size,tile_size,tile_size))

                # 1 =================================================================

                if tile_info[1] == 0:
                    pass

                if tile_info[1] != 0:
                    army_text = font1.render(str(tile_info[2]), True, (255,255,255))
                    tilemap_surface.blit(army_text,(tilemap_x*tile_size,tilemap_y*tile_size))

                # 3 =================================================================


def tile_boarder(color,pos):
    pygame.draw.rect(screen,(color),(pos[0]*tile_size, pos[1]*tile_size, tile_size-tile_outline, tile_outline_beclick))
    pygame.draw.rect(screen,(color),(pos[0]*tile_size, (pos[1]+1)*tile_size-tile_outline-tile_outline_beclick, tile_size-tile_outline, tile_outline_beclick))
    
    pygame.draw.rect(screen,(color),(pos[0]*tile_size, pos[1]*tile_size, tile_outline_beclick, tile_size-tile_outline)) 
    pygame.draw.rect(screen,(color),((pos[0]+1)*tile_size-tile_outline-tile_outline_beclick, pos[1]*tile_size, tile_outline_beclick, tile_size-tile_outline)) 



tilemap_builder()

while True:

    screen.fill((0,0,0))
    tilemap_surface.fill((0,0,0,0))
    country_surface.fill((0,0,0,0))

    tilemap_loarder()

    tile_boarder((255,255,255),[mouse_pos[0]//tile_size,mouse_pos[1]//tile_size])
    
    screen.blit(tilemap_surface, (0, 0))
    screen.blit(country_surface, (0, 0))

    pygame.display.update()

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos

        if event.type == pygame.MOUSEBUTTONDOWN:
            (tilemap[mouse_pos[0]//tile_size][mouse_pos[1]//tile_size])[3] = 2
            army_green = [mouse_pos[0]//tile_size,mouse_pos[1]//tile_size]

        if event.type == pygame.MOUSEBUTTONUP:
            (tilemap[mouse_pos[0]//tile_size][mouse_pos[1]//tile_size])[3] = 1
            army_red = [mouse_pos[0]//tile_size,mouse_pos[1]//tile_size]

        if event.type == pygame.KEYDOWN:

            if event.key == K_f:
                (tilemap[army_green[0]][army_green[1]])[2] -= 1
                (tilemap[army_red[0]][army_red[1]])[2] -= 1

    clock.tick(window_fps)