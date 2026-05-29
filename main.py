"""
Dennis Colak
5/28/2026

BST Visualization using Pygame
This visualization can implement insertions, deletions, and swaps
It can also peform traversals in many different orders
"""

import pygame as pg
import pygame_widgets as pw
from pygame_widgets.button import ButtonArray

from tree import BST
from constants import *


def main():
    pg.init()
    global WIDTH, HEIGHT
    display_info = pg.display.Info()
    WIDTH = display_info.current_w
    HEIGHT = display_info.current_h

    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.NOFRAME)
    pg.display.set_caption("BST Visualization")
    clock = pg.time.Clock()

    button_font = pg.font.SysFont(None, BUTTON_FONT_SIZE)
    _buttons = ButtonArray(
        screen,
        WIDTH - BUTTON_ARRAY_WIDTH,
        HEIGHT - BUTTON_ARRAY_HEIGHT,
        BUTTON_ARRAY_WIDTH,
        BUTTON_ARRAY_HEIGHT,
        (1, 4),
        border=PADDING,
        colour=(255, 0, 0),
        fonts=(button_font, button_font, button_font, button_font),
        radii=(5, 5, 5, 5),
        texts=("Level Order", "Inorder", "Preorder", "Postorder"),
        onClicks=(
            lambda: print(f"Level Order: {bst.level_order_traversal()}"),
            lambda: print(f"Inorder: {bst.inorder_traversal()}"),
            lambda: print(f"Preorder: {bst.preorder_traversal()}"),
            lambda: print(f"Postorder: {bst.postorder_traversal()}"),
        ),
    )

    bst = BST()
    bst.build_from_list(FILLED)
    print(bst)

    while True:
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                return

        screen.fill(BLACK)
        bst.draw(screen)
        pw.update(events)
        pg.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
    pg.quit()
