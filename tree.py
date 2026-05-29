import pygame as pg
import pygame.gfxdraw as gfxdraw

from node import Node
from constants import *


class BST:
    def __init__(self):
        self.root = None
        self.deletion_type = "successor"  # or "predecessor"

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def delete(self, value):  # delete first node w given value
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        # find the node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # leaf node or 1 child?
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 2 children
            temp = self._min_node(
                node.right if self.deletion_type == "successor" else node.left
            )
            node.value = temp.value
            if self.deletion_type == "successor":
                node.right = self._delete_recursive(node.right, temp.value)
            else:
                node.left = self._delete_recursive(node.left, temp.value)

        return node

    def _min_node(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def build_from_list(self, input_list):
        for v in input_list:
            self.insert(v)

    def draw(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        tree_height = self._height(self.root)
        y_offset = 0
        if tree_height > 1:
            y_offset = int(
                (screen_height * (PERCENT_OF_HEIGHT_FILLED / 100) - Y_OFFSET)
                / (tree_height - 1)
            )

        self._draw_recursive(
            screen, self.root, screen_width // 2, Y_OFFSET, screen_width // 4, y_offset
        )

    def _draw_recursive(self, screen, node, x, y, offset, y_offset):
        if node is not None:
            if node.left is not None:
                pg.draw.aaline(
                    screen, WHITE, (x, y), (x - offset, y + y_offset), LINE_WIDTH
                )
                self._draw_recursive(
                    screen, node.left, x - offset, y + y_offset, offset // 2, y_offset
                )

            if node.right is not None:
                pg.draw.aaline(
                    screen, WHITE, (x, y), (x + offset, y + y_offset), LINE_WIDTH
                )
                self._draw_recursive(
                    screen, node.right, x + offset, y + y_offset, offset // 2, y_offset
                )

            gfxdraw.aacircle(screen, x, y, RADIUS, GREEN)
            gfxdraw.filled_circle(screen, x, y, RADIUS, GREEN)
            font = pg.font.SysFont(None, FONT_SIZE)
            text = font.render(str(node.value), True, BLACK)
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def level_order_traversal(self):
        if self.root is None:
            return []

        i = 0
        queue = [self.root]

        while i < len(queue):
            curr = queue[i]

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            i += 1

        return [node.value for node in queue]

    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is None:
            return []
        return [
            *self._inorder_recursive(node.left),
            node.value,
            *self._inorder_recursive(node.right),
        ]

    def preorder_traversal(self):
        return self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is None:
            return []
        return [
            node.value,
            *self._preorder_recursive(node.left),
            *self._preorder_recursive(node.right),
        ]

    def postorder_traversal(self):
        return self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is None:
            return []
        return [
            *self._postorder_recursive(node.left),
            *self._postorder_recursive(node.right),
            node.value,
        ]

    def __str__(self):  # list representation
        return str(self.level_order_traversal())


if __name__ == "__main__":
    bst = BST()
    bst.build_from_list(DEFAULT_BST)
    print(bst.level_order_traversal())
    print(bst.inorder_traversal())
    print(bst.preorder_traversal())
    print(bst.postorder_traversal())
