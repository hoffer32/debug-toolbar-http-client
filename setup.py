import os
from setuptools import setup

license = ""

if os.path.isfile("LICENSE"):
    with open('LICENSE') as f:
        license = f.read()

readme = ""

if os.path.isfile("README.md"):
    with open("README.md") as f:
        readme = f.read()


setup(
    zip_safe=False,
    name='django-debug-toolbar-http-client',
    version='0.93',
    packages=['http_client_panel', 'http_client_panel.panels'],
    package_data={'': ['templates/*']},
    url='https://github.com/hoffer2github/debug-toolbar-http-client',
    license=license,
    author='Hoffer',
    author_email='mhf.hust@gmail.com',
    description='A django-debug-toolbar panel that shows you http client request record',
    install_requires=['django-debug-toolbar>=1.0', 'vcrpy==1.10.4'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Debuggers'],

    long_description=readme,
)
