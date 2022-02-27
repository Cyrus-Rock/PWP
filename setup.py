from setuptools import setup, find_packages

req = 'requirements.txt'

with open(req, 'r') as f:
    setup(name='programmable_web_project',
        version='1.0',
        packages=find_packages(),
        install_requires=list(map(str.strip, f.readlines()))
        )
