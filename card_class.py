class Card:
    def __init__(self, name, rank):
        self._name = name
        self._rank = rank

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if not isinstance(value, int):
            raise ValueError("Rank must be an integer.")
        self._rank = value

    def __str__(self):
        return f"{self.name}"
