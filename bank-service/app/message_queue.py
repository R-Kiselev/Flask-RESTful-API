import json
from pika import BlockingConnection, ConnectionParameters

from .config import RABBITMQ_HOST, RABBITMQ_PORT


class MessageQueue:
    connection_params = ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT
    )

    def send_message_to_queue(self, message: dict, queue: str):
        with BlockingConnection(self.connection_params) as connection:
            with connection.channel() as channel:
                message_json = json.dumps(message)

                channel.queue_declare(queue=queue, durable=True)

                channel.basic_publish(
                    exchange='',
                    routing_key=queue,
                    body=message_json
                )

                print(f"Sent: {message}")
