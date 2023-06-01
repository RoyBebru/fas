from setuptools import setup


setup(name='fig',
    python_requires='>=3.8',
    version='0.0.2',
    description='File Associations and Sorter (FAS)',
    url='https://github.com/RoyBebru/fas',
    author='Roy Bebru',
    author_email='RoyBebru@Gmail.Com',   ### Script Name After Installation
    license='MIT',                       #     ### Import module which must be called
    include_package_data=True,           #     #       ### Function call from module
    packages=["fas"],                    #     #       #
    entry_points = {'console_scripts': 'fas = fas.fas:main'})
