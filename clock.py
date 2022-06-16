
import pygame as p
import math
import datetime

p.init()
FPS = 60
screen = p.display.set_mode((800, 800))
p.display.set_caption("the clock :3")
clock = p.time.Clock()
bg = p.transform.scale(p.image.load("clock.jpg"), (800, 800))


def convertDegree(R, theta):
    y = math.cos(2 * math.pi * theta / 360) * R
    x = math.sin(2 * math.pi * theta / 360) * R
    return x + 400 - 18, -(y - 400) - 18


def printText(text, position):
    font = p.font.SysFont("Castellar", 40, True, False)
    surface = font.render(text, True, "black")
    screen.blit(surface, position)


def main():

    running = False

    while True:

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return

            elif event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:

                    running = not running
                    screen.blit(bg, (0, 0))

                    currentTime = datetime.datetime.now()
                    seconds = currentTime.second
                    minute = currentTime.minute
                    hour = currentTime.hour
                    # minute
                    R = 200
                    theta = (minute + seconds / 60) * (360 / 60)
                    p.draw.line(screen, (0, 0, 0), (400, 400),
                                convertDegree(R, theta), 4)
                    # second
                    R = 175
                    theta = seconds * (360 / 60)
                    p.draw.line(screen, ("red"), (400, 400),
                                convertDegree(R, theta), 4)
                    # hour
                    R = 150
                    theta = (hour + minute / 60 + seconds / 3600) * (360 / 12)
                    p.draw.line(screen, (0, 0, 0), (400, 400),
                                convertDegree(R, theta), 4)
                    p.display.update()
                    p.display.flip()
                # elif event.key == p.K_p:

        if running:
            p.display.update()
            p.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
