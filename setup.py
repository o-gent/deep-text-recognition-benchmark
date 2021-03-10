import setuptools
import os

version = '1.0'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    LongDescription = f.read()

setuptools.setup(
    name='deeptext',
    zip_safe=True,
    version=version,
    description='OCR',
    long_description_content_type="text/markdown",
    long_description=LongDescription,
    url='https://github.com/o-gent/deeptext',
    author='ogent',
    install_requires=[
        "torch"
    ],
    author_email='ogent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
    license='apache',
    packages=setuptools.find_packages()
)
