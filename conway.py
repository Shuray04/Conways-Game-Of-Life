import pygame
import time

class conway:
    cycles = 0
    def __init__(self, window_width, window_height, cell_width, cell_height):
        self.screen=pygame.display.set_mode([window_width, window_height])
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.coords = self.create_list()
        
    def create_list(self):
        list = []
        for y in range(round(pygame.display.get_window_size()[1] / self.cell_height)):
            list.append([])
            for x in range(round(pygame.display.get_window_size()[0] / self.cell_width)):
                list[y].append(0)
        return list
        
    def clear_cells(self):
        self.coords = self.create_list()
        self.cycles = 0
        
    def draw_cell(self, x, y, width, height):
        pygame.draw.rect(self.screen, [0, 0, 0], [x, y, width, height], 0)
        
    def draw_grid(self):
        self.screen.fill([255, 255, 255])
        for i in range(0, pygame.display.get_window_size()[0], self.cell_width):
            pygame.draw.line(self.screen, [0, 0, 0], (i, 0), (i, pygame.display.get_window_size()[1]))
        for i in range(0, pygame.display.get_window_size()[1], self.cell_height):
            pygame.draw.line(self.screen, [0, 0, 0], (0, i), (pygame.display.get_window_size()[0], i))
        
    def update(self):
        new_coords = self.create_list()
                
        for y in range(len(self.coords)):
            for x in range(len(self.coords[y])):
                neighbours = 0
                for offY in range(-1, 2):
                    for offX in range(-1, 2):
                        if x+offX<0 or y+offY<0 or x+offX>len(new_coords[0])-1 or y+offY>len(new_coords)-1:
                            continue
                        elif self.coords[y+offY][x+offX] == True and (offX != 0 or offY != 0):
                            neighbours+=1
                if neighbours == 3 or neighbours == 2 and self.coords[y][x] == True:
                    new_coords[y][x] = 1
                else:
                    new_coords[y][x] = 0
        self.cycles += 1
        self.coords = new_coords
        
    def render(self):
        pygame.display.set_caption("Cycles: " + str(self.cycles), "")
        self.draw_grid()
        for y in range(len(self.coords)):
            for x in range(len(self.coords[y])):
                if self.coords[y][x] == True:
                    self.draw_cell(x*self.cell_width, y*self.cell_height, self.cell_width, self.cell_height)    
        pygame.display.flip()

running=True
c = conway(1200, 800, 20, 20)
c.render()

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        c.coords[int(mouse_y / c.cell_height)][int(mouse_x / c.cell_width)] = 1
        c.render()
    elif pygame.mouse.get_pressed()[2]:
        c.coords[int(mouse_y / c.cell_height)][int(mouse_x / c.cell_width)] = 0
        c.render()
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        c.update()
        c.render()
        time.sleep(0.2)
    if pygame.key.get_pressed()[pygame.K_c]:
        c.clear_cells()
        c.render()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()