Introduction
-------------

This file excercises the use of the API provided by this package. In order to
access the settings of the control panel, you just use a very simple module
import::

    >>> from iservices.controlpanel.api import settings

All settings are available using standar Python dot notation. Example::

    >>> settings.foreground_color
    u'#205C90'

If you access an unknown name, you will get an AttributeError:

    >>> registry.some_unknown_key
    Traceback (most recent call last):
    ...
    NameError: name 'registry' is not defined
    
Also, using getattr(), even on an existing key name, does not make it:

    >>> getattr(settings,foreground_color)
    Traceback (most recent call last):
    ...
    NameError: name 'foreground_color' is not defined

Sometimes, settings on the control panel will have empty values. It is suggested
that, when this happens, the funcionality related to this particular setting
should be disabled or modified in some way.

    >>> def do_something_with(some_setting):
    ...     if some_setting:
    ...             print "Doing stuff when this registry entry is set."
    ...     else:
    ...             print "Disable functionality when this registry is not set."
    ... 
    >>> # the twitterlink setting is empty by default
    >>> print settings.twitterlink
    None
    
    >>> do_something_with(settings.twitterlink)
    Disable functionality when this registry is not set.
    
    >>> settings.twitterlink = 'http://twitter.com/tzicatl'
    >>> do_something_with(settings.twitterlink)
    Doing stuff when this registry entry is set.
    
And that's all there is for the API.

