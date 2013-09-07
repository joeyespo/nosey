"""\
Nosey
-----

Local continuous test runner with nose and watchdog.


Nosey is easy to set up
```````````````````````

::

    $ pip install nosey
    $ cd myproject
    $ nosey
     * Watching /path/to/myproject


Links
`````

* `Website <http://github.com/joeyespo/nosey>`_

"""

import os
import sys
from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    sys.exit(os.system('python setup.py sdist upload'))


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='nosey',
    version='0.1.2',
    description='Local continuous test runner with nose and watchdog.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/nosey',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    install_requires=read('requirements.txt'),
    zip_safe=False,
    entry_points={'console_scripts': ['nosey = nosey.command:main']},
)
