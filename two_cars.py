import pygame
import random

#colours definition
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

#pygame initialisation 
x=pygame.init()
pygame.mixer.init()

screen_x=700
screen_y=500
m1=int(screen_x/4)
m2=int(screen_x/2)
m3=int(screen_x*3/4)
car1_position=[((0+m1)//2,485),((m1+m2)//2,485)]
car2_position=[((m2+m3)//2,485),((m3+screen_x)//2,485)]

gamewindow=pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("mrjk two cars clone")
clock=pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

#for welcome page of the game
def welcomepage():
    background_image = pygame.image.load("back.png").convert()
    background_image=pygame.transform.scale(background_image,(screen_x,screen_y)).convert_alpha()
    pygame.mixer.music.load("despacito.mp3")
    stay=True
    while stay:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                stay=False
            if event.type==pygame.KEYDOWN:
                pygame.mixer.music.play()
                maingame()
        
        gamewindow.fill(white)
        gamewindow.blit(background_image,(0,0))
        pygame.display.update()
        
    pygame.quit()
    quit()

#function for checking gamevoer
def checkgameover():
    pass

#this return the cordinates of our car is currently at
def return_xy_cars(postion_list,postion):
    currentpostion=postion_list[postion]
    x,y=currentpostion[0],currentpostion[1]
    return x,y

#this helps the cars to switch the lanes
def updatecarspostions(car1,car2):
    car1_x,car1_y=return_xy_cars(car1_position,car1)
    pygame.draw.rect(gamewindow,red,[car1_x-20,car1_y-50,40,60])
    car2_x,car2_y=return_xy_cars(car2_position,car2)
    pygame.draw.rect(gamewindow,green,[car2_x-20,car2_y-50,40,60])

#this is the inital displaay setup of the game
def displaysetup(gamewindow,score):
    gamewindow.fill(blue)
    pygame.draw.line(gamewindow,white,(m2,70), (m2,490),3)
    pygame.draw.line(gamewindow,white,(m1,70), (m1,490),1)
    pygame.draw.line(gamewindow,white,(m3,70), (m3,490),1)
    screentext(gamewindow,white,"Score: "+str(score),120,10)

#to display any text in the game window
def screentext(gamewindow,colour,text,x,y):
    message = font.render(text, True,colour)
    gamewindow.blit(message,(x,y))

#main game function
def maingame():
    #gamevariables initialisation
    gameover=False
    exitgame=False
    car1=0
    car2=0
    score=0
    speed=3
    x_postions=[(0+m1)//2,(m1+m2)//2,(m2+m3)//2,(m3+screen_x)//2]
    lane_x=[]
    lane_y=[]
    lanetype=[] 
    lanenumber=[]
 
    #mainloop
    while not exitgame:

        if gameover==True:
            background_image = pygame.image.load("gameover.png").convert()
            background_image=pygame.transform.scale(background_image,(screen_x,screen_y)).convert_alpha()
            gamewindow.fill(white)
            gamewindow.blit(background_image,(0,0))
            text=str(score)
            message1 = font.render(text, True,white)
            gamewindow.blit(message1,(215,215))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcomepage()
        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exitgame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        car1=(car1+1)%2
                    if event.key==pygame.K_RIGHT:
                        car2=(car2+1)%2
            
            gameover=checkgameover()

            #incrementing the score after a circle is consumed and handling gameovers
            if len(lanetype)>0:
                x1,y1=return_xy_cars(car1_position,car1)
                x2,y2=return_xy_cars(car2_position,car2)
                if lanetype[0]=="circle": 
                    
                    if lane_x[0]>(500-15) or lane_y[0]>(500-15):
                        pygame.time.wait(900)
                        gameover=True
                    
                    if (abs(x1-lane_x[0])<40 and abs(y1-lane_y[0])<60+15) or (abs(x2-lane_x[0])<40 and abs(y2-lane_y[0])<60+15):
                        score+=1
                        del lane_x[0]
                        del lane_y[0]
                        del lanetype[0]
                    
                else:
                    if (abs(x1-lane_x[0])<40 and abs(y1-lane_y[0])<60) or (abs(x2-lane_x[0])<40 and abs(y2-lane_y[0])<60):
                        pygame.time.wait(900)
                        gameover=True
                    


            #making each obstacles omove towards car
            for i in range(len(lane_y)):
                lane_y[i]=lane_y[i]+speed


            #initialising and saving the postions of each obstacles
            create=random.randint(1,6)
            if create==1 or create==2 or create==3:
                
                if len(lanetype)>1:
                    if  abs(lane_y[-1]-60)>150:
                        x=random.randint(0,3)
                        lane_x.append(x_postions[x])
                        lane_y.append(60)
                        lanetype.append("circle")
                        lanenumber.append(x)
                else:
                    x=random.randint(0,3)
                    lane_x.append(x_postions[x])
                    lane_y.append(60)
                    lanetype.append("circle")
                    lanenumber.append(x)


            if create==4 or create==5 or create==6:
                if len(lanetype)>1:
                    if  abs(lane_y[-1]-60)>150:
                        x=random.randint(0,3)
                        lane_x.append(x_postions[x])
                        lane_y.append(60)
                        lanetype.append("rectangle")
                        lanenumber.append(x)
                else:
                    x=random.randint(0,3)
                    lane_x.append(x_postions[x])
                    lane_y.append(60)
                    lanetype.append("rectangle")
                    lanenumber.append(x)
 
            
            #displaying in the game windoe
            displaysetup(gamewindow,score) 
            updatecarspostions(car1,car2)
            
            #plotiing the obstacles 
            for i in range(len(lane_y)):
                if lanetype[i]=="circle":
                    pygame.draw.circle(gamewindow,green,(lane_x[i],lane_y[i]),15)
                else:
                    pygame.draw.rect(gamewindow,red,[lane_x[i]-15,lane_y[i]-15,30,30])
            
            #deleting obstacles that are already passed through gamewindow

            if len(lanetype)>1:
                if lane_y[0]>500:
                    del lane_x[0]
                    del lane_y[0]
                    del lanetype[0]
                
            #display update
            pygame.display.update()
            clock.tick(60)

    #gamequit function
    pygame.quit()
    quit()

welcomepage()
# maingame()
