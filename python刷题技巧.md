### python语法相关总结



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

