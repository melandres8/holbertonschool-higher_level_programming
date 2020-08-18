#!/usr/bin/python3
""" CachamaLover 4ever """


def findPeakUtil(arr, low, high, n):
    """ Find peak util """
    mid = low + (high - low)/2
    mid = int(mid)
    if arr == []:
        return None
    if mid == 0 or arr[mid - 1] <= arr[mid] and \
       mid == n - 1 or arr[mid + 1] <= arr[mid]:
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


def find_peak(arr):
    """ function that finds a peak
        in a list of unsorted integers. """
    n = len(arr)
    return findPeakUtil(arr, 0, n - 1, n)
