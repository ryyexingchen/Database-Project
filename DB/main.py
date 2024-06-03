import tkinter as tk
from tkinter import ttk
from views import show_view,show_permission_view,show_workmanage_view,delete_workmanage_view,show_workupload_view,show_userworkdetail_view,show_userworkupdate_view,show_workdetail_view,back_to_worksearch_view,show_comment_view,delete_useraccount
from login import login
from register import register_user
from work import work_upload,user_work_update,work_search
from user import comment_upload
import lib

def user_on_double_click(event):
    # 获取触发事件的 Treeview 控件
    treeview = event.widget
    # 获取双击项的id
    item = treeview.selection()[0]
    work_id = treeview.item(item, "values")[0]
    lib.current_workid = work_id
    # 双击时执行的操作
    show_userworkdetail_view(work_id,userworkdetail_dict,frame_dict)

def search_on_double_click(event):
    # 获取触发事件的 Treeview 控件
    treeview = event.widget
    # 获取双击项的id
    item = treeview.selection()[0]
    work_id = treeview.item(item, "values")[0]
    lib.current_workid = work_id
    # 双击时执行的操作
    show_workdetail_view(work_id,workdetail_dict,frame_dict)

def create_labeled_entry(frame, text, row, width=20):
    label = ttk.Label(frame, text=text, anchor="center")
    label.grid(row=row, column=0, sticky="ew")
    entry = ttk.Entry(frame, width=width)
    entry.grid(row=row, column=1, padx=(0, 10),pady=5)
    return label, entry

def create_labeled_label(frame, text1, row, text2=''):
    label1 = ttk.Label(frame, text=text1, anchor="center")
    label1.grid(row=row, column=0, sticky="ew")
    label2 = ttk.Label(frame, text=text2, anchor="center")
    label2.grid(row=row, column=1, sticky="ew")
    return label1, label2

def create_labeled_combobox(frame, text, row):
    label = ttk.Label(frame, text=text, anchor="center")
    label.grid(row=row, column=0, sticky="ew")
    combobox = ttk.Combobox(frame, values=(), state="readonly")
    combobox.grid(row=row, column=1, padx=(0, 10), pady=5)
    return label, combobox

# 变量命名模式：label/entry/combobox_界面名称(去掉_)_作用;界面名称(去掉_)_button或其他的玩意_作用

# 创建主窗口
root = tk.Tk()
root.title("用户界面")

# -------------------创建Frame--------------------------
login_frame = ttk.Frame(root, padding=10) #登录界面
register_frame = ttk.Frame(root, padding=10) # 注册界面
user_data_frame = ttk.Frame(root, padding=10) # 用户信息界面
permission_frame = ttk.Frame(root, padding=10) # 用户权限界面
workmanage_frame = ttk.Frame(root, padding=10) # 用户作品管理界面
workupload_frame = ttk.Frame(root, padding=10) # 用户作品上传界面
userworkdetail_frame = ttk.Frame(root, padding=10) # 用户作品详细界面
userworkupdate_frame = ttk.Frame(root, padding=10) # 用户作品修改界面
worksearch_frame = ttk.Frame(root, padding=10) # 作品搜索界面
workdetail_frame = ttk.Frame(root, padding=10) # 普通作品详细信息界面
workcomment_frame = ttk.Frame(root, padding=10) # 作品评论信息界面

frame_dict = {'login':login_frame,
              'register':register_frame,
              'user_data':user_data_frame,
              'permission':permission_frame,
              'workmanage':workmanage_frame,
              'workupload':workupload_frame,
              'userworkdetail':userworkdetail_frame,
              'userworkupdate':userworkupdate_frame,
              'worksearch':worksearch_frame,
              'workdetail':workdetail_frame,
              'workcomment':workcomment_frame
              } # 框架词典
