from setuptools import setup


DESCRIPTION = """Uses codap to provide async influxdb"""
setup(
    name='asyncinflux',
    version='0.0.1',
    author='Lateef H. Jackson',
    author_email='lateef.jackson@gmail.com',
    description=(DESCRIPTION),
    license='Apache License V2',
    keywords='influxdb threading gevent eventlet coroutine',
    url='https://github.com/lateefj/asyncinflux',
    packages=['asyncinflux', 'tests'],
    install_requires=[
        'influxdb',
        'codap',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],
)
