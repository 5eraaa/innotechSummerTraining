import numpy as np

# NumPy Statistics - Lab 5 - Part 2

# 1
arr = np.array([[0, 1], [2, 3]])
print(np.max(arr))
print(np.min(arr))

# 2
print(np.max(arr, axis=1))
print(np.min(arr, axis=1))

# 3
arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(np.ptp(arr, axis=1))

# 4
arr = np.array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])
print(np.percentile(arr, 80, axis=1))

# 5
arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(np.median(arr))

# 6
arr = np.array([0, 1, 2, 3, 4])
weights = np.array([1, 2, 3, 4, 5])
print(np.average(arr, weights=weights))

# 7
arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(np.mean(arr, axis=1))
print(np.std(arr, axis=1))
print(np.var(arr, axis=1))

# 8
a1 = np.array([0, 1, 2])
a2 = np.array([2, 1, 0])
print(np.cov(a1, a2))

# 9
a1 = np.array([0, 1, 3])
a2 = np.array([2, 4, 5])
print(np.correlate(a1, a2))

# 10
a1 = np.array([0, 1, 3])
a2 = np.array([2, 4, 5])
print(np.corrcoef(a1, a2))

# 11
a = np.array([1.0, np.nan, np.inf])
print(np.isfinite(a))
print(np.isinf(a))
print(np.isnan(a))
from pandas import NaT
print(np.array([np.datetime64('NaT'), np.datetime64('2021-01-01')]) == np.datetime64('NaT'))
a = np.array([-np.inf, 0, np.inf])
print(np.isneginf(a).astype(int))
print(np.isposinf(a).astype(int))

# 12
a = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])
print(np.bincount(a))

# 13
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print(np.histogram(nums, bins))
