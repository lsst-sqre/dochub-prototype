#####################
LSST DocHub Prototype
#####################

.. image:: https://img.shields.io/pypi/v/lsst-dochub-prototype.svg
   :target: https://pypi.python.org/pypi/lsst-dochub-prototype
   :alt: Python Package Index
.. image:: https://img.shields.io/travis/lsst-sqre/dochub-prototype.svg?branch=master
   :target: https://travis-ci.org/lsst-sqre/dochub-prototype
   :alt: Travis CI build status

Prototype of LSST DocHub (`www.lsst.io`_) as a static website generator.

Usage
=====

::

  #/usr/bin/env python
  from dochubproto import DocHubProto

  p = DocHubProto()
  idx = p.render_index()

Configuration
=============

``DocHubProto`` uses the following environment variables:

- ``KEEPER_URL`` (default ``https://keeper.lsst.codes``).
- ``LOGLEVEL`` (default ``WARNING``).
- ``TEMPLATE_DIR``: directory containing Jinja2 templates (default ``templates``).
- ``UL_TEMPLATE_NAME``: relative path to template for individual document items (default ``doclist.jinja2``).
- ``IDX_TEMPLATE_NAME``: relative path to the ``index.html`` template (default ``index.jinja2``).
- ``MAX_DOCUMENT_DATA_AGE``: maximum cache age in seconds of a document (default ``3600``).

DocHubProto API overview
========================

- ``check_state()`` returns one of:

  - ``STATE_EMPTY`` (``'empty'``)
  - ``STATE_READY`` (``'ready'``)
  - ``STATE_REFRESHING`` (``'refreshing'``)
  - ``STATE_STALE`` (``'stale'``)

  A document is 'stale' if it is older than ``MAX_DOCUMENT_DATA_AGE``.
  
- ``get_document_data()`` and ``get_fresh_document_data()`` return a ``dict`` whose keys are document sections (e.g. ``DMTN``) and within each section, a list ordered by document handle (e.g. ``dmtn-038``).
  
- ``render()`` returns an HTML unordered list entity created from the document data, encoded as UTF-8.

- ``render_index()`` returns an HTML document created from the document data, encoded as UTF-8.
  
- ``debug()``, ``info()``, ``warning()``, ``error()``, and ``critical()`` each log a message at the specified level; it uses a `structlog`_ logger to log JSON output via `apikit`_.

.. _apikit: https://github.com/lsst-sqre/sqre-apikit
.. _structlog: https://structlog.readthedocs.io/en/stable/
.. _`www.lsst.io`: https://www.lsst.io
