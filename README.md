# Lorem ipsum generator

[![PyPI - Downloads](https://pepy.tech/badge/python-lorem)](https://pepy.tech/count/python-lorem)
[![PyPI - Version](https://img.shields.io/pypi/v/python-lorem.svg)](https://pypi.org/project/python-lorem)
[![PyPI - Format](https://img.shields.io/pypi/format/python-lorem.svg)](https://pypi.org/project/python-lorem)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-lorem.svg)](https://pypi.org/project/python-lorem)

[![Travis CI - Status](https://travis-ci.com/JarryShaw/lorem.svg)](https://travis-ci.com/JarryShaw/lorem)
[![Codecov - Coverage](https://codecov.io/gh/JarryShaw/lorem/branch/master/graph/badge.svg)](https://codecov.io/gh/JarryShaw/lorem)
[![License](https://img.shields.io/github/license/jarryshaw/lorem.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

* [Installation](#installation)
* [Usage](#usage)
  * [Get random words](#get-random-words)
    * [`word` -- renerate a list of random words](#word)
    * [`get_word`-- return random words](#get_word)
  * [Get random sentences](#get-random-sentences)
    * [`sentence` -- renerate a list of random sentences](#sentence)
    * [`get_sentence`-- return random sentences](#get_sentence)
  * [Get random paragraphs](#get-random-paragraphs)
    * [`paragraph` -- renerate a list of random paragraphs](#paragraph)
    * [`get_paragraph`-- return random paragraphs](#get_paragraph)
  * [Internal APIs](#internal-apis)
    * [`_TEXT` -- original *lorem ipsum* text pool](#_text)
    * [`_gen_word` -- generate random word](#_gen_word)
    * [`_gen_sentence` -- generate random sentence](#_gen_sentence)
    * [`_gen_paragraph` -- generate random paragraph](#_gen_paragraph)
* [Testing](#testing)

-------------------------------------------------------------------------------

> NB: uses [semantic versioning](https://semver.org).

In publishing and graphic design, *lorem ipsum* is a placeholder text commonly
used to demonstrate the visual form of a document or a typeface without
relying on meaningful content.

The `lorem` module provides a generic access to generating the *lorem ipsum*
text from its very original text:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
> tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
> veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
> commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
> esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
> cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
> est laborum.

## Installation

> Note that the `lorem` module only supports Python versions __since 3.5__ 🐍

Simply run the following to install the current version from PyPI:

```sh
pip install python-lorem
```

Or install the latest version from the git repository:

```sh
git clone https://github.com/JarryShaw/lorem.git
cd lorem
pip install -e .
# and to update at any time
git pull
```

## Usage

Usage of the `lorem` module is rather simple. Depending on your needs, the
`lorem` module provides generation of **word**s, **sentence**s, and
**paragraph**s.

### Get random words

The `lorem` module provides two different ways for getting random words.

<a name="word"></a>

1. ```python
   def word(count=1, func=None, args=(), kwargs={}) -> Iterator[str]: ...
   ```

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

     * `args` -- `Tuple[str]`

       Additional positional arguments for `func`.

       *default*: `()`

     * `kwargs` -- `Dict[str, Any]`

       Additional keyword arguments for `func`.

       *default*: `{}`

   - Returns:

     * `Iterator[str]` -- random words generator

<a name="get_word"></a>

2. ```python
   def get_word(count=1, sep=' ', func=None, args=(), kwargs={}) -> str: ...
   ```

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

     * `args` -- `Tuple[str]`

       Additional positional arguments for `func`.

       *default*: `()`

     * `kwargs` -- `Dict[str, Any]`

       Additional keyword arguments for `func`.

       *default*: `{}`

   - Returns:

     * `str` -- random words

### Get random sentences

The `lorem` module provides two different ways for getting random sentences.

<a name="sentence"></a>

1. ```python
   def sentence(count=1, comma=(0, 2), word_range=(4, 8)) -> Iterator[str]: ...
   ```

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

     * `Iterator[str]` -- random sentence generator

<a name="get_sentence"></a>

2. ```python
   def get_sentence(count=1, sep=' ', comma=(0, 2), word_range=(4, 8)) -> Union[str]: ...
   ```

   Return random sentences.

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

     * `sep` -- `str`

       Seperator between each sentence.

       *default*: `' '`

     * `comma` -- `Tuple[int]`

       Random range for number of commas. The function will use
       `random.randint` to choose a random integer as the number of commas.

       *default*: `(0, 2)`

     * `word_range` -- `Tuple[int]`

       Random range for number of words in each sentence. The function will
       use `random.randint` to choose a random integer as the number of words.

       *default*: `(4, 8)`

   - Returns:

     * `str` -- random sentences


### Get random paragraphs

The `lorem` module provides two different ways for getting random paragraphs.

<a name="paragraph"></a>

1. ```python
   def paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Iterator[str]: ...
   ```

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

     * `Iterator[str]` -- random paragraph generator

<a name="get_paragraph"></a>

2. ```python
   def get_paragraph(count=1, sep=os.linesep, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Union[str]: ...
   ```

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

     * `sep` -- `str`

       Seperator between each paragraph.

       *default*: `os.linesep` (`\r\n` on Windows, `\n` on POSIX)

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

     * `str` -- random paragraphs

### Internal APIs

Following are internal APIs for the `lorem` module.

<a name="_text"></a>

1. ```python
   _TEXT: Tuple[str] = ('ad', 'adipiscing', 'aliqua', 'aliquip', 'amet', 'anim', 'aute', 'cillum', 'commodo',
                        'consectetur', 'consequat', 'culpa', 'cupidatat', 'deserunt', 'do', 'dolor', 'dolore',
                        'duis', 'ea', 'eiusmod', 'elit', 'enim', 'esse', 'est', 'et', 'eu', 'ex', 'excepteur',
                        'exercitation', 'fugiat', 'id', 'in', 'incididunt', 'ipsum', 'irure', 'labore', 'laboris',
                        'laborum', 'lorem', 'magna', 'minim', 'mollit', 'nisi', 'non', 'nostrud', 'nulla',
                        'occaecat', 'officia', 'pariatur', 'proident', 'qui', 'quis', 'reprehenderit', 'sed',
                        'sint', 'sit', 'sunt', 'tempor', 'ullamco', 'ut', 'velit', 'veniam', 'voluptate')
   ```

   Original *lorem ipsum* text pool.

<a name="_gen_pool"></a>

2. ```python
   def _gen_pool(dupe=1) -> Iterator[str]: ...
   ```

   Generate word pool.

   - Args:

     * `dupe` -- `int`

       Duplication to generate the word pool.

       *default*: `1`

   - Returns

     * `Iterator[str]` -- an infinite loop word pool

<a name="_gen_word"></a>

3. ```python
   def _gen_word(pool, func, args=(), kwargs={}) -> str: ...
   ```

   Generate random word.

   - Args:

     * `pool` -- `Iterator[str]`

       Word pool, returned by `_gen_pool`.

     * `func` -- `Optional[Union[str, Callable[[str], str]]]`

       Filter function. It can be an attribute name of `str`, or a customised
       function that takes the original `str` and returns the modified `str`.

     * `args` -- `Tuple[str]`

       Additional positional arguments for `func`.

       *default*: `()`

     * `kwargs` -- `Dict[str, Any]`

       Additional keyword arguments for `func`.

       *default*: `{}`

   - Returns:

     * `str` -- random word

<a name="_gen_sentence"></a>

4. ```python
   def _gen_sentence(pool, comma, word_range) -> str: ...
   ```

   Generate random sentence.

   - Args:

     * `pool` -- `Iterator[str]`

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

<a name="_gen_paragraph"></a>

5. ```python
   def _gen_paragraph(pool, comma, word_range, sentence_range) -> str: ...
   ```

   Generate random paragraph.

   - Args:

     * `pool` -- `Iterator[str]`

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

## Testing

The `lorem` module utilised `unittest.mock` to *patch* the builtin functions
from `random` module. Test cases can be found in [`test.py`](test.py).
**Contributions are welcome.**
