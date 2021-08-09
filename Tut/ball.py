import sys, pygame
pygame.init()

def find_speed(speed):
    new_speed = [speed[0]*0.99999999 , speed[1]*1.0001]
    return new_speed


size = width, height = 720, 480
speed = [2, 1.5]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    speed = find_speed(speed)
    print(speed)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    #screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
