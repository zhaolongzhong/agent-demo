from setuptools import setup, find_packages

setup(
    name='agent-demo',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'agent-demo = main:main',
        ],
    },
)