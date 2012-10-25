#!/usr/bin/env python
"""
eukalypse_now

:copyright: (c) 2012 Dennis Schwertel, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages


tests_require = [
]


install_requires = [
    'south',
    'sphinx',
    'pil',
#    '-e git://github.com/kinkerl/eukalypse.git@master#egg=eukalypse',
    'raven',
    'logan'
]

setup(
    name='eukalypse_now',
    version='0.1',
    author='Dennis Schwertel',
    author_email='s@digitalkultur.net',
    description='eukalypse web server',
    long_description=__doc__,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    license='BSD',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'eukalypse_now = eukalypse_now.utils.runner:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)