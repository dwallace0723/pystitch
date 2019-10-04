import os
from setuptools import setup, find_packages
import codecs

__version__ = None
exec(open("pystitch/version.py").read())

here = os.path.abspath(os.path.dirname(__file__))

long_description = ""
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="pystitchconnect",
    version=__version__,
    description="Python SDK for Stitch Connect API.",
    keywords="stitch",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/dwallace0723/pystitch",
    author="David Wallace",
    author_email="dwallace0723@gmail.com",
    packages=find_packages(),
    install_requires=[
        'requests>=2.22.0',
        'pytz==2019.2'
    ],
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
