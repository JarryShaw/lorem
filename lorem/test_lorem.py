# -*- coding: utf-8 -*-
# pylint: disable=protected-access, unused-argument
"""Test suite for `lorem` module."""

import itertools
import unittest
from typing import TYPE_CHECKING, TypeVar
from unittest import mock

import lorem

if TYPE_CHECKING:
    from typing import Any, Callable, Iterator, Optional, Sequence

# Type variable.
_T = TypeVar('_T')


def islice(iterable: 'Iterator[_T]', stop: 'int') -> 'list[_T]':
    """Wrapper function for :func:`itertools.islice`."""
    return list(itertools.islice(iterable, stop))


def shuffle(x: 'list[Any]',
            random: 'Optional[Callable[[], float]]' = None) -> 'None':
    """Mock :func:`random.shuffle`, but actually do nothing."""


def randint(a: 'int', b: 'int') -> 'int':
    """Mock :func:`random.randint`, but return the lower boundary."""
    return a


def choice_first(seq: 'Sequence[_T]') -> '_T':
    """Mock :func:`random.choice`, but return the first element."""
    return seq[0]


def choice_last(seq: 'Sequence[_T]') -> '_T':
    """Mock :func:`random.choice`, but return the last element."""
    return seq[-1]


def pool(self: 'lorem.LoremGenerator', dupe: 'int' = 1) -> 'Iterator[str]':
    """Mock :func:`lorem.LoremGenerator._gen_pool`, but return a minimised pool."""
    yield from itertools.cycle(['lorem', 'ipsum'])


