# Mask Detection API
This is a REST implementation of the mask detection script created by @chandrikadeb7 (https://github.com/chandrikadeb7/Face-Mask-Detection) using TensorFlow and Keras, written in Python. This project is implemented using the Falcon microframework, managed by supervisor processes and containerized using Docker &amp; Docker Compose.

------------

There are 2 ways to start this project : 

i) **Docker** : This is the easiest way to start this project. If you've docker and docker-compose installer, we could simply run : `docker-compose up -d` in the root folder of the project.

ii) **Local Deployment**: To run this project without Docker, you would have to follow the following steps:
- Create a virtualenv by using : `virtualenv -p python3 .` and install the required packages using : `pip install -r requirements.txt`.
- Next head to the constants file (`utils/constants.py`), and replace BASE_PATH with the path to the folder in which your code is stored.
- We're now ready to startup the API. Run the command : `gunicorn app:api --worker-class gevent -w 1  --bind 0.0.0.0:811` to start the worker for the API.

------------

![](https://github.com/divyam-rai/mask-detection-api/blob/master/MaskDetectionDemo.gif)
