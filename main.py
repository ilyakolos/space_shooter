import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
PLAYER_SIZE = 50
ENEMY_RADIUS = 20
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 3

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простая игра")

# Игрок
player = pygame.Rect(175, 175, PLAYER_SIZE, PLAYER_SIZE)
player_health = 3

# Пули игрока
player_bullets = []

# Враги
enemies = []

# Большой враг
big_enemy = pygame.Rect(
    SCREEN_WIDTH, SCREEN_HEIGHT // 2 - ENEMY_RADIUS * 5, ENEMY_RADIUS * 10, ENEMY_RADIUS * 10
)
big_enemy_health = 5
big_enemy_active = False

# Счетчики
enemies_killed = 0
big_enemy_hits = 0

# Функция для создания врагов
def create_enemy():
    enemy = pygame.Rect(
        SCREEN_WIDTH,
        random.randint(0, SCREEN_HEIGHT - ENEMY_RADIUS * 2),
        ENEMY_RADIUS * 2,
        ENEMY_RADIUS * 2,
    )
    enemies.append(enemy)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED
    if keys[pygame.K_q]:
        bullet = pygame.Rect(player.centerx - 5, player.centery - 5, 10, 10)
        player_bullets.append(bullet)

    # Генерация врагов
    if len(enemies) < 5 and not big_enemy_active:
        create_enemy()

    # Обновление пуль игрока
    for bullet in player_bullets:
        bullet.x += BULLET_SPEED
        if bullet.x > SCREEN_WIDTH:
            player_bullets.remove(bullet)

    # Проверка попадания пуль игрока во врагов
    for bullet in player_bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                player_bullets.remove(bullet)
                enemies.remove(enemy)
                enemies_killed += 1

    # Управление большим врагом
    if enemies_killed >= 10:
        big_enemy_active = True
        if big_enemy.colliderect(player):
            player_health -= 1
        if big_enemy_active and big_enemy_hits >= 5:
            big_enemy_active = False
            big_enemy = pygame.Rect(
                SCREEN_WIDTH,
                SCREEN_HEIGHT // 2 - ENEMY_RADIUS * 5,
                ENEMY_RADIUS * 10,
                ENEMY_RADIUS * 10,
            )
            enemies_killed = 0
            big_enemy_hits = 0

    # Проверка попадания пуль игрока в большого врага
    for bullet in player_bullets[:]:
        if big_enemy.colliderect(bullet):
            player_bullets.remove(bullet)
            big_enemy_hits += 1
            if big_enemy_hits >= 5:
                big_enemy_health -= 1

    # Проверка на окончание игры
    if player_health <= 0:
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Игра окончена!", True, RED)
        screen.blit(game_over_text, (150, 150))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Рисование
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    for bullet in player_bullets:
        pygame.draw.rect(screen, RED, bullet)
    for enemy in enemies:
        pygame.draw.circle(screen, RED, enemy.center, ENEMY_RADIUS)
    if big_enemy_active:
        pygame.draw.circle(screen, RED, big_enemy.center, big_enemy.width // 2)

    # Отображение здоровья игрока
    font = pygame.font.Font(None, 24)
    health_text = font.render(f"Здоровье: {player_health}", True, RED)
    screen.blit(health_text, (10, 10))

    pygame.display.flip()
    pygame.time.delay(30)

# Завершение игры
pygame.quit()
sys.exit()