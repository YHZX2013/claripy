try:
    from setuptools import setup
    from setuptools import find_packages
    packages = find_packages()
except ImportError:
    from distutils.core import setup
    import os
    packages = [x.strip('./').replace('/','.') for x in os.popen('find -name "__init__.py" | xargs -n1 dirname').read().strip().split('\n')]

setup(
    name='claripy',
    version='8.18.10.25',
    packages=packages,
    install_requires=[
        'ana',
        'z3-solver==4.5.1.0.post2',
        'future',
    ],
    description='An abstraction layer for constraint solvers',
    url='https://github.com/angr/claripy',
)