#----------------------------------------------登录界面----------------------------------------------------
label_login_title = ttk.Label(login_frame, text="登录", font=("Arial", 16, "bold"), anchor="center")
label_login_title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=(10, 5))
label_login_username, entry_login_username = create_labeled_entry(login_frame, "用户名/邮箱/手机号", 1)# 创建用户名/邮箱/手机号输入
label_login_password, entry_login_password = create_labeled_entry(login_frame, "密码", 2)# 创建密码输入
# 创建登录按钮
login_button_login = ttk.Button(login_frame, text="登录", command=lambda:login(login_dict,userdata_dict,frame_dict))
login_button_login.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# 创建跳转至注册页面的按钮
login_button_register = ttk.Button(login_frame, text="注册", command=lambda: show_view('register',frame_dict))
login_button_register.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# 使布局更紧凑
for i in range(5):  # 更新这个数字以匹配你的grid中的行数
    login_frame.grid_rowconfigure(i, weight=0)
    login_frame.grid_columnconfigure(0, weight=1)
    login_frame.grid_columnconfigure(1, weight=1)
# ------------------------------------------注册界面-----------------------------------------------------------
label_register_title = ttk.Label(register_frame, text="注册", font=("Arial", 16, "bold"), anchor="center")
label_register_title.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
label_register_username, entry_register_username = create_labeled_entry(register_frame, "用户名", 1)# 创建用户名输入
label_register_phone, entry_register_phone = create_labeled_entry(register_frame, "手机号", 2)# 创建手机号输入
label_register_password, entry_register_password = create_labeled_entry(register_frame, "密码", 3)# 创建密码输入
label_register_email, entry_register_email = create_labeled_entry(register_frame, "邮箱", 4)# 创建邮箱输入
# 创建性别下拉框
label_register_gender = ttk.Label(register_frame, text="性别", anchor="center")
label_register_gender.grid(row=6, column=0, sticky="ew", padx=(0, 10), pady=5)
register_gender_options = ['M', 'W', 'U']  # 性别选项
register_gender_variable = tk.StringVar(register_frame)
register_gender_variable.set('U')  # 设置默认选中的性别
register_drop_down_gender = ttk.Combobox(register_frame, textvariable=register_gender_variable, values=register_gender_options, state="readonly", width=10)
register_drop_down_gender.grid(row=6, column=1, padx=(0, 10), pady=5)
register_drop_down_gender.current(2)  # 设置默认选项为'U'
# 创建注册按钮
button_register_user = ttk.Button(register_frame, text="注册", command= lambda: register_user(register_dict,frame_dict))
button_register_user.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# 创建跳转回登录界面的按钮
button_back_to_login = ttk.Button(register_frame, text="返回登录界面", command=lambda: show_view('login',frame_dict))
button_back_to_login.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# 使布局更紧凑
for i in range(9):
    register_frame.grid_rowconfigure(i, weight=0)
    register_frame.grid_columnconfigure(0, weight=1)
    register_frame.grid_columnconfigure(1, weight=1)

