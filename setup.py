#!/usr/bin/env python3

"setup script"

from setuptools import setup, find_packages


setup(
    name="fredhutch_batch_wrapper",
    version="0.5",
    packages=find_packages(),
    install_requires=['boto3', 'requests'],
    author='Dan Tenenbaum',
    author_email='dtenenba@fredhutch.org',
    description='Fred Hutch Wrapper for AWS Batch',
    license='MIT',
    url='https://github.com/FredHutch/fredhutch_batch_wrapper',

    entry_points={
        'console_scripts': [
            'batchwrapper = fredhutch_batch_wrapper.cmdline:cmdline'
        ]
    }
)
