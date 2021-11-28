Introduction
============

Good tools matter!
++++++++++++++++++

.. figure:: https://imgs.xkcd.com/comics/tar.png
   :alt: xkcd-1168
   :target: https://xkcd.com/1168/
   :scale: 50

   source: `xkcd.com <https://xkcd.com/1168/>`_
   license: `CC BY-NC 2.5 <https://creativecommons.org/licenses/by-nc/2.5/>`_

Why CLIs
++++++++

A well-done CLI is the best format to build a tool, because the CLI can be used on its own to build
any other type of tool, and it provides a direct and explicit separation of responsibilities between
combinations and compositions of tools. For example, a GUI is then built up by first creating a good
CLI tool that does the actual work of the program, and the GUI is only built around providing a good
UI for the user while calling the CLI behind the scenes to handle the requests and visualize the
responses. This means the GUI never has to be concerned with the business logic of the CLI, and the
CLI never has to be concerned with the UI and display of the tool to the user.

