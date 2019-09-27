# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# version string
__version__ = '0.1.0'

# root path
ROOT = os.path.dirname(os.path.realpath(__file__))

# README
with open(os.path.join(ROOT, 'README.md'), encoding='utf-8') as file:
    __doc__ = file.read()

# set-up script for pip distribution
setup(
    name='python-lorem',
    version=__version__,
    author='Jarry Shaw',
    author_email='jarryshaw@icloud.com',
    url='https://github.com/JarryShaw/lorem',
    license='BSD License',
    keywords='lorem loremipsum',
    description='Lorem ipsum generator',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    python_requires='>=3.3',
    py_modules=['lorem'],
    include_package_data=True,
    zip_safe=True,
    package_data={
        '': [
            'LICENSE',
            'README.md',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ]
)
