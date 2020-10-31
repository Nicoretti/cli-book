Command Line Tools
__________________

.. attention::

    Be aware that the linked manual pages usualy point to the linux man page, in some
    cases the parameters and flags sligthly differ on other \*nix system.

Unix "One o One"
================

.. list-table:: Basic Unix Commands
    :header-rows: 1
    :widths: 15 50 25 10

    * - Command
      - Description
      - Category
      - Guide(s)
    * - `rm <https://linux.die.net/man/1/rm>`_
      - Remove files or directories
      - File Operations
      -
    * - `mv <https://linux.die.net/man/1/mv>`_
      - Move (rename) files
      - File Operations
      -
    * - `ls <https://linux.die.net/man/1/ls>`_
      - List directory contents
      - File Operations
      -
    * - `cp <https://linux.die.net/man/1/cp>`_
      - Copy files and directories
      - File Operations
      -
    * - `tar <https://linux.die.net/man/1/tar>`_
      - Archiving utility
      - File Operations
      -
    * - `rmdir <https://linux.die.net/man/1/rmdir>`_
      - Remove empty directories
      - Directory Operations
      -
    * - `mkdir <https://linux.die.net/man/1/mkdir>`_
      - Make directories
      - Directory Operations
      -
    * - `cd <https://linux.die.net/man/1/cd>`_
      - Change the current working directory
      - Directory Operations
      -
    * - `pwd <https://linux.die.net/man/1/ls>`_
      - Print name of current/working directory
      - Directory Operations
      -
    * - `df <https://linux.die.net/man/1/df>`_
      - Report file system disk space usage
      - File System
      -
    * - `du <https://linux.die.net/man/1/du>`_
      - Estimate file space usage
      - File System
      -
    * - `mount <https://linux.die.net/man/1/mount>`_
      - Mount a filesystem
      - File System
      -
    * - `umount <https://linux.die.net/man/1/umount>`_
      - Unmount file systems
      - File System
      -
    * - `cat <https://linux.die.net/man/1/cat>`_
      - Concatenate files and print on the standard output
      - Text
      -
    * - `cut <https://linux.die.net/man/1/cut>`_
      - Remove sections from each line of files
      - Text
      -
    * - `head <https://linux.die.net/man/1/head>`_
      - Output the first part of files
      - Text
      -
    * - `tail <https://linux.die.net/man/1/tail>`_
      - Output the last part of files
      - Text
      -
    * - `grep <https://linux.die.net/man/1/grep>`_
      - Print lines matching a pattern
      - Text
      -
    * - `less <https://linux.die.net/man/1/less>`_
      - Page through text one screenful at a time
      - Text
      -
    * - `echo <https://linux.die.net/man/1/echo>`_
      - Display a line of text
      - Text
      -
    * - `chmod <https://linux.die.net/man/1/chmod>`_
      - Change file mode bits
      - Access Rights
      -
    * - `chown <https://linux.die.net/man/1/chown>`_
      - Change file owner/group
      - Access Rights
      -
    * - `chgrp <https://linux.die.net/man/1/chgrp>`_
      - change group ownership
      - Access Rights
      -
    * - `ps <https://linux.die.net/man/1/ps>`_
      - Report a snapshot of the current processes
      - Process Management
      -
    * - `top <https://linux.die.net/man/1/top>`_
      - Display processes
      - Process Management
      -
    * - `kill <https://linux.die.net/man/1/kill>`_
      - Send a signal to a process / Kill a process
      - Process Management
      -
    * - `man <https://linux.die.net/man/1/man>`_
      - Format and display the one-line manual pages
      - Help
      -
    * - `apropos <https://linux.die.net/man/1/apropos>`_
      - Search the manual page names and descriptions
      - Help
      -

Unix "Advanced"
===============


