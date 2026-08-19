from hdl_verify.transaction import Transaction

class UartTransaction(Transaction):
    """
    One byte over UART

    Start Bit -> 8 Data Bits -> Stop Bit

    Arguments:
        data: The byte value
    """
    
    def __init__(self, data):
        self.data = data

