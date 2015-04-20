import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-mailmangler',
    version='0.1.0',
    description=(
        'Template tags to weakly obfuscate an email behind JavaScript or '
        'a CAPTCHA (a reCAPTCHA)'),
    author='Nick Timkovich',
    author_email='prometheus235@gmail.com',
    license='MIT',
    keywords='captcha mailhide django',

    packages=['mailmangler'],
    install_requires=[
        'recaptcha-client',
        'pycrypto',
    ],

    long_description=read('README.rst'),
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
    ]
)
