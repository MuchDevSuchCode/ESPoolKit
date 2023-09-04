from config import const as SETTINGS
from services import networkSetup

import machine
import socket

networkSetup.do_connect()