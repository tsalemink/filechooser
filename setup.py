import codecs
import os
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# The dependencies variable is used by MAP Client to
# determine if further downloads are required.  Please
# list all dependencies here.
dependencies = ['mapclient', 'PySide2']  # Insert plugin dependencies here

setup(
    name=u'mapclientplugins.multiplefilechooserstep',
    version=find_version("mapclientplugins", "multiplefilechooserstep", "__init__.py"),
    description='',
    long_description="",
    classifiers=[],
    author=u'Hugh Sorby',
    author_email='',
    url='',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', ]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)
