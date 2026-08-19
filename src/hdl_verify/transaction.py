
class Transaction:
    """
    Base class for all transactions. Each subclass defines their own payload
    
    Two behaviors
    1. __repr__ returns a readble string when a scoreboard reports a mismatch
    2. __eq__ returns a boolean when two transactions are compared
    """

    def __repr__(self):
        fields = ", ".join(f"{name}={value}" for name, value in self.__dict__.items())
        return f"{type(self).__name__}({fields})"

    def __eq__(self,other):
        return type(self) is type(other) and self.__dict__ == other.__dict__