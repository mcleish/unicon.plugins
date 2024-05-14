'''
Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

from unicon.eal.dialogs import Statement
from unicon.plugins.generic.statements import GenericStatements, pre_connection_statement_list
from .patterns import FortigatePatterns
from unicon.utils import to_plaintext
from time import sleep

statements = GenericStatements()
patterns = FortigatePatterns()


def new_password_handler(spawn, context, session):
    print("its working?")
    credentials = context.get('credentials')
    new_credential_password = credentials.get('default', {}).get('password')
    new_password = to_plaintext(new_credential_password)
    sleep(0.1)
    spawn.sendline(new_password)
    sleep(0.1)


class FortigateStatements():
    """
        Class that defines the Statements for Gaia plugin
        implementation
    """

    def __init__(self):
        super().__init__()

        self.new_password_stmt = Statement(
            pattern=patterns.new_pw_prompt,
            action=new_password_handler,
            args=None,
            loop_continue=True,
            continue_timer=False)
        
        self.new_password_confirmation_stmt = Statement(
            pattern=patterns.confirm_new_pw_prompt,
            action=new_password_handler,
            args=None,
            loop_continue=True,
            continue_timer=False)


fortigate_statements = FortigateStatements()

#############################################################
# Authentication Statements
#############################################################

authentication_statement_list = [fortigate_statements.new_password_confirmation_stmt,
                                 fortigate_statements.new_password_stmt
                                 ]

connection_statement_list = authentication_statement_list + \
                            pre_connection_statement_list
