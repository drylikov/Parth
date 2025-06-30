import io
from os import path
from setuptools import setup, find_packages

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='parth',
    version=__import__('parth').__version__,
    description='Heuristics based vulnerable parameter scanner',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='drylikov',
    license='',
    url='https://github.com/drylikov/parth',
    download_url='https://github.com/drylikov/parth/archive/v%s.zip' % __import__(
        'parth').__version__,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Topic :: Security',
        'Operating System :: OS Independent',
        'License :: ',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'parth = parth.parth:main'
        ]
    },
    keywords=['hacking', 'vulnerability', 'security', 'scanning', 'pentesting']
)