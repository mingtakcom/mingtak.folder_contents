# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from mingtak.folder_contents.testing import MINGTAK_FOLDER_CONTENTS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that mingtak.folder_contents is properly installed."""

    layer = MINGTAK_FOLDER_CONTENTS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mingtak.folder_contents is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mingtak.folder_contents'))

    def test_browserlayer(self):
        """Test that IMingtakFolderContentsLayer is registered."""
        from mingtak.folder_contents.interfaces import (
            IMingtakFolderContentsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IMingtakFolderContentsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MINGTAK_FOLDER_CONTENTS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['mingtak.folder_contents'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if mingtak.folder_contents is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mingtak.folder_contents'))

    def test_browserlayer_removed(self):
        """Test that IMingtakFolderContentsLayer is removed."""
        from mingtak.folder_contents.interfaces import \
            IMingtakFolderContentsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IMingtakFolderContentsLayer,
            utils.registered_layers())
