import random
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Meteor Mayhem')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 100)

sky_surf = pygame.image.load('burning_bg.png').convert()
ground_surf = pygame.image.load('grass.png').convert_alpha()
cloud_surf = pygame.image.load('cloud.png').convert_alpha()

score_surf = test_font.render('Test', False, (64, 64 ,64))
score_rect = score_surf.get_rect(center = (960, 180) )

meteor_surf = pygame.image.load('meteor.png').convert_alpha()
meteor_rect = meteor_surf.get_rect(midbottom = (200, -100))

dino_surf = pygame.image.load('Dino.png').convert_alpha()
dino_rect = dino_surf.get_rect(midbottom = (200, 1000))
dino_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_rect.bottom >= 1000:
             dino_gravity = -20
    
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, -100))
    
    meteor_rect.y += 10
    if meteor_rect.top >= 1080: meteor_rect.bottom = 0
    screen.blit(meteor_surf, meteor_rect)
    screen.blit(cloud_surf, (0, 0))
    pygame.draw.rect(screen, 'lightgoldenrod2', score_rect)
    screen.blit(score_surf, score_rect)

    # player
    dino_gravity += 1
    dino_rect.y += dino_gravity
    if dino_rect.bottom >= 1000: dino_rect.bottom = 1000
    screen.blit(dino_surf, dino_rect)

    
    pygame.display.update()
    clock.tick(60)



#if __name__ == "__main__":
    #main()