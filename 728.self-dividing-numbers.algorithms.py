class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for num in range(left, right+1):
            str_num = str(num)
            if '0' in str_num:
                continue
            skip_num = False
            for digit in str_num:
                if num % int(digit) != 0:
                    skip_num = True
                    break
            if skip_num:
                continue
            nums.append(num)
        return nums
