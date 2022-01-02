import fractions
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if (str1 + str2 == str2 + str1):
		    # Python3 uses math.gcd
            gcd = fractions.gcd(len(str1), len(str2))
            return str1[:gcd]
        else:
            return ''
