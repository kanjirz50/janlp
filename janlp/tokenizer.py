import MeCab

from .sentence import Sentence
from .token import Morpheme


class Tokenizer:
    def __init__(self, *mecab_kwargs):
        self.__tagger = MeCab.Tagger(*mecab_kwargs)
        self.__tagger.parse("Initialize")

    def tokenize(self, sentence):
        return Sentence([morpheme for morpheme in self.__parse_to_tag(sentence)])

    def __parse_to_tag(self, sentence):
        node = self.__tagger.parseToNode(sentence)
        node = node.next
        while node.next:
            yield Morpheme(node)
            node = node.next
