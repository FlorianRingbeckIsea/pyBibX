from setuptools import setup, find_packages
from pathlib import Path
from Cython.Build import cythonize
import numpy

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='pyBibX',
    version='3.2.8',
    license='GNU',
    author='Valdecy Pereira',
    author_email='valdecy.pereira@gmail.com',
    url='https://github.com/Valdecy/pyBibX',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'bertopic',
        'bert-extractive-summarizer',
        'chardet',
        'llmx',
        'matplotlib',
        'networkx',
        'numpy',
        'pandas',
        'plotly',
        'scipy',
        'scikit-learn',
        'sentencepiece',
        'sentence-transformers',
        'squarify',
        'torch', 
        'torchvision',
        'torchaudio',
        'transformers',
        'umap-learn',
        'openai',
        'wordcloud',
        'Cython'
    ],
    zip_safe=True,
    description='A Bibliometric and Scientometric Library Powered with Artificial Intelligence Tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
     ext_modules=cythonize(
        "pyBibX/base/helpers.pyx", compiler_directives={"language_level": "3"}
    ),
    include_dirs=[numpy.get_include()],
)
