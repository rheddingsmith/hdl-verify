import cocotb
from cocotb.triggers import ClockCycles
from hdl_verify.harness import harness

#register function with cocotb
@cocotb.test()
#define asynchronous function with dut as parameter
async def uart_test(dut):
    
    #await the call to harness
    await harness(dut.i_clk, 10, "ns")
    #pause until 10 cycles have passed
    await ClockCycles(dut.i_clk, 10)
    #print a message verifying the clock works
    dut._log.info("Test run")