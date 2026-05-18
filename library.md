# Python チートシート

---

# set

## 重複削除

```python
a = [1, 2, 2, 3]
print(set(a))
```

出力：

```python
{1, 2, 3}
```

---

## 要素数

```python
a = [1, 2, 2, 3]
print(len(set(a)))
```

出力：

```python
3
```

---

## 集合に追加

```python
s = {1, 2}
s.add(3)

print(s)
```

出力：

```python
{1, 2, 3}
```

---

## 集合の判定

```python
s = {1, 2, 3}

print(2 in s)
print(5 in s)
```

出力：

```python
True
False
```

---

# sorted

## 昇順ソート

```python
A = [3, 1, 2]

print(sorted(A))
```

出力：

```python
[1, 2, 3]
```

---

## 降順ソート

```python
A = [3, 1, 2]

print(sorted(A, reverse=True))
```

出力：

```python
[3, 2, 1]
```

---

## 文字列長でソート

```python
A = ["apple", "kiwi", "banana"]

print(sorted(A, key=len))
```

出力：

```python
['kiwi', 'apple', 'banana']
```

---

## sort()（元を書き換える）

```python
A = [3, 1, 2]

A.sort()

print(A)
```

出力：

```python
[1, 2, 3]
```

---

## sorted() と sort() の違い

- `sorted()`  
  → 新しいリストを返す

- `sort()`  
  → 元のリストを変更する

---

# Counter

```python
from collections import Counter

A = [1, 1, 2, 3, 3, 3]

cnt = Counter(A)

print(cnt)
```

出力：

```python
Counter({3: 3, 1: 2, 2: 1})
```

---

## 個数取得

```python
from collections import Counter

A = [1, 1, 2, 3]

cnt = Counter(A)

print(cnt[1])
print(cnt[3])
```

出力：

```python
2
1
```

---

# list

## 追加

```python
A = [1, 2]

A.append(3)

print(A)
```

出力：

```python
[1, 2, 3]
```

---

## 削除

```python
A = [1, 2, 3]

A.pop()

print(A)
```

出力：

```python
[1, 2]
```

---

# map

## int変換

```python
A = list(map(int, input().split()))
```

入力：

```python
1 2 3
```

出力：

```python
[1, 2, 3]
```

---

# enumerate

## index付きループ

```python
A = ["a", "b", "c"]

for i, x in enumerate(A):
    print(i, x)
```

出力：

```python
0 a
1 b
2 c
```

---

# zip

## 同時ループ

```python
A = [1, 2, 3]
B = ["a", "b", "c"]

for x, y in zip(A, B):
    print(x, y)
```

出力：

```python
1 a
2 b
3 c
```

---

# max / min

```python
A = [3, 1, 5]

print(max(A))
print(min(A))
```

出力：

```python
5
1
```

---

# sum

```python
A = [1, 2, 3]

print(sum(A))
```

出力：

```python
6
```

---

# 2次元配列

```python
H = 3
W = 4

A = [[0] * W for _ in range(H)]

print(A)
```

出力：

```python
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
```

---

# 文字列操作

## 文字数

```python
s = "apple"

print(len(s))
```

出力：

```python
5
```

---

## 逆順

```python
s = "abc"

print(s[::-1])
```

出力：

```python
cba
```

---

## split

```python
s = "a b c"

print(s.split())
```

出力：

```python
['a', 'b', 'c']
```

---

# f文字列

```python
x = 3.141592

print(f"{x:.2f}")
```

出力：

```python
3.14
```

---

# よく使う import

```python
from collections import Counter, deque
from itertools import permutations, combinations
import math
import heapq
import bisect
```
