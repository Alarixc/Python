import pygame
import random

#initializing pygame module
pygame.init()
screen_width=900
screen_height=600

#Colors:
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
pink=(255,153,255)

gameWindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Feckin Game by Alaric")
pygame.display.update()

#Game Specific Variables:
food_size=5
game_over=False
clock=pygame.time.Clock()
snake_size=10
font=pygame.font.SysFont(None,45)

def gamewin_display(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def snake_create(gameWindow,color,snake_list):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,black,(x,y,snake_size,snake_size))


def gameContinue(score):
    gameWindow.fill(black)
    gamewin_display(f"Game Over! Your Score was {score}! Press Enter to feckin play!",red,20,50)
    gamewin_display("You are a disappointment!",red,20,90)
    gamewin_display("This game is a work in progress, so shut up!",red,30,120)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    game_loop()
                    break

def game_loop():
    run=True
    global snake_size
    snake_x=45
    snake_y=55
    vel_x=0
    vel_y=0
    init_velocity=5
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    snake_size=10
    score=0
    fps=60

    snake_list=[]
    snake_length=1
    while run is not False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    vel_x=init_velocity
                    vel_y=0
                if event.key==pygame.K_LEFT:
                    vel_x=-init_velocity
                    vel_y=0
                if event.key==pygame.K_DOWN:
                    vel_y=init_velocity
                    vel_x=0
                if event.key==pygame.K_UP:
                    vel_y=-init_velocity
                    vel_x=0
        snake_x=snake_x+vel_x
        snake_y=snake_y+vel_y
        if abs(snake_x-food_x)<7 and abs(snake_y-food_y)<7:
            score+=1
            pygame.draw.rect(gameWindow,black,[food_x,food_y,snake_size,snake_size])
            food_x=random.randint(20,screen_width/2)
            food_y=random.randint(20,screen_height/2)
            snake_length+=1



        gameWindow.fill(white)
        gamewin_display("Loser's Score: "+str(score*10),pink,5,5)
        pygame.draw.circle(gameWindow,red,(food_x,food_y),5,3)
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)
        if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
            gameContinue(score)
        if snake_length>1:
            for x in range(len(snake_list)):
                for y in range(x,len(snake_list)-1):    
                    if snake_list[x]==snake_list[y+1]:
                        gameContinue(score)
                        break
                
                        
            
        if len(snake_list)>snake_length:
            del snake_list[0]
        # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
        snake_create(gameWindow,black,snake_list)
        pygame.display.update()
        clock.tick(fps)
        

game_loop()
pygame.quit()
quit()
