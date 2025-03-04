给文本文件的中文英文之间添加合理的空格
==================================================

## 文档排版需求

  - [中英文之间需要增加空格](#中英文之间需要增加空格)
  - [中文与数字之间需要增加空格](#中文与数字之间需要增加空格)
  - [数字与单位之间需要增加空格](#数字与单位之间需要增加空格)
  - [全角标点与其他字符之间不加空格](#全角标点与其他字符之间不加空格)

## 脚本用法

```
	python add_spaces.py /path/to/file code  # code 为文件编码，如：gbk, utf8
	# 或者自动猜测文本文件的编码
	python add_spaces.py /path/to/file
```

## 更新历史
### 更新时间：2024-06-26
  - 註解改成繁體中文
  - 代碼改成支援 python 3.6 以上
### 更新时间：2016-08-28
  - 支持对中文里有粗体或斜体英文单词的语句的处理
  - 支持对中文里有粗体或斜体中文字词的语句的处理

## 空格

「有研究显示，打字的时候不喜欢在中文和英文之间加空格的人，感情路都走得很辛苦，有七成的比例会在 34 岁的时候跟自己不爱的人结婚，而其余三成的人最后只能把遗产留给自己的猫。毕竟爱情跟书写都需要适时地留白。

与大家共勉之。」——[vinta/paranoid-auto-spacing](https://github.com/vinta/pangu.js)

### 中英文之间需要增加空格

正确：

> 在 LeanCloud 上，数据存储是围绕 `AVObject` 进行的。

错误：

> 在LeanCloud上，数据存储是围绕`AVObject`进行的。

> 在 LeanCloud上，数据存储是围绕`AVObject` 进行的。

完整的正确用法：

> 在 LeanCloud 上，数据存储是围绕 `AVObject` 进行的。每个 `AVObject` 都包含了与 JSON 兼容的 key-value 对应的数据。数据是 schema-free 的，你不需要在每个 `AVObject` 上提前指定存在哪些键，只要直接设定对应的 key-value 即可。

例外：「豆瓣FM」等产品名词，按照官方所定义的格式书写。

### 中文与数字之间需要增加空格

正确：

> 今天出去买菜花了 5000 元。

错误：

> 今天出去买菜花了 5000元。

> 今天出去买菜花了5000元。

### 数字与单位之间需要增加空格

正确：

> 我家的光纤入户宽带有 10 Gbps，SSD 一共有 20 TB。

错误：

> 我家的光纤入户宽带有 10Gbps，SSD 一共有 10TB。

例外：度／百分比与数字之间不需要增加空格：

正确：

> 今天是 233° 的高温。

> 新 MacBook Pro 有 15% 的 CPU 性能提升。

错误：

> 今天是 233 ° 的高温。

> 新 MacBook Pro 有 15 % 的 CPU 性能提升。

### 全角标点与其他字符之间不加空格

正确：

> 刚刚买了一部 iPhone，好开心！

错误：

> 刚刚买了一部 iPhone ，好开心！

## 参考

- [原作者](https://github.com/robot527/add-spaces)
- [中文文案排版指北](https://github.com/LCTT/TranslateProject/blob/master/%E4%B8%AD%E6%96%87%E6%8E%92%E7%89%88%E6%8C%87%E5%8C%97.md#%E4%B8%AD%E8%8B%B1%E6%96%87%E4%B9%8B%E9%97%B4%E9%9C%80%E8%A6%81%E5%A2%9E%E5%8A%A0%E7%A9%BA%E6%A0%BC)
