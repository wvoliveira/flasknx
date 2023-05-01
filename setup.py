import io
import re

from setuptools import setup


setup(
    name='flasknx',
    version='0.0.1',
    url='https://github.com/wvoliveira/flasknx',
    author='Wellington Oliveira',
    author_email='oliveira@live.it',
    python_requires='>=3.5',
    install_requires=[
        'Flask==2.3.2',
        'Flask-RESTful==0.3.7',
        'prometheus-flask-exporter==0.9.1',
        'py-healthcheck==1.9.0',
        'uwsgi==2.0.18'
    ],
    extras_require={
        'dev': [
            'pytest',
            'coverage'
        ]
    }
)
