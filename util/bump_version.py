# -*- coding: utf-8 -*-

import os
import pkg_resources
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from packaging.version import Version

try:
    import lorem
    version = lorem.__version__
except ImportError:
    version = ''

    with open('lorem.py', 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('__version__'):
                version = line.split('=')[1].strip(" '")

    if not version:
        raise RuntimeError('cannot find version')

# parse version and bump version
ver_obj = pkg_resources.parse_version(version)  # type: Version
base_version = ver_obj.base_version

if ver_obj.is_devrelease:
    dev = cast('int', ver_obj.dev)
    new_ver = base_version + '.dev' + str(dev + 1)

elif ver_obj.is_prerelease:
    pre = cast('tuple[str, int]', ver_obj.pre)
    new_ver = base_version + pre[0] + str(pre[1] + 1)

elif ver_obj.is_postrelease:
    post = cast('int', ver_obj.post)
    new_ver = base_version + '.post' + str(post + 1)

else:
    new_ver = base_version + '.post1'

# write to file
try:
    import lorem
    path = lorem.__file__
except ImportError:
    path = os.path.join('lorem.py')

contents = []  # type: list[str]
with open(path, 'r', encoding='utf-8') as in_file:
    for line in in_file:
        if line.startswith('__version__'):
            line = f'__version__ = {new_ver!r}'
        contents.append(line)

with open (path, 'w', encoding='utf-8') as out_file:
    out_file.writelines(contents)
    out_file.write('\n')

with open(os.path.join('conda', 'build'), 'w') as build:
    build.write('0')
