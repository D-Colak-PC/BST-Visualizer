import pygame as pg
from constants import *


def draw_text_box(screen, text):
    width = screen.get_width()
    height = screen.get_height()
    top = height * (PERCENT_OF_HEIGHT_FILLED / 100)
    pad = height * (TEXT_BOX_PAD_PERCENT / 100)
    rect = pg.Rect(
        int(width * TEXT_LEFT_OFFSET),
        int(top + pad),
        int(width * (1 - 2 * TEXT_LEFT_OFFSET)),
        int(height - top - pad),
    )

    pg.draw.rect(screen, WHITE, rect, 4, 8)

    font = pg.font.SysFont(None, FONT_SIZE)
    text_surface = font.render(
        text, True, WHITE, wraplength=rect.width - 2 * TEXT_PADDING
    )

    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
