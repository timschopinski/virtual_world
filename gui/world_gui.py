import pygame
from world import World
from gui.board import BoardGUI
from utils.point import Point
from gui.gui_labels.choice_list import ChoiceList
from gui.gui_labels.info_label import InfoLabel
from utils.direction import Direction
from utils.color import Color
from comment import Comment
from storage.save import Save


class WorldGUI(World, BoardGUI):

    def __init__(self):
        super().__init__()
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("World Simulator")
        self.info = Comment(self.window)
        self.info.delete_comments()
        self.choice_list = None
        self.info_label = None
        self.active = None

    def draw_world(self):
        self.window.fill(Color.WHITE)
        human = self.get_human()
        for x in range(self.BOARD_ROWS):
            for y in range(self.BOARD_COLUMNS):
                self.draw_field(self.window, x, y)
                if self.choice_list:
                    self.choice_list.display()
                if self.info_label:
                    self.info_label.display()
                if self.board[x][y]:
                    self.board[x][y].draw()
        self.info.add_round_text(self.round)
        if human:
            if human.skill.is_animating:
                human.skill.draw_explosion()

    def another_round(self):
        super().another_round()
        self.info.add_comment(f'Round: {self.round}')

    def create_new_label(self, mouse_position: tuple):
        top_left = Point(mouse_position)
        x = int(top_left.y / self.field_height)
        y = int(top_left.x / self.field_width)
        if self.get_organism_on_field((Point((x, y)))):
            self.info_label = InfoLabel(self.window, self, top_left, (x, y))
        else:
            self.choice_list = ChoiceList(self.window, self, top_left, (x, y))

    def handle_events(self):
        human = self.get_human()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.active = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.choice_list:
                    self.choice_list.handle_user_input(pygame.mouse.get_pos())
                elif self.info_label:
                    self.info_label.handle_user_input(pygame.mouse.get_pos())
                else:
                    self.create_new_label(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                if self.choice_list:
                    break
                elif event.key == pygame.K_UP:
                    if human is not None:
                        human.set_direction(Direction.UP.value)
                    self.another_round()
                elif event.key == pygame.K_DOWN:
                    if human is not None:
                        human.set_direction(Direction.DOWN.value)
                    self.another_round()
                elif event.key == pygame.K_LEFT:
                    if human is not None:
                        human.set_direction(Direction.LEFT.value)
                    self.another_round()
                elif event.key == pygame.K_RIGHT:
                    if human is not None:
                        human.set_direction(Direction.RIGHT.value)
                    self.another_round()
                elif event.key == pygame.K_RETURN:
                    if human is not None:
                        human.unset_direction()
                    self.another_round()
                elif event.key == pygame.K_ESCAPE:
                    self.active = False
                elif event.key == pygame.K_p:
                    human = self.get_human()
                    if human:
                        if not human.skill.is_active:
                            human.skill.activate()
                    # production
                elif event.key == pygame.K_k:
                    print(self.organisms, len(self.organisms))
                    # production
                elif event.key == pygame.K_l:
                    for x in range(self.BOARD_ROWS):
                        for y in range(self.BOARD_COLUMNS):
                            print(self.board[x][y], end=" ")
                        print()
                    print('-----------------------------')

    def display(self):
        fps = 60
        clock = pygame.time.Clock()
        self.active = True

        def redraw_window():
            self.draw_world()
            pygame.display.update()

        while self.active:
            clock.tick(fps)
            self.handle_events()
            redraw_window()
        Save.update_world_state(self.organisms, self.round, self.rows, self.columns)

