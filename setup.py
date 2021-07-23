from setuptools import setup, find_packages

version = "1.1.1"

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.readlines()

setup(
    name="javascriptpy",
    version=version,
    description="This package lets you use Javascript like objects in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Swas.py",
    author_email="cwswas.py@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
    url = "https://github.com/CodeWithSwastik/javascript-py", 
    project_urls={
    "Issue tracker": "https://github.com/CodeWithSwastik/javascript-py/issues",
    },
)
