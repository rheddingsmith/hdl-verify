
class Scoreboard:
    """
    Compares observed DUT output against the expected results

    Expected value is registered when the DUT accepts a request. 
    The matching result appears later once the DUT has produced it.
    Each incoming actual is matched agianst the oldest queued value.

    """
    def __init__(self):

        self.expected = []
        self.matches = 0
        self.mismatches = 0

    def expect(self, transaction):

        self.expected.append(transaction)

    def check(self, transaction):

        assert(len(self.expected) > 0), "DUT produced an output with nothing pending"

        queued_val = self.expected.pop(0)
        if (queued_val == transaction):

            self.matches += 1
        
        else:

            self.mismatches += 1
            print(f'Mismatch Detected. expected = {queued_val}, actual = {transaction}')

    def report(self):

        print(f'Matches: {self.matches}')
        print(f'Mismatches: {self.mismatches}')

        assert(self.mismatches == 0), f'{self.mismatches} Mismatches detected'

        assert(len(self.expected) == 0), "Not all values checked"




