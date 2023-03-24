from ecm.lab_6.task_6_1 import merge_start


def test_merge_start():
    assert merge_start([1, 4, 5, 6], [2, 3, 7, 8]) == ([1, 2, 3, 4, 5, 6, 7, 8], [0, 4, 5, 1, 2, 3, 6, 7])
