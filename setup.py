from setuptools import setup, find_packages

setup(
    name="janlp",
    version="0.0.1",
    description="My preprocessing scripts for Japanese NLP",
    long_description="My preprocessing scripts for Japanese NLP",
    license="MIT",
    url="https://github.com/kanjirz50/janlp",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["mecab-python3>=0.7", "regex>=2018"],
    dependency_links=[],
    python_requires='~=3.3',
)