import numpy as np

# Part 1

# 1
print(np.__version__)
print(np.show_config())

# 2
a = np.array([1, 2, 3, 4])
print(np.all(a))

# 3
print(np.any(a))

# 4
a = np.array([1, 0, np.nan, np.inf])
print(np.isfinite(a))

# 5
print(np.isinf(a))

# 6
print(np.isnan(a))

# 7
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print(np.greater(a, b))
print(np.greater_equal(a, b))
print(np.less(a, b))
print(np.less_equal(a, b))

# 8
print(np.equal(a, b))
print(np.allclose(a, b))

# 9
print(np.concatenate([np.zeros(10), np.ones(10), np.full(10, 5)]))

# 10
print(np.arange(30, 71))

# 11
print(np.arange(30, 71, 2))

# 12
print(np.identity(3))

# 13
print(np.random.rand())

# 14
print(np.arange(15, 56)[1:-1])

# 15
array = np.arange(12).reshape(3, 4)
for row in array:
    print(row)

# 16
print(np.linspace(5, 50, 10))

# 17
v = np.arange(21)
v[(v >= 9) & (v <= 15)] *= -1
print(v)

# 18
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.multiply(a, b))

# 19
print(np.arange(10, 22).reshape(3, 4))

# 20
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix.shape)

# 21
print(np.diag([1, 2, 3, 4, 5]))

# 22
print(np.random.rand(3, 3, 3))

# 23
array = np.arange(6).reshape(2, 3)
print(array.sum())
print(array.sum(axis=0))
print(array.sum(axis=1))

# 24
a = np.array([1, 2, 3])
b = np.array([0, 1, 0])
print(np.inner(a, b))

# 25
M = np.ones((3, 3))
v = np.array([1, 2, 3])
print(M + v)

# 26
a = np.array([1, 2, 3])
b = np.array([1, 2, 4])
print(np.array_equal(a, b))

# 27
print(np.zeros((5, 6)))

# 28
a = np.array([[3, 2], [1, 4]])
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))

# 29
a = np.array([1, 5, 8, 3, 0, 11, 2])
print(a[a < 3])
print(a[a > 8])

# 30
a = np.array([1, 5, 8, 3, 0, 11, 2])
a[a == 5] = -1
a[a < 3] = -2
a[a > 8] = -3
print(a)

# 31
arr = np.arange(16).reshape(4, 4)
print(arr[:, [3, 2, 1, 0]])

# 32
print(arr[::-1, ::-1])

# 33
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.multiply(a, b))

# Part 2

# 1
lst = [12.23, 13.32, 100, 36.32]
print(np.array(lst))

# 2
print(np.arange(2, 11).reshape(3, 3))

# 3
z = np.zeros(10)
z[5] = 11
print(z)

# 4
print(np.arange(12, 38))

# 5
arr = np.arange(12, 38)
print(arr[::-1])

# 6
print(np.array([1, 2, 3, 4], dtype='float32'))

# 7
a = np.array([10, 20, 30])
a = np.append(a, [40, 50, 60, 70, 80, 90])
print(a)

# 8
print(np.empty((3, 4)))
print(np.full((3, 3), 6))

# 9
c = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0])
f = c * 9/5 + 32
print(f)

# 10
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])
print(np.in1d(array1, array2))

# 11
print(np.intersect1d(array1, array2))

# 12
a = np.array([10, 10, 20, 20, 30, 30])
print(np.unique(a))

# 13
a = np.array([0, 10, 20, 40, 60, 80])
b = np.array([10, 30, 40, 50, 70, 90])
print(np.setdiff1d(a, b))

# 14
a = np.array([1, 2])
b = np.array([4, 5])
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 15
arr = np.array([[4, 6], [2, 1]])
print(np.sort(arr, axis=0))
print(np.sort(arr, axis=1))

# 16
arr = np.array([[0, 10, 20], [20, 30, 40]])
print(arr[arr > 10])
print(np.where(arr > 10))

# 17
arr = np.array([[10, 20, 30], [20, 40, 50]])
print(arr.ravel())

# 18
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print(arr.shape, type(arr), arr.dtype)

# 19
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.reshape(3, 2))
print(arr.reshape(2, 3))

# 20
print(np.full((3, 5), 2))

# 21
x = np.array([[1, 2], [3, 4]])
print(np.full_like(x, 10))

# 22
diag = np.array([4, 5, 6, 8])
print(np.diag(diag))

# 23
print(np.arange(0, 50))
print(np.arange(10, 50))

# 24
arr = np.array([[2, 4, 6], [6, 8, 10]])
print(arr[0, 1])

# 25
a = np.array([1.12, 2., 3.45])
print(2 in a)
print(5 in a)
