"""The setup script."""

from setuptools import setup, find_packages

with open("README.adoc") as readme_file:
    readme = readme_file.read()

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Sean Marquez",
    author_email="capsulecorplab@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    description="A collection of python scripts for Advent of Code 2019",
    install_requires=["numpy"],
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords="adventofcode2019",
    name="adventofcode2019",
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/code-for-space/adventofcode2019",
    version="0.1.0",
    zip_safe=False,
)
