Lorem Ipsum Generator
=====================

---------------
Module contents
---------------

Get Random Words
----------------

.. autofunction:: lorem.word
.. autofunction:: lorem.get_word

Get Random Sentences
--------------------

.. autofunction:: lorem.sentence
.. autofunction:: lorem.get_sentence

Get Random Paragraphs
---------------------

.. autofunction:: lorem.paragraph
.. autofunction:: lorem.get_paragraph

Customise Word Pool
-------------------

.. autofunction:: lorem.set_pool

------------------
Internal utilities
------------------

.. autodata:: lorem._TEXT

   The text pool is generated directly from the original lorem ipsum paragraph::

      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
      commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
      esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
      cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
      est laborum.

.. autofunction:: lorem._gen_pool
.. autofunction:: lorem._gen_word
.. autofunction:: lorem._gen_sentence
.. autofunction:: lorem._gen_paragraph
