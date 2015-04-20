from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-mailmangler',
    version='0.1.0',

    description=(
        'Template tags to weakly obfuscate an email behind JavaScript or '
        'a CAPTCHA (a reCAPTCHA)'),
    long_description=long_description,

    url='https://github.com/nicktimko/django-mailmangler',

    author='Nick Timkovich',
    author_email='prometheus235@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],

    keywords='captcha recaptcha mailhide django',

    packages=['mailmangler'],

    install_requires=[
        'recaptcha-client',
        'pycrypto',
    ],
)
