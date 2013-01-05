import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeHandler(FileSystemEventHandler):
    """Listens for changes to files and re-runs tests after each change."""
    def __init__(self, directory=None):
        super(ChangeHandler, self).__init__()
        self.directory = os.path.abspath(directory or '.')

    def on_any_event(self, event):
        if event.is_directory:
            return
        self.run()

    def run(self):
        """Called when a file is changed to re-run the tests with nose."""
        print
        print 'Running unit tests...'
        subprocess.call('nosetests', cwd=self.directory)


def watch(directory=None):
    """Starts a server to render the specified file or directory containing a README."""
    if directory and not os.path.isdir(directory):
        raise ValueError('Directory not found: ' + directory)
    directory = os.path.abspath(directory)

    # Initial run
    event_handler = ChangeHandler()
    event_handler.run()

    # Setup watchdog
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=True)
    observer.start()

    # Watch and run tests until interrupted by user
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
