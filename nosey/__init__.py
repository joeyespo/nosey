"""\
Nosey
-----

Local continuous test runner with nose and watchdog.

:copyright: (c) 2012 by Joe Esposito.
:license: MIT, see LICENSE for more details.
"""

__version__ = '0.1.0'


from . import command
from .watcher import watch
