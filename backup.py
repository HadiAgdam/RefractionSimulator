import pygame
import math
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Light Reflection Simulation")

clock = pygame.time.Clock()
background = (0, 0, 0)


def draw_bottom_line(angle: float, color=(255, 0, 0)):
    x = math.tan(angle * math.pi / 180) * height // 2
    pygame.draw.line(screen, color, (width // 2 - x, height), (width // 2, height // 2), 3)


def draw_top_line(angle: float, color=(0, 255, 0)):
    x = math.tan(angle * math.pi / 180) * height // 2
    pygame.draw.line(screen, color, (width // 2, height // 2), (width // 2 + x, 0), 3)


def draw_dashed_line(start_point, end_point):
    t = 50
    w = 1
    color = (125, 125, 125)

    x = math.fabs(end_point[0] - start_point[0]) // t
    y = math.fabs(end_point[1] - start_point[1]) // t

    x_sum = 0
    y_sum = 0
    for i in range(t // 2):
        pygame.draw.line(screen, color, (start_point[0] + x_sum, start_point[1] + y_sum),
                         (start_point[0] + x_sum + x, start_point[1] + y_sum + y), w)
        x_sum += x * 2
        y_sum += y * 2

    pygame.draw.line(screen, color, (start_point[0] + x_sum, start_point[1] + y_sum), end_point, w)

    # pygame.draw.circle(screen, (255, 0, 0), start_point, 5)
    # pygame.draw.circle(screen, (0, 0, 255), end_point, 5)


def draw_line(n1, n2, a1, color=(255, 0, 0)):
    draw_bottom_line(a1, color)

    a2 = a1 * n1 / n2

    print("a2 :", a2)

    draw_top_line(a2, color)


def init_interface():
    screen.fill(background)

    # bottom half
    pygame.draw.rect(screen, (50, 50, 50), (0, height // 2, width, height // 2))
    # line
    pygame.draw.line(screen, (255, 255, 255), (0, height // 2), (width, height // 2), 3)

    draw_line(2, 1, 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    init_interface()
    # draw_dashed_line((width // 2, 0), (width // 2, height))

    pygame.display.flip()
    clock.tick(60)
