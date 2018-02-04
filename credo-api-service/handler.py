from validator import validate, ValidationException
from flask import g
import pika
import config
from threading import Lock

EXCHANGE_NAME = 'detections'
QUEUE_NAME = 'detections_save'


def handle_detection(message):
    validate(message)
    send_message(message)


def send_message(message):
    # TODO: move to app context initialization?
    if not hasattr(g, 'rabbitmq_lock'):
        g.rabbitmq_lock = Lock()
        g.rabbitmq_lock.acquire()
        g.rabbitmq_connection, g.rabbitmq_channel = connect_rabbitmq()
        g.rabbitmq_lock.release()

    g.rabbitmq_lock.acquire()
    g.rabbitmq_channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='', body=message)
    g.rabbitmq_lock.release()


def connect_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config.RMQ_HOST))
    channel = connection.channel()

    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')

    result = channel.queue_declare(queue=QUEUE_NAME, durable=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name)

    return connection, channel
