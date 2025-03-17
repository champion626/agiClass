#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import redis

# 创建 Redis 连接对象
r = redis.Redis(
    host='localhost',  # Redis 服务器主机地址
    port=6379,         # Redis 服务器端口号
    db=0,              # 选择的数据库编号
    password=None      # 如果 Redis 服务器设置了密码，需要提供密码
)

# 测试连接
try:
    r.ping()
    print("成功连接到 Redis 服务器")
except redis.exceptions.ConnectionError:
    print("无法连接到 Redis 服务器，请检查配置")


# In[ ]:


# 字符串操作
# 设置键值对
r.set('name', 'John')

# 获取键对应的值
name = r.get('name')
print(f"获取到的 name 值为: {name.decode('utf-8')}")

# 自增操作
r.set('counter', 10)
r.incr('counter')
counter = r.get('counter')
print(f"自增后的 counter 值为: {int(counter)}")


# In[ ]:


# 设置哈希字段和值
r.hset('user:1', 'name', 'Alice')
r.hset('user:1', 'age', 25)

# 获取哈希字段的值
name = r.hget('user:1', 'name')
age = r.hget('user:1', 'age')
print(f"用户姓名: {name.decode('utf-8')}, 年龄: {int(age)}")

# 获取哈希的所有字段和值
user_info = r.hgetall('user:1')
for field, value in user_info.items():
    print(f"{field.decode('utf-8')}: {value.decode('utf-8')}")


# In[ ]:


# 从列表左侧插入元素
r.lpush('tasks', 'task1')
r.lpush('tasks', 'task2')

# 获取列表指定范围的元素
tasks = r.lrange('tasks', 0, -1)
for task in tasks:
    print(task.decode('utf-8'))

# 从列表右侧弹出元素
popped_task = r.rpop('tasks')
print(f"弹出的任务: {popped_task.decode('utf-8')}")


# In[ ]:


# 向集合中添加元素
r.sadd('fruits', 'apple')
r.sadd('fruits', 'banana')
r.sadd('fruits', 'cherry')

# 获取集合中的所有元素
fruits = r.smembers('fruits')
for fruit in fruits:
    print(fruit.decode('utf-8'))

# 检查元素是否在集合中
is_apple_in = r.sismember('fruits', 'apple')
print(f"apple 是否在集合中: {is_apple_in}")


# In[ ]:


r.close()

