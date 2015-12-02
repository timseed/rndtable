import pprint
import random

"""
tab and rndtab
Two small classes to assist in the preperation and obfuscation of data for testing purposes
Author: Tim Seed
EMail: tim@sy-edm.com
"""


class tab(object):
    """
    A class that holds data in a 2D

    Attributes:
        rows The number of rows in the table
        cols The number of cols in the table
        data The 2D data object
    """

    def __init__(self, data=""):
        """
        Initialize the class passing in optional data set.
        :param data: a 2D array  [[1,2,3],[4,5,6]]
        :return:
        """

        #print("tab init")
        if not data:
            self.rows = 6
            self.cols = 4
            self.data = [[str.format("r{}c{}", j, i) for i in range(self.cols)] for j in range(self.rows)]
        else:
            try:
                self.setdata(data)
            except Exception as e:
                print(str.format("Error {} occured in setdata", e))

    def dump(self):
        """
        This dumps out the data object using pprint
        """
        pprint.pprint(self.data)

    def setdata(self, data):
        """
        This expects a 2Dimensional array, which it will then store in the class. This will
        recalculate the rows and columns
        :param d:
        :return: nothing
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])


class rndtab(tab):
    """
    Randome Table: Based on tab class
    """

    def __init__(self, data=""):
        """
        Initialize the class passing in optional dataset
        :param data: 2D nested array [[1,2,3],[4,5,6]]
        :return:
        """
        # print("rndtab init")
        super(self.__class__, self).__init__(data=data)
        self.rnddata = []

    def fullrandom(self):
        """
        This will generate random row column data.
        :return: 2D array
        """
        self.rnddata = [
            [self.data[random.randint(0, self.rows - 1)][random.randint(0, self.cols - 1)] for c in range(self.cols)]
            for r in range(self.rows)]
        return self.rnddata

    def random_row(self):
        """
        Generate random data - however data in Column X will only be Randomized with the same ROW X data.
        So if you have a Database table - this ensures the same datatypes
        :return: 2D Randomised array
        """
        self.rnddata = [[self.data[random.randint(0, self.rows - 1)][c] for c in range(self.cols)] for r in
                        range(self.rows)]
        return self.rnddata

    def random_col(self):
        """
        Generate random data - however data in Column X will only be Randomized with the same ROW X data.
        This is not suitable for Database Record Sets which have differing datatypes
        :return: 2D Randomised array
        """

        self.rnddata = [[self.data[r][random.randint(0, self.cols - 1)] for c in range(self.cols)] for r in
                        range(self.rows)]
        return self.rnddata

    def dump(self):
        print("======== Original Data ===========")
        pprint.pprint(self.data)
        print("======== Randomized Data ===========")
        pprint.pprint(self.rnddata)


if __name__ == "__main__":
    t = tab()
    t.dump()
    rt = rndtab()
    print("Full Random")
    rt.fullrandom()
    rt.dump()
    print("Random Row")
    rt.random_row()
    rt.dump()
    print("Random Col")
    rt.random_col()
    rt.dump()
