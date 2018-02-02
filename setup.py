"setup script"

from setuptools import setup, find_packages


setup(
    name="fredhutch_batch_wrapper",
    version="0.1",
    packages=find_packages(),
    install_requires=['boto3>=1.5.22', 'requests>=2.18.4'], # FIXME uncomment
    include_package_data=True,
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
