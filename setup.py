from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(packages=find_packages(),
    name="hccpy-navina",
    version="0.2.3",
    description="hccpy_navina navina fork",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yubin Park",
    author_email="yubin.park@gmail.com",
    url="https://github.com/yubin-park/hccpy",
    license="Apache 2.0", 
    install_requires = ["numpy"],
    include_package_data=True,
    package_data={"hccpy_navina": ["data/*.TXT", "data/*.txt", "data/*.csv", "data/*.json"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ])


