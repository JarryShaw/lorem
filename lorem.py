# -*- coding: utf-8 -*-
"""lorem ipsum generator.

In publishing and graphic design, lorem ipsum is a placeholder text commonly
used to demonstrate the visual form of a document or a typeface without
relying on meaningful content.

The `lorem` module provides a generic access to generating the lorem ipsum text
from its very original text:

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
    est laborum.

Usage of the `lorem` module is rather simple. Depending on your needs, the
`lorem` module provides generation of **word**s, **sentence**s, and
**paragraph**s.

Get Random Words
----------------

The `lorem` module provides two different ways for getting random words.

1. `word` -- generate a list of random words

   ```python
   word(count=1, func=None, args=[], kwargs={}) -> Iterable[str]
   ```

2. `get_word` -- return random words

   ```python
   get_word(count=1, sep=' ', func=None, args=[], kwargs={}) -> str
   ```

Get Random Sentences
--------------------

The `lorem` module provides two different ways for getting random sentences.

1. `sentence` -- generate a list of random sentences

   ```python
   sentence(count=1, comma=(0, 2), word_range=(4, 8)) -> Iterable[str]
   ```

2. `get_sentence` -- return random sentences

   ```python
   get_sentence(count=1, comma=(0, 2), word_range=(4, 8), sep=' ') -> Union[str]
   ```

Get Random Paragraphs
---------------------

The `lorem` module provides two different ways for getting random paragraphs.

1. `paragraph` -- generate a list of random paragraphs

   ```python
   paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Iterable[str]
   ```

2. `get_paragraph` -- return random paragraphs

   ```python
   get_paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10), sep=os.linesep) -> Union[str]
   ```

"""
import os
import random

__all__ = [
    'word', 'sentence', 'paragraph',
    'get_word', 'get_sentence', 'get_paragraph',
]

# original lorem ipsum text pool
_TEXT = ('ad', 'adipiscing', 'aliqua', 'aliquip', 'amet', 'anim', 'aute', 'cillum', 'commodo',
         'consectetur', 'consequat', 'culpa', 'cupidatat', 'deserunt', 'do', 'dolor', 'dolore',
         'duis', 'ea', 'eiusmod', 'elit', 'enim', 'esse', 'est', 'et', 'eu', 'ex', 'excepteur',
         'exercitation', 'fugiat', 'id', 'in', 'incididunt', 'ipsum', 'irure', 'labore', 'laboris',
         'laborum', 'lorem', 'magna', 'minim', 'mollit', 'nisi', 'non', 'nostrud', 'nulla',
         'occaecat', 'officia', 'pariatur', 'proident', 'qui', 'quis', 'reprehenderit', 'sed',
         'sint', 'sit', 'sunt', 'tempor', 'ullamco', 'ut', 'velit', 'veniam', 'voluptate')


def _gen_pool(dupe=1):
    """Generate word pool.

    - Args:

      * `dupe` -- `int`

        Duplication to generate the word pool.

        *default*: `1`

    - Returns

      * `Iterable[str]` -- an infinite loop word pool

    """
    pool = list()
    for _ in range(dupe):
        pool.extend(_TEXT)
    random.shuffle(pool)

    while pool:  # pragma: no cover
        for text in pool:
            yield text
        random.shuffle(pool)


def _gen_word(pool, func, args=[], kwargs={}):  # pylint: disable=dangerous-default-value
    """Generate random word.

    - Args:

      * `pool` -- `Iterable[str]`

        Word pool, returned by `_gen_pool`.

      * `func` -- `Optional[Union[str, Callable[[str], str]]]`

        Filter function. It can be an attribute name of `str`, or a customised
        function that takes the original `str` and returns the modified `str`.

      * `args` -- `List[str]`

        Additional positional arguments for `func`.

        *default*: `[]`

      * `kwargs` -- `Dict[str, Any]`

        Additional keyword arguments for `func`.

        *default*: `{}`

    - Returns:

      * `str` -- random word

    """
    text = next(pool)
    if func is not None:
        if isinstance(func, str) and hasattr(text, func):
            text = getattr(text, func)(*args, **kwargs)
        else:
            text = func(text, *args, **kwargs)
    return text


def _gen_sentence(pool, comma, word_range):
    """Generate random sentence.

    - Args:

      * `pool` -- `Iterable[str]`

        Word pool, returned by `_gen_pool`.

      * `comma` -- `Tuple[int]`

        Random range for number of commas. The function will use
        `random.randint` to choose a random integer as the number of commas.

        *default*: `(0, 2)`

      * `word_range` -- `Tuple[int]`

        Random range for number of words in each sentence. The function will
        use `random.randint` to choose a random integer as the number of words.

        *default*: `(4, 8)`

    - Returns:

      * `str` -- random sentence

    """
    text = _gen_word(pool=pool, func='capitalize')
    for _ in range(random.randint(*word_range) - 1):
        text += ' ' + _gen_word(pool=pool, func=None)

    for _ in range(random.randint(*comma)):
        include_comma = random.choice([True, False])
        if include_comma:
            text += ','
            for _ in range(random.randint(*word_range)):
                text += ' ' + _gen_word(pool=pool, func=None)
            continue
        break
    return text + '.'


