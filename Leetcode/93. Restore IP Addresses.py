from typing import List
import re

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(substr):
            # return re.match("^(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$", substr)
            if int(substr) > 255 or substr[0] == "0" and len(substr) >=2:
                return False
            return True
        valid_ips = []
        def backtrace(ip_str, s, level):
            if s == "" and level == 4:
                valid_ips.append(ip_str)
            for idx in range(1, min(len(s) + 1, 4)):
                if level == 2 and len(s) - idx > 3:
                    continue
                substr = s[:idx]
                if is_valid(substr):
                    sep = "" if ip_str == "" else "."
                    backtrace(ip_str + sep + substr, s[idx:], level + 1)
        backtrace("", s, 0)
        return valid_ips

if __name__ == "__main__":
    s = Solution()
    for str_ in {"101023", "25525511135", "172162541"}:
        print(s.restoreIpAddresses(str_))

    # def is_valid(substr):
    #     return re.match("^(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$", substr)
    # for n in {"17", "216"}:
    #     print(is_valid(n))