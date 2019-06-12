import os
import subprocess
import sys
from setuptools import setup, find_packages, Command

__version__ = None
exec(open("pystitch/version.py").read())

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    README = f.read()


class BaseCommand(Command):
    """Base Command"""

    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def _run(self, s, command):
        try:
            self.status(s + "\n" + " ".join(command))
            subprocess.check_call(command)
        except subprocess.CalledProcessError as error:
            sys.exit(error.returncode)


class ValidateCommand(BaseCommand):
    """Support setup.py validate."""

    description = "Run Python static code analyzer (flake8) and formatter (black)."

    def run(self):
        self._run(
            "Installing test dependencies…",
            [sys.executable, "-m", "pip", "install"] + tests_require,
        )
        self._run("Running black…", [sys.executable, "-m", "black", f"{here}/slack"])
        self._run("Running flake8…", [sys.executable, "-m", "flake8", f"{here}/slack"])


class UploadCommand(BaseCommand):
    """Support setup.py upload. Thanks @kennethreitz!"""

    description = "Build and publish the package."

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self._run(
            "Building Source and Wheel (universal) distribution…",
            [sys.executable, "setup.py", "sdist", "bdist_wheel", "--universal"],
        )

        self._run(
            "Installing Twine dependency…",
            [sys.executable, "-m", "pip", "install", "twine"],
        )

        self._run(
            "Uploading the package to PyPI via Twine…",
            [sys.executable, "-m", "twine", "upload", "dist/*"],
        )

        self._run("Creating git tags…", ["git", "tag", f"v{__version__}"])
        self._run("Pushing git tags…", ["git", "push", "--tags"])


setup(
    name="pystitch",
    version=__version__,
    description="Python SDK for Stitch Connect API.",
    keywords="stitch",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/dwallace0723/pystitch",
    author="David Wallace",
    author_email="dwallace0723@gmail.com",
    packages=find_packages(),
    install_requires=[
        'requests>=2.22.0'
    ],
    tests_require=["flake8", "black"],
    cmdclass={"upload": UploadCommand, "validate": ValidateCommand},
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
