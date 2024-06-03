from tkinter import messagebox
from database import create_connection
from mysql.connector import Error
from views import show_user_data_view
import lib

def login(login_dict,userdata_dict,frame_dict):
    connection = create_connection()
    if connection:
        try:
            username_or_email_or_phone = login_dict['username'].get().strip()
            password = login_dict['password'].get().strip()
            cursor = connection.cursor()

            # 查询用户名、邮箱或手机号
            query = "SELECT * FROM `user` WHERE username = %s OR email = %s OR phone = %s"
            cursor.execute(query, (username_or_email_or_phone, username_or_email_or_phone, username_or_email_or_phone))
            user = cursor.fetchone()
            if user:
                # 验证密码（这里假设密码字段是hashed_password）
                if user[1] == password:  # user[1] 是数据库中的密码字段
                    lib.current_username = user[2] # user[2] 是用户名字段
                    messagebox.showinfo("登录成功", f"欢迎回来，{user[2]}！")
                    show_user_data_view(user[2],userdata_dict,frame_dict)
                else:
                    messagebox.showerror("登录失败", "密码错误")
            else:
                messagebox.showerror("登录失败", "用户不存在")
        except Error as e:
            messagebox.showerror("登录失败", f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        messagebox.showerror("登录失败", "无法连接到数据库")