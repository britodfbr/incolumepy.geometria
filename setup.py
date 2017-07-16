from setuptools import setup, find_packages
import os

def myread(*pnames):
    return open(os.path.join(os.path.dirname(__file__), *pnames)).read()

NAME = 'incolumepy.geometria'
DESCRIPTION = "package with autotesting ()"
AUTHOR = "incolume.com.br"
AUTHOR_EMAIL = "contato at incolume.com.br"
URL = "http://www.incolume.com.br"
LICENSE = myread("LICENSE")
LONG_DESCRIPTION = (
    myread('README.md')
    + '\n'
    'History\n'
    '=======\n'
    + '\n' +
    myread("docs", "HISTORY.rst")
    + "\n"
    'Contributors\n'
    '============\n'
    + '\n' +
    myread('docs', 'CONTRIBUTORS.rst')
    + '\n'
    'Changes\n'
    '=======\n'
    + '\n' +
    myread('docs', 'CHANGES.rst')
    + '\n')

VERSION = myread(NAME.split('.')[0], NAME.split('.')[1], "version.txt").strip()

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,

      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      packages=find_packages(exclude=['ez_setup', "*.tests", "*.tests.*", "tests.*", "tests"]),
      namespace_packages=[NAME.split('.')[0]],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'foo = my_package.some_module:main_func',
              'bar = other_module:some_func',
              'epoch = incolumepy.teste.epoch:epoch ',
          ],
          'gui_scripts': [
              'baz = my_package_gui:start_func',
          ],
      },

      # entry_points="""
      ## -*- Entry points: -*-

      # [distutils.setup_keywords]
      ##paster_plugins = setuptools.dist:assert_string_list

      # [egg_info.writers]
      ##paster_plugins.txt = setuptools.command.egg_info:write_arg
      # """,
      # paster_plugins = [''],
      test_suite='test',
      )
