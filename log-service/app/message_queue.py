import asyncio
import json
from typing import Optional, Callable, Dict, Any
from aio_pika import connect, Connection, Queue
from aio_pika.abc import AbstractIncomingMessage
from aio_pika.exceptions import AMQPError

from .config import settings
from .logging import logger
from .db import get_db_client


RABBITMQ_URL = str(settings.amqp_dsn)


async def save_message(log: Dict[str, Any]) -> None:
    db = await get_db_client()
    db_collection = settings.get_mongodb_collection('logs')

    await db[db_collection].insert_one(log)
    logger.info('Message saved to data storage')


async def on_message(message: AbstractIncomingMessage) -> Optional[Dict[str, Any]]:
    try:
        decoded_message = message.body.decode()
        logger.info(f'Processed message content: {decoded_message}')

        await message.ack()
        logger.info('Message acknowledged')

        return json.loads(decoded_message)
    except Exception as e:
        logger.error(f'Error processing message: {e}')
        await message.nack(requeue=True)
        logger.warning('Message nack with requeue')

        return None


async def save_queue_messages(queue: Queue, on_message: Callable) -> None:
    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            decoded_message = await on_message(message)
            if decoded_message is None:
                continue
            logger.info(f'listener: {decoded_message}')

            await save_message(decoded_message)


async def listen() -> None:
    while True:
        try:
            logger.info('Connecting to RabbitMQ...')
            connection = await connect(RABBITMQ_URL)
            async with connection:
                channel = await connection.channel()
                queue = await channel.declare_queue('log-service', durable=True)

                logger.info('Waiting for messages.')
                await save_queue_messages(queue, on_message)

        except AMQPError as e:
            logger.error(f'RabbitMQ connection error: {e}')
            logger.info('Reconnecting in 5 seconds...')
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f'Unexpected error in listen function: {e}')
            logger.info('Reconnecting in 5 seconds...')
            await asyncio.sleep(5)


async def start_messages_saver():
    logger.info('Starting message saver in background...')
    asyncio.create_task(listen())