.. list-table:: Advanced Unix Commands
    :header-rows: 1
    :widths: 15 50 25 10

    * - Command
      - Description
      - Category
      - Guide(s)
    * - `file <https://linux.die.net/man/1/file>`_
      - Determine file type
      -
      -
    * - `find <https://linux.die.net/man/1/find>`_
      - Search for files in a directory hierachy
      -
      -
    * - `zip <https://linux.die.net/man/1/zip>`_
      - Package and compress (archive) files
      -
      -
    * - `unzip <https://linux.die.net/man/1/unzip>`_
      - List, test and extract compressed files in a ZIP archive
      -
      -
    * - `gzip <https://linux.die.net/man/1/gzip>`_
      - Compress or expand files
      -
      -
    * - `umask <https://linux.die.net/man/1/umask>`_
      - Get or set the file mode creation mask
      - Access Rights
      -
    * - `diff <https://linux.die.net/man/1/diff>`_
      - Compare files line by line
      - Text
      -
    * - `wc <https://linux.die.net/man/1/wc>`_
      - Print newline, word, and byte counts for each file
      - Text
      -
    * - `sort <https://linux.die.net/man/1/sort>`_
      - Sort lines of text files
      - Text
      -
    * - `sed <https://linux.die.net/man/1/sed>`_
      - Stream editor for filtering and transforming text
      - Text
      -
    * - `date <https://linux.die.net/man/1/date>`_
      - Print or set the system date and time
      -
      -
    * - `who <https://linux.die.net/man/1/who>`_
      - Show who is logged on
      -
      -
    * - `dd <https://linux.die.net/man/1/dd>`_
      - Convert and copy a file
      -
      -
    * - `id <https://linux.die.net/man/1/id>`_
      - Print real and effective user and group IDs
      -
      -
    * - `uname <https://linux.die.net/man/1/uname>`_
      - Print system information
      -
      -
    * - `at <https://linux.die.net/man/1/at>`_
      - Queue, exxamine or delete jobs for later execution
      -
      -
    * - `shutdown <https://linux.die.net/man/1/shutdown>`_
      - Bring the system down
      -
      -
    * - `nice <https://linux.die.net/man/1/nice>`_
      - Run a program with modified scheduling priority
      - Process Management
      -
    * - `spell <https://linux.die.net/man/1/spell>`_
      -
      - Text
      -
    * - `ldd <https://linux.die.net/man/1/ldd>`_
      - Print shared library dependencies
      -
      -
    * - `seq <https://linux.die.net/man/1/seq>`_
      - Print a sequence of numbers
      -
      -
    * - `sleep <https://linux.die.net/man/1/sleep>`_
      - Delay for a specified amount of time
      -
      -
    * - `read <https://linux.die.net/man/1/read>`_
      - Read a single line from stdin or file
      -
      -
    * - `tr <https://linux.die.net/man/1/tr>`_
      - Translate or delete characters
      - Text
      -
    * - `tee <https://linux.die.net/man/1/tee>`_
      - Read from standard input and write to standard output and files
      -
      -
    * - `uniq <https://linux.die.net/man/1/uniq>`_
      - Report or omit repeated lines
      - Text
      -
    * - `ifconfig <https://linux.die.net/man/8/ifconfig>`_
      - Configure a network interface
      - Networking
      -
    * - `ip <https://linux.die.net/man/8/ip>`_
      - Show/Manipulate routing, devices, policy and tunnels
      - Networking
      -
    * - `netstat <https://linux.die.net/man/8/netstat>`_
      - Print network connections, routing tables, etc.
      - Networking
      -
    * - `ping <https://linux.die.net/man/8/ping>`_
      - Send ICMP echo request to network host
      - Networking
      -
    * - `telnet <https://linux.die.net/man/1/telnet>`_
      - User interface to the TELNET protocol
      - Networking
      -
    * - `ftp <https://linux.die.net/man/1/ftp>`_
      - Internet file transfer program
      - Networking, File-Transfer
      -
    * - `nslookup <https://linux.die.net/man/1/nslookup>`_
      - Query Internet name servers interactively
      - Networking, Lookup
      -
    * - `finger <https://linux.die.net/man/1/finger>`_
      - User information lookup program
      - Networking, Lookup
      -
    * - `history <https://linux.die.net/man/1/history>`_
      -
      -
      -
    * - `w <https://linux.die.net/man/1/w>`_
      - Show who is logged on and what they are doing
      - System Info
      -
    * - `watch <https://linux.die.net/man/1/watch>`_
      - Execute a program periodically
      -
      -
    * - `whoami <https://linux.die.net/man/1/whoami>`_
      - Print effective userid
      - System Info
      -

My Personal Toolbox
===================

Shell(s)
--------

