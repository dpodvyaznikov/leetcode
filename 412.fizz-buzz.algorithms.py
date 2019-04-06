class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for num in range(1, n + 1):
            div_by_three = (num % 3 == 0)
            div_by_five = (num % 5 == 0)
            string = ''
            if div_by_three:
                string += 'Fizz'
            if div_by_five:
                string += 'Buzz'
            if not string:
                string = str(num)
            result.append(string)
        return result
