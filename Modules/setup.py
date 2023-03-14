from setuptools import setup

setup(
    name='KaggleModule',
    version='0.0.2',    
    description='All tools used for Anders\' kaggle work. Not intended to be used as is by anyone else. as of right now.',
    url='https://github.com/ahll19/Kaggle-Projects',
    author='Anders Højbak Lysgaard Lauridsen',
    author_email='anders.hl.lauridsen@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007',
    packages=['visualizer'],
    install_requires=['pandas',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.11',
    ],
)
