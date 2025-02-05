import json
from pika import BlockingConnection, ConnectionParameters


class MessageQueue:
    connection_params = ConnectionParameters(
        host='rabbitmq',
        port=5672
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
