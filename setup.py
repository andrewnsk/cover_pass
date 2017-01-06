#!/usr/bin/env python

from setuptools import setup


setup(
    name='coverpass',
    version='0.0.1',
    description='testing environment',
    author='Andrew Dorokhin (@andrewnsk)',
    author_email='andrew@dorokhin.moscow',
    url='http://github.com/andrewnsk/cover_pass',
    packages=['coverpass', 'tests.unit'],
      long_description="""\
      It's my own temporary testing project
      """,
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
    ],
    package_data = {
        '': ['*.txt', '*.xsd']
    },
    keywords='unittest test software',
    license='MIT',
    test_suite='tests'
)
