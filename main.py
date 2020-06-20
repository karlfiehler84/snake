import pygame
import random

pygame.init()
pause = True
s_w = 800
s_h = 800
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
otherGreen = (0,70,0)

win = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption("snake by karl")
clock = pygame.time.Clock()

#function that renders each segment of the snake
def snakeRender(snake):
    for part in snake:
        pygame.draw.rect(win, red, (part[0], part[1], 20,20))
#function that renders the food
def foodRender(foodPos):
    pygame.draw.rect(win, green, [foodPos[0], foodPos[1], 20, 20 ])
#function that checks if food was eaten
def foodEaten(foodPos, snake_head):
    if foodPos == snake_head:
        return True
#function to check for collisions
def collCheck(snake_head, snake):
    #check if snake collided with self
    if snake_head in snake[2:]:
        main()
    #check if snake hit edge of screen
    if snake_head[0] < 0:
        main()
    if snake_head[0] > s_w:
        main()
    if snake_head[1] < 0:
        main()
    if snake_head[1] > s_h:
        main()
#main loop
def main():
    score = 0
    font = pygame.font.SysFont("bitstreamverasans", 25)
    text = font.render("score:" + str(score), True, (0, 0, 0))

    snake_head = [260,240]
    snake = [[260, 240]]
    foodPos = [random.randrange(20,s_w,20), random.randrange(20,s_h,20)]
    dir = "UP"
    while True:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause(pause)
        keys = pygame.key.get_pressed()

        #sets direction of snake
        if keys[pygame.K_UP] and dir != "DOWN":
            dir = "UP"
        elif keys[pygame.K_DOWN] and dir != "UP":
            dir = "DOWN"
        elif keys[pygame.K_RIGHT] and dir != "LEFT":
            dir = "RIGHT"
        elif keys[pygame.K_LEFT]  and dir != "RIGHT":
            dir = "LEFT"
        #make snake longer without food (for fun) 
        if keys[pygame.K_SPACE]:
            snake.insert(0, (list(snake_head)))
            score += 1
        #moves head of snake into dir
        if dir == "UP":
            snake_head[1] -= 20
        if dir == "DOWN":
            snake_head[1] += 20
        if dir == "RIGHT":
            snake_head[0] += 20
        if dir == "LEFT":
            snake_head[0] -= 20
        #inserts new piece at cords of head and removes last one
        snake.insert(0, (list(snake_head)))
        snake.pop()
        if foodEaten(foodPos, snake_head):
            snake.insert(0, (list(snake_head)))
            foodPos = [random.randrange(20,s_w,20), random.randrange(20,s_h,20)]
            score += 1
            text = font.render("score: " + str(score), True, (255, 255, 255))
        else:
            if score < 1:
                text = font.render("score: 0", True, (255,255,255))
        #update and draw everything on the screen
        win.fill(otherGreen)
        foodRender(foodPos)
        snakeRender(snake)
        collCheck(snake_head, snake)
        win.blit(text, (0,0))
        pygame.display.update()

def pause(pause):
    font = pygame.font.SysFont("bitstreamverasans", 60)
    text = font.render("paused", True, (0, 0, 0))
    text2 = font.render("press ESC to unpause", True, (0, 0, 0))
    #create pause game loop while pause condition
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
            #render the pause screen
            win.fill((255,255,255))
            win.blit(text, (302 ,400 - text.get_height()))
            win.blit(text2, (101 ,468 - text.get_height()))
            pygame.display.update()

main()