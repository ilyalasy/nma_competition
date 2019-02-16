from setuptools import setup, find_packages

setup(
    name="src",
    version="1.0",
    author="Ilya Lasy",
    packages=find_packages(),
    install_requires=[
        'numpy', 'pandas', 
        'scikit-learn', 
    ]
)