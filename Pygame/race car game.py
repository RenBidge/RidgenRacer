import pygame
import time
import random

pygame.init()
crash_sound = pygame.mixer.Sound('crash.wav')
pygame.mixer.music.load('big_blue_mk8.wav')


display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

thing_blue = (0, 128, 255)
grey = (172, 172, 172)
grass_green = (41, 229, 78)

button_red = (200, 0, 0)
button_green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

player_width = 70
player_height = 140

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('RidgenRacer')
clock = pygame.time.Clock()

carImg1 = pygame.image.load('flaming purple car.png')

carImg2 = pygame.image.load('purple car.png')
carImg3 = pygame.image.load('pink car.png')
carImg4 = pygame.image.load('green car.png')
carImg5 = pygame.image.load('grey car.png')
carImg6 = pygame.image.load('orange car.png')
carImg7 = pygame.image.load('red car.png')
carImg8 = pygame.image.load('yellow car.png')
cars = [carImg2, carImg3, carImg4, carImg5, carImg6, carImg7, carImg8]

pause = False

car_icon = pygame.image.load('car icon.png')
pygame.display.set_icon(car_icon)

def dodged_count(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: ' + str(count), True, black)
    gameDisplay.blit(text, (2, 25))
    

def score_count(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Score: ' + str(count), True, black)
    gameDisplay.blit(text, (2, 2))
    
    
def score_display(count):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects('Your Score: ' + str(count), largeText)
    TextRect.center = ((display_width / 2), (display_height / 2 - 30))
    gameDisplay.blit(TextSurf, TextRect)    
    

def road(roadx, roady, roadw, roadh, colour):
    pygame.draw.rect(gameDisplay, colour, [roadx, roady, roadw, roadh])
    

def road_line(roadlinex, roadliney, roadlinew, roadlineh, colour):
    pygame.draw.rect(gameDisplay, colour, [roadlinex, roadliney, roadlinew, roadlineh])
    

def things(thingx, thingy, thingw, thingh, colour):
    pygame.draw.rect(gameDisplay, colour, [thingx, thingy, thingw, thingh])
    

def car(img, x, y):
    gameDisplay.blit(img, (x, y))
    
    
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects('You Crashed!', largeText)
    TextRect.center = ((display_width / 2), (display_height / 2 - 120))
    gameDisplay.blit(TextSurf, TextRect)
    
    score_display(score)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
            
        button("Retry", 200, 375, 100, 50, button_green, bright_green, normal_game)
        button("Quit", 500, 375, 100, 50, button_red, bright_red, quitgame)
    
        pygame.display.update()
        clock.tick(60)    
    
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

    
def button(msg, x, y, w, h, icolour, acolour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolour, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, icolour, (x, y, w, h))
                
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + w / 2), (y + h / 2))
    gameDisplay.blit(textSurf, textRect)
    
    
