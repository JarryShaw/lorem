# -*- coding: utf-8 -*-
# pylint: disable=docstring-first-line-empty
"""
Lorem Ipsum Generator
=====================

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

1. :func:`word` -- generate a list of random words

   .. code:: python

      word(count=1, func=None, args=(), kwargs={}) -> Iterator[str]

2. :func:`get_word` -- return random words

   .. code:: python

      get_word(count=1, sep=' ', func=None, args=(), kwargs={}) -> str

Get Random Sentences
--------------------

The :mod:`lorem` module provides two different ways for getting random sentences.

1. :func:`sentence` -- generate a list of random sentences

   .. code:: python

      sentence(count=1, comma=(0, 2), word_range=(4, 8)) -> Iterator[str]

2. :func:`get_sentence` -- return random sentences

   .. code :: python

      get_sentence(count=1, sep=' ', comma=(0, 2), word_range=(4, 8)) -> Union[str]

Get Random Paragraphs
---------------------

The :mod:`lorem` module provides two different ways for getting random paragraphs.

1. :func:`paragraph` -- generate a list of random paragraphs

   .. code:: python

      paragraph(count=1, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Iterator[str]

2. :func:`get_paragraph` -- return random paragraphs

   .. code:: python

      get_paragraph(count=1, sep=os.linesep, comma=(0, 2), word_range=(4, 8), sentence_range=(5, 10)) -> Union[str]

Customise Word Pool
-------------------

If wanted, the :mod:`lorem` module also provides an interface to customise the word
pool as you wish.

1. :func:`set_pool` -- customise random word pool

   .. code:: python

      set_pool(pool)

"""
# version string
__version__ = '1.1.2'

# setup attributes
attrs = dict(
    name='python-lorem',
    version=__version__,
    description='Lorem ipsum generator.',
    long_description=__doc__,
    author='Jarry Shaw',
    author_email='jarryshaw@icloud.com',
    maintainer='Jarry Shaw',
    maintainer_email='jarryshaw@icloud.com',
    url='https://github.com/JarryShaw/lorem',
    download_url='https://github.com/JarryShaw/lorem/archive/v%s.tar.gz' % __version__,
    # packages
    py_modules=['lorem'],
    # scripts
    # ext_modules
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    # distclass
    # script_name
    # script_args
    # options
    license='BSD License',
    keywords=[
        'lorem',
        'loremipsum',
    ],
    platforms=[
        'any'
    ],
    # cmdclass
    # data_files
    # package_dir
    obsoletes=[
        'lorem',
        'loremipsum',
    ],
    # provides
    # requires
    # command_packages
    # command_options
    package_data={
        '': [
            'LICENSE',
            'README.md',
        ],
    },
    # include_package_data
    # libraries
    # headers
    # ext_package
    # include_dirs
    # password
    # fullname
    # long_description_content_type
    # python_requires
    # zip_safe
)

try:
    from setuptools import setup

    attrs.update(dict(
        include_package_data=True,
        # libraries
        # headers
        # ext_package
        # include_dirs
        # password
        # fullname
        long_description_content_type='text/x-rst',
        python_requires='>=3.5',
        zip_safe=True,
    ))
except ImportError:
    from distutils.core import setup

# set-up script for pip distribution
setup(**attrs)
