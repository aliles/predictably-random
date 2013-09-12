Rebooting TwoSlug
#################

This week, like last week, I've been revamping an old project and learning some
new tools. This time it's been `TwoSlug`_ receiving my attention.

TwoSlug is a fun little web tool to generate random two word phrases, or slug
lines, using a randomly chosen verb and noun. Words are chosen from Princeton
University's `WordNet`_ database. It was originally written almost year ago, in
a single evening, and hosted on `GitHub`_. Unfortunately it's been limited to a
simple, static, HTML page until now.

Aside from the obligatory themeing, I've added two major new features to
TwoSlug.  The first is an API for requesting your own random slug lines. With
an HTTP GET request you can ask for any combination of verbs, nouns, adjectives
and adverbs. The API will return you random slug line in `JSON`_ format.

The second feature is word definitions using `DuckDuckGo`_'s excellent Instant
Answer `API`_. Definitions are displayed as pop ups on each word. The words
themselves are links to the original definition source. The team at DuckDuckGo
are extremely generous to offer their API with very restrictions.

Now, if I can just get `ElasticSearch`_ to use TwoSlug to generate a random
`node name`_ each time a node starts.

.. _API: https://duckduckgo.com/api
.. _DuckDuckGo: https://duckduckgo.com/
.. _ElasticSearch: http://www.elasticsearch.org/
.. _GitHub: https://github.com/aliles-heroku/twoslug
.. _JSON: http://www.json.com/
.. _TwoSlug: http://twoslug.aaroniles.net/
.. _WordNet: http://wordnet.princeton.edu/
.. _node name: http://www.elasticsearch.org/guide/reference/setup/configuration/
