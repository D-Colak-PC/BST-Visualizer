from pygame_widgets.button import Button
from pygame_widgets.combobox import ComboBox
from pygame_widgets.textbox import TextBox

from constants import *


class NodeControls:
    def __init__(self, screen, width, height, font, bst):
        self.bst = bst

        # delete row
        delete_y = height - (NODE_INPUT_HEIGHT + PADDING) * 2
        self.delete_input = ComboBox(
            screen,
            PADDING,
            delete_y,
            NODE_INPUT_WIDTH,
            NODE_INPUT_HEIGHT,
            choices=self._current_choices(),
            maxResults=NODE_DELETE_MAX_RESULTS,
            direction="up",
            font=font,
            borderRadius=NODE_CONTROL_RADIUS,
            colour=GRAY,
            hoverColour=MID_GRAY,
            pressedColour=DARK_GRAY,
            textHAlign="left",
            textboxKwargs={
                "colour": WHITE,
                "radius": NODE_CONTROL_RADIUS,
                "placeholderText": "Delete",
                "placeholderTextColour": GRAY,
            },
        )
        self.delete_button = Button(
            screen,
            PADDING * 2 + NODE_INPUT_WIDTH,
            delete_y,
            NODE_BUTTON_WIDTH,
            NODE_INPUT_HEIGHT,
            text="Del",
            font=font,
            colour=RED,
            hoverColour=MID_RED,
            pressedColour=DARK_RED,
            radius=NODE_CONTROL_RADIUS,
            onClick=self._on_delete,
        )

        # Add row (bottom)
        add_y = height - NODE_INPUT_HEIGHT - PADDING
        self.add_input = TextBox(
            screen,
            PADDING,
            add_y,
            NODE_INPUT_WIDTH,
            NODE_INPUT_HEIGHT,
            font=font,
            colour=WHITE,
            textColour=BLACK,
            borderColour=BLACK,
            borderThickness=NODE_TEXTBOX_BORDER_THICKNESS,
            radius=NODE_CONTROL_RADIUS,
            placeholderText="Add",
            placeholderTextColour=GRAY,
            onSubmit=self._on_add,
        )
        self.add_button = Button(
            screen,
            PADDING * 2 + NODE_INPUT_WIDTH,
            add_y,
            NODE_BUTTON_WIDTH,
            NODE_INPUT_HEIGHT,
            text="Add",
            font=font,
            colour=GREEN,
            hoverColour=MID_GREEN,
            pressedColour=DARK_GREEN,
            radius=NODE_CONTROL_RADIUS,
            onClick=self._on_add,
        )

    def _current_choices(self):
        return [str(v) for v in sorted(set(self.bst.level_order_traversal()))]

    def _refresh_delete_choices(self):
        self.delete_input.choices = self._current_choices()

    def _on_add(self):
        text = self.add_input.getText().strip()
        try:
            value = int(text)
        except ValueError:
            print(f"Cannot add node: {text!r} is not an integer")
            return
        self.bst.insert(value)
        self.add_input.setText("")
        self._refresh_delete_choices()

    def _on_delete(self):
        text = self.delete_input.getText().strip()
        try:
            value = int(text)
        except ValueError:
            print(f"Cannot delete node: {text!r} is not an integer")
            return
        self.bst.delete(value)
        self.delete_input.textBar.setText("")
        self._refresh_delete_choices()
