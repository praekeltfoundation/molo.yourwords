
molo.yourwords
==============
A molo module that enables user generated content competitions


.. image:: https://img.shields.io/travis/praekelt/molo.yourwords.svg
        :target: https://travis-ci.org/praekelt/molo.yourwords

.. image:: https://img.shields.io/pypi/v/molo.yourwords.svg
        :target: https://pypi.python.org/pypi/molo.yourwords

.. image:: https://coveralls.io/repos/praekelt/molo.yourwords/badge.png?branch=develop
    :target: https://coveralls.io/r/praekelt/molo.yourwords?branch=develop
    :alt: Code Coverage


Note:
This package has since been deprecated in favour of `molo.forms` https://github.com/praekeltfoundation/molo.forms


Installation::
   pip install molo.yourwords

Testing:
   read the .travis.yml file
   follow the instructions under the scripts heading

Django setup::
   ```
   INSTALLED_APPS = (
      ...
      'molo.yourwords',
      ...
   )
   ```


In your urls.py::
from molo.yourwords import urls
url(r"^yourwords/$", include(urls)),


In your main.html::
   ```
   {% load competition_tag %}

   {% block content %}
      {% your_words_competition %}
   {% endblock %}
   ```

In your section page or section page::
   ```
   {% load competition_tag %}

   {% block content %}
    {{% your_words_competition_in_section section %}
   {% endblock %}
   ```
