import os
from setuptools import setup
from setuptools import find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lti_analytics',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='TBD License',  # example license
    description='Adds collection of usage data for LTI tools',
    long_description=README,
    url='http://canvas.harvard.edu/',
    author='Douglas Hall',
    author_email='douglas_hall@harvard.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.8,<1.9',
        'psycopg2==2.6.1',
        'django-pgjson==0.3.1'
    ]
)
