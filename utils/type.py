from enum import Enum, auto


class OrganismType(Enum):

    HUMAN = auto()
    WOLF = auto()
    SHEEP = auto()
    CYBER_SHEEP = auto()
    TURTLE = auto()
    FOX = auto()
    ANTELOPE = auto()
    GRASS = auto()
    GUARANI = auto()
    BORSCH = auto()
    DANDELION = auto()
    WILD_BERRIES = auto()

    @classmethod
    def get_organism_type(cls, organism_type: str) -> 'OrganismType':
        """REturns OrganismType from a string"""
        organism_type = organism_type.upper()
        print(f'{organism_type} -> get_organism_type()')
        if organism_type == 'HUMAN':
            return cls.HUMAN
        elif organism_type == 'WOLF':
            return cls.WOLF
        elif organism_type == 'SHEEP':
            return cls.SHEEP
        elif organism_type == 'CYBER_SHEEP':
            return cls.CYBER_SHEEP
        elif organism_type == 'TURTLE':
            return cls.TURTLE
        elif organism_type == 'FOX':
            return cls.FOX
        elif organism_type == 'ANTELOPE':
            print(f'returning {organism_type} -> get_organism_type()')
            return cls.ANTELOPE
        elif organism_type == 'GRASS':
            return cls.GRASS
        elif organism_type == 'GUARANI':
            return cls.GUARANI
        elif organism_type == 'BORSCH':
            return cls.BORSCH
        elif organism_type == 'DANDELION':
            return cls.DANDELION
        elif organism_type == 'WILD_BERRIES':
            return cls.WILD_BERRIES