def _gen_paragraph(pool, comma, word_range, sentence_range):
    """Generate random paragraph.

    - Args:

      * `pool` -- `Iterable[str]`

        Word pool, returned by `_gen_pool`.

      * `comma` -- `Tuple[int]`

        Random range for number of commas. The function will use
        `random.randint` to choose a random integer as the number of commas.

        *default*: `(0, 2)`

      * `word_range` -- `Tuple[int]`

        Random range for number of words in each sentence. The function will
        use `random.randint` to choose a random integer as the number of words.

        *default*: `(4, 8)`

      * `sentence_range` -- `Tuple[int]`

        Random range for number of sentences in each paragraph. The function
        will use `random.randint` to choose a random integer as the number of
        sentences.

        *default*: `(5, 10)`

    - Returns:

      * `str` -- random paragraph

    """
    text = _gen_sentence(pool=pool, comma=comma, word_range=word_range)
    for _ in range(random.randint(*sentence_range) - 1):
        text += ' ' + _gen_sentence(pool=pool, comma=comma, word_range=word_range)
    return text


def word(count=1, func=None, args=[], kwargs={}):  # pylint: disable=dangerous-default-value
    """Generate a list of random words.

    ```python
    >>> list(word(count=3))
    ['labore', 'tempor', 'commodo']
    >>> list(word(count=3, func='capitalize'))
    ['Ea', 'Lorem', 'Do']
    >>> list(word(count=3, func=lambda s: s.upper()))
    ['UT', 'AMET', 'EXCEPTEUR']
    ```

    - Args:

      * `count` -- `int`

        Number of random words.

        *default*: `1`

      * `func` -- `Optional[Union[str, Callable[[str], str]]]`

        Filter function. It can be an attribute name of `str`, or a customised
        function that takes the original `str` and returns the modified `str`.

        *default*: `None`

      * `args` -- `List[str]`

        Additional positional arguments for `func`.

        *default*: `[]`

      * `kwargs` -- `Dict[str, Any]`

        Additional keyword arguments for `func`.

        *default*: `{}`

    - Returns:

      * `Iterable[str]` -- random words generator

    """
    pool = _gen_pool(count)
    yield from (_gen_word(pool=pool,
                          func=func,
                          args=args,
                          kwargs=kwargs) for _ in range(count))


def sentence(count=1, comma=(0, 2), word_range=(4, 8)):
    """Generate a list of random sentences.

    ```python
    >>> list(sentence())
    ['Aute irure et commodo sunt do duis dolor.']
    ```

    - Args:

      * `count` -- `int`

        Number of random sentences.

        *default*: `1`

      * `comma` -- `Tuple[int]`

        Random range for number of commas. The function will use
        `random.randint` to choose a random integer as the number of commas.

        *default*: `(0, 2)`

      * `word_range` -- `Tuple[int]`

        Random range for number of words in each sentence. The function will
        use `random.randint` to choose a random integer as the number of words.

        *default*: `(4, 8)`

    - Returns:

      * `Iterable[str]` -- random sentence generator

    """
    pool = _gen_pool(count * random.randint(*word_range))
    yield from (_gen_sentence(pool=pool,
                              comma=comma,
                              word_range=word_range) for _ in range(count))


def paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)):
    """Generate a list of random paragraphs.

    ```python
    >>> list(paragraph())
    ['Aute sint et cupidatat aliquip. Non exercitation est aliquip voluptate '
     'fugiat, reprehenderit ad occaecat laboris velit consequat. Magna enim '
     'deserunt aute laborum fugiat exercitation. Aliqua ex sunt fugiat in '
     'magna voluptate. Elit nisi exercitation nostrud. Magna proident et '
     'fugiat eiusmod cupidatat fugiat, sit culpa fugiat non ea eu '
     'reprehenderit elit. Proident mollit mollit ut cillum. Nostrud voluptate '
     'aliquip cupidatat anim.']
    ```

    - Args:

      * `count` -- `int`

        Number of random paragraphs.

        *default*: `1`

      * `comma` -- `Tuple[int]`

        Random range for number of commas. The function will use
        `random.randint` to choose a random integer as the number of commas.

        *default*: `(0, 2)`

      * `word_range` -- `Tuple[int]`

        Random range for number of words in each sentence. The function will
        use `random.randint` to choose a random integer as the number of words.

        *default*: `(4, 8)`

      * `sentence_range` -- `Tuple[int]`

        Random range for number of sentences in each paragraph. The function
        will use `random.randint` to choose a random integer as the number of
        sentences.

        *default*: `(5, 10)`

    - Returns:

      * `Iterable[str]` -- random paragraph generator

    """
    pool = _gen_pool(count * random.randint(*word_range) * random.randint(*sentence_range))
    yield from (_gen_paragraph(pool=pool,
                               comma=comma,
                               word_range=word_range,
                               sentence_range=sentence_range) for _ in range(count))


