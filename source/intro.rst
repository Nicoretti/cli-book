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
As the xkcd ilustrates also CLI's have their downsides, the best tool is of no worth if one
does not know how to use it.

I am a huge fan, trying to tease, make you understand why ...
for sure some stuff sounds trival or not that powerfull ... but once it make click and you
will see the light ;p there is no turning back. (Like UnitTesting, ....)

From a developers and system administrators point of view CLI-Tools are just superior to GUI tools in
most cases. You see an GUI project gone wrong when they start adding a server/service in the background
which can be used to automate the GUI task(s) or retrive inforamtion from the gui.

Important CLI and GUI are interfaces, they both can be done badly and their quality highly
relies on the one creating it. Still getting the basics of a cli right is way simpler
and requires a way smaller tech and sw stack

What does a cli-interface do well:

What does a gui-interface do well:
- visualize complicated data/structures in

if you are a developer cli is a must! embeded way simpler, instant value to the project and the team
(the basic need to be done right!) build up from the basics.
Grow your knowlege with the use cases and the tool.
eat your own dogfood.
early failing.
early integration.

So you are an "end-user" you may don't have a need for a cli but you still can benefit from it


NOTE: A note about tui's, a thing of its own but will be partially discussed here and there.
sometimes there is a fine line between them if tools support both tui and cli interface

A well-done CLI is the best format to build a tool, because the CLI can be used on its own to build
any other type of tool, and it provides a direct and explicit separation of responsibilities between
combinations and compositions of tools. For example, a GUI is then built up by first creating a good
CLI tool that does the actual work of the program, and the GUI is only built around providing a good
UI for the user while calling the CLI behind the scenes to handle the requests and visualize the
responses. This means the GUI never has to be concerned with the business logic of the CLI, and the
CLI never has to be concerned with the UI and display of the tool to the user.

What this book will be about:
+++++++++++++++++++++++++++++
All things, cli
* The Oekosystem and the cli neightbours
* How to use them
* How to write them
* What is out there
* Reference to other great material
* A good starting point


How is this book structured
+++++++++++++++++++++++++++
* Usage
 - Basics
   + Shell
   + Config
 - Advanced
 - Geeks & Nerds
   + Testing
* Implementation
 - Basics
  + Testing
 - Advanced
  + Testing
 - Geeks & Nerds
   + TUIs
* Command Line Tools
 - Basics
 - Advanced
 - Geeks & Nerds

