from pygame_widgets.button import ButtonArray
from constants import *
from .draw import draw_text_box


class TraversalButtons:
    def __init__(self, screen, width, height, font, bst):
        self.bst = bst
        self.screen = screen
        self.output_text = ""
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
                lambda: self._show_order(
                    "Level Order", bst.level_order_traversal()
                ),
                lambda: self._show_order("Inorder", bst.inorder_traversal()),
                lambda: self._show_order("Preorder", bst.preorder_traversal()),
                lambda: self._show_order("Postorder", bst.postorder_traversal()),
            ),
        )

    def _show_order(self, name, order):
        self.output_text = f"{name}: {order}"
        print(self.output_text)

    def draw_output(self):
        if self.output_text:
            draw_text_box(self.screen, self.output_text)
