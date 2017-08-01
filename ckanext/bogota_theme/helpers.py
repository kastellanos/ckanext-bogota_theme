import ckan.plugins.toolkit as toolkit
import pprint

from logging import getLogger

log = getLogger(__name__)

def all_groups():
    '''Return a sorted list of the groups with the most datasets.'''
    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    context = {'ignore_auth': True,
               'for_view': True
              }
    data_dict={'order_by': 'name', 'all_fields': True }

    groups = toolkit.get_action('group_list')( context, data_dict )
    
    filtered = []
    
    log.error("Hola mundo")
    
    for group in groups:
        if group ["package_count"] > 0:
            filtered.append(group)

    return filtered

def all_packages():
    '''Return a sorted list of the packages with the most recent modifications.'''
    # Get a list of all the packages from CKAN, sorted by date.
    context = {'ignore_auth': True,
               'for_view': True
              }
    data_dict={ 'all_fields': True }

    packages = toolkit.get_action('current_package_list_with_resources')( context, data_dict )

    return packages[:4]