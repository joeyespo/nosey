"""\
nosey.command
~~~~~~~~~~~~~

Implements the command-line interface for Nosey.


Usage:
  nosey [options] [<directory>]

Options:
  -h --help         Show this help.
  --version         Show version.
"""

import sys
from docopt import docopt
from .watcher import watch
from . import __version__


def main(argv=None):
    """The entry point of the application."""
    if argv is None:
        argv = sys.argv[1:]
    usage = '\n\n\n'.join(__doc__.split('\n\n\n')[1:])
    version = 'Nosey ' + __version__

    # Parse options and execute
    args = docopt(usage, argv=argv, version=version)
    return watch(args['<directory>'])
