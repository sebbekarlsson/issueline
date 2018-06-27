from setuptools import setup, find_packages


setup(
    name='issueline',
    version='1.0',
    install_requires=[
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'issueline = issueline.bin:run'
        ]
    }
)
