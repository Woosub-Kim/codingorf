from setuptools import setup, find_packages

setup(
    name = 'codingorf',
    version = 'v1.0.0',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'codingorf = codingorf.__main__:main'
        ]
    })
