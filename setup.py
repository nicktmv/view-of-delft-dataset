"""
Setup file for the Xinshuo's Python Toolbox package.
"""

from setuptools import find_packages, setup
setup(
    name="view-of-delft-dataset",
    version="1.0.0",
    author="TU Delft Intelligent Vehicles",
    author_email="no-reply@intelligent-vehicles.org",
    description="This repository shares the documentation and development kit of the View of Delft automotive dataset.",
    long_description=open("readme.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tudelft-iv/view-of-delft-dataset.git",
    packages=find_packages(include=['vod', 'vod.*']),
    install_requires=[
        'k3d==2.16.1',
        'matplotlib==3.8.2',
        'numba==0.59.0',
        'numpy==1.24.3'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

