from zope.component import getUtility
from plone.registry.interfaces import IRegistry

registry = getUtility(IRegistry)
from iservices.controlpanel.interfaces import ISettingsSchema
settings = registry.forInterface(ISettingsSchema)
