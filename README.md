Nosey -- Local continuous test runner
=====================================

Nosey a zero-config command-line application that watches your Python project
for changes with [Watchdog][] and runs your tests with [nose][].

With Nosey you know right away when you've broken the build, and how.


Installation
------------

To install nosey, simply:

```bash
$ pip install nosey
```


Usage
-----

The common use case is to let Nosey run in its own terminal window:

```bash
$ cd myproject
$ nosey
 * Watching /path/to/myproject
```

Now happily develop as usual, checking the terminal every now and
then to see if you've broken anything.


Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository
3. Send a pull request


[nose]: http://nose.readthedocs.org
[watchdog]: http://packages.python.org/watchdog
