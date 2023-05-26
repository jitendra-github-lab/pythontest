import setuptools
from distutils.text_file import TextFile
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED = TextFile(filename=str(Path(__file__).with_name("requirements.txt"))).readlines()

setuptools.setup(
    name='jeet',
    version='0.0.1',
    author='Jitenra Thakur',
    author_email='jitendra@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jitendra-github-lab/pythontest',
    project_urls = {
        "Bug Tracker": "https://github.com/jitendra-github-lab/pythontest/issues"
    },
    license='MIT',
    packages=['jeettest'],
    install_requires=[REQUIRED],
)