
class Coverage:
    """
    Tracks which situation a test has exercised

    Each bin names one situation worth seeing at least once.
    The test samples a bin when the situation occurs and the final percentage reports
    how much of the space was reached.

    Bins are defined by the caller. Sampling an unregistered bin raises "KeyError".
    """
    def __init__(self):

        self.bins = {}

    def add_bin(self, name):

        self.bins[name] = 0

    def sample(self, name):

        self.bins[name] += 1

    def report(self):

        coverage_counter = 0

        if (len(self.bins) != 0):

            for name in self.bins:

                print(f'BIN: {name}, COUNT: {self.bins[name]}')

                if (self.bins[name] > 0):

                    coverage_counter += 1
                
            print(f'Coverage = {coverage_counter / len(self.bins) * 100:.1f}%')

        else:

            print("No coverage bins registered")