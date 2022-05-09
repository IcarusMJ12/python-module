from setuptools import setup


setup(
    name='modulemeta',
    version='0.2.0a1',
    description='A Module metaclass, to make your classes into modules.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/megawidget/python-module',
    author='Igor Kaplounenko',
    author_email='megawidget@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.5',
    packages=['modulemeta'])
