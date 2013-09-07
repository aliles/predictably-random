reStructuredText Viewer
#######################

This week's project was implementing my own `reStructuredText Viewer`_ and
editor for `reStructuredText`_ documents. In the past I have used the `Online
reStructuredText editor`_ for quickly previewing and editing README files
before being publishing on the `Python Package Index`_. While I have been happy
with the online editor, it recently had some stability issues. When I tried to
deploy my own instance I was surprised to find a dependency on `Redis`_.

Not wanting to deploy an instance of Redis as well as a web application, I
decided it was a good opportunity to learn something about `docutils`_. It's
the basis for the `Sphinx`_ documentation generator, I tool I use regularity.
My viewer is a web application built using the `Flask`_ web framework. The
application acts as a `docutils publisher`_, accepting reStructuredText
documents and return rendered HTML. As with other little web applications I've,
the viewer is deployed on `Heroku`_. The source code is available from
`GitHub`_.

So feel free to give my `reStructuredText Viewer`_ a try. But please be kind to
the aesthetics, web design is not my strong suite.

.. _Flask: http://flask.pocoo.org
.. _Github: https://github.com/aliles-heroku/rstviewer
.. _Heroku: https://heroku.com
.. _Online reStructuredText editor: http://rst.ninjs.org/
.. _Python Package Index: https://pypi.python.org/pypi
.. _Redis: http://redis.io/
.. _Sphinx: http://sphinx-doc.org/
.. _docutils: http://docutils.sourceforge.net/
.. _docutils publisher: http://docutils.sourceforge.net/docs/api/publisher.html
.. _reStructuredText Viewer: http://rst.aaroniles.net
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
