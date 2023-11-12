from data import *

boss_shoot = pygame.USEREVENT
pygame.time.set_timer(boss_shoot, 2000)


class Background():
    def __init__(self, image, speed):
        self.IMAGE = image
        self.SPEED = speed
        self.y = 0
        self.y1 = - self.IMAGE.get_height()

    def move(self, window):
        window.blit(self.IMAGE, (0, self.y))
        window.blit(self.IMAGE, (0, self.y1))
        self.y += self.SPEED
        self.y1 += self.SPEED
        if self.y >= setting_win["HEIGHT"]:
            self.y = - self.IMAGE.get_height()
        if self.y1 >= setting_win["HEIGHT"]:
            self.y1 = - self.IMAGE.get_height()


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, speed= None, hp= None):
        super().__init__(x, y, width, height)
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_COUNT = 0
        self.SPEED = speed
        self.HP = hp
    def move_image(self):
        self.IMAGE_COUNT += 1
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10 - 1:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT % 10 == 0:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]





class Hero(Sprite):
    def __init__(self, x, y, width, height, image= None, speed= 5, hp= 3):
        super().__init__(x, y, width, height, image, speed, hp)
        self.MOVE = {"LEFT": False, "RIGHT": False}
        self.BULLET_LIST = list()
        self.LVL = 1
    

    def move(self, window):
        if self.MOVE["LEFT"] == True:
            self.x -= self.SPEED
        if self.MOVE["RIGHT"] == True:
            self.x += self.SPEED
        window.blit(self.IMAGE,(self.x, self.y))
        self.move_image()


class Bot(Sprite):
    def __init__(self,x,y,width,height,image= None,speed= 1,hp= 1, body_damage= 1):
        super().__init__(x,y,width,height,image,speed,hp)
        self.meteors = 0
        self.BODY_DAMAGE = body_damage


    def move(self, window, hero):
        self.y += self.SPEED
        window.blit(self.IMAGE, (self.x, self.y))

        self.meteors += 1

        if self.meteors % (setting_win["FPS"] * 2) == 0:
            bullet_bot_boss_list.append(Bullet(self.centerx, self.bottom, 10, 20, color= (158,96,0)))

        if self.colliderect(hero):
            hero.HP -= self.BODY_DAMAGE
            bot_list.remove(self)
            return 0
        

class Boss(Sprite):
    def __init__(self, x, y, width, height, image=None, speed= 2, hp=10):
        super().__init__(x, y, width, height, image, speed, hp)
        self.ANIMATION = False
        self.LIVE = False
    
    def move(self, window, hero):
        if self.y < 20 and not self.ANIMATION:
            self.y += abs(self.SPEED)
        self.x += self.SPEED
        if self.x < 0 or self.right > setting_win["WIDTH"]:
            self.SPEED *= -1

        if self.ANIMATION == True:
            self.leave(hero)


        window.blit(self.IMAGE, (self.x, self.y))
        self.move_image()

    def leave(self, hero):
        self.y -= abs(self.SPEED)
        if self.bottom < 0:
            self.ANIMATION = False
            hero.LVL += 1
            self.HP = 10 + hero.LVL * 5
            self.x = setting_win["WIDTH"] // 2 - setting_boss["WIDTH"] // 2
            self.y = - setting_boss["HEIGHT"]
            self.LIVE = False



class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, color= None, speed= 2):
        super().__init__(x,y,width,height)
        self.IMAGE = image
        self.COLOR = color
        self.SPEED = speed


    def move_hero(self, hero, window, boss):
        if self.y < 0:
            hero.BULLET_LIST.remove(self)
            return 0
        index = self.collidelist(bot_list)
        if index != -1:
            bot_list[index].HP -= 1
            if bot_list[index].HP == 0:
                bot_list.pop(index)
            hero.BULLET_LIST.remove(self)
            return 0
        if self.colliderect(boss):
            hero.BULLET_LIST.remove(self)
            boss.HP -= 1
            if boss.HP == 0:
                boss.ANIMATION = True
        self.y -= self.SPEED
        pygame.draw.rect(window, self.COLOR, self)



    def move_bot_boss(self,hero,window):
        if self.y > setting_win["HEIGHT"]:
            bullet_bot_boss_list.remove(self)
            return 0
        if self.colliderect(hero):
            hero.HP -= 1
            bullet_bot_boss_list.remove(self)
            return 0
        self.y += self.SPEED
        pygame.draw.rect(window, self.COLOR, self)