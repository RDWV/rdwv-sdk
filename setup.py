from setuptools import find_packages, setup

setup(
    name="rdwv",
    packages=find_packages(exclude=["tests", "tests.*"]),
    version="1.15.0.0",
    license="MIT",
    description="RDWV coins support library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="MrNaif2018",
    author_email="chuff184@gmail.com",
    url="https://github.com/rdwv/rdwv-sdk",
    keywords=["electrum", "daemon", "rdwv", "rdwvcc"],
    install_requires=["jsonrpcclient", "aiohttp<4.0.0", "universalasync"],
    extras_require={"proxy": ["aiohttp_socks"]},
    package_data={"rdwv": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
)
