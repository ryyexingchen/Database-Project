from tkinter import messagebox
import tkinter as tk
from user import show_user_data, view_permission,work_manage,user_work_detail_view,delete_user_account
from database import query_category,query_partition
from comment import comment,update_comment_number
def show_view(view_name,frame_dict):
    # 隐藏所有视图
    for value in frame_dict.values():
        value.pack_forget()
    # 根据视图名称显示目标视图
    try:
        frame_dict[view_name].pack(fill=tk.BOTH, expand=True)
    except:
        messagebox.showerror("错误", "无效的视图名称。")

def show_user_data_view(username,userdata_dict,frame_dict):
    show_view('user_data',frame_dict)
    show_user_data(username,userdata_dict)

def show_permission_view(username,permission_dict,frame_dict):
    show_view('permission',frame_dict)
    view_permission(username,permission_dict)

def show_workmanage_view(username,workmanage_dict,frame_dict):
    workmanage_dict['worklist'].delete(*workmanage_dict['worklist'].get_children()) # 删除之前treeview中的内容
    show_view('workmanage', frame_dict)
    work_manage(username,workmanage_dict)

def delete_workmanage_view(workmanage_dict,frame_dict):
    show_view('user_data', frame_dict)
    workmanage_dict['worklist'].delete(*workmanage_dict['worklist'].get_children())

def show_workupload_view(workupload_dict,frame_dict):
    # 设置下拉框的信息
    workupload_dict['category']['values'] = query_category()
    workupload_dict['partition']['values'] = query_partition()
    show_view('workupload', frame_dict)

def show_userworkdetail_view(work_id,userworkdetail_dict,frame_dict):
    user_work_detail_view(work_id,userworkdetail_dict)
    show_view('userworkdetail',frame_dict)

def show_userworkupdate_view(userworkupdate_dict,frame_dict):
    # 设置下拉框的信息
    userworkupdate_dict['category']['values'] = query_category()
    userworkupdate_dict['partition']['values'] = query_partition()
    show_view('userworkupdate', frame_dict)

def show_workdetail_view(work_id,workdetail_dict,frame_dict):
    update_comment_number(work_id)
    user_work_detail_view(work_id,workdetail_dict)
    show_view('workdetail',frame_dict)

def back_to_worksearch_view(worksearch_dict,frame_dict):
    worksearch_dict['worklist'].delete(*worksearch_dict['worklist'].get_children())
    show_view('worksearch', frame_dict)

def show_comment_view(work_id,workcomment_dict,frame_dict):
    comment(work_id,workcomment_dict)
    update_comment_number(work_id)
    show_view('workcomment', frame_dict)

def delete_useraccount(username,login_dict,frame_dict):
    delete_user_account(username)
    # 清除登录界面entry的内容
    login_dict['username'].delete(0, tk.END)
    login_dict['password'].delete(0, tk.END)
    show_view('login', frame_dict)