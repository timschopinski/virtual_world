from enum import Enum, auto


class OrganismType(Enum):

    HUMAN = auto()
    WOLF = auto()
    SHEEP = auto()
    CYBER_SHEEP = auto()
    GRASS = auto()
    GUARANI = auto()
    BORSCH = auto()

    @classmethod
    def get_organism_type(cls, organism_type: str) -> 'OrganismType':
        organism_type = organism_type.upper()
        if organism_type == 'HUMAN':
            return cls.HUMAN
        elif organism_type == 'WOLF':
            return cls.WOLF
        elif organism_type == 'SHEEP':
            return cls.SHEEP
        elif organism_type == 'CYBER_SHEEP':
            return cls.CYBER_SHEEP
        elif organism_type == 'GRASS':
            return cls.GRASS
        elif organism_type == 'GUARANI':
            return cls.GUARANI
        elif organism_type == 'BORSCH':
            return cls.BORSCH






