'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://github.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

from unicon.plugins.generic.settings import GenericSettings


class FortigateSettings(GenericSettings):

    def __init__(self):
        # inherit any parent settings
        super().__init__()
        self.CONNECTION_TIMEOUT = 300
        self.ESCAPE_CHAR_CALLBACK_PRE_SENDLINE_PAUSE_SEC = 1
        self.HA_INIT_EXEC_COMMANDS = ["config system console",  "set output standard", "end"]
        self.HA_INIT_CONFIG_COMMANDS = []

        # pattern to replace '---(more)---' or '---(more #%)---'   
        self.MORE_REPLACE_PATTERN = r'--More-- '
        # self.ERROR_PATTERN = [
        #     r'^.*?command not found.*$',
        #     r'^.*?[Ii]nvalid command.*$'
        # ]
