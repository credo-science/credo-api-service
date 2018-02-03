import os

RMQ_HOST = os.environ['RMQ_HOST'] if 'RMQ_HOST' in os.environ.keys() else "localhost"
