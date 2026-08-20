from hdl_verify.driver import Driver
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge

class UartDriver(Driver):
    """
    Drives UART transactions ont a uart_tx DUT.

    pin-level protocol:
    present the byte, pulse data-valid for one clock.
    Then wait until the frame is finished before returning.
    Driver stays correct for any baud rate and prevents a new byte
    from being started before the previous frame is finished.

    Queue and dispatch loops come from the Driver class, this only supplies drive_one

    Arguments:
        dut: DUT, expected to have i_clk, i_tx_byte, i_tx_dv, and o_tx_active
    """
    def __init__(self, dut):

        super().__init__()

        self.dut = dut

    async def drive_one(self, transaction):

        self.dut.i_tx_byte.value = transaction.data

        self.dut.i_tx_dv.value = 1

        await RisingEdge(self.dut.o_tx_active)

        self.dut.i_tx_dv.value = 0

        await FallingEdge(self.dut.o_tx_active) 
