```python
from pymongo import MongoClient

# 创建 MongoDB 客户端对象，连接到本地默认端口的 MongoDB 服务器
client = MongoClient('mongodb://localhost:27017/')

# 选择要使用的数据库，如果数据库不存在，在首次插入数据时会自动创建
db = client['test_database']
```


```python
# 选择集合，如果集合不存在，在首次插入数据时会自动创建
collection = db['test_collection']

# 插入单条文档
document = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
result = collection.insert_one(document)
print(f"插入的文档 ID: {result.inserted_id}")

# 插入多条文档
documents = [
    {
        'name': 'Alice',
        'age': 25,
        'city': 'Los Angeles'
    },
    {
        'name': 'Bob',
        'age': 35,
        'city': 'Chicago'
    }
]
result = collection.insert_many(documents)
print(f"插入的多个文档 ID: {result.inserted_ids}")
```


```python
# 查询单条文档
one_document = collection.find_one({'name': 'John'})
print(f"查询到的单条文档: {one_document}")

# 查询多条文档
all_documents = collection.find({'age': {'$gt': 28}})  # 查询年龄大于 28 的文档
for doc in all_documents:
    print(doc)
```


```python
# 更新单条文档
update_result = collection.update_one(
    {'name': 'John'},
    {'$set': {'age': 31}}
)
print(f"更新的文档数量: {update_result.modified_count}")

# 更新多条文档
update_many_result = collection.update_many(
    {'city': 'Los Angeles'},
    {'$inc': {'age': 1}}  # 年龄加 1
)
print(f"更新的多条文档数量: {update_many_result.modified_count}")
```


```python
# 删除单条文档
delete_result = collection.delete_one({'name': 'Bob'})
print(f"删除的文档数量: {delete_result.deleted_count}")

# 删除多条文档
delete_many_result = collection.delete_many({'city': 'Chicago'})
print(f"删除的多条文档数量: {delete_many_result.deleted_count}")
```


```python
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_database']
    # 执行其他操作
except Exception as e:
    print(f"发生错误: {e}")
finally:
    if client:
        client.close()
```


```python
client.close()
```
