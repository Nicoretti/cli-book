Command Line Tools
__________________
In this chapter you find command line and tui tools I made part of my personal toolbox.

Unix "One o One"
================

File operations
---------------
* rm
* mv
* `ls <https://man7.org/linux/man-pages/man1/ls.1.html>`_
* `cp <https://man7.org/linux/man-pages/man1/cp.1.html>`_
* `tar <https://linux.die.net/man/1/tar>`_

Directory operations
--------------------
* rmdir
* `mkdir <https://linux.die.net/man/1/mkdir>`_
* cd
* pwd

File System
-----------
* df
* du
* dd
* mount/umount

Text
----
* `cat <https://man7.org/linux/man-pages/man1/cat.1.html>`_
* cut
* tail
* head
* `grep <https://www.gnu.org/software/grep/manual/grep.html>`_
* `less <https://linux.die.net/man/1/less>`_
* echo

Rights
------
* `chmod <https://linux.die.net/man/1/chmod>`_
* chown
* chgrp

Processes
---------
* ps
* top
* kill

Help
----
* man
* apropos

Unix "Advanced"
===============
* `file <https://man7.org/linux/man-pages/man1/file.1.html>`_
* `find <https://man7.org/linux/man-pages/man1/find.1.html>`_
* `zip <https://linux.die.net/man/1/zip>`_
* `unzip <https://linux.die.net/man/1/unzip>`_
* `gzip <https://www.gnu.org/software/gzip/manual/gzip.html>`_
* `umask <https://man7.org/linux/man-pages/man2/umask.2.html>`_
* diff
* wc
* sort
* sed
* date
* who
* dd
* id
* uname
* cron
* at
* nice
* spell
* ldd
* seq
* sleep
* read
* tr
* tee
* uniq 
* history
* whoami

My Personal Toolbox
===================

Shell(s)
--------
* `zsh <https://www.zsh.org/>`_
* `ipython <https://ipython.org/>`_
* `nushell <https://github.com/nushell/nushell>`_

Development
-----------

Debuggers
+++++++++
* `LLDB <https://lldb.llvm.org/>`_
* `GDB <https://www.gnu.org/software/gdb/>`_

Binaries
++++++++
* `binwalk <https://github.com/ReFirmLabs/binwalk>`_
* `SRecord <http://srecord.sourceforge.net/>`_
* `otool <https://www.unix.com/man-page/osx/1/otool/>`_
* `LLVM Tools <https://llvm.org/docs/CommandGuide/>`_
* `Binutils <https://www.gnu.org/software/binutils/>`_
    - ld
    - as
    - add2line
    - ar
    - c++filt
    - dlltool
    - gold
    - gprof
    - nlmconv
    - nm
    - objcopy
    - objdump
    - ranlib
    - readelf
    - size
    - strings
    - strip
    - windmc
    - windres
* `elfedit <>`_
* `elfutils <>`_
* `elfdump <>`_
* `xxd <https://linux.die.net/man/1/xxd>`_
* `xxd-rs <https://github.com/Nicoretti/xxd-rs>`_
* `hexyl <https://github.com/sharkdp/hexyl>`_

Rust
++++
* `rustup <https://rustup.rs/>`_
* `cargo  <https://github.com/rust-lang/cargo>`_
* `rustc <https://www.rust-lang.org/>`_

C/C++
+++++
* clang
* gcc
* g++
* make


SCM
+++
* `git <https://git-scm.com/>`_
* `gh <https://github.com/cli/cli>`_

Editor(s)
+++++++++
* vim
* neovim
  additions (plugins)
    - plug (plugin list see also vim config)
    - vim-airline
    - vim-airline-themes
    - tagbar
    - rust.vim
    - vim-uuid 
    - nerdtree
    - LanguageClient
    - deoplete.vim
    - fzf
    - fzf.vim
    - vim-fugitive.git
    - nerdtree-git-plugin.git
    - vim-surround

Serial
++++++
* `miniterm <https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm>`_
* `socat <http://www.dest-unreach.org/socat/>`_

Networking
----------
* `tshark <https://www.wireshark.org/docs/man-pages/tshark.html>`_
* `socat <http://www.dest-unreach.org/socat/>`_
* ssh 
    - `client <https://linux.die.net/man/1/ssh>`_
    - `mosh <https://mosh.org/>`_
* `scp <https://linux.die.net/man/1/scp>`_
* `rsync <https://linux.die.net/man/1/rsync>`_
* `curl <https://linux.die.net/man/1/curl>`_
* `wget <https://www.gnu.org/software/wget/>`_
* `iftop <https://linux.die.net/man/8/iftop>`_
* `ifconfig <https://linux.die.net/man/8/ifconfig>`_
* `ip <https://linux.die.net/man/8/ip>`_
* netstat
* ping
* telnet
* ftp
* finger
* `ffsend <https://github.com/timvisee/ffsend>`_
* `w3m <http://w3m.sourceforge.net/>`_
* `lynx <https://lynx.browser.org/>`_


CAN
---
* `can-utils <https://github.com/linux-can/can-utils>`_
* `can-scripts <https://python-can.readthedocs.io/en/master/scripts.html>`


Usb
---
* lsusb

Docs / Writing
--------------
* `graphiz <https://graphviz.org/>`_
* `gnuplot <http://www.gnuplot.info/>`_
* `sphinx <https://www.sphinx-doc.org/en/master/>`_
* `plantuml <https://plantuml.com/de/>`_
* `pandoc <https://pandoc.org/>`_
* `termimad <https://github.com/Canop/termimad>`_

Email
-----
* `isync <https://isync.sourceforge.io/>`_
* `neomutt <https://neomutt.org/>`_
* `notmuch <https://notmuchmail.org/>`_

Encryption / Passwords
----------------------
* `gpg <https://gnupg.org/>`_
* `pass <https://www.passwordstore.org/>`_

Proccesses / Monitoring
-----------------------
* `lsof <>`_
* `strace <>`_
* `ytop <https://github.com/cjbassi/ytop>`_
* `htop <https://linux.die.net/man/1/htop>`_

Unix built-in alternatives
--------------------------
* `ripgrep <https://github.com/BurntSushi/ripgrep>`_
* `bat <https://github.com/sharkdp/bat>`_
* `fd <https://github.com/sharkdp/fd>`_
* `exa <https://github.com/ogham/exa>`_
* `broot <https://github.com/Canop/broot>`_
* `tmux <https://github.com/tmux/tmux/wiki>`_
* python -m zipfile
* python -m tarfile
* urlscan
* urlopen

Encoding/Decoding
-------------------
* python -m base64
* ffmpeg

Formatting
----------
* python -m json.tool

File Manager
------------
* `mc <https://midnight-commander.org/>`_
* `nnn <https://github.com/jarun/nnn>`_
* `ranger <https://github.com/ranger/ranger>`_

Contacts
--------
* ?

Calendar
--------
* `khal <https://github.com/pimutils/khal>`_

Task(s) / Todo
--------------
* `Taskworrior https://taskwarrior.org/>`_
* `ledger <https://www.ledger-cli.org/>`_

Finance
-------
* `ledger <https://www.ledger-cli.org/>`_

Documents
---------
* `papis <https://github.com/papis/papis>`_

Misc
----
* imgmagick
* youtube-dl
