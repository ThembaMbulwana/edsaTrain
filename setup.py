from setuptools import setup, find_packages

setup(
    name='edsaTrain',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA train - building a python package',
	install_requires=['numpy'],
    long_description=open('README.md').read(),
    url='https://github.com/ThembaMbulwana/edsaTrain',
    author='Themba Mbulwana'
)