from setuptools import setup, find_packages
import os

VERSION = '3.0.0'
AUTHOR = 'James E. Bell Jr.'
CONTACT = 'james.e.bell@target.com'


def readme():
    with open('readme.md') as f:
        return f.read()


setup(
    name='tgt_grease',
    version=VERSION,
    author=AUTHOR,
    author_email=CONTACT,
    license="MIT",
    description='Modern distributed automation engine built with love by Target',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Topic :: System',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX'
    ],
    keywords='python automated recovery',
    packages=find_packages(),
    test_suite='nose.collector',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pylint'],
    install_requires=[
        'pymongo==3.8.0',
        'pinject==0.14.1'
    ] + (
         ["pywin32==224"] if "nt" == os.name else []
        ),
    include_package_data=True,
    zip_safe=False,
    scripts=[
        'bin/grease',
        'bin/grease-bridge',
        'bin/grease-daemon',
        'bin/grease.ps1',
    ]
)
