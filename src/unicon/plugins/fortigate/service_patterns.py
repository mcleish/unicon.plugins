"""
Module:
    unicon.plugins.nxos.services.patterns

Authors:
    pyATS TEAM (pyats-support@cisco.com, pyats-support-ext@cisco.com)

Description:
    Module for defining all the Patterns required for the
    nxos related service implementation
"""



class FortigateProvisioningPatterns:
        # NXOS reload pattern
    def __init__(self):
        self.new_password = r'^.*New Password:'
