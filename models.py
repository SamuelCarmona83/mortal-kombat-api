
alignments = ['Good', 'Evil', 'Neutral']
dimensions = ['Earthrealm', 'Outworld', 'Netherrealm', 'Edenia']

class MortalKombatCharacter:

    all_characters = []

    def __init__(self, name, height, weight, fighting_style):
        self.name = name
        self.height = height
        self.weight = weight
        self.fighting_style = fighting_style
        self.dimension = None

        self.alignment = 'Neutral'
        self.abilities = []
        self.fatalities = []

        MortalKombatCharacter.all_characters.append(self)

    def set_alignment(self, alignment):
        if alignment in alignments:
            self.alignment = alignment
        else:
            raise ValueError(f"Invalid alignment. Choose from: {', '.join(alignments)}")

    def serialize(self):
        
        return {
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "fighting_style": self.fighting_style,
            "alignment": self.alignment,
            "abilities": self.abilities,
            "fatalities": self.fatalities,
            "dimension": self.dimension
        }

    @classmethod
    def get_all(cls):
        return cls.all_characters

    @classmethod
    def find_by_name(cls, name):
        for character in cls.all_characters:
            if character.name == name:
                return character
        return None

    def remove_character(self):
        MortalKombatCharacter.all_characters.remove(self)


def initialize_characters():
    scorpion = MortalKombatCharacter("Scorpion", "5'10\"", "175 lbs", "Ninjutsu")
    scorpion.set_alignment("Evil")

    sub_zero = MortalKombatCharacter("Sub-Zero", "6'0\"", "200 lbs", "Cryomancy")
    sub_zero.set_alignment("Good")

    liu_kang = MortalKombatCharacter("Liu Kang", "5'9\"", "160 lbs", "Martial Arts")
    liu_kang.set_alignment("Good")

    raiden = MortalKombatCharacter("Raiden", "6'5\"", "220 lbs", "Thunder God Powers")
    raiden.set_alignment("Good")

initialize_characters()