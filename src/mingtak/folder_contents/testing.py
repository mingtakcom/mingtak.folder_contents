# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mingtak.folder_contents


class MingtakFolderContentsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=mingtak.folder_contents)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mingtak.folder_contents:default')


MINGTAK_FOLDER_CONTENTS_FIXTURE = MingtakFolderContentsLayer()


MINGTAK_FOLDER_CONTENTS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MINGTAK_FOLDER_CONTENTS_FIXTURE,),
    name='MingtakFolderContentsLayer:IntegrationTesting',
)


MINGTAK_FOLDER_CONTENTS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MINGTAK_FOLDER_CONTENTS_FIXTURE,),
    name='MingtakFolderContentsLayer:FunctionalTesting',
)


MINGTAK_FOLDER_CONTENTS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MINGTAK_FOLDER_CONTENTS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MingtakFolderContentsLayer:AcceptanceTesting',
)
