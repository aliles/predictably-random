Begins at the beginning
#######################

My `Begins`_ project is approaching its first beta release. It's actually been
used in operations for a while now, which has produced a steady flow of bug
reports and new feature requests. With a significant milestone for the project
approaching, its fun to reflect of how it got to this point.

The genesis for *Begins* was me toying with syntactic `sugar for Python's
main`_.  I was intrigued with the lack of a protocol over `main`_, like there
is behind `len`_ to `reversed`_. In fact, I was so interested in the question I
attempted `more sugar for Python's main`_, this time with an actual
implementation.

That first implementation was based on Python's `atexit`_ module and made it
into the `list of projects`_ as project *main*. I didn't do much with it until
`Julython`_ and J(an)ulython this year. Julython is a fabulously fun event
designed to help motivate participants to return to those long stagnating
projects, like *Begins*.

For Julython *main* was renamed *Begins*. It moved away from atexit to stack
inspection. (Parts of the interpreter may be shutdown when the functions
registered with atext are called) And created an extensive unit test suite with
nearly 100% `coverage`_.

However, I didn't really feel comfortable publishing *Begins* on PyPI when it
was just a pretty way to begin a program. This felt a little to minimalist to
feature in a Python package. As it turns out I had also been interested in
`sugar for Python's argparse`_. So I decided to add some command line handling
to *Begins*.

After the `0.1`_ release I showed *Begins* to one of my friends. He works on a
large project with a wide selection of plugins. All of which need to inject
command support into the central application if present. I didn't really expect
*Begins* to grow much from that first release. However, they were able to
convince me to add sub-commands and configuration file support. Since then
they've been a steady source of feature requests.

While using *Begins* myself I've come across some new pain points for me.  That
includes converting command line arguments to their desired types. I added the
``begin.convert`` decorator while creating documentation examples. A future
release will significantly improve its utility.

So a little project that was once too insignificant to publish on PyPI, and
then wasn't expected to grow much beyond its first release, has steadily
expanded in scope and functionality beyond expectations. This really shouldn't
surprise me. `Scope creep`_ is a force in every software project. It is however
novel for me to observe and experience it outside of the break neck pace of
professional work.

.. _0.1: https://pypi.python.org/pypi/begins/0.1
.. _Begins: https://pypi.python.org/pypi/begins
.. _Julython: http://www.julython.org/
.. _Scope creep: https://en.wikipedia.org/wiki/Scope_creep
.. _atexit: http://docs.python.org/dev/library/atexit.html
.. _coverage: https://coveralls.io/r/aliles/begins?branch=master
.. _len: http://docs.python.org/3/reference/datamodel.html#object.__len__
.. _list of projects: http://aliles.tumblr.com/post/9500120819/starting-the-list
.. _main: http://docs.python.org/3/library/__main__.html
.. _more sugar for Python's main: http://aliles.tumblr.com/post/7686579735/more-sugar-for-pythons-main
.. _reversed: http://docs.python.org/3/reference/datamodel.html#object.__reversed__
.. _sugar for Python's argparse: http://aliles.tumblr.com/post/7572364196/sugar-for-pythons-argparse
.. _sugar for Python's main: http://aliles.tumblr.com/post/7455032885/sugar-for-pythons-main
