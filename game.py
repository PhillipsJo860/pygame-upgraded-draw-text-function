# Pygame game template

import pygame, sys, config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

# text_font = pygame.font.Font(None, 30)

def draw_line(screen, color, start_pos, end_pos, thickness):
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

def draw_rect(screen, rect, color, thickness):
    pygame.draw.rect(screen, color, rect, thickness)

def draw_circle(screen, center, radius, color, thickness):
    pygame.draw.circle(screen, color, center, radius, thickness)

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True

    text_font = pygame.font.SysFont('Arial', 30)
    while running:
        running = handle_events()
        screen.fill(config.COLOR_WHITE)

        draw_text(screen, 'Hello world', text_font, config.COLOR_BLACK, 220, 150)

        # Calling a grid (Comment this out after you are done coding)
        grid(screen)
        
        pygame.display.flip()

        clock.tick(config.FPS)
    
    pygame.quit()
    sys.exit()

def grid(screen):
    topgrid_pos = {'start1': (1, 0), 'start2': (100, 0), 'start3': (200, 0), 'start4': (300, 0), 'start5': (400, 0), 'start6': (500, 0), 'start7': (600, 0), 'start8': (700, 0), 'start9': (799, 0), 'end1': (1, 20), 'end2': (100, 20), 'end3': (200, 20), 'end4': (300, 20), 'end5': (400, 20), 'end6': (500, 20), 'end7': (600, 20), 'end8': (700, 20), 'end9': (799, 20)}
    sidegrid_pos = {'start1': (0, 1), 'start2': (0, 100), 'start3': (0, 200), 'start4': (0, 300), 'start5': (0, 400), 'start6': (0, 500), 'start7': (0, 599), 'end1': (20, 1), 'end2': (20, 100), 'end3': (20, 200), 'end4': (20, 300), 'end5': (20, 400), 'end6': (20, 500), 'end7': (20, 599)}
    grid_thick = 3
    # Top grid
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start1'], topgrid_pos['end1'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start2'], topgrid_pos['end2'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start3'], topgrid_pos['end3'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start4'], topgrid_pos['end4'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start5'], topgrid_pos['end5'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start6'], topgrid_pos['end6'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start7'], topgrid_pos['end7'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start8'], topgrid_pos['end8'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, topgrid_pos['start9'], topgrid_pos['end9'], grid_thick)
    # Side grid
    draw_line(screen, config.COLOR_BLACK, sidegrid_pos['start1'], sidegrid_pos['end1'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, sidegrid_pos['start2'], sidegrid_pos['end2'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, sidegrid_pos['start3'], sidegrid_pos['end3'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, sidegrid_pos['start4'], sidegrid_pos['end4'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, sidegrid_pos['start5'], sidegrid_pos['end5'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, sidegrid_pos['start6'], sidegrid_pos['end6'], grid_thick)
    draw_line(screen, config.COLOR_BLACK, sidegrid_pos['start7'], sidegrid_pos['end7'], grid_thick)

if __name__ == '__main__':
    main()
