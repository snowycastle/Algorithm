# -*- coding:utf-8 -*-

def heapify(unsorted, index, heap_size):
    left = 2 * (index + 1) - 1
    right = 2 * (index + 1)

    if left < heap_size and unsorted[left] > unsorted[index]:
        largest = left
    else:
        largest = index

    if right < heap_size and unsorted[right] > unsorted[largest]:
        largest = right
    else:
        pass

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    # build max heap
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    # sort
    for i in range(n - 1, 0, -1):
        unsorted[i], unsorted[0] = unsorted[0], unsorted[i]
        heapify(unsorted, 0, i)


if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]

    heap_sort(unsorted)

    print(unsorted)
