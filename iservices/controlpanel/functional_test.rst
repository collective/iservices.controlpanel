Introduction
====================

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

Login as administrator and setup development mode for css stylesheets.
First, login as administrator::
    
    >>> from Products.PloneTestCase.setup import portal_owner, default_password

    >>> browser.open(portal_url+'/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> 'You are now logged in' in browser.contents
    True

Then open portal_css and enable the css debug mode.

    >>> browser.open(portal_url+'/portal_css/manage_cssForm')
    >>> browser.getControl(name='debugmode:boolean').value = '1'
    >>> browser.getControl(label='Save').click()
    
Testing CSS view
-----------------
First of all, we need to see all the tracebacks::

    >>> browser.handleErrors = False

Let's open the root plone page and find out whether our custom css is
there::
 
    >>> browser.open(portal_url)
    >>> 'iservices_controlpanel.css' in browser.contents
    True
    
By default it should be empty::

    >>> browser.open(portal_url+'/iservices_controlpanel.css')
    
    >>> len(browser.contents)
    0

And it should only render something after we enable the css styles on
the control panel page. So first, open the iservices control panel page
and switch on the  "Enable changing plone colors" option.

    >>> browser.open(portal_url+ '/@@iservices-controlpanel')
    >>> 'iServices control panel' in browser.contents
    True
    >>> browser.getControl(name='form.widgets.enable_color_switch:list').value = '1'
    >>> browser.getControl(label='Save').click()
    >>> 'Changes saved' in browser.contents
    True

Finally, load portal_url and, first, see if the css is still there, and
second, see if it has some content.

    >>> browser.open(portal_url)
    >>> 'iservices_controlpanel.css' in browser.contents
    True
    >>> browser.open(portal_url+'/iservices_controlpanel.css')    
    >>> len(browser.contents)
    0
