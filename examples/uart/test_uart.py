import cocotb
from uart_model import uart_model
from uart_driver import UartDriver
from uart_monitor import UartMonitor
from uart_monitor import UartInputMonitor
from uart_transaction import UartTransaction
from uart_coverage import UartCoverage
from hdl_verify.stimulus import generate_values
from hdl_verify.scoreboard import Scoreboard
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

    #Create and set the coverage object
    coverage = UartCoverage()
    coverage.register_bins()

    #create the output monitor
    uart_monitor = UartMonitor(dut)

    #create the input monitor
    uart_input_monitor = UartInputMonitor(dut)

    #create the scoreboard
    scoreboard = Scoreboard()

    #create temporary subscribers to test the monitors
    #Pass output argument to the scoreboard sample coverage
    def subscriber(arg):
        
        scoreboard.check(arg)
        coverage.sample_bins(arg)

        print(f'OUT: {arg}')

    #Pass input argument through golden model then to the scoreboard
    def input_subscriber(arg):

        scoreboard.expect(uart_model(arg))

        print(f'IN: {arg}')

    #add the subscribers and start monitors before sending data
    uart_monitor.add_subscriber(subscriber)
    uart_monitor.start()
    uart_input_monitor.add_subscriber(input_subscriber)
    uart_input_monitor.start()

    #Generate test data
    test_vals = generate_values(10, 0, 0xFF, [0x00, 0xFF, 0x01, 0x80, 0x55])

    #Send test data
    for i in test_vals:
        driver.send(UartTransaction(i))
    
    #pause until 20000 cycles have passed
    await ClockCycles(dut.i_clk, 20000)

    #Report coverage
    coverage.report()

    #Check the scoreboard's report
    scoreboard.report()

    #print a message verifying the clock works
    dut._log.info("Test run")