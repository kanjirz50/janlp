# janlp

```python
>>> from janlp import Tokenizer
>>> t = Tokenizer()
>>> tokens = t.tokenize()
[日本語, NLP, の, 前, 処理, です, 。]
>>> tokens[0]
日本語
>>> tokens[0].is_kanji
True
>>> tokens[0].is_alpha
False
>>> tokens[0].next
NLP
>>> tokens[0].next.is_alpha
True
>>> tokens[0].prev
BOS
```