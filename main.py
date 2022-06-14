
import pygame as p
import logging

def main():
    p.init()
    screen = p.display.set_mode((512, 512))

    p.display.update()

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return
            screen.fill("black")


if __name__ == "__main__":
    main()

