
import sys
import random

import noise
import pygame
from pygame.locals import *



class MainGame:

    def __init__(self): 

        pygame.init()
        pygame.mixer.init()

        self.tile_size = 45
        self.boarder = 64

        self.freq = 9
        self.octaves = 12

        self.mouse_pos = [0,0]

        self.window_fps = 60

        self.window_level = 80
        self.window_size  = [16*self.window_level,9*self.window_level]

        self.window_title = 'SUGT09'

        self.screen = pygame.display.set_mode((self.window_size),pygame.RESIZABLE)

        self.clock = pygame.time.Clock()

        self.font1 = pygame.font.Font('assets/font/LockClock.ttf', 15)

        pygame.display.set_caption(self.window_title)
        #pygame.display.set_icon(G.tl6)
        pygame.display.flip()

    def tilemap_builder(self):

        self.seed = random.randint(100000, 999999)

        # 0 land 1 army
        self.tilemap = [[[int(noise.pnoise2((x/self.freq)+self.seed,(y/self.freq)+self.seed,self.octaves)*100+50),random.randint(0,100)] for x in range(0,self.boarder,1)] for y in range(0,self.boarder,1)]

    def gameloop(self): 

        while True:

            self.screen.fill((0,0,0,0))

            tilemap_n = len(self.tilemap)
            tilemap_m = len(self.tilemap[0])

            for tilemap_x in range(tilemap_n):
                for tilemap_y in range(tilemap_m):

                    tile_info = self.tilemap[tilemap_x][tilemap_y]

                    if -100 <=tile_info[0]<= 15:
                        pygame.draw.rect(self.screen,(100,149,237),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                    if 16 <=tile_info[0]<= 35:
                        pygame.draw.rect(self.screen,(135,206,235),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                    if 36 <=tile_info[0]<= 45:
                        pygame.draw.rect(self.screen,(176,224,230),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                    if 46 <=tile_info[0]<= 58:
                        pygame.draw.rect(self.screen,(240,230,140),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                    if 59 <=tile_info[0]<= 70:
                        pygame.draw.rect(self.screen,(0,179,113),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                    if 70 <=tile_info[0]<= 110:
                        pygame.draw.rect(self.screen,(46,139,87),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                    army_text = self.font1.render(str(tile_info[1]), True, (255, 255, 255))
                    self.screen.blit(army_text,(tilemap_x*self.tile_size,tilemap_y*self.tile_size))

            pygame.draw.rect(self.screen,(255,255,255),((self.mouse_pos[0]//self.tile_size)*self.tile_size,(self.mouse_pos[1]//self.tile_size)*self.tile_size,self.tile_size,self.tile_size))

            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            self.clock.tick(self.window_fps)

if __name__ == "__main__":

    main_game = MainGame()
    main_game.tilemap_builder()
    main_game.gameloop()