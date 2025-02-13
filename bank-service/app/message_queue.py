import json
from pika import BlockingConnection, ConnectionParameters, BasicProperties

from .config import RABBITMQ_HOST, RABBITMQ_PORT


RABBIT_REPLY = "amq.rabbitmq.reply-to"


class MessageQueue:
    # Connect to RabbitMQ

    # Define topic exchange:
    #   - bank.created:
    #       receivers:
    #           email-service
    #   - account.created
    #       receivers:
    #           email-service,
    #           log-service

    # *.created:
    #   email-service
    # account.created:
    #   log-service

    connection_params = ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT
    )

    def on_reply(self, ch, method_frame, properties, body):
        ch.close()
        return body.decode()

    def send_message_to_queue(self, message: dict, queue: str):
        connection = BlockingConnection(self.connection_params)
        channel = connection.channel()
        with connection, channel:
            message = json.dumps(message)

            next(
                channel.consume(
                    queue=RABBIT_REPLY,
                    auto_ack=True,
                    inactivity_timeout=0.1
                )
            )

            # channel.basic_consume(
            #     queue=RABBIT_REPLY,
            #     on_message_callback=self.on_reply,
            #     auto_ack=True
            # )

            channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
            channel.basic_publish(
                exchange="topic_logs",
                routing_key=queue,
                body=message.encode(),
                properties=BasicProperties(reply_to=RABBIT_REPLY)
            )
            print("sent:", message)

            for (method, properties, body) in channel.consume(
                queue=RABBIT_REPLY,
                auto_ack=True,
                inactivity_timeout=0.1
            ):
                response = self.on_reply(channel, method, properties, body)
                print(f'Got response {response}')
                return response
            # channel.start_consuming()
