from setuptools import setup, find_packages

setup(
    name="code-formatter-pro-csharp-20260531_041712",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'code=code:main',
        ],
    },
)
