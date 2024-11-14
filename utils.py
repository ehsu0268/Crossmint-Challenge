ATTRIBUTE_ASTRAL_OBJECT = {
    "POLYANET": ["-", "polyanet"],
    "RIGHT_COMETH": ["right", "cometh"],
    "LEFT_COMETH": ["left", "cometh"],
    "UP_COMETH": ["up", "cometh"],
    "DOWN_COMETH": ["down", "cometh"],
    "BLUE_SOLOON": ["blue", "soloon"],
    "RED_SOLOON": ["red", "soloon"],
    "PURPLE_SOLOON": ["purple", "soloon"],
    "WHITE_SOLOON": ["white", "soloon"]
}


class MatrixUtils:
    @staticmethod
    def get_attribute_astral_object(input):
        """
        Gets attribute and type of astral object in a processed list
        :param input: input (e.g. WHITE_SOLOON)
        :return: []
        """
        return ATTRIBUTE_ASTRAL_OBJECT.get(input, None)
