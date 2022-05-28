from res.const import *

def terminate():
    pygame.image.save(CANVAS,'pic.png')
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def mousePosCorrection(pos):
    return (pos[0] - (WX-CX)/2, pos[1] - (WY-CY)/2)

