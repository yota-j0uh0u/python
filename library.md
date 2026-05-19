# Python チートシート

---

# set

## 重複削除

```
a = [1, 2, 2, 3]
print(set(a))
```

出力：

```python
{1, 2, 3}
```
# abs

## 絶対値表現

```
print(abs(5 - 8))
```

出力：

```
3
```
# sorted

## 小さい順に並べる

```
sorted([4, 6, 5])
```

出力：
```
[4, 5, 6]
```

# count

## 何回出現するか

```
s = "abacaaa"
print(s.count("a"))
```

出力：
```
5
```

# values

## 値だけ取り出す

```
cnt = {
    "a": 5,
    "b": 1,
    "c": 1
}
print(cnt.values())
```

出力：
```
dict_values([5,1,1])
```
