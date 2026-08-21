from uart_transaction import UartTransaction

def uart_model(observed_transaction):
    """
    Models the DUT's behavior: A byte is presented as a parallel input and appears
    unaltered on the serial output. Any other behavior is a bug

    Arguments:
        observed_transaction: What the input monitor logged as the DUT accepting

    Returns:
        The expected transaction on the output's side.
    """
    return UartTransaction(observed_transaction.data)