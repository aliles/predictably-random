Preparing for Mavericks
#######################

Apple has released OSX 10.9, also known as Mavericks. Which means it's time to
prepare for an operating system upgrade again. In the interest of soliciting
feedback, I'm sharing the rough process I'm using for this upgrade.

* **Update all software.** In addition to installing all pending App Store
  updates, I make sure all any applications that have auto-updaters are started
  and they check for new updates. In particular this means running Mail to
  ensure `GPGTools`_ updates GPGMail.
* **Backup all important data.** Most of my important but not confidential data
  is already stored remotely on `GitHub`_ and `Dropbox`_. I'm in the process of
  setting up `Arq`_ to backup the remainder.
* **Update and upgrade Homebrew.** Rather than just upgrade `Homebrew`_, for
  this upgrade I've decided to completely uninstall and reinstall by following
  the uninstall instructions on the `Homebrew FAQ`_ and the commands in `this
  Gist`_.
* **Compile a list of post upgrade procedures.** Currently, the only process
  I've recorded is to use `xcode-select`_ to install the latest command line
  tools.

It's hardly a detailed or rigorous plan. If you do have feedback, or think any
thing is missing, please leave a comment below. Alternatively, there is also
`Twitter`_ or `email`_.

.. _GPGTools: https://gpgtools.org/
.. _GitHub: https://github.com/
.. _Dropbox: https://www.dropbox.com/
.. _Arq: http://www.haystacksoftware.com/arq/
.. _Homebrew: http://brew.sh/
.. _Homebrew FAQ: https://github.com/mxcl/homebrew/wiki/FAQ#how-do-i-uninstall-homebrew
.. _this Gist: https://gist.github.com/mxcl/1173223
.. _xcode-select: https://twitter.com/ogrisel/status/393723457466150912
.. _Twitter: https://twitter.com/aliles
.. _email: mailto:aaron.iles@gmail.com
