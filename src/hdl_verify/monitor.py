import cocotb

class Monitor:
    """
    Base class for bus monitors.

    Monitor observes DUT pins and reconstructs transactions.

    Base owns the observation loop and subscriber list. Subclasses
    implement "recover_one", which should watch pins and return one transaction.
    Each transaction is published to each subscriber so a socreboard and coverage collecter
    can both listen.

    USE:
        monitor = UartMonitor(dut)
        monitor.add_subscriber(scoreboard.check)
        monitor.add_subscriber(coverage.sample)
        monitor.start()
    """

    def __init__(self):

        self.subs = []
    
    def add_subscriber(self, callback):

        self.subs.append(callback)

    def start(self):

        cocotb.start_soon(self._run())

    async def _run(self):

        while True:

            transaction = await self.recover_one()

            for sub in self.subs:
                sub(transaction)

    async def recover_one(self):

        raise NotImplementedError
