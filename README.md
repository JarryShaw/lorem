# Lorem ipsum generator

[![PyPI - Downloads](https://pepy.tech/badge/python-lorem)](https://pepy.tech/count/python-lorem)
[![PyPI - Version](https://img.shields.io/pypi/v/python-lorem.svg)](https://pypi.org/project/python-lorem)
[![PyPI - Format](https://img.shields.io/pypi/format/python-lorem.svg)](https://pypi.org/project/python-lorem)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-lorem.svg)](https://pypi.org/project/python-lorem)

<!-- [![Travis CI - Status](https://travis-ci.com/JarryShaw/lorem.svg)](https://travis-ci.com/JarryShaw/lorem) -->
[![Codecov - Coverage](https://codecov.io/gh/JarryShaw/lorem/branch/master/graph/badge.svg)](https://codecov.io/gh/JarryShaw/lorem)
[![License](https://img.shields.io/github/license/jarryshaw/lorem.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

* [Installation](#installation)
* [Usage](#usage)
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
**paragraph**s:

```python
import lorem

print(lorem.get_sentence(count=3))
```

> Eu consectetur ad et, exercitation fugiat occaecat exercitation cillum non ullamco, elit mollit est consectetur. In ex proident esse est aute est mollit, id minim lorem tempor sunt elit. Dolor aliqua non eiusmod officia esse adipiscing.

Please refer to the [documentation](https://jarryshaw.github.io/lorem/)
for more details.

## Testing

The `lorem` module utilised `unittest.mock` to *patch* the builtin functions
from `random` module. Test cases can be found in [`test_lorem.py`](test_lorem.py).
**Contributions are welcome.**
