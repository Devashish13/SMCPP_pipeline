from setuptools import setup, find_packages

setup(
    name="smcpp_pipeline",
    version="0.1",
    author="Devashish Tripathi",
    author_email="devashishtripathi697@gmail.com",
    description="A python pipeline for implementing smcpp package to decipher demographic history of populations",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.5",
        "pandas>=1.0.5",
        # Add any other package dependencies you need
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
