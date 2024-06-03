from tkinter import messagebox
from mysql.connector import Error
from database import create_connection

def comment(work_id,workcomment_dict):
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = """
                SELECT
                    c.id AS id,
                    u.username AS author,
                    c.content AS content,
                    c.date AS date
                FROM
                    comment c
                JOIN
                    user u ON c.comment_person_id = u.id
                where
	                work_id = %s;
               """
            cursor = connection.cursor()
            cursor.execute(query, (work_id,))
            result = cursor.fetchall()
            # 清除之前commentlist中的内容
            workcomment_dict['commentlist'].delete(*workcomment_dict['commentlist'].get_children())
            if result:
                for comment in result:
                    workcomment_dict['commentlist'].insert("", "end", values=comment)
            else:
                return
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def update_comment_number(work_id):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.callproc('UpdateWorkCommentCount', (work_id,))
        connection.commit()
    except Error as e:
        messagebox.showerror("评论数更新失败", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()