subresync.py [![.github/workflows/build.yml](https://github.com/xingrz/subresync.py/actions/workflows/build.yml/badge.svg)](https://github.com/xingrz/subresync.py/actions/workflows/build.yml)
============

[![pypi][pypi-img]][pypi-url] [![downloads][downloads-img]][downloads-url] [![license][license-img]][license-url] [![issues][issues-img]][issues-url] [![stars][stars-img]][stars-url] [![commits][commits-img]][commits-url]

A simple Python remaster of the VobSub SubResync.

## Install

```sh
pip3 install -U subresync
```

## Usage

```sh
# shift all timestamps forward by 100ms
subresync input.ass -o output.ass -s 100

# shift by comparing the source and target timestamp
subresync input.ass -o output.ass -f 0:01:19.400 -t 1:00:24.330
```

## License

[MIT License](LICENSE)

[pypi-img]: https://img.shields.io/pypi/v/subresync?style=flat-square
[pypi-url]: https://pypi.org/project/subresync/
[downloads-img]: https://img.shields.io/pypi/dm/subresync?style=flat-square
[downloads-url]: https://pypi.org/project/subresync/
[license-img]: https://img.shields.io/github/license/xingrz/subresync.py?style=flat-square
[license-url]: LICENSE
[issues-img]: https://img.shields.io/github/issues/xingrz/subresync.py?style=flat-square
[issues-url]: https://github.com/xingrz/subresync.py/issues
[stars-img]: https://img.shields.io/github/stars/xingrz/subresync.py?style=flat-square
[stars-url]: https://github.com/xingrz/subresync.py/stargazers
[commits-img]: https://img.shields.io/github/last-commit/xingrz/subresync.py?style=flat-square
[commits-url]: https://github.com/xingrz/subresync.py/commits/master
