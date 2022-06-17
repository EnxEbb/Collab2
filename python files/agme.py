import pygame as p
import os
p.font.init()
p.mixer.init()

SPACE_WINDOW_WIDTH = 900
SPACE_WINDOW_HEIGHT = 500
screen = p.display.set_mode((SPACE_WINDOW_WIDTH, SPACE_WINDOW_HEIGHT))
p.display.set_caption("the game")
FPS = 60
VEL = 7
BULLETS_VEL = 12
MAX_BULLETS = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# TODO
# Uncomment these 2 lines and the lines 138, 144, 148, 152 if you want sound played in the game. Warning: IT IS LOUD
# BULLET_HIT_SOUND = p.mixer.Sound("Assets/Grenade+1.mp3")
# BULLER_FIRE_SOUND = p.mixer.Sound("Assets/Gun+Silencer.mp3")

BORDER = p.Rect(SPACE_WINDOW_WIDTH // 2 - 5, 0, 10, SPACE_WINDOW_HEIGHT)

HEALTH_FONT = p.font.SysFont("comicsans", 40)
WINNER_FONT = p.font.SysFont("comicsans", 100)

SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 45

YELLOW_HIT = p.USEREVENT + 1
RED_HIT = p.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = p.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = p.transform.rotate(p.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = p.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = p.transform.rotate(p.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = p.transform.scale(p.image.load(os.path.join(
    "Assets", "space.png")), (SPACE_WINDOW_WIDTH, SPACE_WINDOW_HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    screen.blit(SPACE, (0, 0))
    p.draw.rect(screen, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        f"Health: {str(red_health)}", 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        f"Health: {str(yellow_health)}", 1, WHITE)
    screen.blit(red_health_text, (SPACE_WINDOW_WIDTH -
                red_health_text.get_width() - 10, 10))
    screen.blit(yellow_health_text, (10, 10))

    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    screen.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in red_bullets:
        p.draw.rect(screen, RED, bullet)
    for bullet in yellow_bullets:
        p.draw.rect(screen, YELLOW, bullet)
    p.display.update()


def yellow_handle_movement(key_pressed, yellow):
    if key_pressed[p.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if key_pressed[p.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if key_pressed[p.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if key_pressed[p.K_s] and yellow.y + VEL + yellow.width < SPACE_WINDOW_HEIGHT:  # DOWN
        yellow.y += VEL


def red_handle_movement(key_pressed, red):
    if key_pressed[p.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if key_pressed[p.K_RIGHT] and red.x + VEL + red.width < SPACE_WINDOW_WIDTH:  # RIGHT
        red.x += VEL
    if key_pressed[p.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if key_pressed[p.K_DOWN] and red.y + VEL + red.height < SPACE_WINDOW_HEIGHT:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLETS_VEL
        if red.colliderect(bullet):
            p.event.post(p.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > SPACE_WINDOW_WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLETS_VEL
        if yellow.colliderect(bullet):
            p.event.post(p.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    screen.blit(draw_text, (SPACE_WINDOW_WIDTH // 2 - draw_text.get_width() //
                2, SPACE_WINDOW_HEIGHT // 2 - draw_text.get_height() // 2))
    p.display.update()
    p.time.delay(3000)


def main():
    red = p.Rect(700, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = p.Rect(100, 250, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = p.time.Clock()
    yellow_bullets = []
    red_bullets = []
    red_heath = 10
    yellow_health = 10
    run = True
    while run:
        clock.tick(FPS)
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return

            if event.type == p.KEYDOWN:
                if event.key == p.K_e and len(yellow_bullets) < MAX_BULLETS:
                    bullet = p.Rect(yellow.x + yellow.width,
                                    yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    # BULLER_FIRE_SOUND.play()

                if event.key == p.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = p.Rect(red.x + red.width, red.y +
                                    red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    # BULLER_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_heath -= 1
                # BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                # BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_heath <= 0:
            winner_text = "Yellow wins :D"
        if yellow_health <= 0:
            winner_text = "Red wins :D"

        if winner_text != "":
            draw_winner(winner_text)
            break

        key_pressed = p.key.get_pressed()
        yellow_handle_movement(key_pressed, yellow)
        red_handle_movement(key_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets,
                    yellow_bullets, red_heath, yellow_health)
    main()


if __name__ == "__main__":
    main()
