from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        loop
        '''
        letters = []

        def append_new_letters(start_c, bag_size):
            if len(letters) == 0:
                return [chr(ord(start_c) + i) for i in range(bag_size)]
            else:
                return [c + chr(ord(start_c) + i) for c in letters for i in range(bag_size)]

        for d in digits:
            if d == "7":
                letters = append_new_letters("p", 4)
            elif d == "8":
                letters = append_new_letters("t", 3)
            elif d == "9":
                letters = append_new_letters("w", 4)
            else:
                letters = append_new_letters(chr((ord(d) - ord("2")) * 3 + ord("a")), 3)
        return letters

    def __init__(self):
        self.start_letter = [chr(d * 3 + ord("a")) for d in range(5)] + ["p", "t", "w"]
        self.bag_size = [3 for _ in range(8)]
        self.bag_size[5] = 4
        self.bag_size[7] = 4

    def letterCombinations_rec(self, digits: str) -> List[str]:
        '''
        recursion
        '''
        if len(digits) == 0:
            return []

        c_idx = ord(digits[-1]) - ord("2")
        start_c = self.start_letter[c_idx]
        bag_size = self.bag_size[c_idx]
        pre_digits = digits[:-1]
        if len(pre_digits) == 0:
            return [chr(ord(start_c) + i) for i in range(bag_size)]
        return [c + chr(ord(start_c) + i)
                for c in self.letterCombinations_rec(pre_digits)
                for i in range(bag_size)]

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations_rec("23"))