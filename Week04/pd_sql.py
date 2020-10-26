import pandas as pd
import numpy as np

table_data = pd.DataFrame({
    'id':np.random.randint(1,1000,2000),
    'age':np.random.randint(1,70,2000),
})
# 1. SELECT * FROM data;
print(table_data)

# 2. SELECT * FROM data LIMIT 10;
print(table_data.head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(table_data[['id']])

# 4. SELECT COUNT(id) FROM data;
print(table_data['id'].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(table_data[(table_data['id'] < 1000) & (table_data['age'] > 30)])

table1 = pd.DataFrame({
    'id':np.random.randint(1,1000,2000),
    'order_id':np.random.randint(1,7000,2000),
})

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(table1.groupby('id').agg({'order_id':pd.Series.nunique}))

table2 = pd.DataFrame({
    'id':np.random.randint(1,1000,2000),
    'salay':np.random.randint(5000,12000,2000),
})

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1,table2,on='id'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1, table2]).drop_duplicates())

# 9. DELETE FROM table1 WHERE id=10;
print(table1.drop(table1.query('id==10').index, axis=0)) # axis 接受0或1,。代表操作的轴向，默认为0，按行删除。

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(table1.drop('order_id', axis=1))