# ---------------------------------用户信息界面--------------------------------------------
label_userdata_title = ttk.Label(user_data_frame, text="个人主页", font=("Arial", 16, "bold"), anchor="center")
label_userdata_title.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 5))
label1_userdata_username, label2_userdata_username = create_labeled_label(user_data_frame, "用户名：", 1)# 创建用户名标签
label1_userdata_phone, label2_userdata_phone = create_labeled_label(user_data_frame, "手机号：", 2)# 创建手机号标签
label1_userdata_email, label2_userdata_email = create_labeled_label(user_data_frame, "邮箱：", 3)# 创建邮箱标签
label1_userdata_gender, label2_userdata_gender = create_labeled_label(user_data_frame, "性别：", 4)# 创建性别标签
label1_userdata_regdate, label2_userdata_regdate = create_labeled_label(user_data_frame, "注册日期：", 5)# 创建注册日期标签
label1_userdata_level, label2_userdata_level = create_labeled_label(user_data_frame, "等级：", 6,)# 创建等级标签
label1_userdata_introduction, label2_userdata_introduction = create_labeled_label(user_data_frame, "简介：", 7,"您的简介空空如也")# 创建简介标签
# 添加一个返回登录界面的按钮
userdata_button_back_to_login = ttk.Button(user_data_frame, text="返回登录", command=lambda: show_view('login',frame_dict))
userdata_button_back_to_login.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# 添加一个查看权限的按钮
userdata_button_to_permission = ttk.Button(user_data_frame, text="查看个人权限", command=lambda: show_permission_view(lib.current_username,permission_dict,frame_dict))
userdata_button_to_permission.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
userdata_button_to_workmanage = ttk.Button(user_data_frame, text="管理作品", command=lambda: show_workmanage_view(lib.current_username,workmanage_dict,frame_dict))
userdata_button_to_workmanage.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
userdata_button_to_worksearch = ttk.Button(user_data_frame, text="搜索作品", command=lambda: show_view('worksearch',frame_dict))
userdata_button_to_worksearch.grid(row=11, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
userdata_button_cancel_account =  ttk.Button(user_data_frame, text="注销账户", command=lambda: delete_useraccount(lib.current_username,login_dict,frame_dict))
userdata_button_cancel_account.grid(row=12, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# -----------------------------------------个人权限界面-----------------------------------------
label_permission_title = ttk.Label(permission_frame, text="查看权限", font=("Arial", 16, "bold"), anchor="center")
label_permission_title.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 5))
label1_permission_username, label2_permission_username = create_labeled_label(permission_frame, "用户名：", 1)# 创建用户名标签
label1_permission_VideoQuality, label2_permission_VideoQuality = create_labeled_label(permission_frame, "最高视频画质：", 2)# 创建视频画质权限标签
label1_permission_comment, label2_permission_comment = create_labeled_label(permission_frame, "每日最多评论数：", 3)# 创建评论数标签
label1_permission_DanmuLevel, label2_permission_DanmuLevel = create_labeled_label(permission_frame, "弹幕权限：", 4)# 创建弹幕权限标签
# 添加一个返回用户界面的按钮
permission_button_back_to_userdata = ttk.Button(permission_frame, text="返回个人主页", command=lambda: show_view('user_data',frame_dict))
permission_button_back_to_userdata.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

