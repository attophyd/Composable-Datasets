from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("setup-requirements.txt", "r") as req_file:
    install_requires = req_file.read().splitlines()

setup(
    name="composable_datasets",
    version="0.1.0",
    author="attophyd",
    author_email="attophyd@gmail.com",
    description="A library for composable shortcuts for HF datasets library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/attophyd/composable-datasets",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
