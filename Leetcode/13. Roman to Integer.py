class Solution:
    def romanToInt(self, s: str) -> int:
        r2i_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        for c_idx, c in enumerate(s):
            if c_idx < len(s) - 1 and r2i_map[s[c_idx + 1]] > r2i_map[c]:
                res -= r2i_map[c]
            else:
                res += r2i_map[c]
        return res