from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='comdexpy',
    version='0.0.2',
    packages=['comdexpy', 'comdexpy.interfaces'],
    url='https://github.com/algo-vaultstaking/comdexpy',
    license='MIT',
    author='AlgoRhythm',
    author_email='',
    description='Tools for Comdex wallet management, offline transaction signing and broadcasting',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'ecdsa',
        'bech32',
        'hdwallets',
        'mnemonic',
        'typing-extensions',
        'requests'
      ],
    zip_safe=False,
)
