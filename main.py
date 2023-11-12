from function import *

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("КОСМІЧНИЙ ШУТЕР")



def run():
    game = True
    which_window = 1
    start_time = 0
    end_time = 0
    start_time_boss = 0
    menu = False

    hero = Hero(setting_win["WIDTH"] // 2 - setting_hero["WIDTH"] // 2,
                setting_win["HEIGHT"] - setting_hero["HEIGHT"] -20,
                setting_hero["WIDTH"],
                setting_hero["HEIGHT"],
                image= hero_image_list,
                hp = setting_hero["HP"])
    
    boss = Boss(setting_win["WIDTH"] // 2 - setting_boss["WIDTH"] // 2,
                - setting_boss["HEIGHT"], 
                setting_boss["WIDTH"],
                setting_boss["HEIGHT"],
                image= boss_image_list)


    bg = Background(bg_image, 0.5)

    clock = pygame.time.Clock()
    
    hp_bar = pygame.Rect(10, 10, 200, 15)
    hp_bar_white = pygame.Rect(10,10,200,15)

    font_win_lose = pygame.font.Font(None, 50)
    rect_start = pygame.Rect(400, 200, 200, 60)
    rect_lose = pygame.Rect(400, 300, 200, 60)

    while game:
        events = pygame.event.get()
        if which_window == 1:
            bg.move(window)

            hp_bar.width = (200 / setting_hero["HP"] * hero.HP)
            pygame.draw.rect(window, (255, 255, 255), hp_bar_white)
            pygame.draw.rect(window, (255, 20, 20), hp_bar)


            hero.move(window)
            for bullet in hero.BULLET_LIST:
                bullet.move_hero(hero, window, boss)
            
            if hero.HP == 0:
                menu = True
            

            end_time = pygame.time.get_ticks()
            if end_time - start_time > 2000 and not boss.LIVE:
                bot_list.append(Bot(randint(0, setting_win["WIDTH"] - setting_bot["WIDTH"]),
                                            - setting_bot["HEIGHT"],
                                            setting_bot["WIDTH"],
                                            setting_bot["HEIGHT"],
                                            image= bot_image_list))
                start_time = end_time
            for bot in bot_list:
                bot.move(window, hero)
            for bullet in bullet_bot_boss_list:
                bullet.move_bot_boss(hero,window)
                


            if end_time - start_time_boss > 10000:
                boss.LIVE = True
                boss.move(window, hero)
                if boss.LIVE == False:
                    start_time_boss = end_time
                




            if menu == True:
                pygame.draw.rect(window, (31,58,90), rect_start)
                pygame.draw.rect(window, (31,58,90), rect_lose)
                render_start = font_win_lose.render("START", True, (255, 255, 255))
                render_lose = font_win_lose.render("END", True, (255, 255, 255))
                window.blit(render_start, (rect_start.x + 48, rect_start.y + 13))
                window.blit(render_lose, (rect_start.x + 64, rect_lose.y + 13))
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos
                        if rect_start.collidepoint(x, y):
                            hero.HP = setting_hero["HP"]
                            hero.x = setting_win["WIDTH"] // 2 - hero.width // 2
                            hero.LVL = 1
                            if boss.LIVE == True:
                                boss.ANIMATION = True
                                hero.LVL = 0

                            menu = False
                            for i in range(len(bot_list)):
                                bot_list.pop(0)
                            for i in range(len(bullet_bot_boss_list)):
                                bullet_bot_boss_list.pop(0)
                        if rect_lose.collidepoint(x, y):
                            game = False



            for event in events:
                if event.type == boss_shoot and boss.LIVE:
                    bullet_bot_boss_list.append(Bullet(boss.centerx + 50, boss. bottom, 10, 20, color= (255, 10, 0)))
                    bullet_bot_boss_list.append(Bullet(boss.centerx + -50, boss. bottom, 10, 20, color= (0, 255, 0)))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = True
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = True
                    if event.key == pygame.K_SPACE:
                        hero.BULLET_LIST.append(Bullet(hero.centerx - 5, hero.y, 10, 20, color= (250, 20, 20)))
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = False
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = False


        for event in events:
            if event.type == pygame.QUIT:
                game = False


        clock.tick(setting_win["FPS"])
        pygame.display.flip()



run()