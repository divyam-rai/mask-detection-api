import os
import sys
sys.path.append(os.getenv('BASEPATH'))

import falcon
from falcon_auth.backends import AuthBackend
from utils import constants as cst, general as hp
from utils.redis import Redis

r_redis = Redis()

logger = hp.get_logger("authorization", cst.LOGGER["authorization"])

class Authorization(AuthBackend):
    def __init__(self):
        self.user_loader = ""

    def authenticate(self, req: falcon.Request, resp: falcon.Response, resource):
        return True