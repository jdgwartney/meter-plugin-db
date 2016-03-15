from distutils.core import setup

setup(
    name='tspetl',
    version='0.1.0',
    url="http://github.io/boundary/meter-plugin-db",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['tspetl', ],
    scripts=[
    ],
    package_data={'tspetl': ['templates/*']},
    license='LICENSE',
    entry_points={
        'console_scripts': [
            'tsp-etl = tspetl.etl_cli:main',
         ],
    },
    description='TrueSight Pulse Database Extractor',
    long_description=open('README.txt').read(),
    install_requires=[
       'tspapi',
    ],
)
