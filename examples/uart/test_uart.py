import cocotb
from uart_driver import UartDriver
from uart_monitor import UartMonitor
from uart_transaction import UartTransaction
from cocotb.triggers import ClockCycles
from hdl_verify.harness import harness

#register function with cocotb
@cocotb.test()
#define asynchronous function with dut as parameter
async def uart_test(dut):
    
    #await the call to harness
    await harness(dut.i_clk, 10, "ns")

    #set and start driver
    driver = UartDriver(dut)
    driver.start()

    uart_monitor = UartMonitor(dut)

    def temporary_subscriber(arg):

        print(arg)

    uart_monitor.add_subscriber(temporary_subscriber)

    uart_monitor.start()

    #send test data
    driver.send(UartTransaction(0xA5))
    driver.send(UartTransaction(0x3C))
    driver.send(UartTransaction(0xFF))

    #pause until 3000 cycles have passed
    await ClockCycles(dut.i_clk, 3000)

    #print a message verifying the clock works
    dut._log.info("Test run")