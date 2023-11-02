import curses
import math
import time

def draw_apple(stdscr):
    curses.curs_set(0)  # Ocultar el cursor
    sh, sw = stdscr.getmaxyx()
    apple = ["  @@@@  ",
             " @@@@@@ ",
             "@@@@@@@@",
             "@@@@@@@@",
             " @@@@@@ ",
             "  @@@@  "]

    angle = 0

    while True:
        stdscr.clear()

        for i, row in enumerate(apple):
            y = int(sh / 2 - len(apple) / 2 + i)
            x = int(sw / 2 - len(row) / 2)
            stdscr.addstr(y, x, row)

        stdscr.refresh()
        time.sleep(0.1)

        angle += 10
        if angle >= 360:
            angle = 0
        apple = rotate_apple(apple, angle)

def rotate_apple(apple, angle):
    rotated_apple = ["      ",
                     "      ",
                     "      ",
                     "      ",
                     "      ",
                     "      "]

    for y, row in enumerate(apple):
        for x, char in enumerate(row):
            radians = math.radians(angle)
            new_x = int(x * math.cos(radians) - y * math.sin(radians))
            new_y = int(x * math.sin(radians) + y * math.cos(radians))
            if 0 <= new_x < len(rotated_apple[0]) and 0 <= new_y < len(rotated_apple):
                rotated_apple[new_y] = rotated_apple[new_y][:new_x] + char + rotated_apple[new_y][new_x + 1:]

    return rotated_apple

curses.wrapper(draw_apple)
