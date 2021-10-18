from setuptools import setup, find_packages

# The dependencies variable is used by MAP Client to
# determine if further downloads are required.  Please
# list all dependencies here.
dependencies = ['mapclient', 'PySide2']  # Insert plugin dependencies here

setup(
    name=u'mapclientplugins.multiplefilechooserstep',
    version='0.0',
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
