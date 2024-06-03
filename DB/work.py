from tkinter import messagebox
from views import show_workmanage_view
from mysql.connector import Error
from database import create_connection
from database import query_current_user_id

def work_upload(username,workmanage_dict,workupload_dict,frame_dict):
    connection = create_connection()

    user_id = query_current_user_id(username)
    workname = workupload_dict['workname'].get().strip()
    introduction = workupload_dict['introduction'].get().strip()
    category_id = workupload_dict['category'].current()
    partition_id = workupload_dict['partition'].current()

    # 检查输入是否为空
    if (not workname and (category_id == None) and (partition_id == None)):
        messagebox.showerror("上传失败", "作品名称、类型和分区是必填项。")
        return

    try:
        cursor = connection.cursor()
        # 插入用户数据
        insert_query = """
              INSERT INTO `work` (
              title,
              id_author,
              introduction,
              id_category,
              id_partition,
              view_number,
              like_number,
              comment_number,
              upload_date
              ) VALUES 
              (%s,%s,%s,%s,%s,0,0,0,current_date()
              )
              """
        cursor.execute(insert_query, (workname, user_id, introduction, category_id, partition_id))
        connection.commit()
        messagebox.showinfo("上传成功", "作品上传成功。")

        # 清除之前worklist中的内容
        workmanage_dict['worklist'].delete(*workmanage_dict['worklist'].get_children())
        # 上传成功后跳转回视频管理界面
        show_workmanage_view(username, workmanage_dict,frame_dict)

    except Error as e:
        messagebox.showerror("作品上传失败", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def user_work_update(work_id,username,workmanage_dict,userworkupdate_dict,frame_dict):
    connection = create_connection()

    workname = userworkupdate_dict['workname'].get().strip()
    introduction = userworkupdate_dict['introduction'].get().strip()
    category_id = userworkupdate_dict['category'].current()
    partition_id = userworkupdate_dict['partition'].current()

    # 检查输入是否为空
    if (not workname and (category_id == None) and (partition_id == None)):
        messagebox.showerror("更新失败", "作品名称、类型和分区是必填项。")
        return

    try:
        cursor = connection.cursor()
        query = """
                UPDATE work
                SET title = %s, introduction=%s, id_category=%s, id_partition=%s 
                WHERE id = %s;
                 """
        cursor.execute(query, (workname, introduction, category_id, partition_id, work_id))
        connection.commit()
        messagebox.showinfo("更新成功", "作品更新成功。")

        # 清除之前worklist中的内容
        workmanage_dict['worklist'].delete(*workmanage_dict['worklist'].get_children())
        # 上传成功后跳转回视频管理界面
        show_workmanage_view(username, workmanage_dict, frame_dict)

    except Error as e:
        messagebox.showerror("作品上传失败", f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def work_search(worksearch_dict):
    connection = create_connection()

    keyword = f"%{worksearch_dict['search'].get().strip()}%"
    keyword = "%" if keyword == "%%" else keyword

    try:
        cursor = connection.cursor()
        query = """
                SELECT * FROM work_info
                WHERE title LIKE %s OR category LIKE %s OR author LIKE %s OR `partition` LIKE %s
                 """
        cursor.execute(query, (keyword, keyword, keyword, keyword))
        result = cursor.fetchall()

        if result:
            # 清除之前worksearch中的内容
            worksearch_dict['worklist'].delete(*worksearch_dict['worklist'].get_children())
            for work in result:
                worksearch_dict['worklist'].insert("", "end", values=work)
        else:
            return
    except Error as e:
        messagebox.showerror("错误", f"Database error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()