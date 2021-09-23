
import sys
import random

import noise
import pygame
from pygame.locals import *



class MainGame:

    def __init__(self): 

        pygame.init()
        pygame.mixer.init()

        self.tile_outline = 1
        self.tile_outline_beclick = 3

        self.army_green = 0
        self.army_red = 0

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

        self.tile_outline_surface = pygame.Surface((self.window_size)).convert_alpha()
        self.country_surface = pygame.Surface((self.window_size)).convert_alpha()

        self.clock = pygame.time.Clock()

        self.font1 = pygame.font.Font('assets/font/LockClock.ttf', 15)

        pygame.display.set_caption(self.window_title)
        #pygame.display.set_icon(G.tl6)
        pygame.display.flip()

    def tilemap_builder(self):

        self.seed = random.randint(100000, 999999)

        # 0 tile_boarder 1 land 2 army 3 mouse_pos 4 dv_code
        self.tilemap = [[[0,int(noise.pnoise2((x/self.freq)+self.seed,(y/self.freq)+self.seed,self.octaves)*100+50),0,0,0] for x in range(0,self.boarder,1)] for y in range(0,self.boarder,1)]

    def tile_boarder(self,color,pos):
        pygame.draw.rect(self.screen,(color),(pos[0]*self.tile_size, pos[1]*self.tile_size, self.tile_size-self.tile_outline, self.tile_outline_beclick))
        pygame.draw.rect(self.screen,(color),(pos[0]*self.tile_size, (pos[1]+1)*self.tile_size-self.tile_outline-self.tile_outline_beclick, self.tile_size-self.tile_outline, self.tile_outline_beclick))
        
        pygame.draw.rect(self.screen,(color),(pos[0]*self.tile_size, pos[1]*self.tile_size, self.tile_outline_beclick, self.tile_size-self.tile_outline)) 
        pygame.draw.rect(self.screen,(color),((pos[0]+1)*self.tile_size-self.tile_outline-self.tile_outline_beclick, pos[1]*self.tile_size, self.tile_outline_beclick, self.tile_size-self.tile_outline)) 
        
    def country_builder(self):
        #pygame.draw.rect(self.country_surface,(255,0,0,100),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))
        pass

    def gameloop(self): 

        while True:

            self.screen.fill((0,0,0,0))

            tilemap_n = len(self.tilemap)
            tilemap_m = len(self.tilemap[0])

            for tilemap_x in range(tilemap_n):
                for tilemap_y in range(tilemap_m):

                    tile_info = self.tilemap[tilemap_x][tilemap_y]

                    if tile_info[4] == 0:

                        # 1 =================================================================

                        if -100 <=tile_info[1]<= 15:
                            tile_info[1] = 1
                            
                        if 16 <=tile_info[1]<= 35:
                            tile_info[1] = 2
                            
                        if 36 <=tile_info[1]<= 45:
                            tile_info[1] = 3
                            
                        if 46 <=tile_info[1]<= 58:
                            tile_info[1] = 4
                            
                        if 59 <=tile_info[1]<= 70:
                            tile_info[1] = 5
                            
                        if 70 <=tile_info[1]<= 110:
                            tile_info[1] = 6
                            tile_info[2] = random.randint(0,100)

                        # 2 =================================================================

                        if tile_info[1] == 1 or tile_info[1] == 2 or tile_info[1] == 3:
                            tile_info[2] = 0
                            
                        tile_info[4] = 1

                    if tile_info[4] == 1:

                        # 0 =================================================================

                        if tile_info[0] == 0:
                            pygame.draw.rect(self.tile_outline_surface,(0,0,0,35),(tilemap_x*self.tile_size-self.tile_outline,tilemap_y*self.tile_size-self.tile_outline,self.tile_size+self.tile_outline*2,self.tile_size+self.tile_outline*2))
                            #self.screen.blit(self.tile_outline_surface, (0, 0))

                        if tile_info[0] == 1:
                            #pygame.draw.rect(self.screen,(255,0,0,35),(tilemap_x*self.tile_size-self.tile_outline,tilemap_y*self.tile_size-self.tile_outline,self.tile_size+self.tile_outline*2,self.tile_size+self.tile_outline*2))
                            pass

                        if tile_info[0] == 2:
                            pass

                        # 1 =================================================================

                        if tile_info[1] == 1:
                            pygame.draw.rect(self.screen,(100,149,237),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                        if tile_info[1] == 2:
                            pygame.draw.rect(self.screen,(135,206,235),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                        if tile_info[1] == 3:
                            pygame.draw.rect(self.screen,(176,224,230),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                        if tile_info[1] == 4:
                            pygame.draw.rect(self.screen,(240,230,140),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                        if tile_info[1] == 5:
                            pygame.draw.rect(self.screen,(0,179,113),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))

                        if tile_info[1] == 6:
                            pygame.draw.rect(self.screen,(46,139,87),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))
                            pygame.draw.rect(self.country_surface,(255,0,0,100),(tilemap_x*self.tile_size,tilemap_y*self.tile_size,self.tile_size,self.tile_size))


                        # 2 =================================================================

                        if tile_info[2] == 0:
                            pass

                        if tile_info[2] != 0:
                            army_text = self.font1.render(str(tile_info[2]), True, (255,255,255,100))
                            self.screen.blit(army_text,(tilemap_x*self.tile_size,tilemap_y*self.tile_size))

                        # 3 =================================================================

                        if tile_info[3] == 0:
                            pass

                        if tile_info[3] == 1:
                            main_game.tile_boarder((255,0,0,0),[tilemap_x,tilemap_y])

                        if tile_info[3] == 2:
                            main_game.tile_boarder((0,255,0,0),[tilemap_x,tilemap_y])


            main_game.tile_boarder((255,255,255,0),[self.mouse_pos[0]//self.tile_size,self.mouse_pos[1]//self.tile_size])

            self.screen.blit(self.country_surface, (0, 0))

            pygame.display.update()

            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos

                if event.type == pygame.MOUSEBUTTONDOWN:
                    (self.tilemap[self.mouse_pos[0]//self.tile_size][self.mouse_pos[1]//self.tile_size])[3] = 2
                    self.army_green = [self.mouse_pos[0]//self.tile_size,self.mouse_pos[1]//self.tile_size]

                if event.type == pygame.MOUSEBUTTONUP:
                    (self.tilemap[self.mouse_pos[0]//self.tile_size][self.mouse_pos[1]//self.tile_size])[3] = 1
                    self.army_red = [self.mouse_pos[0]//self.tile_size,self.mouse_pos[1]//self.tile_size]

                if event.type == pygame.KEYDOWN:

                    if event.key == K_f:
                        (self.tilemap[self.army_green[0]][self.army_green[1]])[2] -= 1
                        (self.tilemap[self.army_red[0]][self.army_red[1]])[2] -= 1

            self.clock.tick(self.window_fps)

if __name__ == "__main__":

    main_game = MainGame()
    main_game.tilemap_builder()
    main_game.gameloop()