import os


def watch(directory=None):
    """Starts a server to render the specified file or directory containing a README."""
    if directory and not os.path.isdir(directory):
        raise ValueError('Directory not found: ' + directory)
    directory = os.path.abspath(directory)

    print ' * Watching', directory

    # TODO: implement
    raise NotImplementedError()
