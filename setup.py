import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysmashgg",
    version="1.1.5",
    author="Jeremy Skalla",
    author_email="jthroughs@gmail.com",
    description="Python Wrapper for smash.gg's GraphQL API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeremySkalla/SmashGGPythonWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)