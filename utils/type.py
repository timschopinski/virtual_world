from enum import Enum, auto


class OrganismType(Enum):

    HUMAN = auto()
    WOLF = auto()
    GRASS = auto()
    GUARANI = auto()

    @classmethod
    def get_organism_type(cls, organism_type: str) -> 'OrganismType':
        organism_type = organism_type.upper()
        if organism_type == 'HUMAN':
            return cls.HUMAN
        elif organism_type == 'WOLF':
            return cls.WOLF
        elif organism_type == 'GRASS':
            return cls.GRASS
        elif organism_type == 'GUARANI':
            return cls.GUARANI





