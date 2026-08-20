from hdl_verify.monitor import Monitor
from uart_transaction import UartTransaction
from cocotb.triggers import FallingEdge
from cocotb.triggers import ClockCycles
from cocotb.triggers import RisingEdge

class UartMonitor(Monitor):
    """
    Recovers UART transactions

    Implements the receiver side of an 8N1 framing.
    Waits for the start-bit, delays half a bit-time to sample at the center
    of each bit. Then, samples eight times, once at each bit, and reassembles the byte,
    LSB first.

    Arguments:
        dut: DUT handle, needs "i_clk" and "o_tx_serial" signals
        clks_per_bit: The clock cycles per bit period. Must match the value
        from the DUT. Defaults to 87.
    """
    def __init__(self, dut, clks_per_bit = 87):

        super().__init__()
        
        self.dut = dut
        self.clks_per_bit = clks_per_bit

    async def recover_one(self):

        await FallingEdge((self.dut.o_tx_serial))

        await ClockCycles(self.dut.i_clk, self.clks_per_bit // 2)

        byte = 0

        for i in range(8):

            await ClockCycles(self.dut.i_clk, self.clks_per_bit)

            byte |= int(self.dut.o_tx_serial.value) << i 

        await ClockCycles(self.dut.i_clk, self.clks_per_bit)

        return UartTransaction(byte)



class UartInputMonitor(Monitor):
    """
    Observes bytes accepted by the transmitter

    Wathces the request side of the interface. Transactions represent what the
    DUT was given. Expected values will derive from actual observed values instead
    of from the intended test value.

    Arguments:
        dut: DUT handle, expected values "i_tx_byte" and "o_tx_active"
    """
    def __init__(self, dut):

        super().__init__()
        
        self.dut = dut
    
    async def recover_one(self):

        await RisingEdge((self.dut.o_tx_active))

        byte = int(self.dut.i_tx_byte.value)

        return UartTransaction(byte)


    

