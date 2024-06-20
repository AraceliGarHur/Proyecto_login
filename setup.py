
from setuptools import setup, find_packages

setup(
    name='proyecto_login',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'proyecto_login = proyecto_login.main:main'
        ]
    },
    author='Araceli García Hurtado',
    author_email='araceligh1997@gmail.com',
    description='Paquete para gestionar login de usuarios',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url= 'https://github.com/AraceliGarHur/Proyecto_login',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

 