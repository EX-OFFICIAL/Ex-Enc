import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from ex import main

    main()

elif bit == '32bit':

    from ex2 import main

    main()import os, platform
print('\033[1;92mCONGRATULATIONS YOUR DEVICE HAS BEEN SUPPORT THIS TOOLS')
try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from ex import main

    main()

elif bit == '32bit':

    from ex import main

    main()in()
