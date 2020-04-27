# 2020-04-27

[toc]

## Sql

Structured query language 

https://sqlzoo.net/wiki/

主要是做表查询	表 有字段名 表里面的东西叫纪录 record 存储在服务器上

### basic

| name        | continent | area    | population | gdp          |
| :---------- | :-------- | :------ | :--------- | :----------- |
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |

上面是一个国家地理表，name 国家名字 continent 州 area 面积 pop 人口 gdp 经济总值

```sql
show tables;  -- 用来获取当前数据库有哪些表格
```

我们先来学操作一张表的：

```sql
select columnname(*代表全部列) from tablename
select * from world
```

| name        | continent | area    | population | gdp          | capital | tld  | flag                                                         |
| ----------- | --------- | ------- | ---------- | ------------ | ------- | ---- | ------------------------------------------------------------ |
| Afghanistan | Asia      | 652230  | 32225560   | 21992000000  | Kabul   | .af  | //upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Afghanistan.svg |
| Albania     | Europe    | 28748   | 2845955    | 13039000000  | Tirana  | .al  | //upload.wikimedia.org/wikipedia/commons/3/36/Flag_of_Albania.svg |
| Algeria     | Africa    | 2381741 | 43000000   | 167555000000 | Algiers | .dz  | //upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Algeria.svg |

```sql
select name,gdp from world
```

| name        | gdp          |
| ----------- | ------------ |
| Afghanistan | 21992000000  |
| Albania     | 13039000000  |
| Algeria     | 167555000000 |

```sql
select name,gdp from world where name = 'China' -- 有条件的查询
```

| name  | gdp            |
| ----- | -------------- |
| China | 12234781000000 |

```sql
SELECT name, gdp/population FROM world
  WHERE area > 5000000
 -- 查詢面積為 5,000,000 以上平方公里的國家,對每個國家顯示她的名字和人均國內生產總值(gdp/population)。
```

| name          | gdp/population |
| ------------- | -------------- |
| Australia     | 54833.5437     |
| Brazil        | 9721.37        |
| Canada        | 43337.0907     |
| China         | 8724.3064      |
| Russia        | 10431.3536     |
| United States | 59121.1921     |

```sql
SELECT name, population FROM world
  WHERE name IN ('Ireland', 'Iceland', 'Denmark');
 -- 顯示“Ireland 愛爾蘭”,“Iceland 冰島”,“Denmark 丹麥”的國家名稱和人口。
```

| name    | population |
| ------- | ---------- |
| Denmark | 5822763    |
| Iceland | 364260     |
| Ireland | 4921500    |

```sql
SELECT name, area FROM world
  WHERE area BETWEEN 200000 AND 250000
  -- Between left_bound and right_boud 
  -- 以顯示面積為 200,000 及 250,000 之間的國家名稱和該國面積。
```

| name           | area   |
| -------------- | ------ |
| Belarus        | 207600 |
| Ghana          | 238533 |
| Guinea         | 245857 |
| Guyana         | 214969 |
| Laos           | 236800 |
| Romania        | 238391 |
| Uganda         | 241550 |
| United Kingdom | 242900 |

### Pattern Matching Strings/"Like" 

```sql
like 'F%' 以F开头的
like '%F' 以F结尾的
like '%F%' 中间有F的
```

```sql
SELECT name FROM world
  WHERE name LIKE 'Y%'
  -- 找出以 Y 為開首的國家。
```

| name  |
| ----- |
| Yemen |

```sql
SELECT name FROM world
  WHERE name LIKE 'C%ia'
  -- 找出所有國家,其名字以 C 作開始,ia 作結尾。
```

| name     |
| -------- |
| Cambodia |
| Colombia |
| Croatia  |

```sql
SELECT name FROM world
 WHERE name LIKE '_t%'
 -- 找出所有國家,其名字以t作第二個字母。
```

| name     |
| -------- |
| Ethiopia |
| Italy    |

```sql
SELECT name
  FROM world
 WHERE capital = concat(name, ' City')
 -- concat(str1,str2,str3,str4......) 用来拼接两个字符串
 -- 顯示所有國家名字,其首都是國家名字加上”City”。
```

```sql
select capital,name from world where capital like concat('%',name,'%')
-- 找出所有首都和其國家名字,而首都要有國家名字中出現。
```

```sql
select name,REPLACE(capital, name, "") from world where capital like concat(name,'_%')
-- REPLACE('vessel','e','a') -> 'vassal'
-- 顯示國家名字，及其延伸詞，如首都是國家名字的延伸。  
```

### summary

```sql
-- summary
select column from tablename where condition and conditon or condition
-- condition -> =(相等),<（小于）,>（大于）,Between...and （范围）,In (A,B,C) （在一个列表里）,!=（不等于）
-- column -> * 代表全部列
-- concat(str1,str2,str3,str4......) 用来拼接两个字符串
-- REPLACE('vessel','e','a') -> 'vassal'
-- 四舍五入
ROUND(7253.86, 0)    ->  7254
ROUND(7253.86, 1)    ->  7253.9
ROUND(7253.86,-3)    ->  7000
-- 得到一个str的长度
LENGTH('Hello') -> 5 
-- 取一个字符串左边n位
LEFT('Hello world', 4) -> 'Hell'     
```

