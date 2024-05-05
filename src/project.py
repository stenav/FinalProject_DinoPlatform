import random
import pygame
from sys import exit

def display_score(screen, test_font, start_time):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score:{current_time}', False, (64, 64 ,64))
    score_rect = score_surf.get_rect(center=(960, 180))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.y += 5

        obstacle_list = [obstacle for obstacle in obstacle_list 
                         if obstacle.y < 1080]

        return obstacle_list
    else:
        return []

def collisions(dino, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if dino.colliderect(obstacle_rect):
                return False
    return True
def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption('Meteor Mayhem')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('Pixeltype.ttf', 100)
    game_active = False
    start_time = 0
    score = 0


    sky_surf = pygame.image.load('burning_bg.png').convert()
    ground_surf = pygame.image.load('grass.png').convert_alpha()
    cloud_surf = pygame.image.load('cloud.png').convert_alpha()

    # obstacles
    meteor_surf = pygame.image.load('meteor.png').convert_alpha()
    meteor_surf = pygame.transform.scale(meteor_surf, (300, 300))


    obstacle_rect_list = []


    dino_surf = pygame.image.load('Dino.png').convert_alpha()
    dino_rect = dino_surf.get_rect(midbottom = (200, 1000))
    dino_gravity = 0

    dino_stand = pygame.image.load('Dino.png').convert_alpha()
    dino_stand = pygame.transform.rotozoom(dino_stand, 0, 1)
    dino_stand_rect = dino_stand.get_rect(center = (960, 540))

    # Intro Screen
    game_name = test_font.render('Meteor Mayhem', False, 'Black')
    game_name_rect = game_name.get_rect(center = (960, 240))

    game_msg = test_font.render('Press space to run', False, 'Black')
    game_msg_rect = game_msg.get_rect(center = (960, 780))

    # Timer
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 2600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and dino_rect.bottom >= 1000:
                        dino_gravity = -20
                    elif event.key == pygame.K_a:
                        dino_rect.x -= 200
                    elif event.key == pygame.K_d:
                        dino_rect.x += 200
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

            if event.type == obstacle_timer and game_active:
                obstacle_rect_list.append(meteor_surf.get_rect(center=
                                                            (random.randint(200, 1920),-100)))

        if game_active:
            screen.blit(sky_surf, (0, 0))
            screen.blit(ground_surf, (0, -100))
                    
            screen.blit(cloud_surf, (0, 0))

            score = display_score(screen, test_font, start_time)


            # player
            dino_gravity += 1
            dino_rect.y += dino_gravity
            if dino_rect.bottom >= 1000: dino_rect.bottom = 1000
            dino_rect.clamp_ip (screen.get_rect())
            screen.blit(dino_surf, dino_rect)

            # Obstacle Movement
            obstacle_rect_list = obstacle_movement(obstacle_rect_list)
            for obstacle_rect in obstacle_rect_list:
                 screen.blit(meteor_surf, obstacle_rect)

            # Collision 
            game_active = collisions(dino_rect, obstacle_rect_list)

        else:
            screen.fill('Orangered3')
            screen.blit(dino_stand, dino_stand_rect)
            obstacle_rect_list.clear()
            dino_rect.midbottom = (200, 1000)
            dino_gravity = 0

            score_msg = test_font.render(f'Your Score: {score}', False, 'Black')
            score_msg_rect = score_msg.get_rect(center = (960, 780))
            screen.blit(game_name, game_name_rect)

            if score == 0:
                screen.blit(game_msg, game_msg_rect)
            else:
                screen.blit(score_msg, score_msg_rect)
                

        
        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    main()