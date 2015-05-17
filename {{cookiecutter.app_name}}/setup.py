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
    name='{{ cookiecutter.app_name }}',
    version='0.0.0',
    install_requires=[],
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    keywords='{{ cookiecutter.app_name }}',
    description=description,
    long_description=long_description,
    download_url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/tarball/master',
    packages=['{{ cookiecutter.app_name }}'],
    package_dir={'{{ cookiecutter.app_name }}': '{{ cookiecutter.app_name }}'},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
