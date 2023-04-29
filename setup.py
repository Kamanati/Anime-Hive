from setuptools import setup, find_packages

setup(
    name='anime-hive',
    version='0.1.0',
    description='Simple Tool To get All anime Details No Mater the circumstances Grap each and every details and has Filter Options',
    author='HasanFq',
    author_email='hasanfq818@mail.com',
    url='https://github.com/Kamanati/Anime-Hive',
    packages=find_packages(),
    install_requires=[
        'bs4',
        'pyfiglet',
        'termcolor',
    # other options...
    entry_points={
        'console_scripts': [
            'anime-hive = anime-hive.main:main'

    ],
)

