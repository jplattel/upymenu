from setuptools import setup, find_packages
import sdist_upip

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="upymenu",
    version="0.0.1",
    author="Joost Plattel",
    description="A micropython Menu for LCD Displays",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jplattel/upymenu",
    packages=find_packages(),
    cmdclass={'sdist': sdist_upip.sdist}
)