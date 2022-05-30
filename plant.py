from organism import Organism


class Plant(Organism):
    def __init__(self, position, world):
        super().__init__(position, world)
        self.initiative = 0
        self.is_animal = False

    def collision(self):
        pass
        # self.world.board[self.position.x][self.position.y] = self
        # self.reproduce()

    def extra_behavior(self, enemy):
        pass

    def action(self):
        super().action()
