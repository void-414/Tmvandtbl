from os import getenv

# User information
API_ID = getenv("API_ID", "")
API_HASH = getenv("API_HASH", "")
USER_SESSION = getenv('USER_SESSION', "")
PORT = int(getenv("PORT", "8080"))

# MongoDB information
DATABASE_URL = getenv('DATABASE_URL', "")
DATABASE_NAME = getenv("DATABASE_NAME", "")

# TMV >> Url And Log
TMV_URL = getenv('TMV_URL', "https://www.1tamilmv.love/")
TMV_LOG = int(getenv("TMV_LOG", ""))

# TBL >> Url And Log
TBL_URL = getenv('TBL_URL', "https://www.1tamilblasters.earth/")
TBL_LOG = int(getenv("TBL_LOG", ""))

# GROTP ID>> 
GROUP_ID = int(getenv("GROUP_ID", ""))
