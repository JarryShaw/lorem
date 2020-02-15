# -*- coding: utf-8 -*-
# pylint: disable=protected-access, unused-argument
"""Test suite for `lorem` module."""

import itertools
import typing
import unittest
import unittest.mock as mock

import lorem

#: Type variable.
_T = typing.TypeVar('_T')


def islice(iterable: typing.Iterator[_T], stop: int) -> typing.List[_T]:
    """Wrapper function for :func:`itertools.islice`."""
    return list(itertools.islice(iterable, stop))


def shuffle(x: typing.List[typing.Any],
            random: typing.Optional[typing.Callable[[], float]] = None):
    """Mock :func:`random.shuffle`, but actually do nothing."""


def randint(a: int, b: int) -> int:
    """Mock :func:`random.randint`, but return the lower boundary."""
    return a


def choice_first(seq: typing.Sequence[_T]) -> _T:
    """Mock :func:`random.choice`, but return the first element."""
    return seq[0]


def choice_last(seq: typing.Sequence[_T]) -> _T:
    """Mock :func:`random.choice`, but return the last element."""
    return seq[-1]


def pool(dupe: int = 1) -> typing.Iterator[str]:
    """Mock :func:`lorem._gen_pool`, but return a minimised pool."""
    yield from itertools.cycle(['lorem', 'ipsum'])


class TestLorem(unittest.TestCase):
    """Unittest case for :mod:`lorem` module."""

    # mock :mod:`random` module functions
    #: Mock :func:`random.shuffle`
    mock_shuffle = mock.patch('random.shuffle', shuffle)
    #: Mock :func:`random.randint`
    mock_randint = mock.patch('random.randint', randint)
    #: Mock :func:`random.choice` by choosing the first item.
    mock_choice_first = mock.patch('random.choice', choice_first)
    #: Mock :func:`random.choice` by choosing the last item.
    mock_choice_last = mock.patch('random.choice', choice_last)

    # mock :mod:`lorem` module functions
    #: Mock :data:`lorem._TEXT` by a minimised pool (``['lorem', 'ipsum']``).
    mock_text = mock.patch('lorem._TEXT', ['lorem', 'ipsum'])
    #: Mock :func:`lorem._gen_pool`.
    mock_pool = mock.patch('lorem._gen_pool', pool)

    def test_set_pool(self):
        """Test :func:`lorem.set_pool`."""
        lorem.set_pool(['lorem', 'ipsum'])
        self.assertEqual(lorem._TEXT, ['lorem', 'ipsum'])

    def test_gen_pool(self):
        """Test :func:`lorem._gen_pool`."""
        with self.mock_text:
            with self.mock_shuffle:
                iter_pool = lorem._gen_pool(dupe=2)
                list_pool = islice(iter_pool, 10)
        self.assertEqual(list_pool, ['lorem', 'ipsum', 'lorem', 'ipsum', 'lorem',
                                     'ipsum', 'lorem', 'ipsum', 'lorem', 'ipsum'])

    def test_gen_word(self):
        """Test :func:`lorem._gen_word`."""
        iter_pool = pool()

        word = lorem._gen_word(pool=iter_pool, func=None)
        self.assertEqual(word, 'lorem')

        word = lorem._gen_word(pool=iter_pool, func='capitalize')
        self.assertEqual(word, 'Ipsum')

        word = lorem._gen_word(pool=iter_pool, func=lambda s: s.upper())
        self.assertEqual(word, 'LOREM')

        word = lorem._gen_word(pool=iter_pool, func='replace', args=('i', 'I'))
        self.assertEqual(word, 'Ipsum')

        word = lorem._gen_word(pool=iter_pool, func=lambda s, **kwargs: s, kwargs={'test': 'null'})
        self.assertEqual(word, 'lorem')

    def test_gen_sentence(self):
        """Test :func:`lorem._gen_sentence`."""
        iter_pool = pool()

        with self.mock_randint:
            sentence = lorem._gen_sentence(pool=iter_pool, comma=(0, 2), word_range=(1, 2))
        self.assertEqual(sentence, 'Lorem.')

        with self.mock_randint:
            with self.mock_choice_first:
                sentence = lorem._gen_sentence(pool=iter_pool, comma=(1, 2), word_range=(1, 2))
        self.assertEqual(sentence, 'Ipsum, lorem.')

        with self.mock_randint:
            with self.mock_choice_last:
                sentence = lorem._gen_sentence(pool=iter_pool, comma=(1, 2), word_range=(2, 4))
        self.assertEqual(sentence, 'Ipsum lorem.')

    def test_gen_paragraph(self):
        """Test :func:`lorem._gen_paragraph`."""
        iter_pool = pool()

        with self.mock_randint:
            paragraph = lorem._gen_paragraph(pool=iter_pool, comma=(0, 2),
                                             word_range=(1, 2), sentence_range=(2, 3))
        self.assertEqual(paragraph, 'Lorem. Ipsum.')

        with self.mock_randint:
            with self.mock_choice_first:
                paragraph = lorem._gen_paragraph(pool=iter_pool, comma=(1, 2),
                                                 word_range=(1, 2), sentence_range=(2, 3))
        self.assertEqual(paragraph, 'Lorem, ipsum. Lorem, ipsum.')

        with self.mock_randint:
            with self.mock_choice_last:
                paragraph = lorem._gen_paragraph(pool=iter_pool, comma=(1, 2),
                                                 word_range=(2, 4), sentence_range=(3, 4))
        self.assertEqual(paragraph, 'Lorem ipsum. Lorem ipsum. Lorem ipsum.')

    def test_word(self):
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

    def test_sentence(self):
        """Test :func:`lorem.sentence`."""
        with self.mock_pool:
            with self.mock_randint:
                iter_sentence = lorem.sentence()
                list_sentence = islice(iter_sentence, 1)
        self.assertEqual(list_sentence, ['Lorem ipsum lorem ipsum.'])

    def test_paragraph(self):
        """Test :func:`lorem.paragraph`."""
        with self.mock_pool:
            with self.mock_randint:
                iter_paragraph = lorem.paragraph()
                list_paragraph = islice(iter_paragraph, 1)
        self.assertEqual(list_paragraph, ['Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                          'Lorem ipsum lorem ipsum. Lorem ipsum lorem ipsum. '
                                          'Lorem ipsum lorem ipsum.'])

    def test_get_word(self):
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

    def test_get_sentence(self):
        """Test :func:`lorem.get_sentence`."""
        with self.mock_pool:
            with self.mock_randint:
                sentence = lorem.get_sentence(count=1)
        self.assertEqual(sentence, 'Lorem ipsum lorem ipsum.')

        with self.mock_pool:
            with self.mock_randint:
                sentence = lorem.get_sentence(count=(1, 3))
        self.assertEqual(sentence, 'Lorem ipsum lorem ipsum.')

    def test_get_paragraph(self):
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
