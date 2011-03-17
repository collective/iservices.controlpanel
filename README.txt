Introduction
============

``iservices.controlpanel`` is a plone control panel that provides common
settings for themers and integrators. The idea behind this control panel is that
plone administrators (and not the integrator or programmer) will have the
ability to:

* Define social accounts for use all over the site, specially on themes. The
  programmer/integrator will have to integrate it's product or theme with this
  control panel (hopefully an easy_step) and get this settings to be applied on
  their logic.

* Allows to change the global background and foreground colors that plone uses
  to draw it's interface on plonetheme.sunburs (Actually, only two colors). If the
  user requires more than that, it might be better to craft a complete theme
  product.

* Change the plone logo. The site administrator can change the logo. This
  provides an easy plone theming deployment without the cost of creating a theme
  from scratch just to change the logo.

* Change the footer and colophon text. The site administrator can change the
  text of the footer and colophon without needing the programmer to make changes
  to any theme.

Usage
=====

Install using buildout
-----------------------

Add ``iservices.controlpanel`` to your ``eggs`` subsection::

    eggs = 
        ...
        iservices.controlpanel

This package depends on a set of other packages, hopefully, all packages should
be pulled from pypi automatically. However, you'll have to adjust the
``extends`` subsection according to the following pattern::

    extends =
        http://dist.plone.org/release/<plone-version>/versions.cfg
        ...
        http://good-py.appspot.com/release/plone.app.z3cform/0.5.0-1?plone=<plone-version>
        http://good-py.appspot.com/release/plone.app.registry/1.0b2?plone=<plone-version>

Replace ``<plone-version>`` with the Plone version you are working on, i.e., ``4.0.3``

How to use it on your packages and themes
-----------------------------------------

Of course, If you use this package, you'd want access to the settings it
manages, right? This package has a small API that encapsulates the the
boilerplate code and makes it easy to you to use it.

In order to
access the settings of the control panel, you just use a very simple module
import::

    >>> from iservices.controlpanel.api import settings

All settings are available using standar Python dot notation. Example::

    >>> settings.background_color
    u'#205C90'

If you access an unknown name, you will get an AttributeError:

    >>> registry.some_unknown_key
    Traceback (most recent call last):
    ...
    NameError: name 'registry' is not defined
    
Also, using getattr(), even on an existing key name, does not make it:

    >>> getattr(settings,background_color)
    Traceback (most recent call last):
    ...
    NameError: name 'background_color' is not defined

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

Credits
=======

Author
    Noe Nieto <noe@iservices.com.mx>

Websites
    http://iservices.com.mx/
    http://noenieto.com/
    
Contact-email
    desarrollo@iservices.com.mx


