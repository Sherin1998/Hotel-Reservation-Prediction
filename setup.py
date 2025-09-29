"""
Setup script for MLOPS-PROJECT-1.
"""

from setuptools import setup, find_packages

# Read line by line from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-1",
    version="0.1",
    author="Sherin",
    packages=find_packages(),
    install_requires=requirements,
)
