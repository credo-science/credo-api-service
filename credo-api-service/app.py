from flask import Flask, g

from api import api

app = Flask(__name__)
app.register_blueprint(api)


@app.teardown_appcontext
def close_rabbitmq_connection(exception):
    if hasattr(g, 'rabbitmq_lock'):
        g.rabbitmq_lock.acquire()
        g.rabbitmq_connection.close()
        delattr(g, 'rabbitmq_channel')
        delattr(g, 'rabbitmq_connection')
        delattr(g, 'rabbitmq_lock')
        g.rabbitmq_lock.release()

