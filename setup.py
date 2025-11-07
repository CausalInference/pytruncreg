from setuptools import setup, find_packages

setup(
    name='pytruncreg',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pandas'
    ],
    author='Ryan ODea',
    author_email='ryan.odea@psi.ch',
    description='Truncated Gaussian Regression Models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/CausalInference/pytruncreg'
)
