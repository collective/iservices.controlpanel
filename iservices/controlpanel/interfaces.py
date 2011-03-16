from zope.interface import Interface
from zope.schema import TextLine, SourceText, Bool, URI

from iservices.controlpanel import iservicesMessageFactory as _

class ISettingsSchema(Interface):
    """
        Defines the control panel schema for the iServices Theme
        settings
    """
    rsslink = URI(
                title=_(u"RSS Feed"),
                description=_(u"The URL to your news in RSS format (Clear it to disable)"),
                required=False
                )
    facebooklink = URI(
                    title=_(u"Facebook link"),
                    description=_(u"The URL to your FaceBook web page (Clear it to disable)"),
                    required=False
                    )
    twitterlink = URI(
                    title=_(u"Twitter link"),
                    description=_(u"The URL to your Twitter account (Clear it to disable)"),
                    required=False
                    )
    custom_colophon_enable = Bool (
                    title=_(u'Enable custom colophon text'),
                    default=False,
                    required=False
                    )
    colophon_text = SourceText(
                    title=_(u"Colophon text"),
                    description=_(u"Define the text that will appear on "
                                  u"your colophon (you can use html code)"),
                    default=_(u'Powered by Plone &copy; CMS/WCM and iServices de M&eacute;xico'),
                    required=False,
                    max_length=80
                    )
    custom_footer_enable = Bool (
                    title=_(u'Enable custom footer text'),
                    default=False,
                    required=False
                    )
    footer_text = SourceText(
                    title=_(u'Text - Additional advert area'),
                    description=_(u'HTML text that will appear in the Additional advert area'),
                    default= _(u"The Plone CMS/WSM is copyrighted by the Plone Foundation and Friends."
                               u"It is distributed under the GNU LGPL License."
                               ),
                    required=False
                    )
    foreground_color = TextLine(
                    title=_(u"Background color of the site"),
                    description=_(u", use the HTML/CSS notation. The default is #205C90"),
                    default=u'#205C90',
                    required=False
                    )
    enable_color_switch = Bool (
                    title=_(u'Enable changing plone colors'),
                    description=_(u"Enabling this option and defining the colors below, allows you "
                    u"to do a very basic plone theming for free. It allows you to change the most "
                    "two most prominent colors of the default Plone 4 theme(sunburst)"),
                    default=False,
                    required=False
                    )
    strong_color = TextLine(
                    title=_(u"Strong color for plone"),
                    description=_(u"There are two main prominent colors in the plone Sunburst Theme."
                    u"This option allows you to change the 'blue' color to "
                    u"something that suits your needs. Use the HTML/CSS "
                    u"notation. The default is #205C90"),
                    default=u'#205C90',
                    required=False
                    )
    light_color = TextLine(
                    title=_(u"Light color for plone"),
                    description=_(u"There are two main prominent colors in the plone Sunburst Theme."
                    u"This option allows you to change the 'light gray' color to "
                    u"something that suits your needs. Use the HTML/CSS "
                    u"notation. The default is #DDDDDD"),
                    default=u'#DDDDDD',
                    required=False
                    )
