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
    author='<Your actual name here>',
    author_email='<Your actual e-mail address here>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
