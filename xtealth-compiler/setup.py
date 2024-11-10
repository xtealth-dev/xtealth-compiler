from setuptools import setup, find_packages

setup(
    name='XTEALTH-Compiler',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # List any Python dependencies here
        'numpy',  # Example: If your compiler needs NumPy
    ],
    include_package_data=True,
    package_data={
        '': ['xtealth-compiler/src/*.py', 'xtealth-compiler/include/*.h', 'xtealth-compiler/cmake/*.txt'],  # Add other data files you need
    },
    entry_points={
        'console_scripts': [
            'xtealth-compiler=xtealth.compiler:main',  # Adjust according to the entry point in your main module
        ],
    },
    author='XTEALTH',
    author_email='contact@xtealthglobal.com',
    description='XTEALTH Compiler - A powerful cross-platform programming language compiler.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xtealth-dev',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
)

