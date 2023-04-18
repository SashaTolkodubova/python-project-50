from setuptools import find_packages, setup
setup(
    name='gendiff',
    packages=find_packages(include=['gendiff']),
    version='0.1.0',
    description='Generate difference',
    author='Me',
    license='MIT',
    install_requires=['pyyaml==6.0'],
)