.. list-table::
    :header-rows: 1
    :widths: 25 75

    * - Shell
      - Description
    * - `zsh <https://www.zsh.org/>`_
      - The Z shell
    * - `ipython <https://ipython.org/>`_
      - An enhanced interactive python shell
    * - `nushell <https://github.com/nushell/nushell>`_
      - 

Development
-----------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `LLDB <https://lldb.llvm.org/>`_
      -
      - Debugger
      -
    * - `GDB <https://www.gnu.org/software/gdb/>`_
      - Allows you to see whats going on `inside` another program
      - Debugger
      -
    * - `Binutils <https://www.gnu.org/software/binutils/>`_
      - A collection of binary tools
      - Binaries
      - :ref:`link <Binutils Guide>`
    * - `LLVM Tools <https://llvm.org/docs/CommandGuide/>`_
      -
      - Binaries
      - :ref:`link <LLVM Tools Guide>`
    * - `binwalk <https://github.com/ReFirmLabs/binwalk>`_
      - Various development tools
      - Binaries
      -
    * - `xxd <https://linux.die.net/man/1/xxd>`_
      - Make a hexdump or the reverse
      - Binaries
      -
    * - `xxd-rs <https://github.com/Nicoretti/xxd-rs>`_
      - An xxd clone written in rust
      - Binaries
      -
    * - `hexyl <https://github.com/sharkdp/hexyl>`_
      - Simple hex viewer for the terminal
      - Binaries
      -
    * - `SRecord <http://srecord.sourceforge.net/>`_
      - Collection of tools for manipulating EPROM load files
      - Binaries
      -
    * - `otool <https://www.unix.com/man-page/osx/1/otool/>`_
      - Object file displaying tool
      - Binaries
      -
    * - `elfedit <https://linux.die.net/man/1/arm-linux-gnu-elfedit>`_
      - Update the ELF header of ELF files
      - Binaries
      -
    * - `elfdump <https://linux.die.net/man/1/readelf>`_
      - Display information about ELF file
      - Binaries
      -
    * - `rustup <https://rustup.rs/>`_
      - Installer for systems programming language rust
      - Rust, Toolchain, Compiler
      -
    * - `cargo  <https://github.com/rust-lang/cargo>`_
      - Build and dependency tool for the rust programming language
      - Rust, Build-Tool
      -
    * - `rustc <https://www.rust-lang.org/>`_
      - The rust compiler
      - Rust, Compiler
      -
    * - `clang <https://clang.llvm.org>`_
      - Clang C, C++, and Objective-C compiler
      - C/C++, Compiler
      -
    * - `gcc <https://gcc.gnu.org>`_
      -  GNU project C and C++ compiler
      - C/C++, Compiler
      -
    * - `make <https://www.gnu.org/software/make/>`_
      - GNU make utility to maintain groups of programs
      - Build-Tool
      -
    * - `git <https://git-scm.com/>`_
      - the stupid content tracker
      - SCM, Git
      -
    * - `gh <https://github.com/cli/cli>`_
      - Github CLI
      - SCM, Git
      -
    * - `vim <https://www.vim.org>`_
      -  Vi IMproved, a programmer's text editor
      - Editor
      -
    * - `neovim <https://neovim.io>`_
      - Edit text
      - Editor
      -
    * - `miniterm <https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm>`_
      - A console application that provides a small terminal application
      - Connectivity, Serial
      -



Connectivity
------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `socat <http://www.dest-unreach.org/socat/>`_
      - Multipurpose relay (SOcket CAT)
      - Serial, TCP/IP, Networking
      -
    * - `arpping <https://linux.die.net/man/8/arping>`_
      -
      - Networking
      -
    * - `tshark <https://www.wireshark.org/docs/man-pages/tshark.html>`_
      -
      - Tracing, TCP/IP, Networking
      -
    * - `ssh <https://linux.die.net/man/1/ssh>`_
      -
      - SSH, Networking
      -
    * - `mosh <https://mosh.org/>`_
      -
      - SSH, Networking
      -
    * - `scp <https://linux.die.net/man/1/scp>`_
      -
      - File-Transfer, SSH, Networking
      -
    * - `rsync <https://linux.die.net/man/1/rsync>`_
      -
      - File-Transfer, SSH, Networking
      -
    * - `curl <https://linux.die.net/man/1/curl>`_
      -
      - File-Transfer, Multiprotocol
      -
    * - `wget <https://www.gnu.org/software/wget/>`_
      -
      - File-Transfer, Multiprotocol
      -
    * - `iftop <https://linux.die.net/man/8/iftop>`_
      -
      - Monitoring, Networking
      -
    * - `ffsend <https://github.com/timvisee/ffsend>`_
      -
      - File-Transfer, Multiprotocol
      -
    * - `w3m <http://w3m.sourceforge.net/>`_
      -
      - Webbrowser
      -
    * - `lynx <https://lynx.browser.org/>`_
      -
      - Webbrowser
      -
    * - `can-utils <https://github.com/linux-can/can-utils>`_
      -
      - CAN
      -
    * - `can-scripts <https://python-can.readthedocs.io/en/master/scripts.html>`_
      -
      - CAN
      -
    * - `lsusb <https://linux.die.net/man/8/lsusb>`_
      -
      - USB, System Information
      -

