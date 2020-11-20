from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

required = ['sphinx']

__version__ = 'init'
exec(open('megadoc/version.py').read())

setup(
    name='megadoc',
    packages=find_packages(),
    version=__version__,
    description="Documentation of all commanands/ techniques that I used.",
    author='Yann HALLOUARD',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires=['pytest-runner', 'wheel', 'flake8'],
    tests_require=['pytest', 'pytest-cov', 'treon'],
    install_requires=required,
    license='TOTAL - TDF',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
)
