"""Remple = Rest Simple

For an example use case of Remple, imagine a general-purpose storage service
exposed via an HTTP JSON REST API. This storage service stores packages in
spaces at locations. A package is a directory or a directory that has been
packaged (and compressed) to a file. Spaces are categorized by their medium
of storage and the API that that medium exposes; examples: a POSIX filesystem
space, an S3 space, etc. Each space can contain one or more locations, e.g.,
subpaths within a root filesystem.

This imaginary storage service uses Remple to expose the following resources
via a consistent HTTP JSON interface:

- /locations/ --- purpose-specific locations/paths within a space (see below)
- /spaces/ --- storage space with behaviour specific to its backing system
- /pipelines/ --- external services that can produce packages to be stored

Imagine the additional following resources, which are read-only meaning that
update, create, delete and related mutative operations are disabled:

- /packages/ --- Information Package (SIP, DIP or AIP)
- /file/ --- a file on disk (which is in a package), represented as db row.

All resources have endpoints that follow this pattern::

    +-----------------+-------------+----------------------------+------------+
    | Purpose         | HTTP Method | Path                       | Method     |
    +-----------------+-------------+----------------------------+------------+
    | Create new      | POST        | /<cllctn_name>/            | create     |
    | Get create data | GET         | /<cllctn_name>/new/        | new        |
    | Read all        | GET         | /<cllctn_name>/            | index      |
    | Read specific   | GET         | /<cllctn_name>/<id>/       | show       |
    | Update specific | PUT         | /<cllctn_name>/<id>/       | update     |
    | Get update data | GET         | /<cllctn_name>/<id>/edit/  | edit       |
    | Delete specific | DELETE      | /<cllctn_name>/<id>/       | delete     |
    | Search          | SEARCH      | /<cllctn_name>/            | search     |
    | Search          | POST        | /<cllctn_name>/search/     | search     |
    | Get search data | GET         | /<cllctn_name>/new_search/ | new_search |
    +-----------------+-------------+----------------------------+------------+

.. note:: To remove the search-related routes for a given resource, create a
   ``'searchable'`` key with value ``False`` in the configuration for the
   resource in the ``RESOURCES`` dict. E.g., ``'location': {'searchable':
   False}`` will make the /locations/ resource non-searchable.

.. note:: All resources expose the same endpoints. If a resource needs special
   treatment, it should be done at the corresponding class level. E.g., if
   ``POST /packages/`` (creating a package) is special, then do special stuff
   in ``resources.py::Packages.create``. Similarly, if packages are indelible,
   then ``resources.py::Packages.delete`` should return 404.
"""

from locations.api.beta.remple import API
from locations.api.beta.resources import (
    ArkivumSpaces,
    # Asyncs,
    Callbacks,
    DataverseSpaces,
    DSpaceSpaces,
    DuracloudSpaces,
    Events,
    FedoraSpaces,
    FixityLogs,
    LockssomaticSpaces,
    NFSSpaces,
    S3Spaces,
    SwiftSpaces,
    Files,
    GPGSpaces,
    LocalFilesystemSpaces,
    Locations,
    Packages,
    Pipelines,
    PipelineLocalSpaces,
    Spaces,
    Users,
    Groups,
    Permissions,
    ContentTypes,
)

API_VERSION = 'beta'
SERVICE_NAME = 'Archivematica Storage Service'

resources = {
    'pipeline': {'resource_cls': Pipelines},
    'location': {'resource_cls': Locations},
    'space': {'resource_cls': Spaces},
    'user': {'resource_cls': Users},

    # Space sub-types
    'local_filesystem_space': {'resource_cls': LocalFilesystemSpaces},
    'gpg_space': {'resource_cls': GPGSpaces},
    'arkivum_space': {'resource_cls': ArkivumSpaces},
    'dataverse_space': {'resource_cls': DataverseSpaces},
    'dspace_space': {'resource_cls': DSpaceSpaces},
    'duracloud_space': {'resource_cls': DuracloudSpaces},
    'fedora_space': {'resource_cls': FedoraSpaces},
    'lockssomatic_space': {'resource_cls': LockssomaticSpaces},
    'nfs_space': {'resource_cls': NFSSpaces},
    's3_space': {'resource_cls': S3Spaces},
    'swift_space': {'resource_cls': SwiftSpaces},
    'pipeline_local_space': {'resource_cls': PipelineLocalSpaces},

    # The following resources are read-only because of their super-classes
    'file': {'resource_cls': Files},
    'package': {'resource_cls': Packages},
    'event': {'resource_cls': Events},
    'callback': {'resource_cls': Callbacks},
    'fixity_log': {'resource_cls': FixityLogs},
    'group': {'resource_cls': Groups},
    'permission': {'resource_cls': Permissions},
    'contenttype': {'resource_cls': ContentTypes},
}

api = API(api_version=API_VERSION, service_name=SERVICE_NAME)
api.register_resources(resources)
urls = api.get_urlpatterns()

__all__ = ('urls', 'api')
