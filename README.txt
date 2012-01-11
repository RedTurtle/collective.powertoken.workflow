Introduction
============

A workflow action implementation for `collective.powertoken`__

__ http://plone.org/products/collective.powertoken.core

How to use
==========

Add this product to your Plone installation, then you will be able to register Power Tokens that
performs workflow action when consumed.

>>> from collective.powertoken.core.interfaces import IPowerTokenUtility
>>> utility = getUtility(IPowerTokenUtility)
>>> token = utility.enablePowerToken(document, 'workflow.doAction', workflow_action='publish')
>>> results = utility.consumeAction(document, token)
>>> print results
['published']

You will get the new state of the document as result.

Parameters
----------

``workflow_action``
    Required. You need to provide the workflow action to perform.

Use case
========

You can perform a state change for a document, regardless of your roles in the site.

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
