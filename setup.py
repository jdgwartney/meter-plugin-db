from distutils.core import setup

setup(
    name='tspdb',
    version='0.1.0',
    url="http://github.io/boundary/meter-plugin-db",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['tspdb', ],
    scripts=[
    ],
    package_data={'tspdb': ['templates/*']},
    license='LICENSE',
    description='TrueSight Pulse Database Extractor',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
