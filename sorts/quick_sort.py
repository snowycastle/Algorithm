# -*- coding:utf-8 -*-
import random


def quick_sort(collection):
    length = len(collection)

    if length <= 1:
        return collection
    else:
        p = collection[0]

        less = [x for x in collection[1:] if x <= p]
        large = [x for x in collection[1:] if x > p]

        return quick_sort(less) + [p] + quick_sort(large)


if __name__ == '__main__':
    unsorted = [random.choice(range(10)) for x in range(10)]
    print(f'unsorted:{unsorted}')

    print(f'sorted:{quick_sort(unsorted)}')
