from setuptools import setup

setup(
    name='ff_bot',

    packages=['ff_bot'],

    include_package_data=True,

    version='0.6.9',

    description='ESPN fantasy Basketball Chat Bot',

    author='OneLemonyBoi',

    author_email='noemail@gmail.com',

    install_requires=['requests>=2.0.0,<3.0.0', 'espn_api==0.9.0', 'apscheduler>3.0.0'],

    test_suite='nose.collector',

    tests_require=['nose', 'requests_mock'],

    url='https://github.com/OneLemonyBoi/fantasy_football_chat_bot/',

    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
