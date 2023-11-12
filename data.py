import pygame
from random import randint


pygame.init()


setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 600,
    "FPS": 60
}

setting_hero = {
    "WIDTH": 100,
    "HEIGHT": 50,
    "HP": 5
}

setting_bot = {
    "WIDTH": 100,
    "HEIGHT": 100
}

setting_boss = {
    "WIDTH": 200,
    "HEIGHT": 150
}

hero_image_list = [
    pygame.image.load("image\\player1.png"),
    pygame.image.load("image\\player2.png")
]

bot_image_list = [
    pygame.image.load("image\\enemy.png")
]

boss_image_list = [
    pygame.transform.scale(pygame.image.load("image\\boss1.png"), (setting_boss["WIDTH"], setting_boss["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\boss2.png"), (setting_boss["WIDTH"], setting_boss["HEIGHT"]))
]


bg_image = pygame.transform.scale(pygame.image.load("image\\fon.png"), (setting_win["WIDTH"], setting_win["HEIGHT"]))

bot_list = list()

bullet_bot_boss_list = list()