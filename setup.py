from gettext import install
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mergepdfs", 
    version="0.9.1",
    author="Isabel Sandstrøm, Terje Sandstrom,",
    author_email="isabel@hermit.no",
    description="Python command line program for merging multiple PDF-files to one PDF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HermitAS/mergepdfs",
    packages=['pdfmerger'],
    install_requires=['PyPDF2>=1.26.0'],
    entry_points={'console_scripts': ['mergepdfs = pdfmerger.mergepdfs:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)                                
