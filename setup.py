# Copyright (c) 2021 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

import os

import setuptools


project_name = "style_doc"
keywords = "automation formatter formatting docstring rst reStructuredText black"
install_requires = []
extras_require = {
    "checking": ["black", "flake8", "isort", "mdformat"],
    "optional": [],
    "testing": [],
}


def get_version():
    """Read version from ``__init__.py``."""
    version_filepath = os.path.join(os.path.dirname(__file__), project_name, "__init__.py")
    with open(version_filepath) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.strip().split()[-1][1:-1]
    assert False


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=project_name,
    version=get_version(),
    maintainer="Philip May",
    author="Philip May",
    author_email="philip.may@t-systems.com",
    description="Black for Python docstrings and reStructuredText (rst)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/telekom/style-doc",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=install_requires,
    extras_require=extras_require,
    keywords=keywords,
    entry_points={"console_scripts": ["style-doc = style_doc:cli_main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
