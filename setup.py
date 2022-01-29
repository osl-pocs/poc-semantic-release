#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

with open('requirements_dev.txt', 'r') as f:
    dev_requirements = [l for l in f.read().split('\n') if l.strip()]
dev_requirements += requirements

setup(
    author="Ivan Ogasawara",
    author_email='ivan.ogasawara@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="PoC Semantic Release",
    install_requires=requirements,
    extras_require={'dev': dev_requirements},
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='poc_semantic_release',
    name='poc_semantic_release',
    packages=find_packages(include=['poc_semantic_release']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/osl-incubator/poc_semantic_release',
    version='1.2.2',
    zip_safe=False,
)
