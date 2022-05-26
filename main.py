import pygame
from gui.world_gui import WorldGUI
from menu import Menu


def main():
    world = WorldGUI()
    world.initialize()
    world.display()


# MENU
def main_menu():
    menu = Menu(main)
    menu.display_menu()
    pygame.quit()


if __name__ == '__main__':
    main_menu()
