def merge_arrays(arr1, arr2):
    merged = arr1 + arr2
    merged = list(set(merged))
    merged.sort()
    return merged