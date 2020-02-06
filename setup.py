from setuptools import setup, find_packages

setup(
    name='django-hero-admin',
    version=__import__('django-hero-admin').VERSION,
    description='Theme for Django admin interface using Semantic UI.',
    author='Ilya Karpuk (Perkovec)',
    author_email='perkovec24@gmail.com',
    url='https://github.com/Perkovec/django-hero-admin',
    packages=find_packages('django-hero-admin'),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Environment :: Web Environment',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ]
)