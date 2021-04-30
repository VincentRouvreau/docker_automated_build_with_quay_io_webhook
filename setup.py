# package was structured accordingly to https://docs.python-guide.org/writing/structure/
# setup.py was copied from https://packaging.python.org/tutorials/packaging-projects/
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sample",
    version="0.0.1",
    author="Vincent Rouvreau",
    author_email="vincent.rouvreau@inria.fr",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VincentRouvreau/dockerhub_automated_build",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    # https://python-packaging.readthedocs.io/en/latest/dependencies.html
    install_requires=[
        'numpy',
    ],
)