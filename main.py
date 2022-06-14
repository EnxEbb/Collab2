
import pygame as p
import math
import datetime

p.init()
FPS = 60
screen = p.display.set_mode((800, 800))
p.display.set_caption("Clock")
clock = p.time.Clock()

def convertDegree(R, theta):
    y = math.cos(2 * math.pi * theta / 360) * R
    x = math.sin(2 * math.pi * theta / 360) * R
    return x + 400 - 18, -(y - 400) - 18

def printText(text, position):
    font = p.font.SysFont("Castellar", 40, True, False)
    surface = font.render(text, True, "black")
    screen.blit(surface, position)

def main():
    # pic = p.transform.scale(p.image.load("clock.jpg"), (600, 600))

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return


            currentTime = datetime.datetime.now()
            seconds = currentTime.second
            minute = currentTime.minute
            hour = currentTime.hour

            screen.fill(p.Color("white"))
            p.draw.circle(screen, (0, 0, 0), (400, 400), 400, 4)

            for number in range(1, 13):
                printText(str(number), convertDegree(350, number * 30))

            # minute
            R = 350
            theta = (minute + seconds / 60) * (360 / 60)
            p.draw.line(screen, (0, 0, 0), (400, 400), convertDegree(R, theta), 6)
            # second
            R = 300
            theta = seconds * (360 / 60)
            p.draw.line(screen, ("red"), (400, 400), convertDegree(R, theta), 6)
            # hour
            R = 250
            theta = (hour + minute / 60 + seconds / 3600) * (360 / 12)
            p.draw.line(screen, (0, 0, 0), (400, 400), convertDegree(R, theta), 6)

            p.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    main()

