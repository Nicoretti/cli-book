CLI Syntax
==========
Before you start reading this chapter I highly recommend you read the [POSIX Utility Conventions][POSIX Utility Conventions].
It is approximately a 10-20 minute read which will provide a solid base when it comes to CLIs and their syntax.

Terminology
+++++++++++

If you read about command lines and command line interfaces usually you will find a specific kind of terminology
(*command, utility, subcommand, argument, option, flag, switch, operand*) even though the meaning does slightly differ
depending on which source or in which context a term is mentioned.
To make sure we are all on the same page regarding these terms, please read the following table,
which describes the terms and their meaning in the context of this book.

.. list-table:: 
   :widths: 35 15 50
   :header-rows: 1

   * - Terminology of this Book
     - Description
     - Names in other standards/definitions

   * - command
     - a cli tool / command
     - utility (Posix)

   * - subcommand
     - a subcommand of a command/cmd group
     - 

   * - argument (required/positional)
     - required/positional-argument
     - operand (Posix)

   * - option
     - setting with additional argument
     - option (Posix)

   * - switch
     - Like an option but with a set of mutally exclusive arguments
     - option (Posix)

   * - options
     - Super set of flags + switches + options
     - options (Posix)

.. warning::
    
    with the specification above there is an ambiguity when it comes to using the word options.

Here, options could mean either:

* The plural of an option - a setting with an additional argument
* Options - The super set of flags + switches + options

Therefore, when talking about the plural of option one should say options of type option, and when talking about the super set of all options, switches, and flags one should simply say options.

Anotated CLI Help Example
+++++++++++++++++++++++++

.. code-block::

    Short description what this command does

    usage:

    cmd [flags] [options] <username> <password>

    arguments:
        <username>  which shall be used for the login             # 1. required/positional-argument
        <password>  associated with the specified username        # 2. required/positional-argument

    flags:
        -f, --force                 execute action anyway         # 5. flag
        -h, --help                  show this help message        # 6. flag

    options:
        -i <file>, --input <file>   file which shall be processed # 3. option
        -s <unit>, --speed <unit>   mph,kmh  [default: mph]       # 4. switch

Unix CLI
++++++++

Common CLI Elements
-------------------

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Element
     - Symbol
     - Description

   * - text
     - Text
     - without brackets or braces

   * - upper case text
     - TEXT
     - placeholder for which you must supply a vlaue

   * - text in angle brackets
     - <name>
     - placeholder for which you must supply a value

   * - bracket
     - []
     - optional items

   * - curly braces
     - {}
     - set of mutually exclusive but required items, choose one

   * - braces
     - ()
     - set of mutually exclusive but required items, choose one

   * - vertical bar
     - \|
     - seperates mutually exclusive items

   * - ellipsis
     - …
     - indicates that item (flag, option, arguemtn, ...) can be repeated multiple times

   * - dash
     - \-
     - indicates start of short option(s), if it stands alone it is often used as file argument parameter to specify stdin

   * - double dash
     - \-\-
     - indicates the start of a long option or if not flowed by an option name it indicates the end of the cli arguements for the command


Windows CLI
+++++++++++

Common CLI Elements
-------------------

A definition of the Windows Command Line Syntax can be found [here][Windows Command-Line Syntax].

CLI Element Examples
--------------------

.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - Type
     - Example(s)

   * - argument (required/positional)
     - ARGUMENT, <argument>, <ARGUMENT>

   * - option with value
     - \-\-option=value, \-\-option=VALUE, \-\-option <value>, \-\-option=<value>, \-\-option value, \-\-option VALUE

   * - switch
     - \-\-light={on \| off}, \-\\-power {up \| down}

   * - flag
     - \-\-track, \-\-verbose, \-V

   * - optional items
     - \-\-track, \-\-verbose, \-V, [<argument>]

   * - mutually exclusive required items
     - (\-\-track \| \-\-no-track), <FILE> \| <PATH>, \-\-strengh={low\|mid\|high}

   * - end passing cli arguments
     - `user@host ~$ cli foo -b --this -- other args`

   * - repeating items                    
     - <argument>...


References
++++++++++
* `POSIX Utility Conventions <http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html>`_
* `Windows Command-Line Syntax <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/command-line-syntax-key>`_



