import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="electricity_exchange",
    version="0.0.1",
    author="Khushboo Goyal",
    author_email="kgoyal@tcd.ie",
    description="Meshup of Github and twitter api",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
