from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Anime-recommenders",
    version="0.1",
    author='devendra',
    packages=find_packages(),
    install_requires = requirements,
)