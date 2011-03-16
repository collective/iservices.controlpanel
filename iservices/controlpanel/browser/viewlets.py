from datetime import date
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase, FooterViewlet

class customFooterViewlet(ViewletBase):
    index = ViewPageTemplateFile('footer.pt')
    #from iservices.controlpanel.api import settings
    
    def update(self):
        self.year = date.today().year
        
class customColophonViewlet(ViewletBase):
    index = ViewPageTemplateFile('colophon.pt')
    #from iservices.controlpanel.api import settings
    

