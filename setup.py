from io import open

from setuptools import find_packages, setup

with open('celery_resource_autoscaler/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '1.0.0'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='celery-resource-autoscaler',
    version=version,
    description='Celery plugin to autoscale based on available CPU, memory, or other system attributes.',
    long_description=readme,
    author='Jack Cushman, Travis Johnson',
    author_email='jcushman@law.harvard.edu, travis.johnson2@halliburton.com',
    maintainer='Jack Cushman',
    maintainer_email='jcushman@law.harvard.edu',
    url='https://github.com/jcushman/celery-resource-autoscaler',
    license='MIT',
    keywords=['celery', 'autoscale', 'scale', 'cpu'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=['celery', 'psutil'],
    extras_require={
        'test': ['coverage', 'pytest', 'mock'],
    },
    packages=find_packages(),
)
