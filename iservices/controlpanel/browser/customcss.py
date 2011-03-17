from Products.Five.browser import BrowserView

class customCssView(BrowserView):
    _css_template = """
        a:link, a:visited, #content a:link, #content a:visited, dl.portlet a:link, dl.portlet a:visited {
            color: %(background_color)s;
        }
        #portal-globalnav .selected a, #portal-globalnav a:hover {
            background-color: %(background_color)s;
        }
    """
    def __call__(self):
        from iservices.controlpanel.api import settings
        self.request.response.setHeader('Content-Type','text/css')
        
        if settings.enable_color_switch:
            return self._css_template %{ 'background_color': settings.background_color }
        else:
            return ''

