Nosey -- Local continuous test runner with nose and watchdog
============================================================

Nosey a command-line application for continuously running your Python tests
with nose. Any changes are immediately detected and trigger a re-run of
your tests. Nosey lets you know when you've broken your local build
and gives a detailed report when you've broken any of your tests.


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
