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
* Common Fixutres Shell scripts
    - let it fail


assert_cmd (Rust)
_________________
TBD

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
