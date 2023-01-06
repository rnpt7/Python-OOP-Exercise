"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Construct a new serial generator starting at start"""
        self.start = start
        self.current = start

    def generate(self):
        """Generates the next serial number, and returns the current serial number"""
        serial = self.current
        self.current += 1
        return serial
    
    def reset(self):
        """Reset the serial generator to the start parameter"""
        self.current = self.start