def quitgame():
    pygame.quit()
    quit()
    

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def pause_game():
    
    pygame.mixer.music.pause()
    
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects('Paused', largeText)
    TextRect.center = ((display_width / 2), (display_height / 2 - 50))
    gameDisplay.blit(TextSurf, TextRect)    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)

        
        button("Continue", 200, 375, 100, 50, button_green, bright_green, unpause)
        button("Quit", 500, 375, 100, 50, button_red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(60)
            
            
def game_intro():
    car_startx1 = 65
    car_startx2 = 165
    car_startx3 = 265
    car_startx4 = 365
    car_startx5 = 465
    car_startx6 = 565
    car_startx7 = 665
    car_starty1 = random.randrange(-500, -200)
    car_starty2 = random.randrange(-500, -200)
    car_starty3 = random.randrange(-500, -200)
    car_starty4 = random.randrange(-500, -200)
    car_starty5 = random.randrange(-500, -200)
    car_starty6 = random.randrange(-500, -200)
    car_starty7 = random.randrange(-500, -200)
    car_speed1 = random.randrange(5, 14)
    car_speed2 = random.randrange(5, 14)
    car_speed3 = random.randrange(5, 14)
    car_speed4 = random.randrange(5, 14)
    car_speed5 = random.randrange(5, 14)
    car_speed6 = random.randrange(5, 14)
    car_speed7 = random.randrange(5, 14)
    car_height = 140
    car1 = cars[random.randrange(0, 7)]
    car2 = cars[random.randrange(0, 7)]
    car3 = cars[random.randrange(0, 7)]
    car4 = cars[random.randrange(0, 7)]
    car5 = cars[random.randrange(0, 7)]
    car6 = cars[random.randrange(0, 7)]
    car7 = cars[random.randrange(0, 7)]
    
    roadline_startx = display_width / 2 - 20
    roadline_starty1 = -850
    roadline_starty2 = -250
    roadline_speed = 30
    roadline_width = 40
    roadline_height = 200
    road_startx = 50
    road_starty = 0
    road_width = display_width - 100
    road_height = display_height    
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(grass_green)
        
        road(road_startx, road_starty, road_width, road_height, grey)
        road_line(roadline_startx, roadline_starty1, roadline_width, roadline_height, white)
        roadline_starty1 += roadline_speed
        road_line(roadline_startx, roadline_starty2, roadline_width, roadline_height, white)
        roadline_starty2 += roadline_speed   
        
        car(car1, car_startx1, car_starty1)
        car_starty1 += car_speed1
        car(car2, car_startx2, car_starty2)
        car_starty2 += car_speed2
        car(car3, car_startx3, car_starty3)
        car_starty3 += car_speed3
        car(car4, car_startx4, car_starty4)
        car_starty4 += car_speed4
        car(car5, car_startx5, car_starty5)
        car_starty5 += car_speed5
        car(car6, car_startx6, car_starty6)
        car_starty6+= car_speed6
        car(car7, car_startx7, car_starty7)
        car_starty7 += car_speed7        

        if roadline_starty1 > display_height:
            roadline_starty1 = 0 - road_height
        if roadline_starty2 > display_height:
            roadline_starty2 = 0 - road_height
            
        if car_starty1 > display_height:
            car_starty1 = 0 - car_height
            car_speed1 = random.randrange(5, 15)
            car1 = cars[random.randrange(0, 7)]
        if car_starty2 > display_height:
            car_starty2 = 0 - car_height
            car_speed2 = random.randrange(5, 15)
            car2 = cars[random.randrange(0, 7)]          
        if car_starty3 > display_height:
            car_starty3 = 0 - car_height
            car_speed3 = random.randrange(5, 15)
            car3 = cars[random.randrange(0, 7)]          
        if car_starty4 > display_height:
            car_starty4 = 0 - car_height
            car_speed4 = random.randrange(5, 15)
            car4 = cars[random.randrange(0, 7)]
        if car_starty5 > display_height:
            car_starty5 = 0 - car_height
            car_speed5 = random.randrange(5, 15)
            car5 = cars[random.randrange(0, 7)]           
        if car_starty6 > display_height:
            car_starty6 = 0 - car_height
            car_speed6 = random.randrange(5, 15)
            car6 = cars[random.randrange(0, 7)]  
        if car_starty7 > display_height:
            car_starty7 = 0 - car_height
            car_speed7 = random.randrange(5, 15)
            car7 = cars[random.randrange(0, 7)]
        
        
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('RidgenRacer', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2 - 50))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!", 200, 375, 100, 50, button_green, bright_green, normal_game)
        button("Quit", 500, 375, 100, 50, button_red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(60)
        
        
def normal_game():
    global pause, score
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45)
    y = (display_height * 0.75)
    x_change = 0
    
    roadline_startx = display_width / 2 - 20
    roadline_starty1 = -850
    roadline_starty2 = -250
    roadline_speed = 15
    roadline_width = 40
    roadline_height = 200
    road_startx = 75
    road_starty = 0
    road_width = display_width - 150
    road_height = display_height
    
    car1 = cars[random.randrange(0, 7)]
    car2 = cars[random.randrange(0, 7)]
    car3 = cars[random.randrange(0, 7)]
    car4 = cars[random.randrange(0, 7)]

    car_startx1 = random.randrange(75, display_width - 145)
    car_startx2 = -100
    car_startx3 = -100
    car_startx4 = -100
    car_starty = -600
    car_speed = 4
    car_width = 70
    car_height = 140
    car_count = 1
    
    dodged = 0
    score = 0
    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_p:
                    pause = True
                    pause_game()
            
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    if x_change == 7:
                        x_change = 7
                    else:
                        x_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x_change == -7:
                        x_change = -7
                    else:
                        x_change = 0
                    
        x += x_change
                
        gameDisplay.fill(grass_green)   
        road(road_startx, road_starty, road_width, road_height, grey)
        road_line(roadline_startx, roadline_starty1, roadline_width, roadline_height, white)
        roadline_starty1 += roadline_speed
        road_line(roadline_startx, roadline_starty2, roadline_width, roadline_height, white)
        roadline_starty2 += roadline_speed
        
        car(car1, car_startx1, car_starty)
        car(car2, car_startx2, car_starty)
        car(car3, car_startx3, car_starty)
        car(car4, car_startx4, car_starty)
        car_starty += car_speed

        car(carImg1, x, y)
        dodged_count(dodged)
        score_count(score)
        
        # instead of hitting the walls and doing nothing, change it to crash()
        if x > display_width - player_width - 75 or x < 75:
            crash()
            
        if car_starty > display_height:
            car_starty = 0 - car_height
            dodged += 1
            if dodged < 6:
                score += 1
            elif 5 < dodged < 11:
                score += 2
            elif 10 < dodged < 16:
                score += 3
            elif 15 < dodged:
                score += 4
            
            if dodged % 5 == 0 and car_speed < 9:
                car_speed += 1
                roadline_speed += 3
                if car_width < 280:
                    car_count += 1
                    car_width += 70
            if car_count == 1:
                car_startx1 = random.randrange(75, display_width - 145)
                car1 = cars[random.randrange(0, 7)]
            elif car_count == 2:
                car_startx1 = random.randrange(75, display_width - (75 + 2 * 70))
                car1 = cars[random.randrange(0, 7)]
                car2 = cars[random.randrange(0, 7)]
                car_startx2 = car_startx1 + 70
            elif car_count == 3:
                car_startx1 = random.randrange(75, display_width - (75 + 3 * 70))
                car1 = cars[random.randrange(0, 7)]
                car2 = cars[random.randrange(0, 7)]
                car3 = cars[random.randrange(0, 7)]
                car_startx2 = car_startx1 + 70
                car_startx3 = car_startx2 + 70
            elif car_count == 4:
                car_startx1 = random.randrange(75, display_width - (75 + 4 * 70))
                car1 = cars[random.randrange(0, 7)]
                car2 = cars[random.randrange(0, 7)]
                car3 = cars[random.randrange(0, 7)]
                car4 = cars[random.randrange(0, 7)]
                car_startx2 = car_startx1 + 70
                car_startx3 = car_startx2 + 70
                car_startx4 = car_startx3 + 70

        if roadline_starty1 > display_height:
            roadline_starty1 = 0 - road_height
        if roadline_starty2 > display_height:
            roadline_starty2 = 0 - road_height
            
            
        if y < car_starty -5 + car_height and y + car_height > car_starty + 5:
            if (x > car_startx1 + 5 and x < car_startx1 - 5 + car_width or
                x + player_width > car_startx1 + 5 and x + player_width < car_startx1 - 5 + car_width):
                crash()
            
        pygame.display.update()
        clock.tick(60)
    
    
game_intro()    
normal_game()
pygame.quit()
quit()