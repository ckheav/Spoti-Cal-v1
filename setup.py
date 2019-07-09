from setuptools import setup, find_packages


requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]


setup(
    name='flask_todo',
    version='0.0',
    description='a spotify user music tracker built with flask',
    author='<Kamtochukwu Okafor>',
    author_email='<kamto1.okafor@gmail.com>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
