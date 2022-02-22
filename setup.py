from setuptools import find_packages, setup
setup(
    name='szkopulpylib',
    packages=find_packages(include=['szkopulpylib']),
    version='0.0.1',
    description='szkopulpylib',
    author='Ignac_pro_69',
    license='MIT',
    install_requires=['requests','bs4'],
    setup_requires=['pytest-runner'],
)