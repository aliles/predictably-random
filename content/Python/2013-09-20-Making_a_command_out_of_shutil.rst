Making a command out of shutil
##############################

I love the creating that developers show in making unintended use of a tool to
solve a problem. It doesn't matter if that use is a "good idea" or not.
Regardless of whether it's a "good idea" or not. The ingenuity and problem
solving demonstrated is usually quite fascinating. Like this little hack that
my friend `mjdorma`_ shared with me that uses `Begins`_' sub-commands.

.. code:: python

   import shutil
   import begin

   begin.subcommand(shutil.copy)
   begin.subcommand(shutil.copy2)
   begin.subcommand(shutil.copyfile)
   begin.subcommand(shutil.copymode)
   begin.subcommand(shutil.copystat)
   begin.subcommand(shutil.copytree)
   begin.subcommand(shutil.move)
   begin.subcommand(shutil.rmtree)

   # Patch in doc before the func is wrapped by begin.start
   def patch_doc(doc):
       def decorate(func):
           func.__doc__ = doc
           return func
       return decorate

   @begin.start
   @patch_doc(shutil.__doc__)
   def main():
       pass

This little script gives you access to a number of utility functions from
Python's `shutil`_ module from the command line. Admittedly there are common
Unix utilities that provide most of this functionality. But I still felt it was
a nifty and entertaining use of functionality I had just written.

After using Begins for a few weeks this type of application has become a common
pattern for Begins. Sub-commands excel at creating small administration
programs that are a collection of related commands. Even more exciting is that
others groups are successfully orchestrating much larger systems using Begins
as a framework. Its terrific to know that Begins is meeting its goal of growing
with the developer.

You can download this script from Michael's `original GitHub Gist`_.

.. _Begins: https://pypi.python.org/pypi/begins
.. _shutil: http://docs.python.org/dev/library/shutil.html
.. _mjdorma: https://twitter.com/mjdorma
.. _original GitHub Gist: https://gist.github.com/mjdorma/6145546
