import numpy as np

np.random.seed(1)

class TausGenerator(object):
    """
    Implementing the Tausworthe Generator
    """
    def __init__(self, l, r, q, n):
        """
        Args:
            l (int): length of binary series (eg. 0000 1111 means l = 8)
            r, q (int): preset constants for generation, 2^q - 1 defines the space
                of unique numbers
            n (int): number of PRNs to be generated
        """
        self.l = l
        self.r = r
        self.q = q
        self.n = n
        self.denominator = (1 << l)

    def dec2bin(self, x):
        """
        convert a decimal integer to a binary str with fixed length of self.l
        """
        return bin(x)[2:].zfill(self.l)[-self.l:]

    def normalize(self, x):
        """
        convert a decimal integer to a normalized integer
        """
        return int(self.dec2bin(x), 2)

    def arr2float(self, x):
        """
        convert an array of binary numbers to float:
            [1,0,1,0] -> 1010 -> 10/16
        """
        dec = int('0b' + ''.join(x.astype(str)),2)
        return self.dec2float(dec)

    def dec2float(self, x):
        """
        convert a normalized integer to a float by dividing 2**self.l
        """
        return x/self.denominator

    def initialize(self):
        self.seq = np.random.randint(low=0, high=2, size=self.q) 

    def generate_series(self):
        self.initialize()
        for i in range(self.q, self.l*self.n):
            if self.seq[i-self.r] == self.seq[i-self.q]:
                digit = 0
            else:
                digit = 1
            self.seq = np.append(self.seq, digit)

    def makefloat(self):
        """
        turn numbers in seq to float numbers
        """
        self.seq = self.seq.reshape((-1, self.l))
        return np.apply_along_axis(self.arr2float, 1, self.seq)

    def generate(self):
        self.generate_series()
        return self.makefloat()

