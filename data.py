import pygame
import os

setting_win = {
    "WIDTH": 800,
    "HEIGHT": 600
}
setting_bot = {
    "WIDTH": 100,
    "HEIGHT": 100
}

setting_boss = {
    "WIDTH": 300,
    "HEIGHT": 300
}

bot_list = list()
bullet_boss_list = list()

abs_path = os.path.abspath(__file__ + "/..") + "\\image\\"

bot_images = [pygame.transform.scale(pygame.image.load(abs_path + "bot_1.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"])),
              pygame.transform.scale(pygame.image.load(abs_path + "bot_2.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"]))]

hero_images = [pygame.transform.scale(pygame.image.load(abs_path + "player_forward.png"), (200, 200)),
            pygame.transform.scale(pygame.image.load(abs_path + "player_forward_2.png"), (200, 200))]

boss_images =[pygame.transform.scale(pygame.image.load(abs_path + "player_forward.png"), (300, 300)),
            pygame.transform.scale(pygame.image.load(abs_path + "player_forward_2.png"), (300, 300))]

bullet_image = pygame.image.load(abs_path + "bullet.png")

HP_image = pygame.image.load(abs_path + "HP.png")
bg_image = pygame.image.load(abs_path + "bg.png")