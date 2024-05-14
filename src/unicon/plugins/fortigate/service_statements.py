"""
Module:
    unicon.plugins.service.nxos

Authors:
    pyATS TEAM (pyats-support@cisco.com, pyats-support-ext@cisco.com)

Description:
    Module for defining all Services Statement, handlers(callback) and Statement
    list for service dialog would be defined here.
"""
from time import sleep

from unicon.eal.dialogs import Statement
from unicon.plugins.fortigate.patterns import FortigatePatterns
from unicon.plugins.fortigate.service_patterns import FortigateProvisioningPatterns
from unicon.utils import to_plaintext

from unicon.plugins.generic.service_statements import send_response,\
    login_handler, password_handler, connection_closed_stmt
from unicon.plugins.generic.service_statements import save_env,\
    reload_proceed, auto_install_dialog, \
    setup_dialog, config_byte, login_notready, redundant, confirm_reset,\
    press_enter, confirm_config, module_reload, save_module_cfg,\
    secure_passwd_std

from unicon.plugins.utils import (get_current_credential,
    common_cred_username_handler, common_cred_password_handler, )


def run_level():
    sleep(100)


def nxos_system_up():
    sleep(100)


def new_password_handler(spawn, context, session):
    print("its working?")
    credentials = context.get('credentials')
    new_credential_password = credentials.get('default', {}).get('password')
    new_password = to_plaintext(new_credential_password)
    sleep(0.1)
    spawn.sendline(new_password)
    sleep(0.1)


# Additional statement specific to nxos
pat = FortigateProvisioningPatterns()

new_password = Statement(pattern=pat.new_password,
                   action=new_password_handler,
                   args=None,
                   loop_continue=True,
                   continue_timer=True)


