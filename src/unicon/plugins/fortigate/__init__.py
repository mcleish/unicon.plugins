'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://github.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

from unicon.plugins.generic.connection_provider import GenericSingleRpConnectionProvider
from unicon.plugins.generic import GenericSingleRpConnection, ServiceList
from unicon.plugins.generic import service_implementation as svc
from unicon.plugins.linux import service_implementation as linux_svc
from unicon.plugins.fortigate import service_implementation as fortigate_svc
from unicon.plugins.generic import GenericSingleRpConnectionProvider
from unicon.plugins.fortigate.statemachine import FortigateStateMachine
from unicon.plugins.fortigate.settings import FortigateSettings
from time import sleep







class FortigateConnectionProvider(GenericSingleRpConnectionProvider):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # used for tracking the initial state - it impacts the commands used
        # for state changes
        self.initial_state = ''

    def init_handle(self):
        con = self.connection
        print("im using you")
        self.initial_state = con.state_machine.current_state
        

        # The state machine path commands are different depending on the
        # initial state. If the default shell is configured to be 'expert'
        # mode the path commands are:
        #   'clish' for expert -> clish
        #   'exit' for clish -> expert

        # If the initial state is determined to be 'expert' mode, the
        # commands are updated and the switchto service is used to put
        # the gateway into clish mode.



        self.execute_init_commands()

    def disconnect(self):
        """ Logout and disconnect from the device
        """

        con = self.connection
        if con.connected:
            con.log.info('disconnecting...')
            con.switchto(self.initial_state)
            con.sendline('exit')
            sleep(2)
            con.log.info('closing connection...')
            con.spawn.close()


class ForitgateServiceList(ServiceList):
    """ gaia services """
    def __init__(self):
        super().__init__()

        self.execute = fortigate_svc.FortigateExecute
        self.sendline = svc.Sendline
        self.ping = linux_svc.Ping
        self.switchto = fortigate_svc.FortigateSwitchTo


class FortigateConnection(GenericSingleRpConnection):
    """
    Connection class for Gaia OS connections
    """

    os = 'fortigate'
    platform = None
    chassis_type = 'single_rp'
    state_machine_class = FortigateStateMachine
    connection_provider_class = FortigateConnectionProvider
    subcommand_list = ForitgateServiceList
    settings = FortigateSettings()
