from setuptools import setup

setup(
    name='owping-parser',
    version='0.0.1',
    description='A program to parse the output of owping',
    url='https://github.com/mirgleich/owping-parser',
    license='',  # TODO: license
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Topic :: System :: Networking',
        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',
        # TODO: License
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    py_modules=['owping'],
    keywords='owping network ping',
    project_urls={
        'Tracker': 'https://github.com/mirgleich/owping-parser/issues',
        'Source': 'https://github.com/mirgleich/owping-parser',
    },
    python_requires='>=3',
)