class TestLorem(unittest.TestCase):
    """Unittest case for :mod:`lorem` module."""

    # Mock :func:`random.shuffle`
    mock_shuffle = mock.patch('random.shuffle', shuffle)
    # Mock :func:`random.randint`
    mock_randint = mock.patch('random.randint', randint)
    # Mock :func:`random.choice` by choosing the first item.
    mock_choice_first = mock.patch('random.choice', choice_first)
    # Mock :func:`random.choice` by choosing the last item.
    mock_choice_last = mock.patch('random.choice', choice_last)

    # Mock :func:`lorem._gen_pool`.
    mock_pool = mock.patch('lorem.LoremGenerator._gen_pool', pool)

    def test_lorem_init(self) -> 'None':
        """Test :func:`lorem.__init__`."""
        iter_pool = ['lorem', 'ipsum']
        with self.mock_shuffle:
            inst = lorem.LoremGenerator(pool=iter_pool, dupe=2)
            list_pool = islice(inst.pool, 10)
        self.assertEqual(list_pool, ['lorem', 'ipsum', 'lorem', 'ipsum', 'lorem',
                                     'ipsum', 'lorem', 'ipsum', 'lorem', 'ipsum'])

    def test_gen_word(self) -> 'None':
        """Test :func:`lorem.LoremGenerator.gen_word`."""
        iter_pool = ['lorem', 'ipsum']
        with self.mock_pool:
            inst = lorem.LoremGenerator(pool=iter_pool)

        word = inst.gen_word(func=None)
        self.assertEqual(word, 'lorem')

        word = inst.gen_word(func='capitalize')
        self.assertEqual(word, 'Ipsum')

        word = inst.gen_word(func=lambda s: s.upper())
        self.assertEqual(word, 'LOREM')

        word = inst.gen_word(func='replace', args=('i', 'I'))
        self.assertEqual(word, 'Ipsum')

        word = inst.gen_word(func=lambda s, **kwargs: s, kwargs={'test': 'null'})
        self.assertEqual(word, 'lorem')

    def test_gen_sentence(self) -> 'None':
        """Test :func:`lorem.LoremGenerator.gen_sentence`."""
        iter_pool = ['lorem', 'ipsum']
        with self.mock_pool:
            inst = lorem.LoremGenerator(pool=iter_pool)

        with self.mock_randint:
            sentence = inst.gen_sentence(comma=(0, 2), word_range=(1, 2))
        self.assertEqual(sentence, 'Lorem.')

        with self.mock_randint:
            with self.mock_choice_first:
                sentence = inst.gen_sentence(comma=(1, 2), word_range=(1, 2))
        self.assertEqual(sentence, 'Ipsum, lorem.')

        with self.mock_randint:
            with self.mock_choice_last:
                sentence = inst.gen_sentence(comma=(1, 2), word_range=(2, 4))
        self.assertEqual(sentence, 'Ipsum lorem.')

    def test_gen_paragraph(self) -> 'None':
        """Test :func:`lorem.LoremGenerator.gen_paragraph`."""
        iter_pool = ['lorem', 'ipsum']
        with self.mock_pool:
            inst = lorem.LoremGenerator(pool=iter_pool)

        with self.mock_randint:
            paragraph = inst.gen_paragraph(comma=(0, 2), word_range=(1, 2), sentence_range=(2, 3))
        self.assertEqual(paragraph, 'Lorem. Ipsum.')

        with self.mock_randint:
            with self.mock_choice_first:
                paragraph = inst.gen_paragraph(comma=(1, 2), word_range=(1, 2), sentence_range=(2, 3))
        self.assertEqual(paragraph, 'Lorem, ipsum. Lorem, ipsum.')

        with self.mock_randint:
            with self.mock_choice_last:
                paragraph = inst.gen_paragraph(comma=(1, 2), word_range=(2, 4), sentence_range=(3, 4))
        self.assertEqual(paragraph, 'Lorem ipsum. Lorem ipsum. Lorem ipsum.')

    def test_word(self) -> 'None':
        """Test :func:`lorem.word`."""
        with self.mock_pool:
            iter_word = lorem.word(count=3)
            list_word = islice(iter_word, 3)
        self.assertEqual(list_word, ['lorem', 'ipsum', 'lorem'])

        with self.mock_pool:
            iter_word = lorem.word(count=3, func='capitalize')
            list_word = islice(iter_word, 3)
        self.assertEqual(list_word, ['Lorem', 'Ipsum', 'Lorem'])

        with self.mock_pool:
            iter_word = lorem.word(count=3, func=lambda s: s.upper())
            list_word = islice(iter_word, 3)
        self.assertEqual(list_word, ['LOREM', 'IPSUM', 'LOREM'])

    def test_sentence(self) -> 'None':
        """Test :func:`lorem.sentence`."""
        with self.mock_pool:
            with self.mock_randint:
                iter_sentence = lorem.sentence()
                list_sentence = islice(iter_sentence, 1)
        self.assertEqual(list_sentence, ['Lorem ipsum lorem ipsum.'])

    def test_paragraph(self) -> 'None':
        """Test :func:`lorem.paragraph`."""
        with self.mock_pool:
            with self.mock_randint:
                iter_paragraph = lorem.paragraph()
                list_paragraph = islice(iter_paragraph, 1)
        self.assertEqual(list_paragraph, ['Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                          'Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                          'Lorem ipsum lorem ipsum.'])

    def test_get_word(self) -> 'None':
        """Test :func:`lorem.get_word`."""
        with self.mock_pool:
            with self.mock_randint:
                word = lorem.get_word(count=3)
        self.assertEqual(word, 'lorem ipsum lorem')

        with self.mock_pool:
            with self.mock_randint:
                word = lorem.get_word(count=(3, 5))
        self.assertEqual(word, 'lorem ipsum lorem')

        with self.mock_pool:
            with self.mock_randint:
                word = lorem.get_word(count=3, func='capitalize')
        self.assertEqual(word, 'Lorem Ipsum Lorem')

        with self.mock_pool:
            with self.mock_randint:
                word = lorem.get_word(count=3, func=lambda s: s.upper())
        self.assertEqual(word, 'LOREM IPSUM LOREM')

    def test_get_sentence(self) -> 'None':
        """Test :func:`lorem.get_sentence`."""
        with self.mock_pool:
            with self.mock_randint:
                sentence = lorem.get_sentence(count=1)
        self.assertEqual(sentence, 'Lorem ipsum lorem ipsum.')

        with self.mock_pool:
            with self.mock_randint:
                sentence = lorem.get_sentence(count=(1, 3))
        self.assertEqual(sentence, 'Lorem ipsum lorem ipsum.')

    def test_get_paragraph(self) -> 'None':
        """Test :func:`lorem.get_paragraph`."""
        with self.mock_pool:
            with self.mock_randint:
                paragraph = lorem.get_paragraph(count=1)
        self.assertEqual(paragraph, 'Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                    'Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                    'Lorem ipsum lorem ipsum.')

        with self.mock_pool:
            with self.mock_randint:
                paragraph = lorem.get_paragraph(count=(1, 3))
        self.assertEqual(paragraph, 'Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                    'Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                    'Lorem ipsum lorem ipsum.')


if __name__ == '__main__':
    unittest.main()
