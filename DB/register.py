from tkinter import messagebox
from database import create_connection
from mysql.connector import Error
from views import show_view


def register_user(register_dict,frame_dict):
    connection = create_connection()
    if not connection:
        messagebox.showerror("注册失败", "无法连接到数据库")
        return

    username = register_dict['username'].get().strip()
    password = register_dict['password'].get().strip()
    phone = register_dict['phone'].get().strip()
    email = register_dict['email'].get().strip()
    gender = register_dict['gender'].get()
    # 检查输入是否为空
    if not (username and password and phone and email and gender):
        messagebox.showerror("注册失败", "用户名、密码、手机号、邮箱和性别是必填项。")
        return
    try:
        cursor = connection.cursor()
        # 检查用户名是否已存在
        query = "SELECT * FROM `user` WHERE username = %s"
        cursor.execute(query, (username,))
        if cursor.fetchone():
            messagebox.showerror("注册失败", "用户名已存在，请选择其他用户名。")
            return

        # 插入用户数据
        insert_query = """
          INSERT INTO `user` (
              username,
              password,
              phone,
              email,
              gender,
              regdate
          ) VALUES (
              %s, %s, %s, %s, %s, CURDATE()
          )
          """
        cursor.execute(insert_query, (username, password, phone, email, gender))
        connection.commit()
        messagebox.showinfo("注册成功", "用户注册成功，请登录。")
        show_view('login',frame_dict)  # 注册成功后跳转回登录界面

    except Error as e:
        messagebox.showerror("注册失败", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()