class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # intmax is 2147483647
        # max x such that x <=intmax and rev(x) <= inmax = 2147447412
        if x > 2147447412:
            return 0
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while(x):
            rev = rev * 10 + x % 10
            x /= 10
        rev *= sign
        return rev