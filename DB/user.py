from tkinter import messagebox
from mysql.connector import Error
from database import create_connection,query_current_user_id
from comment import comment,update_comment_number
import tkinter as tk
def show_user_data(username,userdata_dict):
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = "SELECT username, phone, email, gender, regdate, introduction,level FROM `user` WHERE username = %s"
            cursor = connection.cursor()
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                username, phone, email, gender, regdate, introduction, level = result
                userdata_dict['username'].config(text=username)
                userdata_dict['phone'].config(text=phone)
                userdata_dict['email'].config(text=email)
                userdata_dict['gender'].config(text=gender)
                userdata_dict['regdate'].config(text=regdate)
                userdata_dict['level'].config(text=level)
                userdata_dict['introduction'].config(text=introduction)
            else:
                messagebox.showerror("错误", "未找到用户数据。")
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def view_permission(username,permission_dict):
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = """
            SELECT u.username, l.video_quality, l.comment, l.danmu_level
            FROM user AS u
            JOIN level AS l ON u.level = l.level
            WHERE u.username = %s
            """
            cursor = connection.cursor()
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                username, video_quality, comment, danmu_level = result
                danmu = ['不允许发任何弹幕','只允许发普通弹幕','可以发普通弹幕和高级弹幕']
                permission_dict['username'].config(text=username)
                permission_dict['video_quality'].config(text=f'{video_quality}p')
                permission_dict['comment'].config(text=comment)
                permission_dict['danmu_level'].config(text=danmu[int(danmu_level)])

            else:
                messagebox.showerror("错误", "未找到用户数据。")
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def work_manage(username,workmanage_dict):
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = """
                SELECT w.id, c.name, w.title, u.username, w.upload_date
                FROM user AS u
                JOIN work AS w ON u.id = w.id_author
                JOIN category AS c ON c.id = w.id_category
                WHERE u.username = %s
               """
            cursor = connection.cursor()
            cursor.execute(query, (username,))
            result = cursor.fetchall()

            if result:
                for work in result:
                    workmanage_dict['worklist'].insert("", "end", values=work)
            else:
                return
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def user_work_detail_view(work_id,userworkdetail_dict):
    # 创建数据库连接
    connection = create_connection()
    if connection:
        try:
            # 执行查询以获取用户数据
            query = """
                    SELECT w.title, c.name, p.name, w.introduction, w.view_number, w.like_number, w.comment_number
                    FROM `work` AS w
                    JOIN `category` AS c ON c.id = w.id_category
                    JOIN `partition` AS p ON p.id = w.id_partition
                    WHERE w.id = %s
                   """
            cursor = connection.cursor()
            cursor.execute(query, (work_id,))
            result = cursor.fetchone()

            if result:
                workname, category, partition, introduction, viewnumber, likenumber, commentnumber = result
                userworkdetail_dict['workname'].config(text=workname)
                userworkdetail_dict['category'].config(text=category)
                userworkdetail_dict['partition'].config(text=f"{partition}区")
                userworkdetail_dict['introduction'].config(text=introduction)
                userworkdetail_dict['viewnumber'].config(text=viewnumber)
                userworkdetail_dict['likenumber'].config(text=likenumber)
                userworkdetail_dict['commentnumber'].config(text=commentnumber)
            else:
                messagebox.showerror("错误", "未找到用户数据。")
        except Error as e:
            messagebox.showerror("错误", f"Database error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def comment_upload(work_id,username,workcomment_dict):
    connection = create_connection()

    user_id = query_current_user_id(username)
    content = workcomment_dict['comment'].get().strip()

    # 检查输入是否为空
    if not content:
        messagebox.showerror("评论发布失败", "评论为空")
        return

    try:
        cursor = connection.cursor()
        # 插入用户数据
        insert_query = """
                  INSERT INTO `comment` (
                    comment_person_id,
                    work_id,
                    content,
                    date
                  ) VALUES (
                    %s,%s,%s,CURDATE()
                  );
                 """
        cursor.execute(insert_query, (user_id, work_id, content))
        connection.commit()
        messagebox.showinfo("评论发布", "发布成功")
        # 更新评论数
        update_comment_number(work_id)
        # 清除之前commentlist和entry中的内容
        workcomment_dict['commentlist'].delete(*workcomment_dict['commentlist'].get_children())
        workcomment_dict['comment'].delete(0, tk.END)
        comment(work_id, workcomment_dict)
    except Error as e:
        update_comment_number(work_id)
        messagebox.showerror("评论发布失败", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_user_account(username):
    # 创建数据库连接
    connection = create_connection()
    try:
        cursor = connection.cursor()
        # 开启事务
        connection.start_transaction()
        # 首先通过用户名获取用户ID
        get_user_id_sql = "SELECT `id` FROM `user` WHERE `username`=%s"
        cursor.execute(get_user_id_sql, (username,))
        user_id_record = cursor.fetchone()
        user_id = user_id_record[0]
        # 查询待注销账号的所有作品的work.id
        get_work_ids_sql = "SELECT `id` FROM `work` WHERE `id_author`=%s"
        cursor.execute(get_work_ids_sql, (user_id,))
        work_ids = cursor.fetchall()
        if work_ids:
            work_ids_list = [str(work_id[0]) for work_id in work_ids]
            # 构建删除comment表中记录的SQL语句
            delete_comment_sql = (
                "DELETE FROM `comment` "
                "WHERE `comment_person_id`=%s "
                "OR `work_id` IN (%s)"
            )
            # 执行删除comment表中记录的操作
            # 为comment_persen_id传递一个参数，为IN子句传递一个元组参数
            cursor.execute(delete_comment_sql, (user_id,) + tuple(work_ids_list))
            # 执行删除操作
            cursor.execute("DELETE FROM `work` WHERE `id_author`=%s", (user_id,))
            cursor.execute("DELETE FROM `user` WHERE `id`=%s", (user_id,))
            # 提交事务
            connection.commit()
            messagebox.showinfo("用户注销","用户已注销")
        else:
            cursor.execute("DELETE FROM `user` WHERE `id`=%s", (user_id,))
            connection.commit()
            messagebox.showinfo("用户注销", "用户已注销")
    except Error as e:
        print(f"数据库错误: {e}")
        # 如果发生错误，回滚事务
        connection.rollback()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    # work_manage('小明')
    pass