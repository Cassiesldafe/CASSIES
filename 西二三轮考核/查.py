from 初学1 import db, Information
#id_ = int(input())#id查询
#inf_1 = Information.query.get(id_)

#inf_2 = Information.query.filter(Information.completion_status == "待办").paginate(1,5)#查询待办事项
#inf_3 = Information.query.fliter(Information.completion_status == "已完成").paginate(1,5)#查询已完成事项
inf_4 = Information.query.all()#查询所有
#inf_5 = Information.query.filter(Information.)