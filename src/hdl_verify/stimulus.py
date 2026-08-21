import random

def generate_values(count, low, high, directed = None):
    """
    Generate a list of test values using directed and random test cases

    Directed values are placed first. Then, random values are generated within the provided range.

    The randomness comes from Python's "random" module, which cocotb seeds and reports at startup.
    So a run can be reproduced by setting "COCOTB_RANDOM_SEED" to the value from its log.

    Args:
        count: total number of values to return
        low: minimum legal value, inclusive
        high: Maximum legal value, inclusive
        directed: values that must appear, typically value cases
    
    Returns:
        A list of integers to use in testing
    """
    if (directed is None):
        directed = []
    
    test_vals = list(directed)

    while(len(test_vals) < count):
        
        test_vals.append(random.randint(low, high))

    return test_vals


