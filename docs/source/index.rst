.. lorem documentation master file, created by
   sphinx-quickstart on Sat Feb 15 10:18:25 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pythonic Lorem Ipsum Generator
==============================

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   lorem
   test_lorem

In publishing and graphic design, lorem ipsum is a placeholder text commonly
used to demonstrate the visual form of a document or a typeface without
relying on meaningful content.

The :mod:`lorem` module provides a generic access to generating the lorem ipsum
text from its very original text::

   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
   tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
   veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
   commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
   esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
   cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
   est laborum.

Usage of the :mod:`lorem` module is rather simple. Depending on your needs, the
:mod:`lorem` module provides generation of *words*, *sentences*, and
*paragraphs*.

Get Random Words
----------------

The :mod:`lorem` module provides two different ways for getting random words.

1. :func:`~lorem.word` -- generate a list of random words

   .. code:: python

      word(count=1, func=None, args=(), kwargs={}) -> Iterator[str]

2. :func:`~lorem.get_word` -- return random words

   .. code:: python

      get_word(count=1, sep=' ', func=None, args=(), kwargs={}) -> str

Get Random Sentences
--------------------

The :mod:`lorem` module provides two different ways for getting random sentences.

1. :func:`~lorem.sentence` -- generate a list of random sentences

   .. code:: python

      sentence(count=1, comma=(0, 2), word_range=(4, 8)) -> Iterator[str]

2. :func:`~lorem.get_sentence` -- return random sentences

   .. code :: python

      get_sentence(count=1, sep=' ', comma=(0, 2), word_range=(4, 8)) -> Union[str]

Get Random Paragraphs
---------------------

The :mod:`lorem` module provides two different ways for getting random paragraphs.

1. :func:`~lorem.paragraph` -- generate a list of random paragraphs

   .. code:: python

      paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Iterator[str]

2. :func:`~lorem.get_paragraph` -- return random paragraphs

   .. code:: python

      get_paragraph(count=1, sep=os.linesep, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Union[str]

Customise Word Pool
-------------------

If wanted, the :mod:`lorem` module also provides an interface to customise the word
pool as you wish.

1. :func:`~lorem.set_pool` -- customise random word pool

   .. code:: python

      set_pool(pool)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
