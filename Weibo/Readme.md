# 2020-04-24

爬虫 -> 收集数据 
数据是从请求服务器来的->请求方式是http请求->如果是服务器正常相应的话，得到两种格式数据（html，json）-> 解析数据

- html 一般来说解析数据是苦难的 html很难解析，会比较复杂可能 常用的工具 bs4（Beautifulsoup）、lxml
- json 一般来说是别人给你接口（接口就是让你用来发起请求的） 拿到json以后直接 dumps python的数据结构 -> pandas、numpy等等

pandas、numpy、scipy等等这些用于计算的包或者说是数据分析的包
数据来源一般是csv、excel、txt等等文件来的，比如pandas.readcsv() 读取一个分隔符文件
读取以后 -> 文件内容变成 pandas自己定义好的一些数据结构，比如说长枪战锤，这些数据结构帮助你事先封装好了一下分析方法。


层级关系：
- python本身自带的list、dict、set等等 比较简单，但很常用，实现基础功能
- 往上一级numpy，就不是很基础功能，实现一些计算功能
- pandas 实现更复杂的运算
