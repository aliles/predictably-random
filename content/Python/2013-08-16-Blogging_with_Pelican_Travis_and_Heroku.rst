Blogging with Pelican, Travis and Heroku
########################################

It's been over a year since I posted anything to by `Tumblr blog`_. While
Tumblr was a convenient way to start a blog, I now find it difficult to create
content the way I want to. In particular, I want to author posts in
`reStructuredText`_ or `Markdown`_ with high quality support for syntax
highlighting of code. Therefore, I have decided to change to a different
blogging platform.

My new blog is built using the `Pelican`_ static site generator. I consider a
static site to be simpler and easier to deploy and manage, being a collection
of static files. I chose Pelican as it was implemented using `Python`_ (my
favourite software development language) is actively developed and appeared to
have the features I wanted.

For a site theme, I started with the `bootstrap2`_ theme from `Pelican
Themes`_. I then updated the version of the `Bootstrap`_ framework and the
`Font Awesome`_ icon set, tweaked the CSS, fixed some bugs, tweaked the CSS
some more, and finally chose to stop personally `bikeshedding`_ and move
forward. I think it's pretty clear that I'm no web designer. There's still some
annoying behaviour from the `responsive design`_ on mobile phones that I
haven't been able to fix.

Most of my open source projects are hosted on `Github`_, including this blog.
Using a version control system allows me to crate branches for drafts I'm still
working on. I also get to use my preferred `text editor`_. While hosting on
Github allows me to use Travis for continuous integration. Github also has
excellent web based editing, so I can create and work on articles even if I
don't have my laptop.

To publish, I'm using `Travis`_ for `continuous deployment`_ to Heroku.  Travis
makes continuous `Heroku deployment`_ reasonably simple. The most difficult
part of getting this working was realising I needed to explicitly set the
`deploy strategy`_ to use Git. Travis will default to using the Anvil deploy
strategy, which does not work with my `buildpack`_. I ended up forking the
`Pelican buildpack`_ as the content directory wasn't being set correctly. This
caused pages to fail to be built.

`Heroku`_ is very generous to offer each Heroku app enough credits to run a
single web dynamo for free. This is easily enough to meet the tiny demand of
this static site.  Admittedly, Heroku applications running on their free tier
will enter a `sleep state`_ after an hour of inactivity, the few seconds delay
to wake from a sleep state doesn't greatly concern me at the moment.

One feature of Tumblr that I really liked was the ability to post to `Twitter`_
when I publish a new article. To meet this requirement, I created a recipe
using `IFTTT`_ that does the same. It polls the site's news feed for new items,
posting the title and link to my Twitter account.

To acknowledge the projects and companies that have enabled this blog, I have
created a *Powered By* section in the side bar of this site, which will remain
for the foreseeable future. Thank you Python, Pelican, Bootstrap, Font Awesome,
Travis, Heroku and IFTTT. This has been fun.

.. _Bootstrap: http://getbootstrap.com/
.. _Font Awesome: http://fortawesome.github.io/Font-Awesome/
.. _Github: https://github.com/aliles/predictably-random
.. _Heroku: https://travis-ci.org/
.. _Heroku deployment: http://about.travis-ci.org/docs/user/deployment/heroku/
.. _IFTTT: https://ifttt.com/
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _Pelican: http://getpelican.com/
.. _Pelican Themes: http://pelicanthemes.com/
.. _Pelican buildpack: https://github.com/pearkes/heroku-buildpack-pelican
.. _Python: http://python.org/
.. _Travis: https://travis-ci.org/
.. _Tumblr blog: http://aliles.tumblr.com/
.. _Twitter: https://twitter.com/aliles
.. _buildpack: https://github.com/aliles-heroku/heroku-buildpack-pelican
.. _bikeshedding: https://en.wiktionary.org/wiki/bikeshedding
.. _bootstrap2: https://github.com/getpelican/pelican-themes/tree/master/bootstrap2
.. _continuous deployment: http://about.travis-ci.org/blog/2013-07-09-introducing-continuous-deployment-to-heroku/
.. _deploy strategy: http://about.travis-ci.org/docs/user/deployment/heroku/#Deploy-Strategy
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _responsive design: https://en.wikipedia.org/wiki/Responsive_web_design
.. _sleep state: https://devcenter.heroku.com/articles/dynos#dyno-sleeping
.. _text editor: https://github.com/aliles/vim-home
