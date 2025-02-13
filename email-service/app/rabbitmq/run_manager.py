import asyncio

from .message_queue import MessageQueueServer
from ..logging import logger


class MessageQueueManager:
    async def start_messages_listener(self):
        logger.info('Initializing message listener.')
        self.mqserver = MessageQueueServer()

        logger.info('Starting message listener in background.')
        self.task = asyncio.create_task(self.mqserver.run())

    async def stop_message_listener(self):
        logger.info('Stopping message listener.')
        if self.mqserver:
            await self.mqserver.close()
        if self.task:
            logger.info('Cancelling message listener task.')
            self.task.cancel()
