"""
A demosite with oscarapi for demo and documentation purposes
"""
from setuptools import setup, find_packages
import os

__version__ = "0.0.1"

setup(
    name='bookstore',
    version=__version__,
    description="Oscar API Bookstore site",
    long_description=__doc__,
    classifiers=[],
    keywords='',
    author='Luca Bertuol',
    author_email='paiuolo@gmail.com',
    url='https://github.com/paiuolo/django-oscar-api/bookstore',
    license='Copyright',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-oscar-api',
        'django>=1.9, <1.10',
        'django-oscar>=1.3'
    ],
)
