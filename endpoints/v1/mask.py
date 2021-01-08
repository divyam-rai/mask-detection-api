import os
import sys
sys.path.append(os.getenv('BASEPATH'))

import falcon
from utils import constants as cst, general as hp
from services import mask as service
logger = hp.get_logger("mask_endpoint", cst.LOGGER["mask_endpoint"])

class Mask():
    _storage_path = cst.STORAGE_PATH

    def on_get(self, res, resp):
        resp.body = hp.response(200, "SUCCESS", {'name' : 'Ishika Kalwani'}, {})

    def on_post(self, req, resp):
        try:
            input_file = req.get_param('file', None)
            if input_file == None:
                resp.body = hp.response(400, "NO_FILE", {}, {})
                logger.info("No file has been uploaded")
                return
            ext = input_file.filename.split(".")[1]
            logger.info("File extension " + ext)
            if ext not in cst.ACCEPTED_FILE_FORMATS:
                resp.body = hp.response(400, "INVALID_FILE", {}, {})
                logger.info("Wrong full format")
                return
            filename = hp.generate_id_or_pwd(9) + "." + ext
            file_path = os.path.join(self._storage_path, filename)
            temp_file_path = file_path + '~'
            open(temp_file_path, 'wb').write(input_file.file.read())
            os.rename(temp_file_path, file_path)
            result = service.mask_image(file_path)
            os.remove(file_path)
            resp.body = hp.response(200, "Success", result, {})
        except Exception as e:
            logger.error("Something went wrong")
            logger.error(str(e))
            resp.body = hp.response(500, "Error", {}, {})
