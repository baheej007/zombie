import pygame as pg
import sys
import random

pg.init() 

screen = pg.display.set_mode((1370,600))

bg= pg.image.load('bg.jpg')
bg=pg.transform.scale(bg, (1370,600))
zombie_image = pg.image.load('zombie.png')
zombie_image = pg.transform.scale(zombie_image, (40, 40))
gun_image = pg.image.load('gun.png')
gun_image = pg.transform.scale(gun_image, (80,80))
bullet_image = pg.image.load('bullet.png') 
bullet_image = pg.transform.scale(bullet_image, (20, 10))

pg.display.set_caption("Zombie Game") 
pg.display.set_icon(zombie_image)
def create_zombie():
    return [random.randint(1300//2, 1370 - 50), random.randint(50, 600 - 50)]
zombies = [create_zombie() for _ in range(5)]

gun_pos = [0,300]
bullets = [] 
def fire_bullet():
    bullet_pos = [gun_pos[0] + 50, gun_pos[1] + 20] 
    bullets.append(bullet_pos)


def check_collision(bullet, zombie):
    return (bullet[0] >= zombie[0] and bullet[0] <= zombie[0] + 50) and (bullet[1] >= zombie[1] and bullet[1] <= zombie[1] + 50)
    
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
            print(zombies)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                fire_bullet()
                
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        gun_pos[0] -= 5
    if keys[pg.K_RIGHT]:
        gun_pos[0] += 5
    if keys[pg.K_UP]:
        gun_pos[1] -= 5
    if keys[pg.K_DOWN]:
        gun_pos[1] += 5
        
    for bullet in bullets[:]:
        bullet[0] += 10 
        if bullet[0] > 1370:
            bullets.remove(bullet)
        else:
            for x in zombies[:]:
                if check_collision(bullet, x):
                    bullets.remove(bullet) 
                    zombies.remove(zombie)
                    break
    screen.blit(bg, (0, 0))   
    for zombie in zombies:
        screen.blit(zombie_image, zombie)
    screen.blit(gun_image, gun_pos)
    for bullet in bullets:
        screen.blit(bullet_image, bullet)
    pg.display.flip() 
    
pg.quit()
sys.exit()
