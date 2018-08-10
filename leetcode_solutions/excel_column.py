class Solution:
    def __init__(self):
        self.dir = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',           'W', 'X', 'Y', 'Z']
    def test(self, n):
        """
        :type n: int
        :rtype: str
        """
        sol=''
        n=n-1
        if n <= 25:
            return 0, self.dir[n]
        x=n
        while x >=26:
            x = int(x/26)
            if x >= 26:
                x, t = self.test(x)
                sol = sol + t
            else:
                sol = sol + self.dir[x-1]
        sol = sol + self.dir[n%26]
        return x, sol

    def convertToTitleUsingRecursion(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        distance = ord('A')

        while n > 0:
            y = (n-1) % 26
            n = (n-1) // 26
            print(n)
            s = self.dir[y]
            result = ''.join((s, result))
        return result


    # solution using simple while loop

    def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    diary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V',                'W', 'X', 'Y', 'Z']
    l = len(diary)
    output = ''
    rem = 0
    n = n-1
    while(n >= 0):
        if n<26:
            output = diary[n] + output
            break
        rem = n%26
        n = int(n/26)-1
        output = diary[rem] + output
    return output

sol = Solution()
print(sol.convertToTitle(53))
