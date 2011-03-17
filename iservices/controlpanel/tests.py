import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from zope.component import getMultiAdapter

from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite

##################   The plone test layer stuff ############
ptc.setupPloneSite(
    extension_profiles=('iservices.controlpanel:default', )
)

class ControlPanelTestlayer(PloneSite):
    """
    Configure iservices.controlpanel for testing
    """

    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        import iservices.controlpanel
        zcml.load_config("configure.zcml", iservices.controlpanel)
        ztc.installPackage(iservices.controlpanel)
        fiveconfigure.debug_mode = False

    @classmethod
    def tearDown(cls):
        pass

################### Base class for control panel
class BaseTestCase(ptc.PloneTestCase):
    layer = ControlPanelTestlayer

################### Test the control panel
from plone.registry import Registry
#from zope.component import getMultiAdapter
#from Products.CMFCore.utils import getToolByName

from iservices.controlpanel.interfaces import ISettingsSchema

class ControlPanelTestCase(BaseTestCase):
    def afterSetUp(self):
        # Set up the iservices.controlpanel settings registry
        self.loginAsPortalOwner()
        self.registry = Registry()
        self.registry.registerInterface(ISettingsSchema)

    def test_iservices_controlpanel_view(self):
        # Test the iservices setting control panel view
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                            name="iservices-controlpanel")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_controlpanel_view_protected(self):
        from AccessControl import Unauthorized
        self.logout()
        self.assertRaises(Unauthorized,
                        self.portal.restrictedTraverse,
                        '@@iservices-controlpanel')

    def test_controlpanel_keys(self):
        # Test that all the keys declared in the Interface are avilable
        for key_name in ISettingsSchema.names():
            rkey_name = self.registry.records[
                'iservices.controlpanel.interfaces.ISettingsSchema.%s'%key_name]
            self.assertEquals(rkey_name.value, ISettingsSchema[key_name].default)


def test_suite():
    #return unittest.defaultTestLoader.loadTestsFromName(__name__)
    return unittest.TestSuite([
        unittest.makeSuite(ControlPanelTestCase),
        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='iservices.controlpanel',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='iservices.controlpanel.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='iservices.controlpanel',
        #    test_class=TestCase),

        ztc.FunctionalDocFileSuite(
            'api_usage.rst', package='iservices.controlpanel',
            test_class=BaseTestCase),
        ztc.FunctionalDocFileSuite(
            'functional_test.rst', package='iservices.controlpanel',
            test_class=BaseTestCase),
        ])
if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
