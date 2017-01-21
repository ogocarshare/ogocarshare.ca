"""
Integrate OGO's CMS extensions with the Django CMS editing toolbar
"""
from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from .models import FeatureImageExtension


@toolbar_pool.register
class FeatureImageExtensionToolbar(ExtensionToolbar):
    """ Add a menu item for FeatureImageExtension to the Django CMS toolbar """
    # defineds the model for the current toolbar
    model = FeatureImageExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()
        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            _page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item
                current_page_menu.add_modal_item(
                    _('Change Feature Image'),
                    url=url,
                    disabled=not self.toolbar.edit_mode,
                )
