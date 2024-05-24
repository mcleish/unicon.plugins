'''
Author: Adam Mcleish
Contact: adam.mcleish@gmail.com
https://github.com/mcleish

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example

Description:
    This subpackage defines patterns for Fortigate Firewalls
'''

from unicon.plugins.generic.patterns import GenericPatterns


class FortigatePatterns():
    def __init__(self):


        # This system is for authorized use only.
        # login: admin
        # Password:
        self.login_prompt = r'^(.*?)login:\s*$'
        self.password_prompt = r'^(.*?)Password:\s*$'

        # New Password:
        # Confirm Password:
        self.new_pw_prompt = r'^.*New Password:'
        self.confirm_new_pw_prompt = r'^(.*?)Confirm Password:\s*$'
        
        # Last login: Tue Mar 23 22:11:15 on ttyS0
        # hostname #
        self.global_prompt = r'^(.*?)FortiOS-VM64-KVM(.*?)#\s*$'

