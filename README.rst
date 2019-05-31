================================================================================
  Remple: REST Simple
================================================================================

Remple is a simple Python library that helps you to create consistent REST
(HTTP JSON) endpoints for arbitrary Django models.

Usage::

    >>> from remple import API, Resources
    >>> class Users(Resources):
    ...     model_cls = User  # A Django model class
    ...     schema_cls = UserSchema  # A Formencode class
    >>> resources = {'user': {'resource_cls': Users}}
    >>> api = API(api_version='0.1.0', service_name='User City!')
    >>> api.register_resources(resources)
    >>> urls = api.get_urlpatterns()  # Include these in Django urlpatterns


Features
================================================================================

- Auto-generates an OpenAPI 3.0 YAML file and a Swagger UI HTML interface to
  same.
- Auto-generates Python client code which is self-documenting and has
  client-side validation.
- Consistency of endpoints: specific pairings of HTTP method and URI path regex
  are mapped to known endpoints/operations.
- Resources can be defined as *mutable* (*read/write/delete*) or *read-only*.
- APIs built using Remple are thoroughly documented using the OpenAPI 3.0 spec.
- Includes a search endpoint with a simple but expressive data structure for SQL
  WHERE-clause-based search over all exposed resources.


How to Understand OpenAPI 3.0
================================================================================

OpenAPI suffers from too much documentation. I have found this page to be a
good authoritative source:

    https://swagger.io/docs/specification/about/

