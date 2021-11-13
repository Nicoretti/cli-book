Testing
=======
In this chapter we will discuss various ways how to test command line tools.

Unit Tests
----------
Unit tests are highly language and framework specific, therefore we will discuss most of the specific(s) within
the language specific subsections.

Python
______

General structure for testable python cli's
********************************************
TBD

Mocking stdin, stdout, stderr
*****************************
TBD

Make sure argv cann be passed
*****************************
TBD

How to check exit code
**********************
TBD

Rust
______
TBD


Integration Tests
-----------------

What should you be checking
____________________________
* Return Code(s)
* output -> stdout
* Maybe stderr
* output files

Making your CLI testable
_________________________
* timeouts
* count's
* return code
* output stdout/stderr
* input stdin
* input output format(s)

Shell Scripts
_____________
* diff
* shell scripts

.. todo::

    * Shell testing tools?
    * Brickster?

Cram
____
* Creating input files
* Making sure tests fail
    - count
    - poll
    - timeout

* Checking return codes
* checking stdout
* checking stderr
* quirks
    - indention
    - blocking
    - cleanup

Cram Advanced
*************
* Common Fixtures Shell scripts
    - let it fail

Specdown
________


Socat
_____
e.g. connecting client + server impl and verify exit's

Tshark
______
TBD

Curl
______
TBD

Diff
______
TBD

Examples
--------
* Testing GraphQl Endpoint
* Testing RestEndpoint
* Testing Protocol Dissector


References
----------
* `curl <https://curl.se>`_
* `socat <http://www.dest-unreach.org/socat/>`_
* `tshark <https://www.wireshark.org/docs/man-pages/tshark.html>`_
* `diff <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/diff.html>`_
* `cram <https://bitheap.org/cram/>`_
* `specdown <https://specdown.io>`_
* `cucumber <https://cucumber.io/tools/cucumber-open/>`_
    * `Rust <https://github.com/cucumber-rs/cucumber>`_
    * `Python <http://behave.readthedocs.io>`_
    * `Go <https://github.com/cucumber/godog>`_
    * `Cpp <https://github.com/cucumber/cucumber-cpp>`_
    * `Ruby <https://github.com/cucumber/cucumber-ruby>`_
    * `Javascript <https://github.com/cucumber/cucumber-js>`_
    * `JVM <https://github.com/cucumber/cucumber-jvm>`_
    * `Other(s) <https://github.com/cucumber>`_
