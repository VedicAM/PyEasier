from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Making your python experience better'

# Setting up
setup(
    name="PyEasiest",
    version=VERSION,
    author="Yellow Yams(Vedic Mukherjee)",
    author_email="<yellowyams5@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['py2app', 'pyinstaller'],
    keywords=['python', 'PyEasiest', 'quick code', 'fast development', 'easy to use', 'build'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

