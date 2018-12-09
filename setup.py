from setuptools import setup

setup(
    name='vs-ip',
    version='0.1',
    url='http://github.com/peppelg/vs-ip',
    author='peppelg',
    author_email='me@peppelg.space',
    license='The Unlicense',
    scripts=['vs-ip.py'],
    install_requires=['splinter'],
    zip_safe=False
)
