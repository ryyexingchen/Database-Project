from tkinter import messagebox
from mysql.connector import Error, connect

# 数据库配置信息
db_config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'video_admin',
    'port': 3306
}

def create_connection():
    try:
        return connect(**db_config)
    except Error as e:
        print(f"Error: {e}")
        return None

def query_partition():
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = """
                SELECT name
                FROM `partition` 
               """
            cursor = connection.cursor()
            cursor.execute(query, ())
            user = cursor.fetchall()
            if user:
                user = tuple([item[0] for item in user])
                return user
            else:
                messagebox.showerror("错误", "未找到用户数据。")
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def query_category():
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = """
                SELECT name
                FROM `category` 
               """
            cursor = connection.cursor()
            cursor.execute(query, ())
            user = cursor.fetchall()
            if user:
                user = tuple([item[0] for item in user])
                return user
            else:
                messagebox.showerror("错误", "未找到用户数据。")
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def query_current_user_id(username):
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = """
                SELECT id
                FROM `user` 
                WHERE username = %s
               """
            cursor = connection.cursor()
            cursor.execute(query, (username,))
            user = cursor.fetchone()
            if user:
                return user[0]
            else:
                messagebox.showerror("错误", "未找到用户数据。")
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()