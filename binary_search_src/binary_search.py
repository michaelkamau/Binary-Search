class BinarySearch(list):
    def __init__(self, a, b):
        """
        Initialise this class
        :param a: length of the list to be created
        :param b: step or difference between consecutive values
        """
        length = a
        for i in range(a):
            self.append(i+b)
