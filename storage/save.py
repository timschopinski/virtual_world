import os


class Save:
    """ Updates the world state every round and saves it to a file when its called """
    world_state = {}

    def __init__(self, file_path: str):
        self.file_path = os.path.join("storage/saves/", file_path)

    @classmethod
    def _update_world_data(cls, rows, columns, round):
        cls.world_state.update({'world': {}})
        cls.world_state['world'].update({'rows': rows})
        cls.world_state['world'].update({'columns': columns})
        cls.world_state['world'].update({'round': round})

    @classmethod
    def _update_organism_data(cls, organisms):
        cls.world_state.update({'organisms': []})
        for index, organism in enumerate(organisms):
            cls.world_state['organisms'].append({})
            cls.world_state['organisms'][index].update({'type': organism.__str__()})
            cls.world_state['organisms'][index].update({'x': organism.position.x})
            cls.world_state['organisms'][index].update({'y': organism.position.y})
            cls.world_state['organisms'][index].update({'age': organism.age})
            cls.world_state['organisms'][index].update({'strength': organism.strength})
            cls.world_state['organisms'][index].update({'initiative': organism.initiative})

    @classmethod
    def update_world_state(cls, organisms, round, rows, columns):
        cls._update_world_data(rows, columns, round)
        cls._update_organism_data(organisms)

    def save_world_state(self):
        """ Saves the current world state to a file """

        with open(file=self.file_path, mode="w") as f:
            for world_data in self.world_state['world'].values():
                f.write(str(world_data))
                f.write(' ')
            f.write('\n')
            for organisms in self.world_state['organisms']:
                for organism_data in organisms.values():
                    f.write(str(organism_data))
                    f.write(' ')
                f.write('\n')
