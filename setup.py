import runpy
from pathlib import Path

from setuptools import setup, find_packages

classifiers = '''Development Status :: 3 - Alpha
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10'''

name = 'amid'
root = Path(__file__).resolve().parent
with open(root / 'requirements.txt', encoding='utf-8') as file:
    requirements = file.read().splitlines()
with open(root / 'README.md', encoding='utf-8') as file:
    long_description = file.read()
version = runpy.run_path(root / name / '__version__.py')['__version__']

setup(
    name=name,
    packages=find_packages(include=(name,)),
    include_package_data=True,
    version=version,
    description='A curated list of medical imaging datasets with unified interfaces',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/neuro-ml/amid',
    download_url='https://github.com/neuro-ml/amid/archive/v%s.tar.gz' % version,
    keywords=['medical imaging', 'dataset'],
    classifiers=classifiers.splitlines(),
    install_requires=requirements,
    python_requires='>=3.6',
)
