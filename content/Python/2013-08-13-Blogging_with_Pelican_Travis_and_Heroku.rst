Blogging with Pelican, Travis and Heroku
########################################

It's been over a year since I posted anything to by `Tumblr blog`_. While
Tumblr was a convenient way to start a blog, I now find it difficult to create
content the way I want to. In particular, I want to author posts in
`reStructuredText`_ or `Markdown`_ and have high quality support for syntax
highlighting of code. To meet those requirements, I have decided to relaunch my
blog on a new platform.

This blog is deployed using the `Pelican`_ static site generator. A static site
is simple to deploy and manage, being a collection of files. I chose Pelican as
it was implemented using `Python`_, my preferred software development language,
is actively developer and appeared to have the features I desired.

To theme this blog I started with the `bootstrap2`_ theme. I then updated the
versions of `Bootstrap`_ framework and `Font Awesome`_ icon set, tweaked the
CSS, fixed some bugs, tweaked the CSS some more, and finally chose to stop
personally `bikeshedding`_ and move forward. I think it's pretty clear that I'm
no web designer.

Most of my open source projects are hosted on `Github`_, as is this blog.
Hosting on Github enables me to use `Travis`_ for continuous integration. For
my blog, I'm using Travis for `continuous deployment`_ to `Heroku`_. Travis
makes continuous `Heroku deployment`_ reasonably simple.

Heroku is generous to offer all each up enough free credits to run a web dynamo
for free. I ultimately forked the `Pelican buildpack`_ and used my own
`buildpack`_ to ensure that the content directory is set correctly. (Otherise
pages fail to build) With the `Pelican buildpack`_ this is easily enough to
meet the demand for this blog. (Yes, all six of you). Heroku applications
running on their free tier will enter a `sleep state`_ after an hour of
inactivity, the couple of seconds delay before loading doesn't greatly concern
me.

To acknowledge the projects and companies that have enabled this blog, I have
created a *Powered By* section in the side bar of this site. Considering the
flexibility and control I now have, I encountered remarkably few issues while
setting this new blog up.

.. _Bootstrap: http://getbootstrap.com/G
.. _Font Awesome: http://fortawesome.github.io/Font-Awesome/
.. _Github: https://github.com/aliles/predictably-random
.. _Heroku: https://travis-ci.org/
.. _Heroku deployment: http://about.travis-ci.org/docs/user/deployment/heroku/
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Pelican: http://getpelican.com/
.. _Pelican buildpack: https://github.com/pearkes/heroku-buildpack-pelican
.. _Python: http://python.org/
.. _Travis: https://travis-ci.org/
.. _Tumblr blog: http://aliles.tumblr.com/
.. _buildpack: https://github.com/aliles-heroku/heroku-buildpack-pelican
.. _bikeshedding: https://en.wiktionary.org/wiki/bikeshedding
.. _bootstrap2: https://github.com/getpelican/pelican-themes/tree/master/bootstrap2
.. _continuous deployment: http://about.travis-ci.org/blog/2013-07-09-introducing-continuous-deployment-to-heroku/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _sleep state: https://devcenter.heroku.com/articles/dynos#dyno-sleeping
