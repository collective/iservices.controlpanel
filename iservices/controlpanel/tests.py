import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from zope.component import getMultiAdapter

from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite(
    extension_profiles=('iservices.controlpanel:default', )
)


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

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
    
    def afterSetUp(self):
        # Set up the iservices.controlpanel settings registry
        from plone.registry import Registry
        import iservices.controlpanel
        
        self.loginAsPortalOwner()
        self.registry = Registry()
        self.registry.registerInterface(iservices.controlpanel.interfaces.ISettingsSchema)
        
    def test_iservices_controlpanel_view(self):
        # Test the iservices setting control panel view
        view = getMultiAdapter((self.portal, self.portal.REQUEST), 
                               name="iservices-controlpanel")
        view = view.__of__(self.portal)
        self.failUnless(view())        

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
    #return unittest.TestSuite([

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

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='iservices.controlpanel',
        #    test_class=TestCase),

     #   ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
