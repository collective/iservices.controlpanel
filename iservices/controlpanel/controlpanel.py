from plone.app.registry.browser import controlpanel

from iservices.controlpanel.interfaces import ISettingsSchema
from iservices.controlpanel import iservicesMessageFactory as _

class SettingsEditForm(controlpanel.RegistryEditForm):
    schema = ISettingsSchema
    label = _(u"iServices control panel")
    description = _(u"Generic settings control panel")

    def updateFields(self):
        super(SettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(SettingsEditForm, self).updateWidgets()

class IservicesControlPanel(controlpanel.ControlPanelFormWrapper):
    """
        Control Panel form wrapper
    """
    form = SettingsEditForm
