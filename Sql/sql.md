# 2020-04-27

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

# 2020-04-29

### \ 转义字符。

```sql
select * from nobel where winner = 'EUGENE O\'NEILL'
-- \ 转义字符。
```

### order by 表示按某一列排序

```sql
select column from tabel where condition order by column1,column2... (desc 表示降序）
-- order by 关键字，表示按某一列排序
```

### select within select

Select 返回的也是一种表结构

```sql
SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')
-- List each country name where the population is larger than that of 'Russia'.
-- 5 Percentages of Germany https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial
select name, CONCAT(ROUND(epop/gpop*100),'%') from
(select population as gpop from world where name='Germany') as t1,
(select name, population as epop from world where continent='Europe' ) as t2
-- 6 Bigger than every country in Europe
select name from world where gdp > ALL(select gdp from world where continent ='Europe' and gdp not in ('null'))
-- 或者
select name from world where gdp > (select MAX(gdp) from world where continent ='Europe')
-- 7 Largest in each continent
SELECT continent, name, area FROM world as x
  WHERE area >= ALL
    (SELECT area FROM world as y
        WHERE y.continent=x.continent
          AND area>0)
 
```

### group by 分组

```sql
SELECT continent, MIN(name) AS name
FROM world 
GROUP BY continent
-- 如果对某一列进行了group by 那么select 后面只能跟 该列 或者其他列的各种聚合 （COUNT、MAX、MIN）
```

### sql 执行顺序

1. **FROM & JOIN**
2. **WHERE**
3. **GROUP BY**
4. **HAVING**
5. **SELECT**
6. **ORDER BY**
7. **LIMIT**

# 2020-04-30

### 去重

```sql
SELECT DISTINCT region FROM bbc
-- distinct column_name
```

### 聚集函数

#### SUM求和

```sql
SELECT SUM(population), SUM(gdp)
  FROM bbc
  WHERE region = 'Europe'
-- 统计了欧洲的总人口，总gdp
```

#### COUNT计数

```sql
SELECT COUNT(population)
  FROM bbc
  WHERE region = 'Europe'
```

#### MAX、MIN最值

```sql
SELECT MAX(population)
  FROM bbc
  WHERE region = 'Europe'
```

#### AVG求平均

```sql
SELECT AVG(population)
  FROM bbc
  WHERE region = 'Europe'
```

### Using GROUP BY and HAVING

By including a `GROUP BY` clause functions such as `SUM` and `COUNT` are applied to groups of items sharing values. When you specify `GROUP BY continent` the result is that you get only one row for each different value of `continent`. All the other columns must be "aggregated" by one of `SUM`, `COUNT` ...

The `HAVING` clause allows use to filter the groups which are displayed. The `WHERE` clause filters rows before the aggregation, the `HAVING` clause filters after the aggregation.

If a `ORDER BY` clause is included we can refer to columns by their position.

```sql
-- For each continent show the number of countries:
SELECT continent, COUNT(name)
  FROM world
 GROUP BY continent
-- For each continent show the total population:
SELECT continent, SUM(population)
  FROM world
 GROUP BY continent
-- **WHERE and GROUP BY. The WHERE filter takes place before the aggregating function.**
-- For each relevant continent show the number of countries that has a population of at least 200000000.
SELECT continent, COUNT(name)
  FROM world
 WHERE population>200000000
 GROUP BY continent
-- **GROUP BY and HAVING. The HAVING clause is tested after the GROUP BY.**
-- Show the total population of those continents with a total population of at least half a billion.
SELECT continent, SUM(population)
  FROM world
 GROUP BY continent
HAVING SUM(population)>500000000
```



# The JOIN operation

game table

| id   | mdate        | stadium                   | team1 | team2 |
| :--- | :----------- | :------------------------ | :---- | :---- |
| 1001 | 8 June 2012  | National Stadium, Warsaw  | POL   | GRE   |
| 1002 | 8 June 2012  | Stadion Miejski (Wroclaw) | RUS   | CZE   |
| 1003 | 12 June 2012 | Stadion Miejski (Wroclaw) | GRE   | CZE   |
| 1004 | 12 June 2012 | National Stadium, Warsaw  | POL   | RUS   |

goal table

| matchid | teamid | player               | gtime |
| :------ | :----- | :------------------- | :---- |
| 1001    | POL    | Robert Lewandowski   | 17    |
| 1001    | GRE    | Dimitris Salpingidis | 51    |
| 1002    | RUS    | Alan Dzagoev         | 15    |
| 1002    | RUS    | Roman Pavlyuchenko   | 82    |

eteam table

| id   | teamname       | coach            |
| :--- | :------------- | :--------------- |
| POL  | Poland         | Franciszek Smuda |
| RUS  | Russia         | Dick Advocaat    |
| CZE  | Czech Republic | Michal Bilek     |
| GRE  | Greece         | Fernando Santos  |



```sql
SELECT *
  FROM game JOIN goal ON (id=matchid)
```

| id   | mdate       | stadium                  | team1 | team2 | matchid | teamid | player               | gtime |
| ---- | ----------- | ------------------------ | ----- | ----- | ------- | ------ | -------------------- | ----- |
| 1001 | 8 June 2012 | National Stadium, Warsaw | POL   | GRE   | 1001    | POL    | Robert Lewandowski   | 17    |
| 1001 | 8 June 2012 | National Stadium, Warsaw | POL   | GRE   | 1001    | GRE    | Dimitris Salpingidis | 51    |

```sql
SELECT player, teamid ,stadium, mdate
FROM game JOIN goal ON (id=matchid)
WHERE teamid = "GER"
-- show the player, teamid, stadium and mdate for every German goal.
```