def get_word(count=1, sep=' ', func=None, args=[], kwargs={}):  # pylint: disable=dangerous-default-value
    """Return random words.

    ```python
    >>> get_word(count=3)
    'anim voluptate non'
    >>> get_word(count=3, func='capitalize')
    'Non Labore Ut'
    >>> get_word(count=3, func=lambda s: s.upper())
    'NISI TEMPOR CILLUM'
    ```

    - Args:

      * `count` -- `Union[int, Tuple[int]]`

        Number of random words. To generate random number of words, supply a
        2-element tuple of `int`, the function will use `random.randint` to choose
        a random integer as the number of random words.

        *default*: `1`

      * `sep` -- `str`

        Seperator between each word.

        *default*: `' '`

      * `func` -- `Optional[Union[str, Callable[[str], str]]]`

        Filter function. It can be a function name of `str`, or a customised
        function that takes the original `str` and returns the modified `str`.

        *default*: `None`

      * `args` -- `List[str]`

        Additional positional arguments for `func`.

        *default*: `[]`

      * `kwargs` -- `Dict[str, Any]`

        Additional keyword arguments for `func`.

        *default*: `{}`

    - Returns:

      * `str` -- random words

    """
    if isinstance(count, tuple):
        count = random.randint(*count)
    return sep.join(word(count, func, args, kwargs))


def get_sentence(count=1, comma=(0, 2), word_range=(4, 8), sep=' '):
    """Return random sentences.

    ```python
    >>> get_sentence()
    'Nostrud laboris lorem minim sit culpa, aliqua nostrud in amet, sint pariatur eiusmod esse.'
    ```

    - Args:

      * `count` -- `Union[int, Tuple[int]]`

        Number of random sentences. To generate random number of sentences,
        supply a 2-element tuple of `int`, the function will use
        `random.randint` to choose a random integer as the number of random
        sentences.

        *default*: `1`

      * `comma` -- `Tuple[int]`

        Random range for number of commas. The function will use
        `random.randint` to choose a random integer as the number of commas.

        *default*: `(0, 2)`

      * `word_range` -- `Tuple[int]`

        Random range for number of words in each sentence. The function will
        use `random.randint` to choose a random integer as the number of words.

        *default*: `(4, 8)`

      * `sep` -- `str`

        Seperator between each sentence.

        *default*: `' '`

    - Returns:

      * `str` -- random sentences

    """
    if isinstance(count, tuple):
        count = random.randint(*count)
    return sep.join(sentence(count, comma, word_range))


def get_paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10), sep=os.linesep):
    """Return random paragraphs.

    ```python
    >>> get_paragraph()
    'Exercitation magna sunt excepteur irure adipiscing commodo duis. Est '
    'ipsum qui deserunt, deserunt nostrud reprehenderit esse. Do velit '
    'est in velit sed. Sunt officia officia lorem. Commodo lorem '
    'exercitation veniam officia pariatur velit. Deserunt deserunt sed '
    'consequat laborum consequat dolor. Et consectetur irure sint elit tempor,'
    ' est minim nisi eiusmod id excepteur. Minim cillum veniam sed aliquip '
    'anim sit, pariatur nostrud ex cillum laboris laborum. Laborum ullamco '
    'mollit elit. Amet id incididunt ipsum sed.'
    ```

    - Args:

      * `count` -- `int`

        Number of random paragraphs. To generate random number of paragraphs,
        supply a 2-element tuple of `int`, the function will use
        `random.randint` to choose a random integer as the number of random
        paragraphs.

        *default*: `1`

      * `comma` -- `Tuple[int]`

        Random range for number of commas. The function will use
        `random.randint` to choose a random integer as the number of commas.

        *default*: `(0, 2)`

      * `word_range` -- `Tuple[int]`

        Random range for number of words in each sentence. The function will
        use `random.randint` to choose a random integer as the number of words.

        *default*: `(4, 8)`

      * `sentence_range` -- `Tuple[int]`

        Random range for number of sentences in each paragraph. The function
        will use `random.randint` to choose a random integer as the number of
        sentences.

        *default*: `(5, 10)`

      * `sep` -- `str`

        Seperator between each paragraph.

        *default*: `' '`

    - Returns:

      * `str` -- random paragraphs

    """
    if isinstance(count, tuple):
        count = random.randint(*count)
    return sep.join(paragraph(count, comma, word_range, sentence_range))
