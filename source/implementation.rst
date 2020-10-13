Implementation
==============

CLI Interface
+++++++++++++
TBD: how to design the cli user and process interface, consider: stdin, stderr, stdout, exit code, signals

User friendlyness
+++++++++++++++++
TBD: Easy to use, good defaults, common case easy, not common possible but hard, Be descriptive (short vs. long options/flags), auto color if tty, ...

Python
++++++

Libaries
--------
* `Click <https://click.palletsprojects.com/en/7.x/>`_
* `Docopt <http://docopt.org/>`_
* `Prompt-Toolkit <https://python-prompt-toolkit.readthedocs.io/en/master/>`_

Talks
-----
* `Docopt talk <https://www.youtube.com/watch?v=pXhcPJK5cMc>`_
* `Writing Awesome Command-Line Programms in Python <https://www.youtube.com/watch?v=gR73nLbbgqY>`_
* `Aweseom command line tools in python (repl) <https://www.youtube.com/watch?v=hJhZhLg3obk>`_
* `Lets make better command line applications <https://www.youtube.com/watch?v=ubXXmQzzNGo>`_


Ruby
++++
If you want to learn or read about more details on how to create great command line tools using ruby,
I highly recommend you read this * `Book <https://pragprog.com/book/dccar/build-awesome-command-line-applications-in-ruby>`_,
it covers the topic exhaustively.

Talks
-----
* `Make awesome command line apps with ruby <https://www.youtube.com/watch?v=1ILEw6Qca3U>`_

References
----------
* `Build Awesome Command-Line Applications in Ruby <https://pragprog.com/book/dccar/build-awesome-command-line-applications-in-ruby>`_


Rust
++++
The rust community has crated a working group ([CLI-WG][CLI-WG]) which is focusing an creating information and tooling
for people which are interested in creating cli tools using rust. I'll recomend you take a look at their [book][Command Line Applicaitons in Rust].

Libraries
---------
* `clap-rs <https://clap.rs/>`_

References
----------
* `CLI-WG <https://github.com/rust-lang-nursery/cli-wg>`_
* `CLI-WG Book <https://rust-lang-nursery.github.io/cli-wg/>`_


