Homebrewing with Homebrew
#########################

I'm a bit of an Apple fan, doing a lot of my private development using Mac OSX.
Apple doesn't distribute OSX with many of the software packages I want
installed. Instead, I use `Homebrew`_ to install new packages, track
dependencies and updates, and remove everything again when I am done.

However, even the extensive collection of packages Homebrew provides doesn't
cover every piece of obscure or unusual software that I might want to install.
So I created a `Homebrew Tap`_ which I called `Arcane`_ to manage these
packages.

Homebrew introduced Taps in `0.9`_. Taps Taps are a way of creating
repositories of Homebrew formula that are independent of the main Homebrew
repository. Homebrew maintains a `list of interesting taps`_, but anyone can
create their own.

Creating a new Tap is straight forward. First, `create a new repository`_ on
`Github`_. There is a `naming convention`_ to creating Tap repository, they
must begin with ``homebrew-``. The remainder is the name of the Tap.

Once the new repository is created, it can be *tapped* using ``brew tap
user/repo``. Where ``user`` is your GitHub user account and ``repo`` is the
name of your Tap repository. (The bit after ``homebrew-``) The repository will
be cloned into ``/usr/local/Library/Taps``.

Now you can begin creating formula for your new Tap. Homebrew has a guide on
how to `create a new formula`_ that covers the basics. Unfortunately you will
likely need to review existing formula to learn the more advanced features of
Homebrew.

After running ``brew create``, a new formula will be created in
``/usr/local/Library/Formula``. As formula are `Ruby`_ scripts you can move the
formula from its initial location to your Tap repository in
``/usr/local/Library/Taps/user-repo``. After moving the formula its necessary
to run ``brew tap --repair`` to ensure a symbolic link to the formula is
created in ``/usr/local/Library/Formula``. Without this link Homebrew is unable
to find the formula to install it.

Once your finished developing your formula, commit it to the repository.
Congratulations, you are now the maintainer of a Homebrew Tap of interesting
formula. As a bonus, it's now possible to repeatedly and reliably install (and
remove) your software again at any time in the future.

.. _0.9: https://github.com/mxcl/homebrew/wiki/Homebrew-0.9
.. _Arcane: https://github.com/aliles/homebrew-arcane
.. _GitHub: https://github.com/
.. _Homebrew: http://brew.sh/
.. _Homebrew Tap: https://github.com/mxcl/homebrew/wiki/brew-tap
.. _Ruby: http://www.ruby-lang.org/
.. _create a new formula: https://github.com/mxcl/homebrew/wiki/Formula-Cookbook
.. _create a new repository: https://help.github.com/articles/creating-a-new-repository
.. _list of interesting taps: https://github.com/mxcl/homebrew/wiki/Interesting-Taps-%26-Branches
.. _naming convention: https://github.com/mxcl/homebrew/wiki/brew-tap#naming-conventions-and-limitations
