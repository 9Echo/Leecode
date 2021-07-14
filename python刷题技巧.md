### python语法相关总结

#### OJ 输入输出模板——int型数字

> 输入：
>
> 1 5
>
> 10 20
>
> 输出：
>
> 6
>
> 30

```python
while True:
    try:
        a, b = map(int, input().split())
        print(int(a+b))
    except:
        break
```

> 输入：
>
> 2
>
> 1 5
>
> 10 20
>
> 输出：
>
> 6
>
> 30


```python
"""
第一种
"""
n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))
    print(a + b)
    
"""
第二种
"""
def sum(a, b):
    return a + b

input()
while True:
    try:
        data = [int(string) for string in input().split()]
        print(sum(*data))
    except:
        break
```

```python
"""
如果输入的a，b都为0即结束
"""
while True:
    try:
        a,b =map(int,input().split(" "))
        if(a==0 and b==0):
            break
        else:
            print(a+b)
    except:
        break
```

```python
"""
输入的是个数组，当输入0时结束输入
每一行的第一个数字表示当前数组的个数n，后面一次输入n个数
"""
while True:
    try:
        l = list(map(int, input().split()))
        if not l[0]:
            break
        else:
            n = l[0]
            print(sum(l[1:n+1]))
            # pritn(sum(l[1:]))
    except:
        break
```

#### OJ模板输入输出——字符串

> 输入
>
> 5
>
> c d a bb e
>
> 输出
>
> a bb c d e

注意不能直接输出 print(sorted(list))，这样结果是字符串数组，要挨个输出。

```python
while True:
    try:
        n = int(input())
        l = list(map( str, input().split()))
        if n != len(l):
            break
        else:
            print(" ".join(sorted(l)))
    except:
        break
```

如果输入输出不是空格隔开而是”，“

```python
while True:
    try:
        li = map(str, input().split(','))
        print(",".join(sorted(li)))
    except:
        break
```



#### return 操作

最终返回布尔值，可以不用判断，直接return时做逻辑判断，省去代码量

```python
if not string:
    return True
return False
```

改写为：

```python
return not string
```

#### 判断是否为数字or字母

```python
str1 = '123'
str2 = 'abc'
str3 = '123abc'
error = 'a 1 !'
print(str1.isdigit(), str2.isdigit())    # True False
print(str2.isalpha(), str3.isalpha())    # True False
print(str3.isalnum(), error.isalnum())   # True False
```

#### sorted(list) vs list.sort()

```python
"""
list.sort()
1. 在原列表上操作，返回 None
2. 只有list可用，字符串、字典都没有
sorted(list)
1. 原列表不受影响，在一个新的列表上排序，返回一个列表
2. 字符串、字典都可以用
"""

s = "abcd"
print(sorted(s))
>>> ["a", "b", "c", "d"]
print(sorted(s, reverse=True))
>>> ["d", "c", "b", "a"]

dic = {"s": 1, "a": 2, "c": 3}         
print(sorted(dic.keys()))
>>> ['a', 'c', 's']

dic = {"s": 1, "a": 2, "c": 3}
# 按照字典的key排序(降序)（返回一个字典）
print(sorted(dic.items(), reverse=True))
>>> [('s', 1), ('c', 3), ('a', 2)]
# 按照values排序，key是items()里的（key,value),reverse为True表示逆序，默认为增
print(sorted(dic.items(), key=lambda x:x[1]))
>>> [('s', 1), ('a', 2), ('c', 3)]
```

