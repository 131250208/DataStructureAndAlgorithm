def replaceSpace(self, s):
    # write code here
    count = 0
    for c in s:
        if c == " ":
            count += 1

    s_new = s + "_" * (count * 2)
    p2, p1 = len(s_new - 1), len(s - 1)
    s = s_new
    while p1 != 0:
        if s[p1] != " ":
            s[p2] = s[p1]
            p1 -= 1
            p2 -= 1
        else:
            s[p2] = "0"
            p2 -= 1
            s[p2] = "2"
            p2 -= 1
            s[p2] = "%"
            p2 -= 1
            p1 -= 1
    return s_new
if __name__ == "__main__":
    s = ""
    print(replaceSpace(s))