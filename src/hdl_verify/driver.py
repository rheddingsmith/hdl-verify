import cocotb
from cocotb.queue import Queue


class Driver:
    """
    Base calss for transaction drivers.

    drivers turn transactions into pin-level activity on the DUT.
    It uses an internal queue and a background loop pulls from it.

    Still need to implement "drive_one" to do the pin-level work. Everything else is handled already

    USE:

        driver = UartDriver(dut)
        driver.start()
        driver.send(UartTransaction(0xA5))
    """

    def __init__(self):

       self.queue = Queue()

    def send(self, transaction):

        self.queue.put_nowait(transaction)

    def start(self):

        cocotb.start_soon(self._run())

    async def _run(self):

        while True:
            transaction = await self.queue.get()
            await self.drive_one(transaction)

    async def drive_one(self, transaction):

        raise NotImplementedError





