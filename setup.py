from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Anime-Hive',
  version='0.0.1',
  description='Simple Tool To get All anime Details No Mater the circumstances Grap each and every details and has Filter Options',
  url='',  
  author='hasanfq',
  author_email='hasanfq818@mail.com,
  license='MIT', 
  classifiers=classifiers,
  
  packages=find_packages(),
  install_requires=['bs4,pyfiglet,termcolor'] 
)
