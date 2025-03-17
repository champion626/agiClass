```python
import mysql.connector

# 建立数据库连接
def create_connection():
    try:
        # 请根据实际情况修改数据库连接信息
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="mysql",
            password="mysql@Lele310115",
            database="everbetter"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"连接数据库时出错: {err}")
        return None

# 创建表（如果表不存在）
def create_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("表 'users' 创建成功。")
    except mysql.connector.Error as err:
        print(f"创建表时出错: {err}")

# 插入数据
def insert_user(connection, name, age):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        data = (name, age)
        cursor.execute(insert_query, data)
        connection.commit()
        print(f"用户 {name} 插入成功。")
    except mysql.connector.Error as err:
        print(f"插入用户时出错: {err}")

# 查询数据
def select_users(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        users = cursor.fetchall()
        if users:
            print("所有用户信息:")
            for user in users:
                print(f"ID: {user[0]}, 姓名: {user[1]}, 年龄: {user[2]}")
        else:
            print("未找到用户信息。")
    except mysql.connector.Error as err:
        print(f"查询用户时出错: {err}")

# 更新数据
def update_user(connection, user_id, new_name, new_age):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE users SET name = %s, age = %s WHERE id = %s"
        data = (new_name, new_age, user_id)
        cursor.execute(update_query, data)
        connection.commit()
        print(f"用户 ID 为 {user_id} 的信息更新成功。")
    except mysql.connector.Error as err:
        print(f"更新用户信息时出错: {err}")

# 删除数据
def delete_user(connection, user_id):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM users WHERE id = %s"
        data = (user_id,)
        cursor.execute(delete_query, data)
        connection.commit()
        print(f"用户 ID 为 {user_id} 的信息删除成功。")
    except mysql.connector.Error as err:
        print(f"删除用户信息时出错: {err}")

# 主函数，用于调用上述功能
def main():
    # 建立数据库连接
    connection = create_connection()
    if connection:
        # 创建表
        create_table(connection)

        # 插入数据
        insert_user(connection, "张三", 25)
        insert_user(connection, "李四", 30)

        # 查询数据
        select_users(connection)

        # 更新数据
        update_user(connection, 1, "张小三", 26)

        # 再次查询数据
        select_users(connection)

        # 删除数据
        delete_user(connection, 2)

        # 最后一次查询数据
        select_users(connection)

        # 关闭数据库连接
        connection.close()

if __name__ == "__main__":
    main()
```
