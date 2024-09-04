from setuptools import setup, find_packages

setup(
    name="unipkg",
    version="0.1.0",
    author="Evan Fosmark",
    author_email="evan@makermix.com",
    description="A unified API for various package managers.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/efosmark/unipkg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[ ],
    entry_points={ },
)
