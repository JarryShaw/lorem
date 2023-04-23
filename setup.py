# -*- coding: utf-8 -*-
"""Lorem ipsum generator.

In publishing and graphic design, lorem ipsum is a placeholder text commonly
used to demonstrate the visual form of a document or a typeface without
relying on meaningful content.

The `lorem` module provides a generic access to generating the lorem ipsum text
from its very original text:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
> tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
> veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
> commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
> esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
> cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
> est laborum.

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
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

if sys.version_info[0] <= 2:
    raise OSError("python-lorem does not support Python 2!")

try:
    from setuptools import setup
    from setuptools.command.build_py import build_py
    from setuptools.command.develop import develop
    from setuptools.command.install import install
    from setuptools.command.sdist import sdist
except:
    raise ImportError("setuptools is required to install python-lorem!")


def refactor(path: 'str') -> 'None':
    """Refactor code."""
    import subprocess  # nosec: B404

    if sys.version_info < (3, 6):
        try:
            subprocess.check_call(  # nosec
                [sys.executable, '-m', 'f2format', '--no-archive', path]
            )
        except subprocess.CalledProcessError as error:
            print('Failed to perform assignment expression backport compiling.'
                  'Please consider manually install `bpc-f2format` and try again.', file=sys.stderr)
            sys.exit(error.returncode)

    if sys.version_info < (3, 8):
        try:
            subprocess.check_call(  # nosec
                [sys.executable, '-m', 'walrus', '--no-archive', path]
            )
        except subprocess.CalledProcessError as error:
            print('Failed to perform assignment expression backport compiling.'
                  'Please consider manually install `bpc-walrus` and try again.', file=sys.stderr)
            sys.exit(error.returncode)

        try:
            subprocess.check_call(  # nosec
                [sys.executable, '-m', 'poseur', '--no-archive', path]
            )
        except subprocess.CalledProcessError as error:
            print('Failed to perform assignment expression backport compiling.'
                  'Please consider manually install `bpc-poseur` and try again.', file=sys.stderr)
            sys.exit(error.returncode)


class lorem_sdist(sdist):
    """Modified sdist to run PyBPC conversion."""

    def make_release_tree(self, base_dir: 'str', *args: 'Any', **kwargs: 'Any') -> 'None':
        super(lorem_sdist, self).make_release_tree(base_dir, *args, **kwargs)

        # PyBPC compatibility enforcement
        #refactor(os.path.join(base_dir, 'lorem'))


class lorem_build_py(build_py):
    """Modified build_py to run PyBPC conversion."""

    def build_package_data(self) -> 'None':
        super(lorem_build_py, self).build_package_data()

        # PyBPC compatibility enforcement
        #refactor(os.path.join(self.build_lib, 'lorem'))


class lorem_develop(develop):
    """Modified develop to run PyBPC conversion."""

    def run(self) -> 'None':  # type: ignore[override]
        super(lorem_develop, self).run()

        # PyBPC compatibility enforcement
        #refactor(os.path.join(self.install_lib, 'lorem'))


class lorem_install(install):
    """Modified install to run PyBPC conversion."""

    def run(self) -> 'None':
        super(lorem_install, self).run()

        # PyBPC compatibility enforcement
        #refactor(os.path.join(self.install_lib, 'lorem'))  # type: ignore[arg-type]


setup(
    cmdclass={
        'sdist': lorem_sdist,
        'build_py': lorem_build_py,
        'develop': lorem_develop,
        'install': lorem_install,
    },
    long_description=__doc__,
    long_description_content_type='text/markdown',
)
