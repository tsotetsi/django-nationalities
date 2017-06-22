from setuptools import setup

from nationalities import __version__


version_str = "".join(str(n) for n in __version__)

CLASSIFIERS = [
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Environment :: Web Environment',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
]

setup(
    name='django-nationalities',
    description='django nationalities.',
    long_description='Django nationalities',
    version=version_str,
    packages=['nationalities'],
    include_package_data=True,
    zip_safe=False,
    author='Thapelo Tsotetsi',
    author_email='info@thapelotsotetsi.co.za',
    url="https://github.com/tsotetsi/django-nationalities",
    license='MIT',
    keywords='django nationalities',
    classifiers=CLASSIFIERS,
)
