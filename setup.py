"""PyPI Setup For Audire Package"""

import os
import re
import setuptools


def _read(filename, version=False):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf8") as file:
        text = file.read()
    if version:
        return re.search(r'__version__ = "(.*?)"', text).group(1)
    return text


setuptools.setup(
    name="Audire",
    packages=setuptools.find_packages(),
    version=_read("audire/__init__.py", version=True),
    license="MIT",
    description="A Package to search and get download links for songs from various platforms asynchronously.",
    long_description=_read("README.md"),
    long_description_content_type="text/markdown",
    author="Eren",
    author_email="linuxguy312@segfault.net",
    url="https://github.com/LinuxGuy312/Audire",
    keywords=["songs", "song", "music", "youtube", "ytm", "Audire", "audire"],
    install_requires=["aiohttp", "bs4"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires="~=3.7",
)
