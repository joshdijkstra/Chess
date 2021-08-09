import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

FPS = 30
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tracking System")
ball = pygame.image.load("intro_ball.gif")
rectangle = pygame.Rect(ball.get_rect())
rectangle_draging = False
clock = pygame.time.Clock()
running = True
while running:
    # - events -
    mx , my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False
        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
    screen.fill(WHITE)
    screen.blit(ball, rectangle)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
