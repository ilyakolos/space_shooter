import pygame
import os
from random import randint

pygame.init()


setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 600,
    "FPS": 60
}

setting_hero = {
    "WIDTH": 100,
    "HEIGHT": 100,
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
abs_path = os.path.abspath(__file__ + "/..")
abs_path = os.path.join(abs_path, "image")
hero_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"v2player1.png")), (setting_hero["WIDTH"], setting_hero["HEIGHT"])),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"v2player2.png")), (setting_hero["WIDTH"], setting_hero["HEIGHT"]))
]

bot_image_list = [
    pygame.image.load(os.path.join(abs_path,"enemy.png"))
]

boss_image_list = [
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"boss1.png")), (setting_boss["WIDTH"], setting_boss["HEIGHT"])),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"boss2.png")), (setting_boss["WIDTH"], setting_boss["HEIGHT"]))
]

buff_hp_image = pygame.image.load(os.path.join(abs_path, "HPbuff.png"))

bg_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path,"fon.png")), (setting_win["WIDTH"], setting_win["HEIGHT"]))

bot_list = list()

bullet_bot_boss_list = list()

buff_list = list()
