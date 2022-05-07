from setuptools import setup


setup(
    name='module',
    version='1.0.0',
    description='A module metaclass, to make your classes into modules.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/megawidget/python-module',
    author='Igor Kaplounenko',
    author_email='megawidget@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=['module'])
