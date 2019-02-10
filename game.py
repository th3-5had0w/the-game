import pygame, random
from time import sleep
pygame.init()
pygame.font.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('piano.wav')
color = (0, 255, 0)
color1 = (255, 255, 255)
background_color = (255, 0, 0)
font = pygame.font.SysFont('Arial', 14)
font1 = pygame.font.SysFont('Times New Roman', 10)
image = pygame.image.load('scy.jpg')
word = font.render('Drag your mouse here', True, color)
word1 = font.render('Drag the mouse and there will be a gift for you', False, color1)
display = pygame.display.set_mode((700, 703))
pygame.display.set_caption('The Game - Created by th3_5had0w')
x = random.randint(0, 550)
y = random.randint(0, 680)
i = 0
max = random.randint(7, 14)
coordinates = (x, y, 150, 20)
pygame.draw.rect(display, background_color, coordinates)
display.blit(word, (x+3.5, y+1.5))
display.blit(word1, (5, 3))
while i < max:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
    if x < mouse_pos[0] < x+150 and y < mouse_pos[1] < y+20:
        display.fill((0, 0, 0))
        x = random.randint(0, 550)
        y = random.randint(0, 680)
        coordinates = (x, y, 150, 20)
        pygame.draw.rect(display, background_color, coordinates)
        display.blit(word, (x+3.5, y+1.5))
        display.blit(word1, (5, 3))
        i += 1
    pygame.display.update()
sound.play()
sleep(0.75)
display.blit(image, (0, 0))
pygame.display.flip()
while True:
    sound.play()
