from setuptools import setup

setup(
    name='some_app',
    version='0.0.1',
    description='Some App',
    author='devnine99',
    author_email='devnine99@gmail.com',
    url='https://github.com/devnine99',
    license='MIT',
    python_requires='>=3',
    install_requires=['kafka-python'],
    py_modules=['some_app'],
    packages=['some_app'],
)
