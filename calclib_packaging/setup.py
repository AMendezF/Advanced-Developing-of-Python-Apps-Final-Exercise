from setuptools import setup, find_packages

setup(
    name='calclib',
    version='1.0',
    author='Alejandro Mendez Fernandez',
    author_email='name@domain.com',
    #package_dir={'': 'src'},
    #packages=find_packages(where='src'),
    packages=['calclib'],
    test_suite='nose.collector',
    tests_require=['nose'],
    url='https://name.domain',
    license='GNU-3',
    description='Contains a float vector calculator with safe input check.',
    long_description=open('README.rst').read(),
    python_requires='>=3.7.*',
    install_requires=[]
)
