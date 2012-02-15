# -*- coding: utf-8 -*-

from zope.component import getUtility

from Products.DCWorkflow.DCWorkflow import WorkflowException

from collective.powertoken.core.interfaces import IPowerTokenUtility
from collective.powertoken.core.exceptions import PowerTokenConfigurationError

from collective.powertoken.workflow.tests.base import TestCase

class TestWorkflow(TestCase):

    def afterSetUp(self):
        self.setRoles(('Manager', ))
        portal = self.portal
        portal.invokeFactory(type_name="Document", id="public_doc")
        doc1 = portal.public_doc
        doc1.edit(title="A test document")
        portal.portal_workflow.doActionFor(doc1, 'publish')
        self.doc1 = portal.public_doc

        portal.invokeFactory(type_name="Document", id="private_doc")
        doc2 = portal.private_doc
        doc2.edit(title="Another test document")
        self.doc2 = portal.private_doc
        self.utility = getUtility(IPowerTokenUtility)
        self.request = self.portal.REQUEST
        self.logout()
        self.setRoles(('Anonymous', ))

    def test_configuration(self):
        token = self.utility.enablePowerToken(self.doc1, 'workflow.doAction')
        self.assertRaises(PowerTokenConfigurationError, self.utility.consumeActions, self.doc1, token)

    def test_actionForAnonymous(self):
        token = self.utility.enablePowerToken(self.doc1, 'workflow.doAction', workflow_action='publish')
        self.assertRaises(WorkflowException, self.utility.consumeActions, self.doc1, token)
        token = self.utility.enablePowerToken(self.doc1, 'workflow.doAction', roles=['Contributor'], workflow_action='publish')
        self.assertRaises(WorkflowException, self.utility.consumeActions, self.doc1, token)
        token = self.utility.enablePowerToken(self.doc2, 'workflow.doAction', roles=['Manager'], workflow_action='publish')
        self.assertEqual(self.utility.consumeActions(self.doc2, token), ['published'])
        self.assertEqual(self.portal.portal_workflow.getInfoFor(self.doc2, 'review_state'), 'published')

    def test_comment(self):
        token = self.utility.enablePowerToken(self.doc2, 'workflow.doAction', roles=['Manager'], workflow_action='publish')
        self.utility.consumeActions(self.doc2, token, comment='Hello darling!')
        self.assertEqual(self.portal.portal_workflow.getInfoFor(self.doc2, 'comments') ,'Hello darling!')

    def test_security(self):
        token = self.utility.enablePowerToken(self.doc2, 'workflow.doAction', roles=['Manager'], workflow_action='publish')
        self.utility.consumeActions(self.doc2, token)
        self.assertEqual(self.portal.portal_workflow.getInfoFor(self.doc1, 'review_state'), 'published')
        self.assertEquals(self.portal.portal_membership.getAuthenticatedMember().getRolesInContext(self.doc1), ['Anonymous'])


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestWorkflow))
    return suite
