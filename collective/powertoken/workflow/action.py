# -*- coding: utf-8 -*-

from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from collective.powertoken.core.interfaces import IPowerActionProvider
from collective.powertoken.core.exceptions import PowerTokenConfigurationError

class WorkflowActionProvider(object):
    """
    Perform workflow action on the given content.
    
    The workflow transition that will be executed must be given in the params attribute:
        {'workflow_action': 'publish'}
    """
    implements(IPowerActionProvider)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def doAction(self, action):
        if not action.params.get('workflow_action'):
            raise PowerTokenConfigurationError('workflow.doAction need the workflow_action parameter in the IPowerActionConfiguration object')
        context = self.context
        portal_workflow = getToolByName(context, 'portal_workflow')
        portal_workflow.doActionFor(context, action.params['workflow_action'])
        return portal_workflow.getInfoFor(context, 'review_state')