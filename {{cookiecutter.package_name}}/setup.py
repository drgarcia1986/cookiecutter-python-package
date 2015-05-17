# -*- coding: utf-8 -*-
from setuptools import setup


def read(fname):
    """ Return file content. """
    with open(fname) as f:
        content = f.read()

    return content


description = '{{ cookiecutter.project_short_description }}'
try:
    long_description = read('README.md')
except:
    long_description = description


setup(
    name='{{ cookiecutter.package_name }}',
    version='0.0.0',
    install_requires=[],
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    keywords='{{ cookiecutter.package_name }}',
    description=description,
    long_description=long_description,
    download_url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.package_name}}/tarball/master',
    packages=['{{ cookiecutter.package_name }}'],
    package_dir={'{{ cookiecutter.package_name }}': '{{ cookiecutter.package_name }}'},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
