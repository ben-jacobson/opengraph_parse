import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opengraph_parse", 
    version="0.0.2",
    author="Ben Jacobson",
    author_email="ben_jacobson@live.com",
    description="Parses Open Graph meta tags of web pages and returns a handy JSON-like object. Use this to generate preview of web pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ben-jacobson/opengraph_parse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
