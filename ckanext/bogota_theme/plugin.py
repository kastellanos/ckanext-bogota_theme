import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Bogota_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'bogota_theme')

    def get_helpers(self):
        import helpers
        return {
            'all_groups': helpers.all_groups,
            'all_packages': helpers.all_packages,
        }