import numpy as np
from Others.Sort.quick_sort import my_quick_sort
import time


def _check_items(sorted_list, sorted_list_ground):
    if len(sorted_list) != len(sorted_list_ground):
        return False
    for i in range(len(sorted_list)):
        if sorted_list[i] != sorted_list_ground[i]:
            return False
    return True


if __name__ == "__main__":
    def test_acc():
        sample_list = np.random.random_integers(0, 100, 100)
        sample_list = sample_list.tolist()
        sorted_list_ground = sorted(sample_list[:])
        my_quick_sort(sample_list, 0, len(sample_list) - 1)
        # print(sample_list)
        # print(sorted_list_ground)
        return _check_items(sample_list, sorted_list_ground)

    # ---------------------------------------------------
    times = 10000
    t1 = time.time()
    for i in range(times):
        assert test_acc()
    print("{} times, using {}s".format(times, time.time() - t1))