Documenttation & Writing
------------------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `graphiz <https://graphviz.org/>`_
      -
      - Visualization
      -
    * - `gnuplot <http://www.gnuplot.info/>`_
      -
      - Plot, Image
      -
    * - `sphinx <https://www.sphinx-doc.org/en/master/>`_
      -
      -
      -
    * - `plantuml <https://plantuml.com/de/>`_
      -
      - UML
      -
    * - `pandoc <https://pandoc.org/>`_
      -
      - Format Converter
      -
    * - `termimad <https://github.com/Canop/termimad>`_
      -
      - Markdown, Renderer
      -

Email
-----

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `isync <https://isync.sourceforge.io/>`_
      -
      -
      -
    * - `neomutt <https://neomutt.org/>`_
      -
      -
      -
    * - `notmuch <https://notmuchmail.org/>`_
      -
      -
      -

Encryption / Passwords
----------------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `gpg <https://gnupg.org/>`_
      -
      -
      -
    * - `pass <https://www.passwordstore.org/>`_
      -
      -
      -

Proccesses / Monitoring
-----------------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `lsof <https://linux.die.net/man/8/lsof>`_
      -
      -
      -
    * - `strace <https://linux.die.net/man/1/strace>`_
      -
      -
      -
    * - `ytop <https://github.com/cjbassi/ytop>`_
      -
      -
      -
    * - `htop <https://linux.die.net/man/1/htop>`_
      -
      -
      -

Standard Unix Tools Alternatives
--------------------------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `ripgrep <https://github.com/BurntSushi/ripgrep>`_
      -
      -
      -
    * - `bat <https://github.com/sharkdp/bat>`_
      -
      -
      -
    * - `fd <https://github.com/sharkdp/fd>`_
      -
      -
      -
    * - `exa <https://github.com/ogham/exa>`_
      -
      -
      -
    * - `broot <https://github.com/Canop/broot>`_
      -
      -
      -
    * - `tmux <https://github.com/tmux/tmux/wiki>`_
      -
      -
      -
    * - python -m zipfile
      -
      -
      -
    * - python -m tarfile
      -
      -
      -

Encoding/Decoding
-------------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)

    * - python -m base64
      -
      -
      -


Formatting
----------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)

    * - python -m json.tool
      -
      -
      -

File Manager
------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `mc <https://midnight-commander.org/>`_
      -
      -
      -
    * - `nnn <https://github.com/jarun/nnn>`_
      -
      -
      -
    * - `ranger <https://github.com/ranger/ranger>`_
      -
      -
      -

Contacts
--------
TBD


Calendar
--------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `khal <https://github.com/pimutils/khal>`_
      -
      -
      -

Task(s) / Todo
--------------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `Taskworrior <https://taskwarrior.org/>`_

      -
      -
      -
    * - `ledger <https://www.ledger-cli.org/>`_
      -
      -
      -

Finance
-------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `ledger <https://www.ledger-cli.org/>`_
      -
      -
      -

Documents
---------

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - `papis <https://github.com/papis/papis>`_
      -
      -
      -

Misc
----

.. list-table::
    :widths: 15 50 25 10
    :header-rows: 1

    * - Tool
      - Description
      - Category
      - Guide(s)
    * - urlscan
      -
      -
      -
    * - urlopen
      -
      -
      -
    * - imgmagick
      -
      -
      -
    * - youtube-dl
      -
      -
      -

CLI Configuration Files
========================
TBD

