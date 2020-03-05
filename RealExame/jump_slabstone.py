
if __name__ == "__main__":
    inp = input()
    inps = inp.split(" ")
    n, m = int(inps[0]), int(inps[1])
    invalid = 1 << 31
    steps = [invalid for _ in range(m + 1)]  # the min steps from i to m
    steps[m] = 0
    for i in range(m - 1, n - 1, -1):
        for j in range(2, i):  # look for a possible prime number
            if j ** 2 > i:
                break
            if i % j == 0 and i + j <= m:
                steps[i] = min(steps[i + j] + 1, steps[i])
            if i % j == 0 and i + i // j <= m:
                steps[i] = min(steps[i + i // j] + 1, steps[i])
    print steps[n]


