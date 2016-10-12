class BinarySearch(list):
    def __init__(self, a, b):
        """
        Initialise this class
        :param a: length of the list to be created
        :param b: step or difference between consecutive values
        """
        self.length = a
        for i in range(b, a * b + b, b):
            self.append(i)

    def search(self, val):
        res = {'count': 0}
        array = sorted(self)
        left = 0
        right = len(self) - 1
        while left <= right:
            res['count'] += 1
            middle = (left + right) / 2
            if array[middle] < val:
                left = middle + 1
            elif array[middle] > val:
                right = middle - 1
            else:
                res['index'] = middle
                return res
        # val not found
        res['index'] = -1
        return res
