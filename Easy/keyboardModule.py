import pygame

# Creating a 'game' window to handle a key press
def init():
    pygame.init() #lint error - disregard for now
    win = pygame.display.set_mode((400, 400))

# Acquiring the key strokes
def getKey(keyName):
    ans = False

    for event in pygame.event.get(): pass

    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))

    if keyInput[myKey]:
        ans = True
    pygame.display.update()

    return ans

def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")

#if running this file as the root do this
if __name__ == "__main__":
    init()

    while True:
        main()