'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://github.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

from unicon.plugins.fortigate.statements import FortigateStatements
from unicon.statemachine import Path, State
from unicon.plugins.generic.statemachine import GenericSingleRpStateMachine
from .patterns import FortigatePatterns
from unicon.eal.dialogs import Dialog

patterns = FortigatePatterns()
statements = FortigateStatements()


class FortigateStateMachine(GenericSingleRpStateMachine):

    def __init__(self, hostname=None, learn_hostname=False):
        super().__init__(hostname, learn_hostname)

    def create(self):
        '''
        statemachine class's create() method is its entrypoint. This showcases
        how to setup a statemachine in Unicon.
        '''
        
        global_config = State('global_config', patterns.global_prompt)
        login = State("login", patterns.login_prompt)
        password = State("password", patterns.password_prompt)
        new_password = State("new_pw", patterns.new_pw_prompt)

        self.add_state(login)
        self.add_state(password)
        self.add_state(new_password)
        self.add_state(global_config)


        login_to_new_password = Path(password, new_password, "\r\nYou are forced to change your password. Please input a new password.\r\nNew Password: ", Dialog([statements.new_password_stmt]))
        # expert_to_clish = Path(expert, clish, 'exit', None)

        self.add_path(login_to_new_password)
        # self.add_path(expert_to_clish)












