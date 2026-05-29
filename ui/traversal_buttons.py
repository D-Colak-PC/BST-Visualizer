from pygame_widgets.button import ButtonArray
from constants import *


class TraversalButtons:
    def __init__(self, screen, width, height, font, bst):
        self.bst = bst
        self.array = ButtonArray(
            screen,
            width - BUTTON_ARRAY_WIDTH,
            height - BUTTON_ARRAY_HEIGHT,
            BUTTON_ARRAY_WIDTH,
            BUTTON_ARRAY_HEIGHT,
            TRAVERSAL_BUTTON_SHAPE,
            border=PADDING,
            colour=RED,
            fonts=(font,) * TRAVERSAL_BUTTON_COUNT,
            radii=(PADDING,) * TRAVERSAL_BUTTON_COUNT,
            texts=("Level Order", "Inorder", "Preorder", "Postorder"),
            onClicks=(
                lambda: print(f"Level Order: {bst.level_order_traversal()}"),
                lambda: print(f"Inorder: {bst.inorder_traversal()}"),
                lambda: print(f"Preorder: {bst.preorder_traversal()}"),
                lambda: print(f"Postorder: {bst.postorder_traversal()}"),
            ),
        )