#---------------------------------------用户作品管理界面-----------------------------------------
label_workmanage_title = ttk.Label(workmanage_frame, text="作品管理", font=("Arial", 16, "bold"), anchor="center")
label_workmanage_title.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=(10, 5))
workmanage_treeview = ttk.Treeview(workmanage_frame, columns=("id","Category","Name", "Author", "Date"), show="headings")
workmanage_treeview.heading("id", text="作品编号")
workmanage_treeview.heading("Category", text="类型")
workmanage_treeview.heading("Name", text="名称")
workmanage_treeview.heading("Author", text="作者")
workmanage_treeview.heading("Date", text="发布日期")
workmanage_treeview.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=(10, 5))
workmanage_scrollbar = ttk.Scrollbar(workmanage_frame, orient="vertical", command=workmanage_treeview.yview)
workmanage_scrollbar.grid(row=1, column=4, sticky="ns")
workmanage_treeview.configure(yscrollcommand=workmanage_scrollbar.set)
workmanage_treeview.bind("<Double-1>",user_on_double_click)
workmanage_button_upload = ttk.Button(workmanage_frame, text="上传作品", command=lambda: show_workupload_view(workupload_dict,frame_dict))
workmanage_button_upload.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
workmanage_button_back_to_userdata = ttk.Button(workmanage_frame, text="返回个人主页", command=lambda: delete_workmanage_view(workmanage_dict,frame_dict))
workmanage_button_back_to_userdata.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
# ----------------------------------------用户作品上传界面---------------------------------------
label_workupload_title = ttk.Label(workupload_frame, text="作品上传", font=("Arial", 16, "bold"), anchor="center")
label_workupload_title.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=(10, 5))
label_workupload_workname, entry_workupload_workname = create_labeled_entry(workupload_frame, "名称", 1)# 创建名称输入
label_workupload_introducion, entry_workupload_introducion = create_labeled_entry(workupload_frame, "简介", 2)# 创建简介输入
label_workupload_category, combobox_workupload_category = create_labeled_combobox(workupload_frame, "作品类型", 3)# 创建作品类型输入
label_workupload_partition, combobox_workupload_partition = create_labeled_combobox(workupload_frame, "分区", 4)# 创建分区输入
workupload_button_upload = ttk.Button(workupload_frame, text="上传", command=lambda: work_upload(lib.current_username,workmanage_dict,workupload_dict,frame_dict))
workupload_button_upload.grid(row=5, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
workupload_button_back_to_workmanage = ttk.Button(workupload_frame, text="放弃上传", command=lambda: show_workmanage_view(lib.current_username,workmanage_dict,frame_dict))
workupload_button_back_to_workmanage.grid(row=6, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
# ----------------------------------------用户作品详细界面---------------------------------------
label_userworkdetail_title = ttk.Label(userworkdetail_frame, text="详细信息", font=("Arial", 16, "bold"), anchor="center")
label_userworkdetail_title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=(10, 5))
label1_userworkdetail_workname, label2_userworkdetail_workname = create_labeled_label(userworkdetail_frame, "作品名称：", 1)# 创建作品名称标签
label1_userworkdetail_category, label2_userworkdetail_category = create_labeled_label(userworkdetail_frame, "作品类型：", 2)# 创建作品类型标签
label1_userworkdetail_partition, label2_userworkdetail_partition = create_labeled_label(userworkdetail_frame, "作品分区：", 3)# 创建作品分区标签
label1_userworkdetail_introduction, label2_userworkdetail_introduction = create_labeled_label(userworkdetail_frame, "作品简介：", 4)# 创建作品简介标签
label1_userworkdetail_view_number, label2_userworkdetail_view_number = create_labeled_label(userworkdetail_frame, "播放量：", 5)# 创建播放量标签
label1_userworkdetail_like_number, label2_userworkdetail_like_number = create_labeled_label(userworkdetail_frame, "点赞数：", 6)# 创建点赞数标签
label1_userworkdetail_comment_number, label2_userworkdetail_comment_number = create_labeled_label(userworkdetail_frame, "评论数：", 7)# 创建评论数标签
workupload_button_to_update = ttk.Button(userworkdetail_frame, text="修改作品信息", command=lambda: show_userworkupdate_view(userworkupdate_dict,frame_dict))
workupload_button_to_update.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
workupload_button_back_to_workmanage = ttk.Button(userworkdetail_frame, text="返回作品管理界面", command=lambda: show_workmanage_view(lib.current_username,workmanage_dict,frame_dict))
workupload_button_back_to_workmanage.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# ---------------------------------------用户作品修改界面-----------------------------------------
label_userworkupdate_title = ttk.Label(userworkupdate_frame, text="修改作品信息", font=("Arial", 16, "bold"), anchor="center")
label_userworkupdate_title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=(10, 5))
label_userworkupdate_workname, entry_userworkupdate_workname = create_labeled_entry(userworkupdate_frame, "作品名称：", 1)# 创建作品名称标签
label_userworkupdate_category, combobox_userworkupdate_category = create_labeled_combobox(userworkupdate_frame, "作品类型：", 2)# 创建作品类型标签
label_userworkupdate_partition, combobox_userworkupdate_partition = create_labeled_combobox(userworkupdate_frame, "作品分区：", 3)# 创建作品分区标签
label_userworkupdate_introduction, entry_userworkupdate_introduction = create_labeled_entry(userworkupdate_frame, "作品简介：", 4)# 创建作品简介标签
userworkupdate_button_update = ttk.Button(userworkupdate_frame, text="更新", command=lambda: user_work_update(lib.current_workid,lib.current_username,workmanage_dict,userworkupdate_dict,frame_dict))
userworkupdate_button_update.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
userworkupdate_button_back_to_userworkdetail = ttk.Button(userworkupdate_frame, text="返回详细信息界面", command=lambda: show_userworkdetail_view(lib.current_workid,userworkdetail_dict,frame_dict))
userworkupdate_button_back_to_userworkdetail.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# -------------------------------------作品搜索界面----------------------------------------------
label_worksearch_title = ttk.Label(worksearch_frame, text="全站作品搜索", font=("Arial", 16, "bold"), anchor="center")
label_worksearch_title.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=(10, 5))
entry_worksearch_search= ttk.Entry(worksearch_frame, width=20)
entry_worksearch_search.grid(row=1, column=0, columnspan=2, sticky="ew" ,padx=(0, 10),pady=5)#  创建作品简介标签
worksearch_button_search = ttk.Button(worksearch_frame, text="搜索", command=lambda: work_search(worksearch_dict))
worksearch_button_search.grid(row=1, column=2, columnspan=1, sticky="ew", padx=10, pady=5)

worksearch_treeview = ttk.Treeview(worksearch_frame, columns=("id", "Category", "Title", "Author", "Partition", "Date"), show="headings")
worksearch_treeview.heading("id", text="作品编号")
worksearch_treeview.heading("Category", text="类型")
worksearch_treeview.heading("Title", text="名称")
worksearch_treeview.heading("Author", text="作者")
worksearch_treeview.heading("Partition", text="分区")
worksearch_treeview.heading("Date", text="发布日期")
worksearch_treeview.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10, pady=(10, 5))
worksearch_scrollbar = ttk.Scrollbar(worksearch_frame, orient="vertical", command=worksearch_treeview.yview)
worksearch_scrollbar.grid(row=2, column=4, sticky="ns")
worksearch_treeview.configure(yscrollcommand=worksearch_scrollbar.set)
worksearch_treeview.bind("<Double-1>",search_on_double_click)

worksearch_button_back_to_userdata = ttk.Button(worksearch_frame, text="返回个人主页", command=lambda: delete_workmanage_view(worksearch_dict,frame_dict))
worksearch_button_back_to_userdata.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
# ----------------------------------------用户作品详细界面---------------------------------------
label_workdetail_title = ttk.Label(workdetail_frame, text="详细信息", font=("Arial", 16, "bold"), anchor="center")
label_workdetail_title.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=(10, 5))
label1_workdetail_workname, label2_workdetail_workname = create_labeled_label(workdetail_frame, "作品名称：", 1)# 创建作品名称标签
label1_workdetail_category, label2_workdetail_category = create_labeled_label(workdetail_frame, "作品类型：", 2)# 创建作品类型标签
label1_workdetail_partition, label2_workdetail_partition = create_labeled_label(workdetail_frame, "作品分区：", 3)# 创建作品分区标签
label1_workdetail_introduction, label2_workdetail_introduction = create_labeled_label(workdetail_frame, "作品简介：", 4)# 创建作品简介标签
label1_workdetail_view_number, label2_workdetail_view_number = create_labeled_label(workdetail_frame, "播放量：", 5)# 创建播放量标签
label1_workdetail_like_number, label2_workdetail_like_number = create_labeled_label(workdetail_frame, "点赞数：", 6)# 创建点赞数标签
label1_workdetail_comment_number, label2_workdetail_comment_number = create_labeled_label(workdetail_frame, "评论数：", 7)# 创建评论数标签
workdetail_button_to_comment = ttk.Button(workdetail_frame, text="查看作品评论", command=lambda: show_comment_view(lib.current_workid,workcomment_dict,frame_dict))
workdetail_button_to_comment.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
workdetail_button_back_to_workdesearch = ttk.Button(workdetail_frame, text="返回搜索界面", command=lambda: back_to_worksearch_view(worksearch_dict,frame_dict))
workdetail_button_back_to_workdesearch.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
# --------------------------------------作品评论界面---------------------------------------------
label_workcomment_title = ttk.Label(workcomment_frame, text="评论", font=("Arial", 16, "bold"), anchor="center")
label_workcomment_title.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=(10, 5))

workcomment_treeview = ttk.Treeview(workcomment_frame, columns=("id", "Author", "Content", "Date"), show="headings")
workcomment_treeview.heading("id", text="评论编号")
workcomment_treeview.heading("Author", text="发布人")
workcomment_treeview.heading("Content", text="内容")
workcomment_treeview.heading("Date", text="发布日期")
workcomment_treeview.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=(10, 5))
workcomment_scrollbar = ttk.Scrollbar(workcomment_frame, orient="vertical", command=workcomment_treeview.yview)
workcomment_scrollbar.grid(row=1, column=4, sticky="ns")
workcomment_treeview.configure(yscrollcommand=workcomment_scrollbar.set)

label_workcomment_comment = ttk.Label(workcomment_frame, text="请写下你的评论：", anchor="center")
label_workcomment_comment.grid(row=2, column=0, sticky="w")
entry_workcomment_comment = ttk.Entry(workcomment_frame, width=20)
entry_workcomment_comment.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=(0, 10), pady=5)

workcomment_button_upload = ttk.Button(workcomment_frame, text="发布", command=lambda: comment_upload(lib.current_workid,lib.current_username,workcomment_dict))
workcomment_button_upload.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
workcomment_button_back_to_workdetail = ttk.Button(workcomment_frame, text="返回详细信息界面", command=lambda: show_workdetail_view(lib.current_workid,workdetail_dict,frame_dict))
workcomment_button_back_to_workdetail.grid(row=5, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
# ---------------------------创建字典，包含界面上所有有用的组件---------------------------------------
login_dict = {'username':entry_login_username,
              'password':entry_login_password}
register_dict = {'username':entry_register_username,
                 'phone':entry_register_phone,
                 'email':entry_register_email,
                 'password':entry_register_password,
                 'gender':register_gender_variable}
userdata_dict = {'username':label2_userdata_username,
                 'phone':label2_userdata_phone,
                 'email':label2_userdata_email,
                 'gender':label2_userdata_gender,
                 'regdate':label2_userdata_regdate,
                 'introduction':label2_userdata_introduction,
                 'level':label2_userdata_level}
permission_dict = {'username':label2_permission_username,
                   'video_quality':label2_permission_VideoQuality,
                   'comment':label2_permission_comment,
                   'danmu_level':label2_permission_DanmuLevel}
workmanage_dict = {'worklist':workmanage_treeview}
workupload_dict = {'workname':entry_workupload_workname,
                   'introduction':entry_workupload_introducion,
                   'category':combobox_workupload_category,
                   'partition':combobox_workupload_partition}
userworkdetail_dict = {'workname':label2_userworkdetail_workname,
                       'category':label2_userworkdetail_category,
                       'partition':label2_userworkdetail_partition,
                       'introduction':label2_userworkdetail_introduction,
                       'viewnumber':label2_userworkdetail_view_number,
                       'likenumber':label2_userworkdetail_like_number,
                       'commentnumber':label2_userworkdetail_comment_number}
userworkupdate_dict = {'workname':entry_userworkupdate_workname,
                       'category':combobox_userworkupdate_category,
                       'partition':combobox_userworkupdate_partition,
                       'introduction':entry_userworkupdate_introduction}
worksearch_dict = {'search':entry_worksearch_search,
                   'worklist':worksearch_treeview}
workdetail_dict = {'workname':label2_workdetail_workname,
                   'category':label2_workdetail_category,
                   'partition':label2_workdetail_partition,
                   'introduction':label2_workdetail_introduction,
                   'viewnumber':label2_workdetail_view_number,
                   'likenumber':label2_workdetail_like_number,
                   'commentnumber':label2_workdetail_comment_number}
workcomment_dict = {'commentlist':workcomment_treeview,
                    'comment':entry_workcomment_comment}
# ----------------------------初始化---------------------------------
# 默认显示登录界面
login_frame.pack(fill=tk.BOTH, expand=True)
# 运行主循环
root.mainloop()