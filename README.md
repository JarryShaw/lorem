# Lorem ipsum generator

In publishing and graphic design, *lorem ipsum* is a placeholder text commonly
used to demonstrate the visual form of a document or a typeface without
relying on meaningful content.

The `lorem` module provides a generic access to generating the *lorem ipsum*
text from its very original text:

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

## Get random words

The `lorem` module provides two different ways for getting random words.

1. `word(count=1, func=None, args=[], kwargs={}) -> Iterable[str]`

   Generate a list of random words.

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

2. `get_word(count=1, sep=' ', func=None, args=[], kwargs={}) -> str`

   Return random words.

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

## Get random sentences

The `lorem` module provides two different ways for getting random sentences.

1. `sentence(count=1, comma=(0, 2), word_range=(4, 8)) -> Iterable[str]`

   Generate a list of random sentences.

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

2. `get_sentence(count=1, comma=(0, 2), word_range=(4, 8), sep=' ') -> Union[str]`

   Return random sentences.

   ```python
   >>> sentence()
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


## Get random paragraphs

The `lorem` module provides two different ways for getting random paragraphs.

1. `paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Iterable[str]`

   Generate a list of random paragraphs.

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

2. `get_paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Union[str]`

   Return random paragraphs.

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


## Internal APIs

1. `_TEXT: Tuple[str]`

   Original *lorem ipsum* text pool.

2. `_gen_pool(dupe=1) -> Iterable[str]`

   Generate word pool.

   - Args:

     * `dupe` -- `int`

       Duplication to generate the word pool.

       *default*: `1`

   - Returns

     * `Iterable[str]` -- an infinite loop word pool

3. `_gen_word(pool, func, args=[], kwargs={}) -> str`

   Generate random word.

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

4. `_gen_sentence(pool, comma, word_range) -> str`

   Generate random sentence.

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

5. `_gen_paragraph(pool, comma, word_range, sentence_range) -> str`

   Generate random paragraph.

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
