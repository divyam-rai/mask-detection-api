import sys
BASE_PATH = "/usr/src/app"
sys.path.append(BASE_PATH)

STORAGE_PATH = BASE_PATH + '/uploaded_files'

LOGGER = {
    "mask_endpoint" : BASE_PATH + "/logs/mask_endpoint.log",
    "mask_service" : BASE_PATH + "/logs/mask_service.log",
    "authorization" : BASE_PATH + "/logs/authorization.log"
}

ACCEPTED_FILE_FORMATS = ["jpg", "png"]

REDIS_HOST = ""
REDIS_PORT = 0000
REDIS_SESSION_MAP = "MASK_DETECTION_SERVICE"

ENCRYPTION_KEY = "Vsa8BD+YQ1obQbfhudCPy2kn/x6O7Io="
ENCRYPT_RESPONSE = False

ROUTE_PREFIX = "/api/v1"

REQUIRED_FIELDS_MAP = {
    
}

ERROR_TITLES = {
    "HTTP_400": "Forbidden",
    "HTTP_401": "Unauthorized",
    "HTTP_404": "Not Found",
    "HTTP_500": "Unhandled Exception",
    "HTTP_202": "Accepted",
    "HTTP_200": "Ok"
}

ERROR_CODE = {
    "MISSING_REQUIRE_PARAMETER": "MISSING_REQUIRE_PARAMETER",
}

ARGS = {
    "face" : BASE_PATH + "/utils/face_detections/face_detector",
    "image" : "",
    "model" : BASE_PATH + "/utils/face_detections/mask_detector.model",
    "confidence" : 0.6
}