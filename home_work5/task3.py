import pygame as pg
import sys

def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return "Piece"
    return False


pg.init()
SIZE_BLOCK = 100
MARGIN = 15
width = height = SIZE_BLOCK * 3 + MARGIN * 4

size_window = (width, height)
screen = pg.display.set_mode(size_window)
pg.display.set_caption("Крестики-нолики")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0

game_over = False
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)

        elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (SIZE_BLOCK + MARGIN)
            row = y_mouse // (SIZE_BLOCK + MARGIN)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(BLACK)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = RED
                elif mas[row][col] == 'o':
                    color = GREEN
                else:
                    color = WHITE
                x = col * SIZE_BLOCK + (col + 1) * MARGIN
                y = row * SIZE_BLOCK + (row + 1) * MARGIN
                pg.draw.rect(screen, color, (x, y, SIZE_BLOCK, SIZE_BLOCK))
                if color == RED:
                    pg.draw.line(screen, WHITE, (x + 5, y + 5), (x + SIZE_BLOCK - 5, y + SIZE_BLOCK - 5), 3)
                    pg.draw.line(screen, WHITE, (x + SIZE_BLOCK - 5, y + 5), (x + 5, y + SIZE_BLOCK - 5), 3)
                elif color == GREEN:
                    pg.draw.circle(screen, WHITE, (x + SIZE_BLOCK // 2, y + SIZE_BLOCK // 2), SIZE_BLOCK // 2 - 3, 3)

    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(BLACK)
        font = pg.font.SysFont('stxingkai', 80)
        text1 = font.render(game_over, True, WHITE)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_width() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pg.display.update()
