import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

#register function with cocotb
@cocotb.test()
#define asynchronous function with dut as parameter
async def uart_test(dut):
    
    #create clock (100 MHz) and store as clk
    clk = Clock(dut.i_clk, 10, "ns")
    #.start to create coroutine and .start_soon to run in background
    cocotb.start_soon(clk.start())
    #pause until 10 cycles have passed
    await ClockCycles(dut.i_clk, 10)
    #print a message verifying the clock works
    dut._log.info("Test run")