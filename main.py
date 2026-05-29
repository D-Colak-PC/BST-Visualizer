"""
Dennis Colak
5/28/2026

BST Visualization using Pygame
This visualization can implement insertions, deletions, and swaps
It can also peform traversals in many different orders
"""

import pygame as pg
import pygame_widgets as pw
from ui.traversal_buttons import TraversalButtons
from ui.controls import NodeControls

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

    bst = BST()
    bst.build_from_list(FILLED)
    print(bst)

    button_font = pg.font.SysFont(None, BUTTON_FONT_SIZE)
    traversal_buttons = TraversalButtons(
        screen,
        WIDTH,
        HEIGHT,
        button_font,
        bst,
    )
    node_controls = NodeControls(
        screen,
        WIDTH,
        HEIGHT,
        button_font,
        bst,
    )

    while True:
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                return

        screen.fill(BLACK)
        bst.draw(screen)
        pw.update(events)
        pg.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pg.quit()
