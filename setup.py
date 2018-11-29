# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='melodia',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.0',

    description='Generates a midi file from existing wav file',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/justinsalamon/melodia',

    # Author details
    author='Justin Salamon',

    # Choose your license
    license='Apache',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='melodia midi',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['joblib==0.11', 'mir_eval==0.4', 'librosa==0.5.1', 'midiutil==1.2.1', 'vamp==1.1.0', 'jams==0.3.1',
                      'numpy==1.13.1', 'scipy==0.19.1'],


    entry_points={
        'console_scripts': [
            'audio_to_midi_melodia=melodia:main',
        ],
    },
)
