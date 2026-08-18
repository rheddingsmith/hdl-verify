import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

async def harness(clock, period = 10, unit = "ns", reset = None, rst_active = 1, rst_cycles = 5):
    """
    Start the DUT's clock and apply a reset if it has one

    Arguments are passed as a signal so the function can work with any DUT

    Arguments:
        clock = connect to the DUT's clock (ex: dut.i_clk)
        period = Clock period
        unit = unit of time for the period
        reset = connect to the DUT's reset (defaults to None)
        rst_active = the value that causes a reset (1 for active high, 0 for active low. defaults to 1)
        rst_cycles = number of clock cycles the reset holds for (defaults to 5)

    Returns:
        The running clock object
    """

    clk = Clock(clock, period, unit)
    cocotb.start_soon(clk.start())

    if (reset is not None):
        reset.value = rst_active
        await ClockCycles(clock, rst_cycles)
        reset.value = rst_active ^ 1
        await ClockCycles(clock, 1)

    return clk
    

    
    