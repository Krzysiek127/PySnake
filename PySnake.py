print("PySnake by Krzysiek127")
import random,pygame,winsound,time

music = True
musicFile = "Snake.mp3"
clear_path = True
running = True

dead_offset = 20

screen = pygame.display.set_mode((256, 256), 0, 32)
pygame.init()

background = (random.randint(0,100),random.randint(0,100),random.randint(0,100))
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
points = 0

startTime = time.time()

pygame.draw.rect(screen,background,(0,0,256,256))

cordX = random.randint(2,7)
cordY = random.randint(2,7)

pointX = random.randint(1,7)
pointY = random.randint(1,7)
pygame.draw.rect(screen,red,(pointX*32,pointY*32,32,32))

volume = 0.2

if music:
    pygame.mixer.music.load(musicFile)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(1,0.0)

def IGHT_IMMA_HEAD_OUT():
    IMMASTOPYOURIGHTTHERE = 0
    while True:
        IMMASTOPYOURIGHTTHERE +=1
def coordinate_check():
    global cordX,cordY
    if cordX<0:
        cordX = 0
    if cordX>7:
        cordX = 7
    if cordY<0:
        cordY = 0
    if cordY>7:
        cordY = 7
def inputs():
    global running,cordX,cordY,volume
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_RIGHT]:
            cordX +=1
        if keys[pygame.K_LEFT]:
            cordX -=1
        if keys[pygame.K_UP]:
            cordY -=1
        if keys[pygame.K_DOWN]:
            cordY +=1
        if keys[pygame.K_u]:
            volume += 0.1
            if volume>1:
                volume = 1
            print(volume)
        if keys[pygame.K_p]:
            volume -= 0.1
            if volume<0:
                volume = 0
            print(volume)
def render():
    pygame.draw.rect(screen,green,(cordX*32,cordY*32,32,32))
def ateDot():
    global cordX,cordY,pointX,pointY,points
    if cordX==pointX and cordY==pointY:
        points +=1
        pointX = random.randint(0, 7)
        pointY = random.randint(0, 7)
        pygame.draw.rect(screen, red, (pointX*32, pointY*32, 32, 32))
        winsound.Beep(440,10)
try:
    while running:
        coordinate_check()
        inputs()
        render()
        ateDot()

        pygame.mixer.music.set_volume(volume)

        TimeElapsed = startTime - time.time()
        timeText = str(int(abs(TimeElapsed))) ## Programming SPAGHET (ik dead meme)
        if int(timeText)==points+dead_offset:
            print("YOU DIED!")
            running = False
        pygame.display.set_caption("P: " + str(points) + " C: " + str(cordX) + "," + str(cordY) + " T: " + timeText)
        pygame.display.update()
        if clear_path:
            pygame.draw.rect(screen, background, (cordX * 32, cordY * 32, 32, 32))
    pygame.quit()
except SystemExit:
    pygame.quit()
IGHT_IMMA_HEAD_OUT()