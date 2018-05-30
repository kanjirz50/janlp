import regex


class BOS:
    def __init__(self, next_node, label="BOS"):
        self.next = next_node
        self.prev = self

        self.__label = label

    def __str__(self):
        return self.__label

    def __repr__(self):
        return self.__str__()


class EOS:
    def __init__(self, prev_node, label="EOS"):
        self.next = self
        self.prev = prev_node

        self.__label = label

    def __str__(self):
        return self.__label

    def __repr__(self):
        return self.__str__()


class Morpheme:
    def __init__(self, node):
        self.surface = node.surface
        self.features = node.feature.split(",")

        self.pos = self.features[0]
        self.pos_s1 = self.features[1]
        self.pos_s2 = self.features[2]
        self.pos_s3 = self.features[3]
        self.conj = self.features[4]
        self.form = self.features[5]
        self.orig = self.features[6]

        if len(self.features) < 8:
            self.reading = None
            self.reading2 =None
        else:
            self.reading = self.features[7]
            self.reading2 = self.features[8]

        self.next = None
        self.prev = None

    @property
    def is_alpha(self):
        return regex.fullmatch(r"^[a-zA-Z]+$", self.surface) is not None

    @property
    def is_hiragana(self):
        return regex.fullmatch(r"^\p{Hiragana}+$", self.surface) is not None

    @property
    def is_katakana(self):
        return regex.fullmatch(r"^\p{Katakana}+$", self.surface) is not None

    @property
    def is_kanji(self):
        return regex.fullmatch(r"^\p{Han}+$", self.surface) is not None

    def __str__(self):
        return self.surface

    def __repr__(self):
        return self.__str__()
