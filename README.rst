About tgapp-categories
-------------------------

tgapp-categories is a Pluggable application for TurboGears2.

Installing
-------------------------------

tgapp-categories can be installed both from pypi or from github::

    pip install tgappcategories

should just work for most of the users

Plugging tgapp-categories
----------------------------

In your application *config/app_cfg.py* import **plug**::

    from tgext.pluggable import plug

Then at the *end of the file* call plug with tgappcategories::

    plug(base_config, 'tgappcategories')

You will be able to access the plugged application at
*http://localhost:8080/tgappcategories*.

Available Hooks
----------------------

tgapp-categories makes available a some hooks which will be
called during some actions to alter the default
behavior of the appplications:

Exposed Partials
----------------------

tgapp-categories exposes a bunch of partials which can be used
to render pieces of the blogging system anywhere in your
application:

Exposed Templates
--------------------

The templates used by registration and that can be replaced with
*tgext.pluggable.replace_template* are:
