from 初学1 import db, TODOLIST
id_ = int(input())#id查询
inf_1 = TODOLIST.query.get(id_)
inf_2 = TODOLIST.query.filter(TODOLIST.completion_status == "待办").paginate(1,5)#查询待办事项
inf_3 = TODOLIST.query.fliter(TODOLIST.completion_status == "已完成").paginate(1,5)#查询已完成事项
inf_4 = TODOLIST.query.all()#查询所有
