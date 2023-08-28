from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md'), encoding='utf-8').read()

version = '0.1.0'

setup(
    name='subresync',
    version=version,
    author='XiNGRZ',
    author_email='hi@xingrz.me',
    description='A simple Python remaster of the VobSub SubResync',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/xingrz/subresync.py',
    license='MIT',
    packages=find_packages(),
    scripts=['bin/subresync'],
    install_requires=[
        'pyass>=0.1.2',
    ],
)
